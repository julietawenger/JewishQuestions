import os
import requests
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Fetch Sefaria sources
def fetch_sefaria_sources(query):
    """Simple search through Sefaria API."""
    url = f"https://www.sefaria.org/api/search-wrapper"
    params = {"query": query, "size": 5, "type": "text"}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        results = response.json()
        
        # Parse the hits from the Sefaria response
        texts = []
        for r in results.get("hits", []):
            ref = r.get("ref", "Unknown reference")
            snippet = r.get("highlighted", {}).get("text", ["No highlighted text"])[0]
            texts.append(f"Source: {ref}\nSnippet: {snippet}")
        
        # If no sources found, return a default message
        return texts if texts else ["No sources found."]
    
    except Exception as e:
        return [f"Error fetching sources: {e}"]

# Query Gemini with references
def answer_with_gemini(question, sources):
    """Ask Gemini to answer using the given sources."""
    # Prepare the prompt for Gemini (Gemini 1.5 Pro)
    prompt = (
        f"You are a rabbinic scholar with deep knowledge of Jewish law, Torah, and the Talmud.\n"
        f"Answer the following question based ONLY on these sources:\n\n"
        + "\n".join(f"- {s}" for s in sources) +
        f"\n\nQuestion: {question}\nAnswer with references."
    )
    
    try:
        model = genai.GenerativeModel('models/gemini-1.5-pro')  # Ensure this model exists
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error generating answer: {e}"

# Example usage:
if __name__ == "__main__":
    query = "What is the meaning of Tzedakah?"
    
    # Step 1: Fetch Sefaria sources
    sources = fetch_sefaria_sources(query)
    print("Sources found:")
    for source in sources:
        print(source)
    
    # Step 2: Get the answer from Gemini
    answer = answer_with_gemini(query, sources)
    print("\nAnswer from Gemini:")
    print(answer)