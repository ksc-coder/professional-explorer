import streamlit as st
import google.generativeai as genai

# --- 1. SETUP ---
# PASTE YOUR KEY INSIDE THE QUOTES BELOW
API_KEY = "AIzaSyBfKwhNCpSyGS8v9W-qBfWlQMEcEQqo0Qo"

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# --- 2. YOUR FULL KNOWLEDGE BASE ---
THE_ARCHIVE = """
1. [cite_start]Career Overview: Began in a litigation boutique where the margin for error was roughly the size of a misplaced comma. Consistently the smallest team among Chambers & Partners and Legal500-ranked practices. The work was never small. Learned fast. Foundation built on precision, pace, and judgment [cite: 4-8].

2. Core Competencies: 
- [cite_start]Statutory Interpretation: Reading legislation like an engineer reads system diagrams—holistically and contextually [cite: 11-15]. 
- [cite_start]Ambiguity: Arguing from first principles; identifying unintended consequences before they surface [cite: 23-29].
- [cite_start]Advocacy: Messaging tailored to the audience—the "Parental Rule" of calibration [cite: 30-39].
- [cite_start]Negotiation: Serving as a "translator" between legal, technical, commercial, and policy domains [cite: 40-44].
- [cite_start]Conflict Resolution: Prioritizing settlement and narrowing issues pragmatically [cite: 56-62].
- Relationships: The "Barista Lesson"—being a litigator is about running the entire café, not just making coffee. [cite_start]It's about earning trust and rapport [cite: 63-70].

3. Arbitration: Fellow of the Chartered Institute of Arbitrators (FCIArb). [cite_start]Expert in cross-border disputes, procedural fairness, and harmonizing competing protocols [cite: 71-77].

4. Leadership: Managed junior members as a Senior Associate. Mentored by Dato’ Malik Imtiaz Sarwar. [cite_start]Aiming to be "the senior I once needed" [cite: 78-81].

5. Key Impacts:
- [cite_start]Telco: Advised Malaysia’s major telcos on 5G implementation; resolved multi-billion-ringgit disputes [cite: 89-92].
- Fintech: Secured landmark win for algorithm-based credit scoring; [cite_start]5% share-price increase [cite: 93-95].
- [cite_start]Energy: Negotiated for a Fortune Global 500® O&G company against a state government [cite: 96-98].
- [cite_start]Competition: Acted for Grab against MyCC in RM86M penalty dispute [cite: 99-102].
- [cite_start]Regulatory: Defended directors in Securities Commission civil actions [cite: 103-105].

6. Strategy & Transition: Litigation is firefighting in 99 buildings at once. [cite_start]Transitioning to design the fire-prevention architecture and governance frameworks [cite: 132-137].

7. [cite_start]Sabbatical (Since Sept 2025): Focusing on Blockchain ethics (HKU), Crisis Management (Dartmouth), and Leadership (Harvard) [cite: 138-144]. [cite_start]Currently studying European data protection (CIPP/E)[cite: 147].
"""

# --- 3. UI STYLING (Branding from Public Facing Package) ---
st.set_page_config(page_title="Suk Chyi: Interactive Experience Explorer", layout="centered")

st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700&display=swap');
    
    /* Background and Text Colors */
    .stApp {{
        background-color: #2f4f4e; /* Executive green-grey */
        color: #E0E0E0;
        font-family: 'Montserrat', sans-serif;
    }}
    
    /* Search Bar Styling */
    .stTextInput>div>div>input {{
        background-color: #3e615f;
        color: #E0E0E0;
        border: 1px solid #a3c1b0;
        border-radius: 4px;
    }}
    
    /* Response Box Styling */
    .response-box {{
        background-color: rgba(255, 255, 255, 0.05);
        padding: 25px;
        border-left: 4px solid #a3c1b0;
        margin-top: 20px;
        line-height: 1.6;
    }}
    
    h1, h2, h3 {{
        color: #E0E0E0;
        font-family: 'Montserrat', sans-serif;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 4. THE INTERFACE ---
st.title("Suk Chyi: Interactive Experience Explorer")
[cite_start]st.markdown("##### *Your experience, made searchable. Your judgment, made legible.* [cite: 225]")

query = st.text_input("Enter a keyword, skill, or industry (e.g. '5G', 'Ambiguity', 'First Principles')", placeholder="Start typing...")

if query:
    # This prompt forces the AI to use your specific tone and citations
    system_prompt = f"""
    You are the 'Suk Chyi: Interactive Experience Explorer'. 
    Tone: Crisp, Senior, Thoughtful. [cite_start]A 'breath of fresh air'[cite: 200].
    
    Task:
    Search the provided Archive for '{query}'. 
    - Use the user's specific phrasing (microns, engineer's diagrams, firefighting).
    - Map transferrable capabilities clearly.
    - Provide a concise synthesis of Suk Chyi's operating style.
    - Mention 2 related keywords at the end.
    - [cite_start]End with: 'For clarifications, contact Suk Chyi at: www.linkedin.com/in/khoosukchyi'[cite: 222].

    Archive:
    {THE_ARCHIVE}
    """
    
    with st.spinner("Retrieving signal..."):
        try:
            response = model.generate_content(system_prompt)
            st.markdown(f'<div class="response-box">{response.text}</div>', unsafe_allow_html=True)
        except Exception as e:
            st.error("Check your API key in the code.")

st.divider()
[cite_start]st.caption("Not a CV. Not a chatbot. A precision retrieval engine. [cite: 207, 229]")
