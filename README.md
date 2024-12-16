# Dog Breed Finder

Dog Breed Finder is a Flask-based web application that allows users to search for information about different dog breeds and find breeds based on specific criteria like compatibility with children, living environment, and training requirements.

## Features

* **Breed Information**: View detailed information about specific dog breeds.
* **Search Tool**: Find dog breeds based on user-defined criteria (e.g., suitable for small apartments, good with children).
* **Dynamic Forms**: Select a breed from a dropdown menu, and get instant information through an interactive interface.

## Installation

### Requirements

* Python 3.7+
* Flask
* A web browser (to view the app)

### Steps

1. Clone the repository:
```shell
git clone https://github.com/5mikachu/dog-breed-finder.git
cd dog-breed-finder
```

2. Install required dependencies:
```shell
pip install -r requirements.txt
```

3. Ensure you have a valid `dogs.json` file in the root directory. This file contains the dog breed data in the following structure:
```json
{
    "Affenpinscher": {
        "height": ["9", "11.5"],
        "weight": ["7", "10"],
        "life": ["12", "15"],
        "affectionate_family": "3",
        "children": "3",
        "other_dogs": "3",
        "shedding": "3",
        "groom_frequency": "3",
        "drooling": "1",
        "coat_type": ["wiry"],
        "coat_length": ["short", "medium"],
        "strangers": "5",
        "playfulness": "3",
        "protective": "3",
        "adaptability": "3",
        "trainability": "3",
        "energy": "3",
        "barking": "3",
        "stimulation_needs": "3"
    },
}
```

4. Run the Flask application:
```shell
python app.py
```

5. Open your browser and navigate to http://127.0.0.1:5000 to access the app.

## Usage

### Accessing Breed Information

1. Go to the "Breed Information" page.
2. Select a dog breed from the dropdown menu.
3. View the detailed information about the selected breed.

### Searching for Breeds

1. Go to the "Search" page.
2. Fill out the form with your needs and situation (e.g., children, apartment size).
3. Submit the form to see a list of matching breeds.

## Contributing

Contributions are welcome if you find a bug or want to add a feature!

### File Structure

```text
├── app.py               # Main application logic
├── templates            # HTML templates for Flask routes
│   ├── index.html
│   ├── header.html
│   ├── breed_info.html
│   ├── research.html
│   └── search.html
├── static               # Static files (JavaScript, CSS)
│   ├── scripts.js
│   └── styles.css
├── criteria.json
├── dogs.json            # JSON data file containing breed information
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

### Adding Search Criteria

1. Open `criteria.json`
2. Add the criteria in the following format:
``` json
"[criterium_id]": {
        "label": "[Excplenation of the criterium]",
        "options": {
            "[option_id_1]": "[Excplenation of option 1]",
            "[option_id_n]": "[Excplenation of option n]"
        }
    }
```
