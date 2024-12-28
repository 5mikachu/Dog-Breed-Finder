# Technical Details for Developers

## File Structure
The application’s structure is as follows:
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

## Setting Up Locally
1. Clone the repository and install dependencies:
   ```bash
   git clone https://github.com/5mikachu/Dog-Breed-Finder.git
   cd Dog-Breed-Finder
   pip install -r requirements.txt
   ```
2. Ensure the `dogs.json` and `criteria.json` files are in the root directory.
3. Run the application:
   ```bash
   python app.py
   ```
4. Open the browser at `http://127.0.0.1:5000`.

## Extending Search Criteria
1. Edit `criteria.json` to add a new search field:
   ```json
   "new_criteria": {
       "label": "[Criteria Description]",
       "options": {
           "option1": "[Option 1 Description]",
           "option2": "[Option 2 Description]"
       }
   }
   ```
2. Update the `search` route in `app.py` to include the new criteria logic.