"""
💪 Workout Tracker — Streamlit app with glassmorphism design.
3x/week training: Full Body or Abs workout.
"""

import datetime
import time

import streamlit as st

from config import (
    ABS_EXERCISES,
    DEFAULT_SETS,
    FULLBODY_EXERCISES,
    REST_DURATION,
)
from styles import get_css

# ─────────────────────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="💪 Workout Tracker",
    page_icon="💪",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────────────────────
# SESSION STATE INITIALISATION
# ─────────────────────────────────────────────────────────────

def init_state() -> None:
    defaults = {
        "page": "home",
        "workout_type": None,
        "current_exercise_index": 0,
        "current_set": 1,
        "total_sets": DEFAULT_SETS,
        "completed_exercises": [],
        "timer_active": False,
        "timer_start": None,
        "timer_duration": REST_DURATION,
        # timer_expired: set True when countdown hits 0.
        # Checked at the TOP of each renderer to auto-advance
        # before any sleep/rerun logic runs.
        "timer_expired": False,
        "hold_index": 0,
        "plank_side_index": 0,
        "sets_completed": {},
        "workout_start_time": None,
    }
    for key, val in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val


def reset_workout() -> None:
    st.session_state.current_exercise_index = 0
    st.session_state.current_set = 1
    st.session_state.completed_exercises = []
    st.session_state.timer_active = False
    st.session_state.timer_start = None
    st.session_state.timer_duration = REST_DURATION
    st.session_state.timer_expired = False
    st.session_state.hold_index = 0
    st.session_state.plank_side_index = 0
    st.session_state.sets_completed = {}
    st.session_state.workout_start_time = None


def jump_to_exercise(target_idx: int) -> None:
    stop_timer()
    leaving_idx = st.session_state.current_exercise_index
    st.session_state.sets_completed[leaving_idx] = st.session_state.current_set

    completed = st.session_state.completed_exercises
    already_finished = target_idx < len(completed) and completed[target_idx]

    if already_finished:
        restored_set = 1
        st.session_state.completed_exercises[target_idx] = False
    else:
        restored_set = st.session_state.sets_completed.get(target_idx, 1)

    st.session_state.current_exercise_index = target_idx
    st.session_state.current_set = restored_set
    st.session_state.hold_index = 0
    st.session_state.plank_side_index = 0


# ─────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────

def get_exercises():
    if st.session_state.workout_type == "fullbody":
        return FULLBODY_EXERCISES
    return ABS_EXERCISES


def inject_css() -> None:
    st.markdown(get_css(), unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
# TIMER HELPERS
# ─────────────────────────────────────────────────────────────

def start_rest_timer(duration: int = REST_DURATION) -> None:
    st.session_state.timer_active  = True
    st.session_state.timer_expired = False
    st.session_state.timer_start   = datetime.datetime.now()
    st.session_state.timer_duration = duration


def stop_timer() -> None:
    st.session_state.timer_active  = False
    st.session_state.timer_expired = False
    st.session_state.timer_start   = None


def get_timer_remaining() -> float:
    """Returns seconds remaining on the active timer. Negative means expired."""
    if not st.session_state.timer_active or st.session_state.timer_start is None:
        return 0.0
    elapsed = (datetime.datetime.now() - st.session_state.timer_start).total_seconds()
    return st.session_state.timer_duration - elapsed


def render_timer_display(duration_seconds: int, label: str = "⏱ Rest Time") -> float:
    """Renders the timer UI. Returns remaining seconds (may be negative)."""
    elapsed = (datetime.datetime.now() - st.session_state.timer_start).total_seconds()
    remaining = max(0.0, duration_seconds - elapsed)

    mins = int(remaining) // 60
    secs = int(remaining) % 60
    time_str = f"{mins:02d}:{secs:02d}"
    fill_pct = (remaining / duration_seconds * 100) if duration_seconds > 0 else 0
    warning_cls = " warning" if remaining < 30 else ""

    st.markdown(
        f"""
        <div class="glass-card timer-container">
            <div class="timer-label">{label}</div>
            <div class="timer-display{warning_cls}">{time_str}</div>
            <div class="timer-progress-track">
                <div class="timer-progress-fill" style="width:{fill_pct:.1f}%"></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    return remaining


# ─────────────────────────────────────────────────────────────
# WORKOUT PROGRESSION
# ─────────────────────────────────────────────────────────────

def advance_exercise() -> None:
    """Mark current exercise done and move to the next (or completion screen)."""
    stop_timer()
    idx = st.session_state.current_exercise_index
    st.session_state.completed_exercises[idx] = True
    next_idx = idx + 1
    exercises = get_exercises()
    if next_idx >= len(exercises):
        st.session_state.page = "complete"
    else:
        st.session_state.current_exercise_index = next_idx
        completed = st.session_state.completed_exercises
        already_finished = next_idx < len(completed) and completed[next_idx]
        restored_set = st.session_state.sets_completed.get(next_idx, 1)
        st.session_state.current_set = 1 if already_finished else restored_set
        st.session_state.hold_index = 0
        st.session_state.plank_side_index = 0


# ─────────────────────────────────────────────────────────────
# RENDER: Clickable exercise checklist
# ─────────────────────────────────────────────────────────────

def render_exercise_checklist(exercises: list, current_index: int) -> None:
    completed = st.session_state.completed_exercises

    st.markdown(
        '<div class="glass-card" style="padding:1.1rem 1.2rem;">'
        '<div class="section-header">Today\'s Exercises</div>',
        unsafe_allow_html=True,
    )

    for i, ex in enumerate(exercises):
        is_done   = i < len(completed) and completed[i]
        is_active = i == current_index

        status_icon = "✅" if is_done else ("▶️" if is_active else "○")
        item_cls    = "exercise-item done" if is_done else ("exercise-item active" if is_active else "exercise-item")
        label       = f"{ex.get('emoji', '')} {ex['name']}"

        set_hint = ""
        if ex.get("type", "reps") == "reps" and not is_done:
            saved_set  = st.session_state.sets_completed.get(i, 1)
            total_sets = st.session_state.total_sets if st.session_state.workout_type == "fullbody" else ex.get("sets", 3)
            if saved_set > 1:
                set_hint = f" ({saved_set - 1}/{total_sets})"

        st.markdown(f'<div class="{item_cls}">', unsafe_allow_html=True)
        if st.button(f"{status_icon}  {label}{set_hint}", key=f"jump_ex_{i}", use_container_width=True):
            jump_to_exercise(i)
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
# EXERCISE RENDERERS
# ─────────────────────────────────────────────────────────────

def render_reps_exercise(ex: dict, idx: int) -> None:
    is_fullbody = st.session_state.workout_type == "fullbody"
    total_sets  = st.session_state.total_sets if is_fullbody else ex.get("sets", 3)
    current_set = st.session_state.current_set
    reps        = ex.get("reps", 15)
    is_last_ex  = idx == len(get_exercises()) - 1

    # ── Handle active rest timer ──────────────────────────────
    if st.session_state.timer_active:
        remaining = get_timer_remaining()

        if remaining <= 0:
            # Timer just expired — clear it and re-render immediately
            # without sleep so buttons are available right away
            stop_timer()
            st.rerun()
            return

        # Timer still running — show skip + countdown
        col_skip, _ = st.columns([1, 2])
        with col_skip:
            st.markdown('<div class="btn-skip">', unsafe_allow_html=True)
            if st.button("⏭ Skip Rest", key=f"skip_{idx}_{current_set}"):
                stop_timer()
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

        render_timer_display(st.session_state.timer_duration, "⏱ Rest Time")
        time.sleep(1)
        st.rerun()
        return

    # ── All sets done for this exercise ───────────────────────
    if current_set > total_sets:
        st.markdown(
            '<div class="glass-card-inner" style="text-align:center;">'
            '<div style="font-size:1.4rem;color:#22d3ee;font-weight:700;">✅ All sets complete!</div>'
            '</div>',
            unsafe_allow_html=True,
        )
        if st.button("Next Exercise →", key=f"next_{idx}"):
            advance_exercise()
            st.rerun()
        return

    # ── Active set ────────────────────────────────────────────
    st.markdown(
        f'<div class="glass-card">'
        f'<div class="set-label">Set {current_set} of {total_sets}</div>'
        f'<div class="reps-label">🎯 {reps} reps</div>'
        f'</div>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="btn-primary">', unsafe_allow_html=True)
    if st.button(f"✅ Complete Set {current_set}", key=f"complete_set_{idx}_{current_set}"):
        next_set = current_set + 1
        st.session_state.current_set = next_set
        st.session_state.sets_completed[idx] = next_set
        if next_set > total_sets:
            if is_last_ex:
                advance_exercise()
            else:
                start_rest_timer(REST_DURATION)
        else:
            start_rest_timer(REST_DURATION)
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)


def render_hold_series_exercise(ex: dict, idx: int) -> None:
    holds    = ex["holds"]
    hold_idx = st.session_state.hold_index
    all_done = hold_idx >= len(holds)

    # ── Post-series rest timer ────────────────────────────────
    if st.session_state.timer_active and all_done:
        remaining = get_timer_remaining()
        if remaining <= 0:
            stop_timer()
            advance_exercise()
            st.rerun()
            return

        col_skip, _ = st.columns([1, 2])
        with col_skip:
            st.markdown('<div class="btn-skip">', unsafe_allow_html=True)
            if st.button("⏭ Skip Rest", key=f"skip_hold_rest_{idx}"):
                stop_timer()
                advance_exercise()
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

        render_timer_display(st.session_state.timer_duration, "⏱ Rest Time")
        time.sleep(1)
        st.rerun()
        return

    if all_done:
        advance_exercise()
        st.rerun()
        return

    current_hold = holds[hold_idx]

    # ── Hold-countdown timer ──────────────────────────────────
    if st.session_state.timer_active:
        remaining = get_timer_remaining()
        if remaining <= 0:
            stop_timer()
            st.session_state.hold_index += 1
            nxt = st.session_state.hold_index
            if nxt < len(holds):
                start_rest_timer(holds[nxt]["duration"])
            else:
                start_rest_timer(REST_DURATION)
            st.rerun()
            return

        render_timer_display(current_hold["duration"], f"⏱ Hold {hold_idx + 1}")
        time.sleep(1)
        st.rerun()
        return

    # ── Dot progress indicator ────────────────────────────────
    dots_html = '<div class="hold-dot-row">'
    for i in range(len(holds)):
        cls = "done" if i < hold_idx else ("active" if i == hold_idx else "")
        dots_html += f'<div class="hold-dot {cls}"></div>'
    dots_html += "</div>"

    st.markdown(
        f'<div class="glass-card">{dots_html}'
        f'<div class="set-label" style="margin-top:0.5rem;">Hold {hold_idx+1} of {len(holds)}</div>'
        f'<div class="reps-label">⏱ {current_hold["duration"]} seconds</div>'
        f'<div style="color:rgba(255,255,255,0.6);font-size:0.9rem;margin-bottom:0.75rem;">{current_hold["name"]}</div>'
        f'</div>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="btn-primary">', unsafe_allow_html=True)
    if st.button(f"▶️ Start Hold {hold_idx + 1}", key=f"start_hold_{idx}_{hold_idx}"):
        start_rest_timer(current_hold["duration"])
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)


def render_timed_sides_exercise(ex: dict, idx: int) -> None:
    sides    = ex["sides"]
    side_idx = st.session_state.plank_side_index
    duration = ex["duration"]
    all_done = side_idx >= len(sides)

    # ── Post-series rest timer ────────────────────────────────
    if st.session_state.timer_active and all_done:
        remaining = get_timer_remaining()
        if remaining <= 0:
            stop_timer()
            advance_exercise()
            st.rerun()
            return

        col_skip, _ = st.columns([1, 2])
        with col_skip:
            st.markdown('<div class="btn-skip">', unsafe_allow_html=True)
            if st.button("⏭ Skip Rest", key=f"skip_plank_rest_{idx}"):
                stop_timer()
                advance_exercise()
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

        render_timer_display(st.session_state.timer_duration, "⏱ Rest Time")
        time.sleep(1)
        st.rerun()
        return

    if all_done:
        advance_exercise()
        st.rerun()
        return

    current_side = sides[side_idx]

    # ── Side-countdown timer ──────────────────────────────────
    if st.session_state.timer_active:
        remaining = get_timer_remaining()
        if remaining <= 0:
            stop_timer()
            st.session_state.plank_side_index += 1
            nxt = st.session_state.plank_side_index
            if nxt < len(sides):
                start_rest_timer(duration)
            else:
                start_rest_timer(REST_DURATION)
            st.rerun()
            return

        col_skip, _ = st.columns([1, 2])
        with col_skip:
            st.markdown('<div class="btn-skip">', unsafe_allow_html=True)
            if st.button(f"⏭ Skip {current_side}", key=f"skip_side_{idx}_{side_idx}"):
                stop_timer()
                st.session_state.plank_side_index += 1
                nxt = st.session_state.plank_side_index
                if nxt < len(sides):
                    start_rest_timer(duration)
                else:
                    start_rest_timer(REST_DURATION)
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

        render_timer_display(duration, f"⏱ {current_side} Side")
        time.sleep(1)
        st.rerun()
        return

    # ── Dot progress indicator ────────────────────────────────
    dots_html = '<div class="hold-dot-row">'
    for i in range(len(sides)):
        cls = "done" if i < side_idx else ("active" if i == side_idx else "")
        dots_html += f'<div class="hold-dot {cls}"></div>'
    dots_html += "</div>"

    st.markdown(
        f'<div class="glass-card">{dots_html}'
        f'<div class="set-label" style="margin-top:0.5rem;">{current_side} Side — {side_idx+1} of {len(sides)}</div>'
        f'<div class="reps-label">⏱ {duration} seconds</div>'
        f'</div>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="btn-primary">', unsafe_allow_html=True)
    if st.button(f"▶️ Start {current_side} Side", key=f"start_plank_{idx}_{side_idx}"):
        start_rest_timer(duration)
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
# RENDER: Active exercise dispatcher
# ─────────────────────────────────────────────────────────────

def render_active_exercise() -> None:
    exercises = get_exercises()
    idx = st.session_state.current_exercise_index
    ex  = exercises[idx]

    st.markdown(
        f'<div class="exercise-title">{ex.get("emoji", "")} {ex["name"]}</div>',
        unsafe_allow_html=True,
    )
    st.markdown('<div class="glass-divider"></div>', unsafe_allow_html=True)

    ex_type = ex.get("type", "reps")
    if ex_type == "reps":
        render_reps_exercise(ex, idx)
    elif ex_type == "hold_series":
        render_hold_series_exercise(ex, idx)
    elif ex_type == "timed_sides":
        render_timed_sides_exercise(ex, idx)


# ─────────────────────────────────────────────────────────────
# RENDER: Home page
# ─────────────────────────────────────────────────────────────

def render_home_page() -> None:
    st.markdown(
        '<div class="app-title">💪 Workout Tracker</div>'
        '<div class="app-subtitle">3x / week training plan</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="glass-card" style="text-align:center;padding:1.4rem 1.6rem;">'
        '<div style="color:rgba(255,255,255,0.6);font-size:0.95rem;">Select today\'s workout to begin</div>'
        '</div>',
        unsafe_allow_html=True,
    )
    col1, col2 = st.columns(2, gap="medium")
    with col1:
        st.markdown('<div class="btn-home">', unsafe_allow_html=True)
        if st.button("🏋️ Full Body\nWorkout", key="btn_fullbody"):
            st.session_state.workout_type = "fullbody"
            st.session_state.page = "setup"
            reset_workout()
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="btn-home">', unsafe_allow_html=True)
        if st.button("🔥 Abs\nWorkout", key="btn_abs"):
            st.session_state.workout_type = "abs"
            st.session_state.page = "workout"
            reset_workout()
            st.session_state.completed_exercises = [False] * len(ABS_EXERCISES)
            st.session_state.workout_start_time = datetime.datetime.now()
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align:center;margin-top:2rem;color:rgba(255,255,255,0.35);font-size:0.82rem;">'
        "Full Body: 5 exercises · 4–8 sets · 15 reps each &nbsp;|&nbsp; Abs: 3 exercises · mixed reps & holds"
        "</div>",
        unsafe_allow_html=True,
    )


# ─────────────────────────────────────────────────────────────
# RENDER: Setup page
# ─────────────────────────────────────────────────────────────

def render_setup_page() -> None:
    st.markdown('<div class="app-title">🏋️ Full Body Workout</div>', unsafe_allow_html=True)
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-header">Workout Setup</div>'
        '<div style="color:rgba(255,255,255,0.7);margin-bottom:1rem;">'
        "Choose how many sets you want to do for each exercise today.</div>",
        unsafe_allow_html=True,
    )
    total_sets = st.select_slider(
        "Sets per exercise",
        options=[4, 5, 6, 7, 8],
        value=st.session_state.total_sets,
        key="set_slider",
    )
    st.markdown("</div>", unsafe_allow_html=True)
    total_reps = total_sets * 15 * len(FULLBODY_EXERCISES)
    st.markdown(
        f'<div class="glass-card-inner" style="text-align:center;">'
        f'<div style="color:rgba(255,255,255,0.55);font-size:0.88rem;">Today\'s volume</div>'
        f'<div style="font-size:2rem;font-weight:800;color:#a78bfa;">{total_sets} sets</div>'
        f'<div style="color:rgba(255,255,255,0.55);font-size:0.88rem;">per exercise · {total_reps} total reps</div>'
        f'</div>',
        unsafe_allow_html=True,
    )
    col_back, col_start = st.columns([1, 2], gap="small")
    with col_back:
        st.markdown('<div class="btn-back">', unsafe_allow_html=True)
        if st.button("← Back", key="setup_back"):
            st.session_state.page = "home"
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
    with col_start:
        st.markdown('<div class="btn-primary">', unsafe_allow_html=True)
        if st.button("🚀 Start Workout", key="setup_start"):
            st.session_state.total_sets = total_sets
            st.session_state.page = "workout"
            st.session_state.completed_exercises = [False] * len(FULLBODY_EXERCISES)
            st.session_state.workout_start_time = datetime.datetime.now()
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
# RENDER: Workout page
# ─────────────────────────────────────────────────────────────

def render_workout_page() -> None:
    exercises     = get_exercises()
    total         = len(exercises)
    completed_cnt = sum(1 for c in st.session_state.completed_exercises if c)
    pct           = completed_cnt / total if total else 0
    wname = "🏋️ Full Body Workout" if st.session_state.workout_type == "fullbody" else "🔥 Abs Workout"

    col_back, col_title = st.columns([1, 4], gap="small")
    with col_back:
        st.markdown('<div class="btn-back">', unsafe_allow_html=True)
        if st.button("← Home", key="back_home"):
            st.session_state.page = "home"
            reset_workout()
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
    with col_title:
        st.markdown(
            f'<div style="font-size:1.1rem;font-weight:700;color:#a78bfa;padding-top:0.4rem;">{wname}</div>',
            unsafe_allow_html=True,
        )

    st.markdown(
        f'<div style="font-size:0.82rem;color:rgba(255,255,255,0.5);margin-bottom:0.3rem;">'
        f'{completed_cnt} of {total} exercises complete — tap any exercise to jump to it</div>',
        unsafe_allow_html=True,
    )
    st.progress(pct)
    st.markdown("<br>", unsafe_allow_html=True)

    col_list, col_active = st.columns([1, 2], gap="medium")
    with col_list:
        render_exercise_checklist(exercises, st.session_state.current_exercise_index)
    with col_active:
        render_active_exercise()


# ─────────────────────────────────────────────────────────────
# RENDER: Completion page
# ─────────────────────────────────────────────────────────────

def render_completion_page() -> None:
    exercises = get_exercises()
    wname     = "Full Body Workout" if st.session_state.workout_type == "fullbody" else "Abs Workout"
    elapsed_str = ""
    if st.session_state.workout_start_time:
        elapsed = datetime.datetime.now() - st.session_state.workout_start_time
        elapsed_str = f"~{int(elapsed.total_seconds()) // 60} minutes"

    st.markdown(
        '<div class="complete-title">🎉 Workout Complete!</div>'
        f'<div class="complete-subtitle">{wname} · {elapsed_str}</div>',
        unsafe_allow_html=True,
    )
    st.markdown('<div class="glass-card"><div class="section-header">Summary</div>', unsafe_allow_html=True)
    for i, ex in enumerate(exercises):
        emoji   = ex.get("emoji", "")
        ex_type = ex.get("type", "reps")
        if ex_type == "reps":
            total_sets = st.session_state.total_sets if st.session_state.workout_type == "fullbody" else ex.get("sets", 3)
            sets_done  = max(0, st.session_state.sets_completed.get(i, 1) - 1)
            reps       = ex.get("reps", 15)
            detail     = f"{sets_done} sets × {reps} reps = {sets_done * reps} reps"
        elif ex_type == "hold_series":
            detail = "3 × 30s holds completed"
        else:
            detail = "2 sides × 45s completed"
        st.markdown(
            f'<div class="summary-item">'
            f'<span style="font-size:1.3rem;">{emoji}</span>'
            f'<span><strong>{ex["name"]}</strong><br>'
            f'<span style="color:rgba(255,255,255,0.55);font-size:0.85rem;">{detail}</span></span>'
            f'</div>',
            unsafe_allow_html=True,
        )
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="btn-primary">', unsafe_allow_html=True)
    if st.button("🔄 Start New Workout", key="new_workout"):
        st.session_state.page = "home"
        reset_workout()
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
# MAIN ROUTER
# ─────────────────────────────────────────────────────────────

def main() -> None:
    inject_css()
    init_state()
    page = st.session_state.page
    if page == "home":
        render_home_page()
    elif page == "setup":
        render_setup_page()
    elif page == "workout":
        render_workout_page()
    elif page == "complete":
        render_completion_page()
    else:
        st.session_state.page = "home"
        st.rerun()


if __name__ == "__main__":
    main()
