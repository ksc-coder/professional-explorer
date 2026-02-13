import streamlit as st
import google.generativeai as genai
import google.api_core.exceptions as exceptions
import os

# --- 1. THE ENGINE ---
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    st.error("Connection Error: The API Key is not configured in Secrets.")
    st.stop()

try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-flash-latest')
except Exception as e:
    st.error(f"Engine failed to start: {e}")

# --- 2. KNOWLEDGE BASE ---
THE_ARCHIVE = """
Professional Knowledge Base (Markdown)

1. The Executive Narrative (The "Why")
**From Firefighting to Architecture:**
"Litigation is the professional equivalent of firefighting in 99 buildings at once. I’m ready to sit at the table designing the fire-prevention architecture, the escalation pathways, and the governance frameworks that stop the fires from starting."
**The Value Proposition:**
I don't just argue the law; I translate it. I bridge the gap between rigid regulatory frameworks and fluid commercial goals. My background is in high-stakes dispute resolution, which means I have been trained to identify the point of failure before a project even launches.

2. Strategic Impact & Commercial Value (The "What")
* **Regulatory Strategy (5G Implementation):** Advised Malaysia’s four major telcos on nationwide 5G rollout. This wasn't just a legal dispute; it was a multi-billion-ringgit alignment of technology, competition policy, and national infrastructure.
    * *Skill:* Navigating the intersection of public policy and private commercial interest.
* **Commercial Certainty (Fintech/CTOS):** Secured a landmark win validating algorithm-based credit scoring.
    * *Impact:* Provided industry-wide regulatory certainty and directly contributed to a **5% rise in share price** for the client.
    * *Takeaway:* Legal strategy that drives tangible market value.
* **Crisis Management (Antitrust/MyCC):** Managed a high-profile challenge against a proposed **RM86 million penalty** for a major Southeast Asian e-hailing platform.
    * *Focus:* Procedural propriety and checking investigative overreach.
    * *Skill:* Keeping cool when the numbers are large and the timeline is short.
* **Geopolitical Negotiation (Energy):** Acted for a Fortune Global 500® O&G company in sensitive negotiations with a state government involving national resource ownership.
    * *Skill:* Balancing statutory interpretation with diplomatic nuance.

3. The "Operating System" (The "How")
* **The "Small Team" Efficiency:** Bred in a boutique firm where we were consistently the smallest team against the biggest names.
    * *Result:* I treat process as a force multiplier. I build workflows to compress turnaround times and automate admin so I can focus on strategy. I don't need an army; I need a plan.
* **The "Barista" Principle:** (Derived from early work experience). "Being a barista isn’t just about making coffee; it’s about running the café."
    * *Application:* In-house, this means I don't just "do legal." I view the business holistically—understanding how a contract affects Ops, Finance, and Sales.
* **Interpretation Philosophy:** I read legislation the way engineers read schematics: holistically and structurally. I look for the "mischief" (policy intent) behind the rule, not just the literal text.

4. Functional Competencies
* **Investigation Fluency:** Deep experience in the architecture of investigations—identifying the limits of power, ensuring procedural fairness, and conducting witness interviews that separate signal from noise.
* **Stakeholder Management:** Frequently served as the "translator" between technical teams (engineers), commercial teams (C-suite), and regulatory bodies. I draft language that aligns divergent interests.
* **Cross-Border Agility:** Fellow of the Chartered Institute of Arbitrators (FCIArb). Expert in harmonizing differing procedural rules and navigating international enforcement.

5. Future Focus & Upskilling (2025-Present)
* **Current Status:** Transitioning from practice to strategic/in-house roles.
* **Sabbatical Focus:** Bridging the gap between traditional law and future tech.
    * *Fintech:* Blockchain ethics and asset compliance (HKU).
    * *Crisis Comms:* Strategic reputational risk (Dartmouth).
    * *Data Privacy:* Preparing for CIPP/E (European Data Protection).

6. The Executive Playbook (Transferable Skills)
* **Adaptability:** Trained to rotate across industries, geographies, and functions on the fly. Accustomed to mastering unfamiliar businesses (from O&G to Fintech) rapidly.
* **Problem Disaggregation:** Mastered the art of breaking "sprawling, messy problems" into solvable parts. Sharpened judgment through high-stakes pattern recognition.
* **No Job Too Small:** Being in a small team meant no room for ego. I have rolled up my sleeves for everything from bundling documents to Board meetings—approaching both with the same standard of care.
* **Systems-Driven Leadership:** My default mode is to fix what is broken, reimagine what is possible, and scale what works. I bring a horizontal approach to leadership and a high comfort with ambiguity.
"""

# --- 3. DESIGN ---
st.set_page_config(page_title="KSC | Professional Experience Explorer", layout="centered")

st.markdown("""
<style>
body { background-color: white; }

.block-container {
    max-width: 750px !important;
    padding-top: 2rem !important;
    padding-bottom: 2rem !important;
}

/* Typography */
.name-title {
    font-size: 45px; font-weight: 700; color: #6f6f6f; margin-bottom: 5px; text-align: left;
}
.main-title {
    font-size: 32px; font-weight: 700; color: black; margin-bottom: 25px; text-align: left;
}
.instruction {
    font-size: 20px; font-weight: 600; color: #6f6f6f; margin-bottom: 15px; text-align: left;
}

/* Search Input Styling */
input.stTextInput {
    border-radius: 10px !important;
    border: 1px solid #E2E8F0 !important;
    padding: 14px !important;
    background-color: #F8FAFC !important;
    color: #1E293B !important;
}
/* Focus State - Green/Grey to match request */
input.stTextInput:focus {
    border-color: #94a3b8 !important;
    box-shadow: 0 0 0 2px rgba(148, 163, 184, 0.2) !important;
}
input::placeholder {
    color: black !important; opacity: 1; font-size: 18px;
}

/* Result Box */
.response-box {
    background-color: #F8FAFC;
    padding: 30px;
    border-radius: 12px;
    border: 1px solid #F1F5F9;
    line-height: 1.8;
    color: #334155;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    margin-top: 30px;
}
/* Paragraph spacing fix */
.response-box p {
    margin-bottom: 1.5em; /* Force space between paragraphs */
}
.response-box ul { margin-top: 10px; padding-left: 20px; }
.response-box li { margin-bottom: 5px; }

/* Footer & Relocated Paragraphs */
.bottom-container { margin-top: 60px; border-top: 1px solid #F1F5F9; padding-top: 20px; padding-bottom: 40px; }
.disclaimer-large { font-size: 18px; font-weight: 700; color: #475569; margin-bottom: 10px; }
.description-body { font-size: 15px; color: #64748b; line-height: 1.6; margin-bottom: 10px; }
.contact-small { font-size: 14px; color: #6f6f6f; margin-top: 0; }
a { text-decoration: none; color: #6f6f6f; }
a:hover { text-decoration: underline; }

/* Hide Streamlit Default Elements */
div[data-testid="stToolbar"] { visibility: hidden; height: 0%; position: fixed; }
div[data-testid="stDecoration"] { visibility: hidden; height: 0%; position: fixed; }
div[data-testid="stStatusWidget"] { visibility: hidden; height: 0%; position: fixed; }
#MainMenu { visibility: hidden; height: 0%; }
header { visibility: hidden; height: 0%; }
footer { visibility: hidden; height: 0%; }
/* Animated underline for LinkedIn link */
a.linkedin-link {
    position: relative;
    text-decoration: none;
}

a.linkedin-link::after {
    content: "";
    position: absolute;
    left: 0;
    bottom: -2px;
    width: 0%;
    height: 1px;
    background-color: #6f6f6f;
    transition: width 0.25s ease-out;
}

a.linkedin-link:hover::after {
    width: 100%;
}
/* Ensure white background on all devices */
body { 
    background-color: white !important; 
}

.stApp {
    background-color: white !important;
}

.main {
    background-color: white !important;
}

[data-testid="stAppViewContainer"] {
    background-color: white !important;
}
/* Force all Streamlit text inputs to be white on all devices */
input, textarea {
    background-color: #FFFFFF !important;
    color: black !important;
}

/* Streamlit text input wrapper */
.stTextInput > div > div {
    background-color: #FFFFFF !important;
    border: 1px solid #E2E8F0 !important;
    border-radius: 10px !important;
}

/* iOS/Android autofill overrides */
input:-webkit-autofill {
    -webkit-box-shadow: 0 0 0px 1000px white inset !important;
    box-shadow: 0 0 0px 1000px white inset !important;
}

/* Extra selector to catch mobile WebKit rendering */
input[type="text"] {
    background-color: white !important;
    -webkit-appearance: none !important;
}

/* Override dark-mode user agent styling on mobile */
@media (prefers-color-scheme: dark) {
    input, textarea {
        background-color: white !important;
        color: black !important;
        -webkit-text-fill-color: black !important;
    }
}
/* Mobile loading banner */
.loading-banner {
    display: none;
    background: #F1F5F9;
    padding: 12px 18px;
    border-radius: 8px;
    margin-top: 20px;
    font-size: 15px;
    color: #475569;
    border: 1px solid #E2E8F0;
}
</style>
""", unsafe_allow_html=True)

# --- 4. UI LAYOUT ---
st.markdown('<div class="name-title">KHOO SUK CHYI</div>', unsafe_allow_html=True)
st.markdown('<div class="main-title">Interactive Professional Experience Explorer</div>', unsafe_allow_html=True)
st.markdown('<div class="instruction">Enter a keyword, skill, or industry (e.g., “strategy”, “policy”, “negotiation”) </div>', unsafe_allow_html=True)

# SEARCH INPUT
query = st.text_input("", placeholder="Start typing here ...", label_visibility="collapsed")

# --- 5. LOGIC & GENERATION ---

# Mobile loading banner placeholder (hidden until JS shows it)
loading_placeholder = st.markdown(
    '<div class="loading-banner" id="mobile-loading">Analyzing experience...</div>',
    unsafe_allow_html=True
)

if query:
    # Force loading banner to appear instantly on mobile
    st.markdown("""
        <script>
        const banner = window.parent.document.getElementById('mobile-loading');
        if (banner) { banner.style.display = 'block'; }
        </script>
        """,
        unsafe_allow_html=True
    )
    
    system_prompt = f"""
    ROLE: You are a senior executive advisor for Suk Chyi.
    
    STEP 1: CHECK FOR DATA EXISTENCE
    - Does the specific term "{query}" appear in the Archive?
    - YES: Proceed to describe her experience directly.
    - NO: You MUST start the response with this exact phrase: "The archive does not seem to contain specific data on '{query}'." 
          THEN, pivot immediately to Section 6 (The Executive Playbook). 
          Explain that while she may not have that specific keyword, her "muscle memory" is shaped by high-stakes intensity. 
          Use these specific phrases: 
          - "Trained to rotate across industries and master unfamiliar businesses on the fly."
          - "Rolled up her sleeves for everything from bundling to Board meetings."
          - "A methodical, systems-driven approach to breaking messy problems into solvable parts."

   STEP 2: CONTEXTUAL REFRAMING (CRITICAL)
    - **If query is about "Litigation/Court":** Discuss the cases (MyCC, Federal Court) as legal victories.
    - **If query is about "Strategy/In-House/Management":** Reframe the litigation experience as "Risk Management" and "Crisis Prevention." Focus on the *commercial impact* (e.g., the 5% share price, the 5G rollout) rather than the legal argument. 
    - **If query is about "Why/Transition":** Use the "Firefighting vs. Architecture" narrative.

    STEP 3: PRONOUN RULES (CRITICAL)
    - ALWAYS start the first sentence with "Suk Chyi" (never "She").
    - After the first mention, you may use "she/her" for subsequent references.
   
    STEP 4: FORMATTING (CRITICAL)
    - Use DOUBLE LINE BREAKS (\\n\\n) between every paragraph.
    - Keep paragraphs short (2-4 lines).
    - Tone: Polished, sophisticated, senior, subtly witty, confidently intelligent. Avoid "resume speak"—sound like a peer discussing a colleague.
    - Treat the user as a peer (another executive), not a junior.

    ARCHIVE:
    {THE_ARCHIVE}
    
    QUERY: "{query}"
    """

    # ------------------------------
    # Correct indentation begins here
    # ------------------------------
    with st.spinner("Analyzing experience..."):
        try:
            response = model.generate_content(system_prompt)
            if response.text:
                st.markdown(
                    f'<div class="response-box">{response.text}</div>',
                    unsafe_allow_html=True
                )
        # 1. SPECIFIC CATCH: The Quota Limit (429 Error)
        except exceptions.ResourceExhausted:
            st.markdown(
                """
                <div class="response-box" style="border-left: 4px solid #94a3b8; background-color: #f1f5f9;">
                    As the saying goes: <strong>休息是为了走更长远的路</strong> — 
                    a little pause now fuels the journey ahead. The Explorer is taking that moment. 
                    It’ll be back shortly.
                </div>
                """, 
                unsafe_allow_html=True
            )

        # 2. GENERAL CATCH: All other errors (Connection, etc.)
        except Exception as e:
            st.error(f"Something went wrong. Technical details: {e}")

    # Hide banner once the model finishes (or fails)
    st.markdown("""
        <script>
        const banner = window.parent.document.getElementById('mobile-loading');
        if (banner) { banner.style.display = 'none'; }
        </script>
        """,
        unsafe_allow_html=True
    )

# --- 6. RELOCATED BOTTOM CONTENT ---
st.markdown(f"""
    <div class="bottom-container">
        <div class="disclaimer-large">A note on method — and audacity:</div>
        <div class="description-body">
            This document is not a credential. It is an attempt at one.<br>
            The premise: if you can architect knowledge for an AI — structure signal, strip noise, anticipate how it will be read and misread — you can probably architect it for a regulator, a boardroom, or a cross-functional task force. Same muscle. Different domain.<br>
            Is it perfect? Absolutely not. But sending it anyway, in this form, to you? That takes a certain kind of confidence.<br>
            Call it gall. Call it conviction. Either way, it should score for effort — and effort, in the right hands, is simply strategy in motion.
        </div>
        <div class="contact-small">
            NB: There are enough em-dashes here to flag this as AI-touched. For clarification, confirmation, or the graceful correction of any hallucination, please contact Suk Chyi directly at:
            <a href="https://www.linkedin.com/in/khoosukchyi" class="linkedin-link" target="_blank">www.linkedin.com/in/khoosukchyi</a>.
        </div>
    </div>
    """, unsafe_allow_html=True)
