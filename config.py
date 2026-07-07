"""
Workout definitions and app constants.
"""

FULLBODY_EXERCISES = [
    {
        "name": "Pull-ups",
        "emoji": "🏋️",
        "type": "reps",
        "reps": 15,
        "min_sets": 0,
        "max_sets": 10,
        "description_steps": [
            "Hang from a bar with hands slightly wider than shoulder width.",
            "Engage your core and keep your legs still.",
            "Pull your chest toward the bar by driving your elbows down.",
            "Pause briefly at the top without swinging.",
            "Lower under control until your arms are straight.",
        ],
        "image_url": "assets/pullups.png",
    },
    {
        "name": "Push-ups",
        "emoji": "💪",
        "type": "reps",
        "reps": 15,
        "min_sets": 0,
        "max_sets": 10,
        "description_steps": [
            "Start in a high plank with hands slightly wider than shoulder width.",
            "Form a straight line from head to heels and brace your core.",
            "Lower your chest toward the floor by bending your elbows.",
            "Keep elbows roughly at a 45° angle from your torso.",
            "Press the floor away to return to the starting position.",
        ],
        "image_url": "assets/pushups.png",
    },
    {
        "name": "Dips",
        "emoji": "🤸",
        "type": "reps",
        "reps": 15,
        "min_sets": 0,
        "max_sets": 10,
        "description_steps": [
            "Support yourself on parallel bars with arms straight.",
            "Keep chest up and shoulders down away from your ears.",
            "Bend your elbows to lower until shoulders are just below elbows.",
            "Avoid swinging or letting shoulders round forward.",
            "Press back up by driving strongly through your hands.",
        ],
        "image_url": "assets/dips.png",
    },
    {
        "name": "Squats",
        "emoji": "🦵",
        "type": "reps",
        "reps": 15,
        "min_sets": 0,
        "max_sets": 10,
        "description_steps": [
            "Stand with feet slightly wider than shoulder width, toes slightly turned out.",
            "Brace your core and keep your chest up.",
            "Push your hips back first, then bend your knees to lower.",
            "Keep your heels down and knees tracking over your toes.",
            "Drive through your feet to stand up and squeeze your glutes.",
        ],
        "image_url": "assets/squats.png",
    },
    {
        "name": "Rows",
        "emoji": "🚣",
        "type": "reps",
        "reps": 15,
        "min_sets": 0,
        "max_sets": 10,
        "description_steps": [
            "Hold the handles or bar with a neutral spine.",
            "Pull your elbows back, squeezing your shoulder blades together.",
            "Pause briefly with the handles close to your torso.",
            "Lower under control without rounding your back.",
            "Repeat with smooth, controlled reps.",
        ],
        "image_url": "assets/rows.png",
    },
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
            {"name": "Core Hold 1 — Hands down, legs up", "duration": 30},
            {"name": "Core Hold 2 — Hands up, legs up", "duration": 30},
            {"name": "Core Hold 3 — Hands up, legs alternate", "duration": 30},
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
DEFAULT_SETS  = 4     # default for full-body if user hasn't chosen yet
