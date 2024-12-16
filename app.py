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

    :return criteria_values:
    """
    criteria: dict[str, dict[str]] = load_json("criteria.json")
    criteria_values: dict[str, str | None] = {key: request.form.get(key) for key in criteria.keys()}
    return criteria_values


# Landing page
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


# Breed information page
@app.route("/breeds/<breed_name>", methods=["GET", "POST"])
@app.route("/breeds", methods=["GET", "POST"])
def breed_info(breed_name: str = None):
    data: dict[str, dict[str, int | list[str]]] = load_json("dogs.json")

    if request.method == "POST":
        raw_breed_info = data.get(breed_name)

        if raw_breed_info:
            return jsonify(raw_breed_info)
        else:
            return jsonify({"error": "Breed not found"}), 404

    return render_template("breed_info.html", breeds=list(data.keys()))


# Search page for dogs based on criteria
@app.route("/search", methods=["GET", "POST"])
def search():
    breeds: dict[str, dict[str, int | list[str]]] = load_json("dogs.json")
    criteria: dict[str, dict[str]] = load_json("criteria.json")

    if request.method == "POST":
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

        matching_breeds: list[str] = [breed for breed in breeds.keys() if breed not in not_matching_breeds]

        return render_template("search.html", breeds=matching_breeds, search=True, criteria=criteria)

    return render_template("search.html", search=False, criteria=criteria)


@app.route("/research")
def research():
    return render_template("research.html")


if __name__ == "__main__":
    app.run()
