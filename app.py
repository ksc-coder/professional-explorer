import streamlit as st
import google.generativeai as genai

# --- 1. SETUP ---
# PASTE YOUR KEY INSIDE THE QUOTES BELOW
API_KEY = "AIzaSyBfKwhNCpSyGS8v9W-qBfWlQMEcEQqo0Qo"

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# --- 2. YOUR FULL KNOWLEDGE BASE ---
THE_ARCHIVE = """
Career Overview: Started in a litigation boutique where the margin for error was roughly the size of a misplaced comma. Consistently the smallest team among Chambers & Partners and Legal500-ranked practices. The work was never small; you learned fast or didn’t last. I learned fast.

Core Competencies:
- Statutory Interpretation: Reading legislation like an engineer reads system diagrams—holistically and contextually. Materials: Hansard, white papers, and regulatory consultations.
- Operating in Ambiguity: Arguing from first principles and building tight micro- and macro-level reasoning.
- Advocacy & Persuasion: Tailored messaging based on the 'Parental Rule'—how you ask your dad is never how you ask your mom.
- Conflict Resolution: Objective problem-solving in high-emotion environments; prioritizing settlement and narrowing issues.
- Relationship Building: The 'Barista Lesson'—being a litigator is about running the entire café, earning trust, and building durable partnerships.

Representative Matters:
- Telecommunications: Advised Malaysia’s major telcos on the 5G implementation; resolved multi-billion-ringgit disputes.
- Data & Fintech: Secured a landmark win for algorithm-based credit scoring; led to regulatory certainty and a 5% share-price increase.
- Energy & Geopolitics: Represented a Fortune Global 500® O&G company in high-stakes negotiations with a state government.
- Competition: Acted for a major SE Asian e-hailing platform (Grab) against MyCC in an RM86M penalty dispute.

Strategic Pivot:
- Litigation is firefighting in 99 buildings at once. I am transitioning to designing the fire-prevention architecture and governance frameworks.
- Sabbatical Focus: Blockchain ethics (HKU), Crisis Management (Dartmouth), and Cross-functional Leadership (Harvard).
- Current Focus: European data protection (CIPP/E).
"""

# --- 3. UI STYLING ---
st.set_page_config(page_title="Suk Chyi: Interactive Experience Explorer", layout="centered")

st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700&display=swap');
    
    .stApp {{
        background-color: #2f4f4e; /* Executive green-grey */
        color: #E0E0E0;
        font-family: 'Montserrat', sans-serif;
    }}
    
    .stTextInput>div>div>input {{
        background-color: #3e615f;
        color: #E0E0E0;
        border: 1px solid #a3c1b0;
        border-radius: 4px;
    }}
    
    .response-box {{
        background-color: rgba(255, 255, 255, 0.05);
        padding: 25px;
        border-left: 4px solid #a3c1b0;
        margin-top: 20px;
        line-height: 1.6;
    }}
    
    h1, h2, h3, h5 {{
        color: #E0E0E0;
        font-family: 'Montserrat', sans-serif;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 4. THE INTERFACE ---
st.title("Suk Chyi: Interactive Experience Explorer")
st.markdown("##### *Your experience, made searchable. Your judgment, made legible.*")

query = st.text_input("Enter a keyword, skill, or industry...", placeholder="e.g. 5G, Ambiguity, or First Principles")

if query:
    system_prompt = f"Using this Archive: {THE_ARCHIVE}, explain the experience related to '{query}' in a crisp, senior, and thoughtful tone. Map transferrable capabilities and mention 2 related keywords. End with: 'For clarifications, contact Suk Chyi at: www.linkedin.com/in/khoosukchyi'."
    
    with st.spinner("Retrieving signal..."):
        try:
            response = model.generate_content(system_prompt)
            st.markdown(f'<div class="response-box">{{response.text}}</div>', unsafe_allow_html=True)
        except Exception as e:
            st.error("Check your API key in the code.")

st.divider()
st.caption("Not a CV. Not a chatbot. A precision retrieval engine.")
