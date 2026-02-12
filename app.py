import streamlit as st
import google.generativeai as genai
import os

# --- 1. THE ENGINE ---
# This pulls the key from the 'Vault' you just set up in Streamlit Cloud
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    st.error("Connection Error: The API Key is not configured in Secrets.")
    st.stop()

try:
    genai.configure(api_key=API_KEY)
    # Changed to 'gemini-flash-latest' to fix the 404 error
    model = genai.GenerativeModel('gemini-flash-latest')
except Exception:
    st.error("Engine failed to start. Please check your API key.")

# --- 2. YOUR KNOWLEDGE BASE (THE ARCHIVE) ---
# Paste the content of your 'Markdown Knowledge Base.docx' here.
# Keep the triple quotes ( \"\"\" ) at the top and bottom.
THE_ARCHIVE = """
Professional Knowledge Base (Markdown)
A structured, high-signal, AI-friendly representation of experience, capabilities, and intellectual operating system.
________________________________________
1. Career Overview
I began my career in a litigation boutique where the margin for error was roughly the size of a misplaced comma.
We were consistently the smallest team among Chambers & Partners and Legal500-ranked practices, which meant two things:
1.	The work was never small.
2.	You learned fast or you didn’t last.
I learned fast.
My foundation was built in environments where precision, pace, and judgment mattered more than headcount. The work required moving seamlessly between statutory text, policy intent, commercial incentives, and human behaviour — often under tight timelines and high scrutiny.
________________________________________
2. Core Competencies
2.1 Statutory & Policy Interpretation
I read legislation the way engineers read system diagrams:
•	Holistically
•	Contextually
•	With an eye on the underlying mischief and policy intent
Regular materials included:
•	Hansard
•	Parliamentary debates
•	White papers
•	Task force reports
•	Regulatory consultations
I frequently worked with NGOs, regulators, and think tanks — the policy ecosystem behind the black-letter law.
________________________________________
2.2 Operating in Ambiguity
Trained to:
•	Argue from first principles
•	Build tight micro- and macro-level reasoning
•	Anticipate industry-wide impacts
•	Identify unintended consequences before they surface
Ambiguity wasn’t a roadblock; it was the starting point.
________________________________________
2.3 Advocacy & Persuasion
Strong oral and written advocacy, tailored to:
•	Judges
•	Regulators
•	C-suite
•	Cross-functional teams
•	Operational stakeholders
My former boss once said:
“How you ask your dad is never how you ask your mom.”
A memorable way of teaching message-audience calibration — a skill that has since become a core part of my operating system.
________________________________________
2.4 Negotiation & Stakeholder Alignment
I frequently served as:
•	Primary negotiator
•	Front-line point of contact
•	Translator between legal, technical, commercial, and policy domains
I draft contractual language that brings together divergent commercial, technical, and regulatory interests — framing clauses that opposing stakeholders can still get behind. My role was to bridge gaps, align incentives, and steer fragmented groups toward a shared, practical outcome.
________________________________________
2.5 Cross-Functional Problem Solving
Worked closely with:
•	Instructing solicitors
•	Engineering teams
•	Finance
•	Operations
•	Sales
•	Regulators
•	Industry experts
The job required multilingual fluency — not in literal languages, but in domain “dialects.”
________________________________________
2.6 Conflict Resolution
Grounded in the true purpose of dispute resolution:
•	Prioritise settlement where possible
•	Establish common ground
•	Narrow issues pragmatically
•	Keep sight of the bigger picture
One of the most profound professional muscles I developed: objective problem-solving in high-emotion environments.
________________________________________
2.7 Relationship Building
I once worked part-time as a barista.
Lesson learned from my manager:
“Being a barista isn’t just about making coffee — it’s about running the entire café.”
Practice was the same. It wasn’t just about arguing cases. It was about:
•	Earning trust
•	Building rapport
•	Forming durable partnerships
With judges, regulators, fellow members of the Bar, clients across divisions, and even opposing counsel.
________________________________________
3. Arbitration Expertise (FCIArb)
As a Fellow of the Chartered Institute of Arbitrators, I built expertise in:
•	Complex cross-border disputes
•	Evidence-taking standards
•	Procedural fairness
•	Harmonising competing rules, protocols, and enforcement pathways
•	Evaluating remedies and understanding grievances
________________________________________
4. Leadership & Mentorship
As a Senior Associate, I managed and supervised junior team members.
I was mentored by exceptional seniors, including Dato’ Malik Imtiaz Sarwar — and I’ve always aimed to be the senior I once needed.
A junior once told me:
“Any senior will thrive with your support, and any junior will grow under your guidance.”
Across 9+ years — intern → paralegal → pupil → associate → senior associate — I had front-row access to:
•	Strategy
•	Thought leadership
•	Complex decision-making
•	Principled advocacy
This shaped the backbone of my professional judgment.
________________________________________
5. Key Impacts & Representative Matters
Telecommunications & Infrastructure
•	Advised Malaysia’s four major telcos on nationwide 5G implementation
•	Resolved multi-billion-ringgit disputes at the intersection of technology, law, and policy
•	Provided competition, regulatory, and strategic advice
Data & Fintech
•	Secured a landmark win affirming the legality of an algorithm-based credit scoring model
•	Resulted in regulatory certainty and contributed to a 5% share-price increase for a major reporting agency
Energy & Geopolitics
•	Represented a Fortune Global 500® O&G company in sensitive negotiations with a state government
•	Navigated statutory, commercial, and geopolitical complexities
Competition & Antitrust
•	Acted for a major Southeast Asian e-hailing platform in judicial review against MyCC
•	Challenged an RM86M proposed penalty for alleged abuse of dominance
•	Focused on procedural fairness and investigative standards
Regulatory Enforcement
•	Lead associate and second-chair in Securities Commission civil actions
•	Represented a Big Four audit firm in judicial reviews on investigative findings
Corporate Governance
•	Advised on director liabilities, auditors’ duties, and internal governance for MNCs and GLCs
Appellate Advocacy
•	Regularly appeared before the Federal Court
•	Contributed to jurisprudence on governance and accountability
Leadership & Ops
•	Supervised junior lawyers in complex advocacy
•	Built internal workflows to improve efficiency
________________________________________
6. Strategic Capabilities
Trained to rotate across industries, geographies, and functions with minimal ramp-up.
Core strengths include:
•	Deconstructing sprawling problems
•	Reassembling them into solvable parts
•	Driving alignment across sceptical or siloed stakeholders
•	Rapid mastery of unfamiliar domains
•	Proactive issue-spotting and pattern recognition
Clear, structured thinking was non-negotiable.
So was the ability to challenge assumptions without breaking trust.
________________________________________
7. Executive Operating System
Where I lack a specific experience, I bring a transferable playbook shaped by high-stakes decision environments:
•	Systems-driven diagnostics
•	Methodical problem framing
•	Comfort with ambiguity
•	Ability to scale what works and redesign what doesn’t
•	Muscle memory for breaking complexity into tractable components
•	A horizontal, cross-domain leadership style
________________________________________
8. Career Transition Rationale
Litigation is the professional equivalent of firefighting in 99 buildings at once.
I’m ready to sit at the table designing:
•	the fire-prevention architecture
•	the escalation pathways
•	the governance frameworks
that stop the fires from starting.
This isn’t a step back — it’s a step toward strategic impact.
________________________________________
9. Sabbatical (Since September 2025)
After nearly a decade in practice, I took a purposeful sabbatical to broaden my aperture.
The goal: bridge traditional legal practice with the future of regulation.
Key Focus Areas
•	Fintech & Digital Assets: Blockchain ethics, asset compliance, risk strategy (HKU)
•	Crisis Management: Reputational risk & comms frameworks (Dartmouth College)
•	Leadership & Influence: Cross-functional influence and strategic partnership (Harvard University)
•	Digital Fluency: Blockchain and digital asset legal concepts (Binance Academy)
This period reframed me from a litigator to a strategic partner capable of navigating emerging regulatory frontiers.
________________________________________
10. Current Focus
Currently studying European data protection, with plans to sit for the CIPP/E exam this year.
Simultaneously job-hunting — ready to apply my experience in governance, accountability, risk, and structured problem-solving to a mission-driven team.
________________________________________
11. Keywords Index (For Search or Model Ingestion)
•	statutory interpretation
•	policy analysis
•	regulatory strategy
•	litigation
•	arbitration
•	cross-functional leadership
•	stakeholder management
•	ambiguity navigation
•	problem decomposition
•	negotiation
•	telecommunications
•	fintech
•	digital assets
•	energy
•	competition law
•	governance
•	enforcement
•	crisis management
•	risk strategy
•	data protection
•	CIPP/E
•	strategic advisory
•	executive decision-making
"""

# ---------------------------------------------------
# 3. DESIGN — CLEAN, POLISHED VERSION
# ---------------------------------------------------

st.set_page_config(page_title="KSC | Professional Experience Explorer", layout="centered")

st.markdown("""
<style>

body {
    background-color: white;
}

/* Reduce giant Streamlit top padding */
.block-container {
    max-width: 750px !important;
    margin: auto;
    padding-top: 2rem !important;
    padding-bottom: 2rem !important;
}

/* Name (big grey bold) */
.name-title {
    font-size: 40px;
    font-weight: 700;
    color: #6f6f6f;
    margin-bottom: 5px;
    text-align: left;
}

/* Main title (big black bold) */
.main-title {
    font-size: 32px;
    font-weight: 700;
    color: black;
    margin-bottom: 25px;
    text-align: left;
}

/* Instruction (medium grey bold) */
.instruction {
    font-size: 20px;
    font-weight: 600;
    color: #6f6f6f;
    margin-bottom: 15px;
    text-align: left;
}

/* Improve search bar appearance */
input.stTextInput {
    border-radius: 10px !important;
    border: 1px solid #E2E8F0 !important;
    padding: 14px !important;
    background-color: #F8FAFC !important;
}

/* Placeholder text */
input::placeholder {
    color: black !important;
    opacity: 1;
    font-size: 18px;
}

/* Footer small grey text */
.description-small {
    font-size: 14px;
    color: #6f6f6f;
    margin-top: 20px;
    text-align: left;
}

.disclaimer-small-bold {
    font-size: 14px;
    font-weight: 600;
    color: #6f6f6f;
}

.contact-small {
    font-size: 14px;
    color: #6f6f6f;
    text-align: left;
}

.contact-small-bold {
    font-size: 14px;
    font-weight: 600;
    color: #6f6f6f;
}

/* Response box */
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


# ---------------------------------------------------
# 4. UI — EXACT TEXT YOU SPECIFIED (POLISHED LAYOUT)
# ---------------------------------------------------

st.markdown('<div class="name-title">KHOO SUK CHYI</div>', unsafe_allow_html=True)
st.markdown('<div class="main-title">Interactive Professional Experience Explorer</div>', unsafe_allow_html=True)
st.markdown('<div class="instruction">Enter a keyword, skill, or industry (e.g., "strategy", "policy", "leadership") </div>', unsafe_allow_html=True)

# Search Input (no extra box)
query = st.text_input("", placeholder="Start typing here ...", label_visibility="collapsed")

# Footer text — merged into one clean paragraph
st.markdown(
    """
    <div class="description-small">
        This is a high-signal, interactive map of a legal career.
        <span class="disclaimer-small-bold" style="margin-left: 5px;">
            It is neither a CV nor a chatbot.
        </span>
    </div>

    <div class="contact-small" style="margin-top: 12px;">
        For clarifications or confirmation of any output, please contact Suk Chyi directly at:
        <a href="https://www.linkedin.com/in/khoosukchyi" class="contact-small-bold linkedin-link" target="_blank" style="margin-left: 3px; color: #6f6f6f;">www.linkedin.com/in/khoosukchyi</a>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------
# 5. AI ENGINE (UNCHANGED)
# ---------------------------------------------------

if query:
    system_prompt = f"""
    ROLE & PERSONA:
    You are the "Experience Explorer" and a senior executive advisor for Suk Chyi. 
    Your tone is polished, crisp, intellectually confident, and subtly witty—a breath of fresh air in a corporate world. 
    Avoid tech-bro slang, corporate jargon, or "LinkedIn-cringe" enthusiasm. Think sophisticated, sharp, and high-signal.

    STYLE REFERENCE (EMULATE THIS NARRATIVE):
    "She began her career in a litigation boutique where the margin for error was a single misplaced comma. 
    Consistently the smallest team among Chambers-ranked practices, it meant the work was never small. 
    She learned fast because she had to. She reads laws the way engineers read system diagrams: holistically and contextually."

    STRICT OPERATING RULES:

---------------------------------------------
FORMAT RULES (NON-NEGOTIABLE)
---------------------------------------------
1. All output must be written in short paragraphs of 2–4 lines.
2. Insert exactly ONE blank line between paragraphs.
3. No blank lines inside a paragraph.
4. Bullet points only for lists of 3 or more items.
5. A paragraph may contain multiple sentences but must appear as one continuous block.

---------------------------------------------
QUOTATION RULES
---------------------------------------------
Use quotation marks ONLY for the two quotes already in the archive.

---------------------------------------------
QUOTE USAGE LIMITATION
---------------------------------------------
The quote “Any senior will thrive with your support, and any junior will grow under your guidance.” 
may ONLY appear when the query relates to leadership, mentorship, management, people development, 
team culture, or senior–junior dynamics. 
It must NOT appear in responses to general skills such as “strategy”, “policy”, “regulatory”, 
“analysis”, or other non-leadership topics.

---------------------------------------------
PRONOUN RULES
---------------------------------------------
Refer to Suk Chyi using she/her.

---------------------------------------------
TRANSFERABILITY RULES
---------------------------------------------
If the archive directly mentions "{query}":
- Use explicit content.

If not:
1. Begin with: “The archive does not contain specific data on "{query}".”
2. Then map only adjacent experience already in the archive.
3. Never guess or invent.

---------------------------------------------
ARCHIVE (STRICT SOURCE)
---------------------------------------------
{THE_ARCHIVE}

"""

    with st.spinner("Analyzing experience..."):
        try:
            response = model.generate_content(system_prompt)
            st.markdown('<div class="response-box">', unsafe_allow_html=True)
            st.markdown(response.text)
            st.markdown('</div>', unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Something went wrong. Technical details: {e}")
