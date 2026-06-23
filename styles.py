"""
Glassmorphism CSS for the Workout Tracker app.
Call get_css() and inject with st.markdown(..., unsafe_allow_html=True).
"""


def get_css() -> str:
    return """
<style>
/* ────────────────────────────────────────────
   RESET & FULL-PAGE BACKGROUND
──────────────────────────────────────────── */
html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"], .stApp {
    background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%) !important;
    min-height: 100vh !important;
    color: #ffffff !important;
}

/* Remove Streamlit chrome */
#MainMenu, footer, header, [data-testid="stHeader"],
[data-testid="stToolbar"], [data-testid="stDecoration"],
[data-testid="stStatusWidget"] {
    display: none !important;
}

/* Remove default top padding */
[data-testid="stAppViewContainer"] > .main > .block-container {
    padding-top: 1.5rem !important;
    padding-bottom: 2rem !important;
    max-width: 900px !important;
}

/* ────────────────────────────────────────────
   GLASS CARD
──────────────────────────────────────────── */
.glass-card {
    background: rgba(255, 255, 255, 0.07);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 16px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.35);
    padding: 1.6rem 1.8rem;
    margin-bottom: 1rem;
}

.glass-card-inner {
    background: rgba(255, 255, 255, 0.04);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.10);
    border-radius: 12px;
    padding: 1.2rem 1.4rem;
    margin-bottom: 0.75rem;
}

/* ────────────────────────────────────────────
   TYPOGRAPHY
──────────────────────────────────────────── */
.app-title {
    font-size: 2.6rem;
    font-weight: 800;
    text-align: center;
    background: linear-gradient(90deg, #a78bfa, #22d3ee);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 0.25rem;
    letter-spacing: -0.5px;
}

.app-subtitle {
    text-align: center;
    color: rgba(255,255,255,0.55);
    font-size: 0.95rem;
    margin-bottom: 2rem;
    letter-spacing: 0.5px;
}

.section-header {
    font-size: 1.25rem;
    font-weight: 700;
    color: #a78bfa;
    margin-bottom: 0.9rem;
    border-bottom: 1px solid rgba(167, 139, 250, 0.25);
    padding-bottom: 0.4rem;
}

.exercise-title {
    font-size: 1.9rem;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 0.2rem;
}

.set-label {
    font-size: 1.1rem;
    color: rgba(255,255,255,0.65);
    margin-bottom: 0.5rem;
}

.reps-label {
    font-size: 1.35rem;
    font-weight: 700;
    color: #22d3ee;
    margin-bottom: 1.1rem;
}

/* ────────────────────────────────────────────
   TIMER
──────────────────────────────────────────── */
.timer-container {
    text-align: center;
    padding: 1.5rem 1rem;
}

.timer-label {
    font-size: 1rem;
    color: rgba(255,255,255,0.55);
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 0.4rem;
}

.timer-display {
    font-size: 5rem;
    font-weight: 900;
    font-family: 'Courier New', Courier, monospace;
    background: linear-gradient(90deg, #a78bfa, #22d3ee);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    text-shadow: none;
    filter: drop-shadow(0 0 18px rgba(167,139,250,0.55));
    line-height: 1;
    letter-spacing: 2px;
}

.timer-display.warning {
    background: linear-gradient(90deg, #f59e0b, #ef4444);
    -webkit-background-clip: text;
    background-clip: text;
    filter: drop-shadow(0 0 18px rgba(239,68,68,0.55));
}

.timer-progress-track {
    width: 100%;
    height: 8px;
    background: rgba(255,255,255,0.10);
    border-radius: 99px;
    margin: 1rem auto 0;
    max-width: 340px;
    overflow: hidden;
}

.timer-progress-fill {
    height: 100%;
    border-radius: 99px;
    background: linear-gradient(90deg, #a78bfa, #22d3ee);
    transition: width 0.8s linear;
}

/* ────────────────────────────────────────────
   EXERCISE CHECKLIST
──────────────────────────────────────────── */
.exercise-item {
    display: flex;
    align-items: center;
    gap: 0.65rem;
    padding: 0.65rem 0.9rem;
    border-radius: 10px;
    margin-bottom: 0.45rem;
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.07);
    color: rgba(255,255,255,0.55);
    font-size: 0.92rem;
    transition: all 0.2s ease;
}

.exercise-item.done {
    background: rgba(34, 211, 238, 0.08);
    border: 1px solid rgba(34, 211, 238, 0.25);
    color: #22d3ee;
}

.exercise-item.active {
    background: rgba(167, 139, 250, 0.14);
    border: 1px solid rgba(167, 139, 250, 0.5);
    color: #ffffff;
    font-weight: 700;
    box-shadow: 0 0 12px rgba(167, 139, 250, 0.25);
}

.exercise-item .check-icon {
    font-size: 1rem;
    min-width: 1.2rem;
}

/* ────────────────────────────────────────────
   PROGRESS BAR OVERRIDE
──────────────────────────────────────────── */
[data-testid="stProgress"] > div > div > div {
    background: linear-gradient(90deg, #a78bfa, #22d3ee) !important;
    border-radius: 99px !important;
}

[data-testid="stProgress"] > div {
    background: rgba(255,255,255,0.10) !important;
    border-radius: 99px !important;
    height: 10px !important;
}

/* ────────────────────────────────────────────
   STREAMLIT BUTTONS — glassmorphism override
──────────────────────────────────────────── */
.stButton > button {
    background: rgba(167, 139, 250, 0.15) !important;
    border: 1px solid rgba(167, 139, 250, 0.45) !important;
    color: #ffffff !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    font-size: 0.95rem !important;
    padding: 0.55rem 1.2rem !important;
    transition: all 0.2s ease !important;
    backdrop-filter: blur(10px) !important;
    width: 100%;
}

.stButton > button:hover {
    background: rgba(167, 139, 250, 0.30) !important;
    border-color: rgba(167, 139, 250, 0.75) !important;
    box-shadow: 0 0 18px rgba(167, 139, 250, 0.35) !important;
    transform: translateY(-1px) !important;
    color: #ffffff !important;
}

.stButton > button:active {
    transform: translateY(0px) !important;
}

/* Primary / CTA button variant */
.btn-primary > button {
    background: linear-gradient(135deg, rgba(167,139,250,0.4), rgba(34,211,238,0.25)) !important;
    border: 1px solid rgba(167,139,250,0.65) !important;
    font-size: 1.05rem !important;
    padding: 0.75rem 1.5rem !important;
    box-shadow: 0 4px 20px rgba(167,139,250,0.25) !important;
}

.btn-primary > button:hover {
    box-shadow: 0 0 28px rgba(167,139,250,0.5) !important;
}

/* Skip/danger button */
.btn-skip > button {
    background: rgba(239, 68, 68, 0.12) !important;
    border: 1px solid rgba(239, 68, 68, 0.4) !important;
    color: #fca5a5 !important;
    font-size: 0.9rem !important;
}

.btn-skip > button:hover {
    background: rgba(239, 68, 68, 0.25) !important;
    box-shadow: 0 0 16px rgba(239,68,68,0.3) !important;
}

/* Home screen big buttons */
.btn-home > button {
    background: linear-gradient(135deg, rgba(167,139,250,0.2), rgba(34,211,238,0.12)) !important;
    border: 1px solid rgba(167,139,250,0.5) !important;
    font-size: 1.2rem !important;
    padding: 1.1rem 1rem !important;
    border-radius: 14px !important;
    box-shadow: 0 4px 24px rgba(0,0,0,0.25) !important;
}

.btn-home > button:hover {
    background: linear-gradient(135deg, rgba(167,139,250,0.35), rgba(34,211,238,0.22)) !important;
    box-shadow: 0 0 30px rgba(167,139,250,0.4) !important;
}

/* Back button */
.btn-back > button {
    background: rgba(255,255,255,0.06) !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    color: rgba(255,255,255,0.7) !important;
    font-size: 0.85rem !important;
    padding: 0.4rem 0.8rem !important;
    width: auto !important;
}

.btn-back > button:hover {
    background: rgba(255,255,255,0.12) !important;
    color: #ffffff !important;
}

/* ────────────────────────────────────────────
   SLIDERS / INPUTS
──────────────────────────────────────────── */
[data-testid="stSlider"] label,
[data-testid="stNumberInput"] label {
    color: rgba(255,255,255,0.75) !important;
    font-weight: 600 !important;
}

[data-testid="stSlider"] .stSlider > div > div > div > div {
    background: linear-gradient(90deg, #a78bfa, #22d3ee) !important;
}

/* ────────────────────────────────────────────
   COMPLETION SCREEN
──────────────────────────────────────────── */
.complete-title {
    font-size: 3rem;
    font-weight: 900;
    text-align: center;
    background: linear-gradient(90deg, #a78bfa, #22d3ee);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    filter: drop-shadow(0 0 20px rgba(167,139,250,0.5));
    margin-bottom: 0.5rem;
}

.complete-subtitle {
    text-align: center;
    color: rgba(255,255,255,0.6);
    font-size: 1.05rem;
    margin-bottom: 2rem;
}

.summary-item {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 0.7rem 1rem;
    border-radius: 10px;
    background: rgba(34,211,238,0.07);
    border: 1px solid rgba(34,211,238,0.2);
    color: rgba(255,255,255,0.85);
    margin-bottom: 0.5rem;
    font-size: 0.95rem;
}

/* ────────────────────────────────────────────
   BADGE / TAG
──────────────────────────────────────────── */
.badge {
    display: inline-block;
    padding: 0.2rem 0.65rem;
    border-radius: 99px;
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.5px;
    text-transform: uppercase;
}

.badge-purple {
    background: rgba(167,139,250,0.2);
    border: 1px solid rgba(167,139,250,0.4);
    color: #c4b5fd;
}

.badge-cyan {
    background: rgba(34,211,238,0.12);
    border: 1px solid rgba(34,211,238,0.35);
    color: #67e8f9;
}

/* ────────────────────────────────────────────
   CUSTOM SCROLLBAR
──────────────────────────────────────────── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: rgba(255,255,255,0.04); border-radius: 99px; }
::-webkit-scrollbar-thumb { background: rgba(167,139,250,0.4); border-radius: 99px; }
::-webkit-scrollbar-thumb:hover { background: rgba(167,139,250,0.65); }

/* ────────────────────────────────────────────
   DIVIDER
──────────────────────────────────────────── */
.glass-divider {
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(167,139,250,0.35), transparent);
    margin: 1rem 0;
}

/* Streamlit hr override */
hr {
    border-color: rgba(255,255,255,0.08) !important;
}

/* ────────────────────────────────────────────
   HOLD INDEX INDICATOR
──────────────────────────────────────────── */
.hold-dot-row {
    display: flex;
    gap: 0.5rem;
    justify-content: center;
    margin: 0.75rem 0 0.5rem;
}

.hold-dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: rgba(255,255,255,0.2);
    border: 1px solid rgba(255,255,255,0.25);
}

.hold-dot.active {
    background: #a78bfa;
    box-shadow: 0 0 8px rgba(167,139,250,0.7);
}

.hold-dot.done {
    background: #22d3ee;
    box-shadow: 0 0 8px rgba(34,211,238,0.5);
}
</style>
"""
