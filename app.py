from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

PROGRAMS = {
    "Fat Loss (FL)": {
        "workout": (
            "Mon: 5x5 Back Squat + AMRAP\n"
            "Tue: EMOM 20min Assault Bike\n"
            "Wed: Bench Press + 21-15-9\n"
            "Thu: 10RFT Deadlifts/Box Jumps\n"
            "Fri: 30min Active Recovery"
        ),
        "diet": (
            "B: 3 Egg Whites + Oats Idli\n"
            "L: Grilled Chicken + Brown Rice\n"
            "D: Fish Curry + Millet Roti\n"
            "Target: 2,000 kcal"
        ),
        "color": "#e74c3c",
    },
    "Muscle Gain (MG)": {
        "workout": (
            "Mon: Squat 5x5\n"
            "Tue: Bench 5x5\n"
            "Wed: Deadlift 4x6\n"
            "Thu: Front Squat 4x8\n"
            "Fri: Incline Press 4x10\n"
            "Sat: Barbell Rows 4x10"
        ),
        "diet": (
            "B: 4 Eggs + PB Oats\n"
            "L: Chicken Biryani (250g Chicken)\n"
            "D: Mutton Curry + Jeera Rice\n"
            "Target: 3,200 kcal"
        ),
        "color": "#2ecc71",
    },
    "Beginner (BG)": {
        "workout": (
            "Circuit Training: Air Squats, Ring Rows, Push-ups.\n"
            "Focus: Technique Mastery & Form (90% Threshold)"
        ),
        "diet": (
            "Balanced Tamil Meals: Idli-Sambar, Rice-Dal, Chapati.\n"
            "Protein: 120g/day"
        ),
        "color": "#3498db",
    },
}

GYM_METRICS = {
    "capacity": "150 Users",
    "area": "10,000 sq ft",
    "break_even": "250 Members",
}


@app.get("/")
def home():
    selected = request.args.get("program", "")
    if selected not in PROGRAMS:
        selected = ""

    return render_template(
        "index.html",
        programs=PROGRAMS,
        selected=selected,
        metrics=GYM_METRICS,
    )


@app.get("/health")
def health():
    return jsonify({"status": "healthy"}), 200


@app.get("/api/programs")
def list_programs():
    return jsonify(PROGRAMS), 200


@app.get("/api/programs/<path:program_name>")
def get_program(program_name):
    program = PROGRAMS.get(program_name)

    if program is None:
        return jsonify({"error": "Program not found"}), 404

    return jsonify({"name": program_name, **program}), 200


@app.errorhandler(404)
def not_found(_error):
    if request.path.startswith("/api/"):
        return jsonify({"error": "Endpoint not found"}), 404

    return "Page not found", 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
