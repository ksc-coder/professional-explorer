import streamlit as st
import google.generativeai as genai

# --- 1. THE ENGINE ---
# PASTE YOUR KEY EXACTLY INSIDE THE QUOTES
API_KEY = "AIzaSyBfKwhNCpSyGS8v9W-qBfWlQMEcEQqo0Qo"

try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("Engine failed to start. Please check your API key.")

# --- 2. THE ARCHIVE (Your Knowledge Base) ---
THE_ARCHIVE = """
Foundational Experience:
- Started in a litigation boutique; smallest team among Chambers & Partners/Legal500-ranked practices[cite: 4].
- Margin for error measured in microns; learned fast[cite: 4, 7].
- Reading legislation like an engineer reads system diagrams: holistically and contextually [cite: 12-14].
- Fluent in 'domain dialects' across legal, engineering, finance, and operations[cite: 55].

Key Impacts:
- 5G Implementation: Advised Malaysia’s 4 major telcos; multi-billion-ringgit disputes [cite: 90-91].
- Credit Scoring: Landmark win for algorithm-based models; 5% share-price increase [cite: 94-95].
- Energy: Fortune Global 500® O&G negotiations vs. state government [cite: 97-98].
- Competition: Defended Southeast Asian e-hailing platform in RM86M penalty dispute [cite: 100-101].

The Operating System:
- The 'Parental Rule': Message calibration based on audience [cite: 38-39].
- The 'Barista Lesson': Practice is about running the entire café—trust, rapport, and partnership [cite: 65-70].
- Firefighting vs. Architecture: Transitioning from fighting 99 fires to designing the fire-prevention architecture [cite: 132-136].
- Current: Mastering European data protection (CIPP/E)[cite: 147].
"""

# --- 3. THE LUXE UI STYLING ---
st.set_page_config(page_title="Suk Chyi | Experience Explorer", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
    
    .stApp {
        background-color: #0F1115; /* Deep Charcoal */
        color: #FFFFFF;
        font-family: 'Inter', sans-serif;
    }
    .stTextInput>div>div>input {
        background-color: #1A1D23;
        color: #FFFFFF;
        border: 1px solid #333A45;
        border-radius: 8px;
        padding: 12px;
    }
    .response-box {
        background-color: #1A1D23;
        padding: 30px;
        border: 1px solid #333A45;
        border-radius: 12px;
        margin-top: 25px;
        line-height: 1.8;
        font-weight: 300;
    }
    h1 { font-weight: 600; letter-spacing: -1px; }
    .highlight { color: #8E9AAF; font-weight: 600; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. THE INTERFACE ---
st.title("Suk Chyi")
st.markdown("<p style='color: #8E9AAF;'>Interactive Experience Explorer</p>", unsafe_allow_html=True)
st.markdown("---")

query = st.text_input("Search by concept, industry, or skill...", placeholder="Try 'Ambiguity', '5G', or 'First Principles'")

if query:
    system_prompt = f"""
    Context: {THE_ARCHIVE}
    User Query: {query}
    Instruction: Act as a precision retrieval engine. 
    Tone: Crisp, senior, and thoughtful[cite: 200]. 
    Format: 
    1. Direct answer using specific phrasing (microns, firefighting, etc.).
    2. 'Transferable Capability' section.
    3. 'Related Keywords' section.
    """
    
    with st.spinner("Extracting signal..."):
        try:
            response = model.generate_content(system_prompt)
            st.markdown(f'<div class="response-box">{response.text}</div>', unsafe_allow_html=True)
        except:
            st.error("Check your API key. It may be typed incorrectly or inactive.")

st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("Your experience, made searchable. Your judgment, made legible. [cite: 225]")
