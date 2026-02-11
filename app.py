import streamlit as st
import google.generativeai as genai

# --- 1. THE ENGINE ---
# PASTE YOUR KEY INSIDE THESE QUOTES
API_KEY = "AIzaSyAIoY9lyAcDt1aOxwPfd8Eft9SXgd0rV_0"

try:
    genai.configure(api_key=API_KEY)
    # Using the most stable model name to avoid the 404 error
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception:
    st.error("Engine failed to start. Please check your API key in the code.")

# --- 2. YOUR KNOWLEDGE BASE ---
# Paste the content of your 'Markdown Knowledge Base.docx' here.
# Keep the triple quotes ( \"\"\" ) at the top and bottom.
THE_ARCHIVE = """
PASTE YOUR WORD DOCUMENT TEXT HERE
"""

# --- 3. LIGHT MODE UI STYLING ---
st.set_page_config(page_title="Suk Chyi | Experience Explorer", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
    
    .stApp {
        background-color: #FFFFFF; /* Clean White */
        color: #1E293B; /* Slate Grey Text */
        font-family: 'Inter', sans-serif;
    }
    
    .stTextInput>div>div>input {
        background-color: #F8FAFC; 
        border: 1px solid #E2E8F0;
        border-radius: 10px;
        padding: 15px;
        color: #1E293B;
    }
    
    .response-box {
        background-color: #F8FAFC;
        padding: 30px;
        border-radius: 12px;
        border: 1px solid #F1F5F9;
        line-height: 1.8;
        color: #334155;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    
    h1 { color: #0F172A; font-weight: 600; }
    
    /* Footer Styling */
    .footer {
        font-size: 0.85rem;
        color: #64748B;
        margin-top: 50px;
        border-top: 1px solid #E2E8F0;
        padding-top: 20px;
    }
    a { color: #2563EB; text-decoration: none; }
    a:hover { text-decoration: underline; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. THE INTERFACE ---
st.title("Khoo Suk Chyi")
st.markdown("<p style='color: #64748B;'>Interactive Professional Experience Explorer</p>", unsafe_allow_html=True)

query = st.text_input("Enter a keyword, skill, or industry (e.g. '5G', 'Arbitration', 'Ambiguity')", 
                      placeholder="Start typing here...")

if query:
    # This prompt tells the AI to behave as your "Explorer"
    system_prompt = f"""
    Using only the professional archive below, answer the query '{query}'.
    
    Guidelines:
    1. Use the specific phrasing from the archive (e.g., microns, engineer's diagrams, firefighting).
    2. Map transferrable capabilities clearly.
    3. Maintain a senior, crisp, and professional tone.
    4. If the information isn't in the archive, say you don't have specific data on that.
    
    Archive:
    {THE_ARCHIVE}
    """
    
    with st.spinner("Analyzing Experience..."):
        try:
            response = model.generate_content(system_prompt)
            st.markdown(f'<div class="response-box">{response.text}</div>', unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Something went wrong. Technical details: {e}")

# --- 5. THE NEW DISCLAIMER & FOOTER ---
st.markdown(f"""
    <div class="footer">
        <p>A high-signal, interactive map of a legal and regulatory career, based only upon the uploaded knowledge base. 
        It is neither a CV nor a chatbot.</p>
        <p>It does not generate new experience or make unverifiable claims.</p>
        <p>For clarifications or confirmation of any output, please contact Suk Chyi directly at:<br>
        <a href="https://www.linkedin.com/in/khoosukchyi" target="_blank">www.linkedin.com/in/khoosukchyi</a></p>
    </div>
    """, unsafe_allow_html=True)
