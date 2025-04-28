import streamlit as st
from utils import fetch_sefaria_sources, answer_with_gemini

st.set_page_config(page_title="JewishQuestions: Torah & Talmud Answers", page_icon="🕍")

st.title("🕍 JewishQuestions: Torah and Talmud Q&A")
st.markdown("Ask any question about the Tanach or Gemara. We'll answer with real sources!")

# Input box
user_question = st.text_input("What would you like to ask?", placeholder="e.g., What does the Torah say about Shabbat?")

if st.button("Get Answer") and user_question:
    with st.spinner("Searching for sources..."):
        sources = fetch_sefaria_sources(user_question)
    
    st.subheader("📖 Sources Found:")
    for src in sources:
        st.markdown(f"- {src}")
    
    with st.spinner("Generating answer..."):
        answer = answer_with_gemini(user_question, sources)
    
    st.subheader("📝 Answer:")
    st.markdown(answer)

st.sidebar.title("About")
st.sidebar.info(
    """
    **JewishQuestions** is a Torah and Talmud Q&A app built using Streamlit, Sefaria API, and Gemini.
    
    - 🔍 Sources from Sefaria
    - 🤖 Reasoning by Gemini Pro
    """
)
