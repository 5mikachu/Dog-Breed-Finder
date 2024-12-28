import json

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


def load_json(file_name: str) -> dict:
    """
    Load a JSON file

    :param file_name:
    :return:
    """
    with open(file_name) as f:
        return json.load(f)


def create_criteria_values() -> dict[str, str | None]:
    """
    Create the dict of all the criteria

    :return criteria_values: Dict of all the criteria
    """
    criteria: dict[str, dict[str]] = load_json("criteria.json")
    criteria_values: dict[str, str | None] = {key: request.form.get(key) for key in criteria.keys()}
    return criteria_values


def get_matching_breeds() -> list[str]:
    """
    Get the list of matching breeds based on the criteria values

    :return: List of matching breeds
    """
    breeds: dict[str, dict[str, int | list[str]]] = load_json("dogs.json")
    criteria_values: dict[str, str | None] = create_criteria_values()

    not_matching_breeds: list[str] = [
        breed for breed, info in breeds.items() if any([
            (criteria_values["children"] == "yes" and int(info.get("children", 1)) < 3),
            (criteria_values["other_dogs"] == "yes" and int(info.get("other_dogs", 1)) < 3),
            (criteria_values["living_situation"] == "small_apartment" and int(info.get("energy", 1)) > 1),
            (criteria_values["living_situation"] == "house_with_yard" and int(info.get("energy", 1)) > 3),
            (criteria_values["training_time"] == "low" and int(info.get("stimulation_needs", 1)) < 3)
        ])
    ]

    return [breed for breed in breeds.keys() if breed not in not_matching_breeds]


def get_exercise_tips(raw_breed_info) -> list[str]:
    """
    Get the exercise tips based on the breed information

    :param raw_breed_info:
    :return: List of exercise tips
    """
    exercise_tips: list[str] = []

    if int(raw_breed_info.get("energy")) > 3:
        exercise_tips.append("High energy level - make sure to exercise them regularly")
    if int(raw_breed_info.get("drooling")) > 3:
        exercise_tips.append("High drooling level - make sure to have a towel handy")
    if int(raw_breed_info.get("shedding")) > 3:
        exercise_tips.append("High shedding level - make sure to brush them regularly")

    return exercise_tips


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
        if breed_name == "None" or None:
            return jsonify({"error": "No breed selected"}), 200

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
