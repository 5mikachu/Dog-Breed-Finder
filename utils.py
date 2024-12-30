import json

from flask import request


def load_json(file_name: str) -> dict:
    """
    Load a JSON file
    :param file_name:
    :return:
    """
    try:
        with open(file_name) as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: {file_name} not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from {file_name}.")
        return {}


def create_criteria_values() -> dict[str, str | None]:
    """
    Create the dict of all the criteria

    :return criteria_values: Dict of all the criteria
    """
    criteria: dict[str, dict[str]] = load_json("criteria.json")
    criteria_values: dict[str, str | None] = {key: request.form.get(key) for key in criteria.keys()}

    for key, value in criteria_values.items():
        if value not in ["yes", "no", "small_apartment", "house_with_yard", "low", None]:
            criteria_values[key] = None

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
