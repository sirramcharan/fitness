def get_css() -> str:
    return """
<style>
/* App background: deep, sleek gradient */
.stApp {
    background: radial-gradient(circle at top left, #1f2933 0%, #0f172a 35%, #020617 100%);
    color: #e5e7eb;
}

/* Hide default Streamlit chrome */
header, .st-emotion-cache-16txtl3, footer {
    visibility: hidden;
    height: 0;
}

/* Glass container core */
.glass-card {
    background: rgba(15, 23, 42, 0.6);
    border-radius: 18px;
    border: 1px solid rgba(148, 163, 184, 0.45);
    box-shadow:
        0 18px 50px rgba(15, 23, 42, 0.75),
        0 0 0 1px rgba(15, 23, 42, 0.7);
    backdrop-filter: blur(24px) saturate(180%);
    padding: 1.4rem 1.6rem;
}

/* Inner glass block (used for summary, steps, etc.) */
.glass-card-inner {
    background: rgba(15, 23, 42, 0.75);
    border-radius: 16px;
    border: 1px solid rgba(148, 163, 184, 0.35);
    box-shadow: 0 12px 35px rgba(15, 23, 42, 0.65);
    backdrop-filter: blur(18px) saturate(170%);
    padding: 1.1rem 1.3rem;
}

/* Divider line */
.glass-divider {
    height: 1px;
    width: 100%;
    background: linear-gradient(90deg, rgba(148, 163, 184, 0.05), rgba(148, 163, 184, 0.7), rgba(148, 163, 184, 0.05));
    margin: 0.7rem 0 1rem;
}

/* Titles */
.app-title {
    font-size: 2.2rem;
    font-weight: 800;
    letter-spacing: 0.04em;
    color: #f9fafb;
    text-align: center;
    margin-bottom: 0.4rem;
}
.app-subtitle {
    font-size: 0.95rem;
    color: rgba(148, 163, 184, 0.9);
    text-align: center;
    margin-bottom: 1.6rem;
}
.exercise-title {
    font-size: 1.4rem;
    font-weight: 700;
    color: #f9fafb;
}

/* Section header */
.section-header {
    font-size: 0.92rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: rgba(148, 163, 184, 0.95);
    margin-bottom: 0.8rem;
}

/* Buttons base */
button[kind="primary"],
.btn-primary button,
.btn-home button,
.btn-back button,
.btn-skip button {
    border-radius: 999px !important;
    border: 1px solid rgba(148, 163, 184, 0.7) !important;
    background: radial-gradient(circle at top left, #4f46e5 0%, #6366f1 35%, #0ea5e9 100%) !important;
    color: #f9fafb !important;
    font-weight: 600 !important;
    letter-spacing: 0.03em;
    box-shadow:
        0 12px 40px rgba(56, 189, 248, 0.45),
        0 0 0 1px rgba(15, 23, 42, 0.8);
    padding: 0.65rem 1.1rem !important;
}

/* Button hover */
button[kind="primary"]:hover,
.btn-primary button:hover,
.btn-home button:hover,
.btn-back button:hover,
.btn-skip button:hover {
    filter: brightness(1.08);
    box-shadow:
        0 18px 60px rgba(56, 189, 248, 0.55),
        0 0 0 1px rgba(15, 23, 42, 0.9);
}

/* Secondary/back buttons */
.btn-back button {
    background: rgba(15, 23, 42, 0.7) !important;
    border-color: rgba(148, 163, 184, 0.6) !important;
    box-shadow: 0 10px 26px rgba(15, 23, 42, 0.8);
}

/* Home choice buttons */
.btn-home {
    display: block;
}
.btn-home button {
    width: 100%;
    padding: 1rem 1.2rem !important;
    font-size: 0.95rem !important;
}

/* Exercise list items */
.exercise-item {
    margin-bottom: 0.45rem;
}
.exercise-item button {
    width: 100%;
    text-align: left !important;
    border-radius: 999px !important;
    background: rgba(15, 23, 42, 0.6) !important;
    border: 1px solid rgba(148, 163, 184, 0.45) !important;
    color: #e5e7eb !important;
    font-size: 0.9rem !important;
}
.exercise-item.active button {
    border-color: #38bdf8 !important;
    box-shadow: 0 0 0 1px rgba(56, 189, 248, 0.8);
}
.exercise-item.done button {
    border-color: #22c55e !important;
    color: #bbf7d0 !important;
}

/* Timer */
.timer-container {
    margin-top: 0.5rem;
}
.timer-label {
    font-size: 0.9rem;
    color: rgba(148, 163, 184, 0.9);
    margin-bottom: 0.3rem;
}
.timer-display {
    font-family: "SF Mono", ui-monospace, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
    font-size: 2.4rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    color: #e5e7eb;
    text-shadow: 0 0 26px rgba(56, 189, 248, 0.6);
    margin-bottom: 0.4rem;
}
.timer-display.warning {
    color: #f97316;
    text-shadow: 0 0 26px rgba(249, 115, 22, 0.8);
}
.timer-progress-track {
    width: 100%;
    height: 6px;
    border-radius: 999px;
    background: rgba(15, 23, 42, 0.9);
    overflow: hidden;
}
.timer-progress-fill {
    height: 100%;
    border-radius: 999px;
    background: linear-gradient(90deg, #4f46e5, #6366f1, #0ea5e9);
}

/* Hold/plank dots */
.hold-dot-row {
    display: flex;
    gap: 0.35rem;
    margin-bottom: 0.4rem;
}
.hold-dot {
    width: 10px;
    height: 10px;
    border-radius: 999px;
    background: rgba(148, 163, 184, 0.35);
}
.hold-dot.active {
    background: #0ea5e9;
}
.hold-dot.done {
    background: #22c55e;
}

/* Summary items */
.summary-item {
    display: flex;
    gap: 0.75rem;
    align-items: flex-start;
    margin-bottom: 0.75rem;
}
.summary-item span:first-child {
    min-width: 1.8rem;
}

/* Progress bar override */
.css-1dc0d3s, .stProgress > div > div {
    background: rgba(15, 23, 42, 0.8) !important;
}
.stProgress > div > div > div {
    background: linear-gradient(90deg, #4f46e5, #6366f1, #0ea5e9) !important;
}

/* Scrollbar */
::-webkit-scrollbar {
    width: 8px;
}
::-webkit-scrollbar-track {
    background: rgba(15, 23, 42, 0.9);
}
::-webkit-scrollbar-thumb {
    background: rgba(148, 163, 184, 0.6);
    border-radius: 999px;
}
::-webkit-scrollbar-thumb:hover {
    background: rgba(148, 163, 184, 0.9);
}
/* Center main content container */
.main-container {
    max-width: 720px;
    margin: 0 auto;
    padding: 3rem 1.5rem 3.5rem;
}

/* Ensure home glass card uses full container width */
.main-container .glass-card {
    width: 100%;
}
</style>
"""
