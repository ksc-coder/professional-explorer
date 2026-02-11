import streamlit as st
import google.generativeai as genai

# --- 1. THE ENGINE ---
# PASTE YOUR KEY INSIDE THESE QUOTES
API_KEY = "AIzaSyAIoY9lyAcDt1aOxwPfd8Eft9SXgd0rV_0"

try:
    genai.configure(api_key=API_KEY)
    # Changed to 'gemini-flash-latest' to fix the 404 error
    model = genai.GenerativeModel('gemini-flash-latest')
except Exception:
    st.error("Engine failed to start. Please check your API key.")

# --- 2. YOUR KNOWLEDGE BASE ---
# 1. Open your 'Markdown Knowledge Base.docx'
# 2. Select ALL the text in that document and copy it.
# 3. DELETE the sentence below and PASTE your text inside the triple quotes.
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
My role was often to align incentives, bridge fragmented views, and move groups toward a shared, workable solution.
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
    }
    
    h1 { color: #0F172A; font-weight: 600; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. THE INTERFACE ---
st.title("Suk Chyi")
st.markdown("<p style='color: #64748B;'>Interactive Experience Explorer</p>", unsafe_allow_html=True)
st.markdown("---")

query = st.text_input("Search for a skill, industry, or keyword (e.g. '5G', 'Arbitration', 'Ambiguity')", 
                      placeholder="Enter keyword here...")

if query:
    system_prompt = f"""
    Context: {THE_ARCHIVE}
    User Query: {query}
    Instruction: Answer using the specific language from the archive. 
    Tone: Senior, professional, and crisp.
    Format: Use bullet points for 'Transferable Capabilities'.
    """
    
    with st.spinner("Synthesizing..."):
        try:
            response = model.generate_content(system_prompt)
            st.markdown(f'<div class="response-box">{response.text}</div>', unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Something went wrong. Technical details: {e}")

st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("A precision retrieval engine for the curated knowledge base of Suk Chyi.")
