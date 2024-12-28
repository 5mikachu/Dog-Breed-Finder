from flask import Flask, render_template, request, jsonify

from utils import load_json, get_matching_breeds, get_exercise_tips

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    """
    Home page
    """
    return render_template("index.html")


@app.route("/breeds/<breed_name>", methods=["GET", "POST"])
@app.route("/breeds", methods=["GET", "POST"])
def breed_info(breed_name: str = None):
    """
    Breed information page

    :param breed_name:
    """
    data: dict[str, dict[str, int | list[str]]] = load_json("dogs.json")

    if request.method == "POST":
        if not breed_name or breed_name == "None" or breed_name not in data:
            return jsonify({"error": "No breed selected or breed not found"}), 200

        raw_breed_info = data.get(breed_name)

        if raw_breed_info:
            exercise_tips = get_exercise_tips(raw_breed_info)
            return jsonify({"breed_info": raw_breed_info, "exercise_tips": exercise_tips})
        else:
            return jsonify({"error": "Breed not found"}), 404

    return render_template("breed_info.html", breeds=list(data.keys()))


@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Search page for dogs based on criteria
    """
    criteria: dict[str, dict[str]] = load_json("criteria.json")

    if request.method == "POST":
        matching_breeds: list[str] = get_matching_breeds()
        return render_template("search.html", breeds=matching_breeds, search=True, criteria=criteria)

    return render_template("search.html", search=False, criteria=criteria)


@app.route("/research")
def research():
    """
    Research page
    """
    return render_template("research.html")


if __name__ == "__main__":
    app.run()
