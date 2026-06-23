# 💪 Workout Tracker

A personal workout tracker for a 3×/week training plan, built with **Streamlit** and styled with a **glassmorphism** dark theme.

---

## What it does

- **Two workout modes:** Full Body or Abs
- **Full Body** — 5 exercises (Pull-ups, Push-ups, Dips, Squats, Rows), each 15 reps × 4–8 sets (you choose before starting)
- **Abs** — 3 exercises:
  - Crucifix Crunches — 15 reps × 3 sets
  - Core Hold Series — 3 consecutive 30-second holds
  - Side Plank Raises — 45 seconds each side (Left then Right)
- **4-minute rest timer** starts automatically after each set / exercise block, with a **Skip Rest** button
- **Live countdown** with a gradient progress bar (reruns every second using `st.rerun()`)
- **Exercise checklist** showing your progress through the session
- **Completion summary** with rep totals when you finish

---

## Run locally

```bash
# 1. Clone or copy the project folder
cd workout-tracker

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch
streamlit run app.py
```

The app will open at `http://localhost:8501`.

---

## Deploy to Streamlit Cloud

1. Push the `workout-tracker/` folder to a **public GitHub repository**.
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
3. Click **New app**, select your repo and set the **Main file path** to `app.py`.
4. Click **Deploy** — that's it.

The `.streamlit/config.toml` file is picked up automatically and sets the dark theme base.

---

## File structure

```
workout-tracker/
├── app.py              # Main Streamlit app — all page routing and rendering logic
├── config.py           # Workout definitions (exercises, sets, durations, constants)
├── styles.py           # Glassmorphism CSS returned by get_css()
├── requirements.txt    # Python dependencies (just streamlit)
├── .streamlit/
│   └── config.toml     # Dark theme base + server settings
└── README.md           # This file
```

### Key design decisions

| Concern | Approach |
|---|---|
| Timer | `datetime.datetime.now()` stored in `session_state`; `time.sleep(1)` + `st.rerun()` drives the countdown |
| State | All mutable state lives in `st.session_state` — survives reruns |
| Styling | CSS injected via `st.markdown(..., unsafe_allow_html=True)`; Streamlit chrome hidden |
| Modularity | Separate render functions per page and per exercise type |

---

## Customising

- **Change rest duration:** edit `REST_DURATION` in `config.py` (seconds).
- **Add exercises:** append to `FULLBODY_EXERCISES` or `ABS_EXERCISES` in `config.py`.
- **Change colours:** edit the gradient and accent variables at the top of `styles.py`.
