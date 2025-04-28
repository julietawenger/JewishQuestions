# Jewish Texts Question Answering App

This app uses a language model (Gemini API) fine-tuned on Jewish texts (e.g., Torah, Talmud) to answer user questions based on the sources.

## Features
- **Question Answering:** Ask questions about Jewish texts, and get answers sourced directly from relevant passages in the Torah, Talmud, and more.
- **References Provided:** The app provides references to the sources used for generating the answer.

## Setup

### 1. Clone the repository
```bash
git clone <repository_url>
cd <repository_name>
```
### 2. Set up your virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Set up environment variables
Create a ```.env``` file in the project root and add your Google API Key.
```bash
GOOGLE_API_KEY=your-google-api-key
```
### 5. Run the app
```bash
Start the Streamlit app:
```
### Model Information

This app uses Gemini API for generating responses based on Jewish texts. The sources used for answering the questions are retrieved from the Sefaria API.

## License
This project is licensed under the MIT License.
