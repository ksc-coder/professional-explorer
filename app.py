import streamlit as st
import google.generativeai as genai
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
1. Career Overview
I began my career in a litigation boutique where the margin for error was roughly the size of a misplaced comma.
We were consistently the smallest team among Chambers & Partners and Legal500-ranked practices, which meant two things:
1. The work was never small.
2. You learned fast or you didn’t last.
I learned fast.
My foundation was built in environments where precision, pace, and judgment mattered more than headcount. The work required moving seamlessly between statutory text, policy intent, commercial incentives, and human behaviour — often under tight timelines and high scrutiny.

2. Core Competencies
2.1 Statutory & Policy Interpretation
I read legislation the way engineers read system diagrams:
• Holistically
• Contextually
• With an eye on the underlying mischief and policy intent
Regular materials included: Hansard, Parliamentary debates, White papers, Task force reports, Regulatory consultations.
I frequently worked with NGOs, regulators, and think tanks — the policy ecosystem behind the black-letter law.

2.2 Operating in Ambiguity
Trained to:
• Argue from first principles
• Build tight micro- and macro-level reasoning
• Anticipate industry-wide impacts
• Identify unintended consequences before they surface
Ambiguity wasn’t a roadblock; it was the starting point.

2.3 Advocacy & Persuasion
Strong oral and written advocacy, tailored to: Judges, Regulators, C-suite, Cross-functional teams.
My former boss once said: "How you ask your dad is never how you ask your mom."
A memorable way of teaching message-audience calibration — a skill that has since become a core part of my operating system.

2.4 Negotiation & Stakeholder Alignment
I frequently served as: Primary negotiator, Front-line point of contact, Translator between legal, technical, commercial, and policy domains.
I draft contractual language that brings together divergent commercial, technical, and regulatory interests — framing clauses that opposing stakeholders can still get behind. My role was to bridge gaps, align incentives, and steer fragmented groups toward a shared, practical outcome.

2.5 Cross-Functional Problem Solving
Worked closely with: Instructing solicitors, Engineering teams, Finance, Operations, Sales, Regulators.
The job required multilingual fluency — not in literal languages, but in domain “dialects.”

2.6 Conflict Resolution
Grounded in the true purpose of dispute resolution: Prioritise settlement where possible, Establish common ground, Narrow issues pragmatically, Keep sight of the bigger picture.
One of the most profound professional muscles I developed: objective problem-solving in high-emotion environments.

2.7 Relationship Building
I once worked part-time as a barista.
Lesson learned from my manager: "Being a barista isn’t just about making coffee — it’s about running the entire café."
Practice was the same. It wasn’t just about arguing cases. It was about earning trust, building rapport, and forming durable partnerships with judges, regulators, and opposing counsel.

3. Arbitration Expertise (FCIArb)
As a Fellow of the Chartered Institute of Arbitrators, I built expertise in: Complex cross-border disputes, Evidence-taking standards, Procedural fairness, Harmonising competing rules, Evaluating remedies.

4. Leadership & Mentorship
As a Senior Associate, I managed and supervised junior team members.
I was mentored by exceptional seniors, including Dato’ Malik Imtiaz Sarwar — and I’ve always aimed to be the senior I once needed.
A junior once told me: "Any senior will thrive with your support, and any junior will grow under your guidance."
Across 9+ years, I had front-row access to strategy, thought leadership, and principled advocacy.

5. Key Impacts & Representative Matters

[CATEGORY: NEGOTIATION & STRATEGY]
Telecommunications & Infrastructure: Advised Malaysia’s four major telcos on nationwide 5G implementation. Resolved multi-billion-ringgit disputes at the intersection of technology, law, and policy.
Energy & Geopolitics: Represented a Fortune Global 500® O&G company in sensitive negotiations with a state government. Navigated statutory, commercial, and geopolitical complexities.
Corporate Governance: Advised on director liabilities, auditors’ duties, and internal governance for MNCs and GLCs.

[CATEGORY: LITIGATION & JUDICIAL REVIEW]
Data & Fintech: Secured a landmark win affirming the legality of an algorithm-based credit scoring model (CTOS). Resulted in regulatory certainty and contributed to a 5% share-price increase.
Competition & Antitrust: Acted for a major Southeast Asian e-hailing platform (Grab) in judicial review against MyCC challenging an RM86M penalty. Focused on procedural fairness.
Regulatory Enforcement: Lead associate in Securities Commission civil actions. JR for Big Four audit firm challenging investigative findings.
Appellate Advocacy: Regularly appeared before the Federal Court.

6. Strategic Capabilities
Trained to rotate across industries, geographies, and functions with minimal ramp-up.
Core strengths include: Deconstructing sprawling problems, Reassembling them into solvable parts, Driving alignment across sceptical or siloed stakeholders.
Clear, structured thinking was non-negotiable.

7. Executive Operating System
Where I lack a specific experience, I bring a transferable playbook shaped by high-stakes decision environments: Systems-driven diagnostics, Methodical problem framing, Comfort with ambiguity, A horizontal cross-domain leadership style.

8. Career Transition Rationale
Litigation is the professional equivalent of firefighting in 99 buildings at once.
I’m ready to sit at the table designing the fire-prevention architecture, the escalation pathways, and the governance frameworks that stop the fires from starting.
This isn’t a step back — it’s a step toward strategic impact.

9. Sabbatical (Since September 2025)
Focus: Fintech & Digital Assets (HKU), Crisis Management (Dartmouth), Leadership (Harvard), Digital Fluency (Binance).
Goal: Bridge traditional legal practice with the future of regulation.

10. Current Focus
Studying European data protection (CIPP/E). Job-hunting for roles in governance, accountability, risk, and structured problem-solving.
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
    font-size: 40px; font-weight: 700; color: #6f6f6f; margin-bottom: 5px; text-align: left;
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
.bottom-container { margin-top: 60px; border-top: 1px solid #F1F5F9; padding-top: 20px; }
.disclaimer-large { font-size: 18px; font-weight: 700; color: #475569; margin-bottom: 10px; }
.description-body { font-size: 15px; color: #64748b; line-height: 1.6; margin-bottom: 20px; }
.contact-small { font-size: 14px; color: #6f6f6f; margin-top: 12px; }
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
</style>
""", unsafe_allow_html=True)

# --- 4. UI LAYOUT ---
st.markdown('<div class="name-title">KHOO SUK CHYI</div>', unsafe_allow_html=True)
st.markdown('<div class="main-title">Interactive Professional Experience Explorer</div>', unsafe_allow_html=True)
st.markdown('<div class="instruction">Enter a keyword, skill, or industry (e.g., "strategy", "policy", "negotiation") </div>', unsafe_allow_html=True)

# SEARCH INPUT
query = st.text_input("", placeholder="Start typing here ...", label_visibility="collapsed")

# --- 5. LOGIC & GENERATION ---
if query:
    system_prompt = f"""
    ROLE: You are a senior executive advisor for Suk Chyi.
    
    STEP 1: CHECK FOR DATA EXISTENCE
    - Does the specific term "{query}" appear in the Archive?
    - YES: Proceed to describe her experience directly.
    - NO: You MUST start the response with this exact phrase: "The archive does not seem to contain specific data on '{query}'." Then, and only then, bridge to her transferable skills (e.g., "However, her experience in [X] demonstrates...").

    STEP 2: CHECK FOR CONTEXT (NEGOTIATION VS LITIGATION)
    - If query is "Negotiation/Deal/Strategy": EXCLUDE court judgments (e.g., MyCC, CTOS). Focus on the Telco 5G and O&G deals.
    - If query is "Litigation/Court/Dispute": INCLUDE the court judgments.

    STEP 3: FORMATTING (CRITICAL)
    - Use DOUBLE LINE BREAKS (\\n\\n) between every paragraph.
    - Keep paragraphs short (2-4 lines).
    - Tone: Polished, sophisticated, senior. Use "she/her".

    ARCHIVE:
    {THE_ARCHIVE}
    
    QUERY: "{query}"
    """

    with st.spinner("Analyzing experience..."):
        try:
            response = model.generate_content(system_prompt)
            if response.text:
                st.markdown(f'<div class="response-box">{response.text}</div>', unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Something went wrong. Technical details: {e}")

# --- 6. RELOCATED BOTTOM CONTENT ---
st.markdown(f"""
    <div class="bottom-container">
        <div class="disclaimer-large">A final note on method — and audacity:</div>
        <div class="description-body">
            This document is not a credential. It is an attempt at one.<br>
            The premise: if you can architect knowledge for an AI — structure signal, strip noise, anticipate how it will be read and misread — you can probably architect it for a regulator, a boardroom, or a cross-functional task force. Same muscle. Different domain.<br>
            Is it perfect? Almost certainly not. But sending it anyway, in this form, to you? That takes a certain kind of confidence.<br>
            Call it gall. Call it conviction. Either way, it should score for effort — and effort, in the right hands, is simply strategy in motion.
        </div>
        <div class="contact-small">
            For clarification, confirmation, or the graceful correction of any hallucination, please contact Suk Chyi directly at:
            <a href="https://www.linkedin.com/in/khoosukchyi" class="linkedin-link" target="_blank">www.linkedin.com/in/khoosukchyi</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
