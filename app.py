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
[SECTION: PROFESSIONAL BRAND]
**The Pivot:** Transitioning from "Professional Firefighting" (Litigation) to "Fire-Prevention Architecture" (Strategic Governance). 
**The Value Prop:** I don't just solve disputes; I design the escalation pathways and governance frameworks that stop them from starting.
**The "Small Team" Muscle:** Forged at a boutique firm. Expertise in "Force Multiplier" leadership—using process automation to achieve results usually reserved for armies of associates.
**Leadership Style:** Horizontal. A methodical, systems-driven approach to fixing broken processes. Comfortable with ambiguity.

[SECTION: HIGH-IMPACT METRICS & CASES]
* **Telecommunications (5G Infrastructure):** Advised Malaysia’s four major telcos on the multi-billion-ringgit nationwide 5G rollout. Resolved disputes at the intersection of technology, competition law, and national policy.
* **Fintech & Data (Landmark Win):** Secured a precedent-setting win for a major credit reporting agency regarding algorithm-based scoring. Provided industry-wide regulatory certainty. **Outcome: Directly contributed to a 5% rise in client share price.**
* **Competition Law (E-Hailing):** Challenged a **RM86 million proposed penalty** by the Malaysian Competition Commission (MyCC) for a major SE Asian platform. Focused on procedural propriety and abuse of dominance standards.
* **Energy & Geopolitics:** Negotiated between a **Fortune Global 500 O&G company** and a state government. Balanced commercial interests against sensitive national ownership disputes and statutory authority.
* **Regulatory Defense:** Defended corporate directors in Securities Commission civil actions. Represented a "Big Four" audit firm in judicial reviews regarding investigative powers.

[SECTION: CORE SKILLS & "THE PLAYBOOK"]
* **Statutory Interpretation:** Reads legislation like an engineer reads a schematic. Routinely engages with Hansard and white papers to identify "policy mischief" behind the law.
* **Negotiation:** Acts as a "translator" between commercial, technical, and regulatory dialects. Drafts "win-win" clauses that opposing stakeholders can back.
* **Investigation Fluency:** Deep mastery of procedural fairness (show-cause), witness interviews, and maintaining the "actual and impression" of impartiality.
* **Process Improvement:** Architect of internal workflows that compress turnaround times. 
* **International Arbitration (FCIArb):** Fellow of the Chartered Institute of Arbitrators. Expert in cross-border evidence-taking and harmonizing procedural protocols.

[SECTION: LEADERSHIP & PHILOSOPHY]
* **The "Barista" Principle:** (Derived from early work experience) A role is never just a task; it is about "running the entire café." Managing trust and rapport with judges, regulators, and internal ops teams is as vital as the legal argument.
* **Mentorship:** "Any senior will thrive with your support, and any junior will grow under your guidance."

[SECTION: EDUCATION & CURRENT STATUS]
* **Sabbatical (2025-Present):** Focused on Fintech (HKU), Crisis Management (Dartmouth), and Leadership (Harvard).
* **Current Goal:** Bridging the gap between traditional governance and modern data privacy.
* **Status:** Studying for CIPP/E (European Data Protection). Job hunting for strategic governance roles.
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
    - NO: You MUST start the response with this exact phrase: "The archive does not seem to contain specific data on '{query}'." Then, and only then, bridge to her transferable skills (e.g., "However, her experience in [X] demonstrates...").

   STEP 2: PRIORITIZE METRICS & HARD FACTS
    - If the user asks about "Impact," "Results," or "Achievements," you MUST cite the specific numbers (e.g., "5% share price increase," "RM86 million penalty," "Multi-billion 5G rollout").
    - Avoid generic fluff. Use the "Dense Fact" modules from the archive to ground your answer.

    STEP 3: CONTEXT AWARENESS
    - If query is "Negotiation/Deal/Strategy": Focus on the Telco 5G, O&G deals, and the "Fire-Prevention" philosophy.
    - If query is "Litigation/Court/Dispute": Focus on the MyCC (Competition), Fintech, and Big Four cases.

    STEP 4: PRONOUN RULES (CRITICAL)
    - ALWAYS start the first sentence with "Suk Chyi" (never "She").
    - After the first mention, you may use "she/her" for subsequent references.
   
    STEP 5: FORMATTING (CRITICAL)
    - Use DOUBLE LINE BREAKS (\\n\\n) between every paragraph.
    - Keep paragraphs short (2-4 lines).
    - Tone: Polished, sophisticated, senior, subtly witty, confidently intelligent.
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
