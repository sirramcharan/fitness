"""
Workout definitions and app constants.
"""

FULLBODY_EXERCISES = [
    {"name": "Pull-ups", "emoji": "🏋️", "type": "reps", "reps": 15, "min_sets": 4, "max_sets": 8},
    {"name": "Push-ups", "emoji": "💪", "type": "reps", "reps": 15, "min_sets": 4, "max_sets": 8},
    {"name": "Dips",     "emoji": "🤸", "type": "reps", "reps": 15, "min_sets": 4, "max_sets": 8},
    {"name": "Squats",   "emoji": "🦵", "type": "reps", "reps": 15, "min_sets": 4, "max_sets": 8},
    {"name": "Rows",     "emoji": "🚣", "type": "reps", "reps": 15, "min_sets": 4, "max_sets": 8},
]

ABS_EXERCISES = [
    {
        "name": "Crucifix Crunches",
        "emoji": "🔥",
        "type": "reps",
        "reps": 15,
        "sets": 3,
    },
    {
        "name": "Core Hold Series",
        "emoji": "🧘",
        "type": "hold_series",
        "holds": [
            {"name": "Core Hold 1 — Hands down, legs up",        "duration": 30},
            {"name": "Core Hold 2 — Hands up, legs up",           "duration": 30},
            {"name": "Core Hold 3 — Hands up, legs alternate",    "duration": 30},
        ],
    },
    {
        "name": "Side Plank Raises",
        "emoji": "⚡",
        "type": "timed_sides",
        "duration": 45,
        "sides": ["Left", "Right"],
    },
]

REST_DURATION = 240   # 4 minutes in seconds
DEFAULT_SETS  = 6     # default for full-body if user hasn't chosen yet
