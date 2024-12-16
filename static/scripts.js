document.addEventListener("DOMContentLoaded", function () {
    if (window.location.href === "http://127.0.0.1:5000/breeds") {
        window.location.replace("http://127.0.0.1:5000/breeds/None");
    }
});

document.addEventListener("DOMContentLoaded", function () {
    const breedSelect = document.getElementById("breed");
    const pathArray = window.location.pathname.split('/');
    const breedFromURL = pathArray[pathArray.length - 1];  // Get the breed from the URL

    if (breedFromURL) {
        for (let i = 0; i < breedSelect.options.length; i++) {
            if (breedSelect.options[i].value.toLowerCase() === breedFromURL) {
                breedSelect.selectedIndex = i;
                break;
            }
        }

        renderBreedInfo(breedFromURL)
    }
});

document.getElementById('breed').addEventListener('change', function () {
    updateURL(this.value);
    renderBreedInfo(this.value);
});

// Function to get breed information and push it to the page
function renderBreedInfo(breedName) {
    // AJAX request to get breed information
    fetch(`/breeds/${breedName}`, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
    })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                document.getElementById('breedInfo').innerHTML = `<p>${data.error}</p>`;
            } else {
                document.getElementById('breedInfo').innerHTML = `
                <div class="flex-item">
                    <h2>Physical Attributes</h2>
                    <ul>
                        <li><strong>Height:</strong> <br /> <em>${data.height}</em></li>
                        <li><strong>Weight:</strong> <br /> <em>${data.weight}</em></li>
                        <li><strong>Life Expectancy:</strong> <br /> <em>${data.life}</em></li>
                        <li><strong>Coat Type:</strong> <br /> <em>${data.coat_type}</em></li>
                        <li><strong>Coat Length:</strong> <br /> <em>${data.coat_length}</em></li>
                    </ul>
                </div>

                <div class="flex-item">
                    <h2>Temperament</h2>
                    ${renderBar('Affectionate with Family', data.affectionate_family)}
                    ${renderBar('Good with Children', data.children)}
                    ${renderBar('Good with Other Dogs', data.other_dogs)}
                    ${renderBar('Friendliness with Strangers', data.strangers)}
                    ${renderBar('Playfulness Level', data.playfulness)}
                    ${renderBar('Protective Nature', data.protective)}
                </div>

                <div class="flex-item">
                    <h2>Care Requirements</h2>
                    ${renderBar('Shedding Level', data.shedding)}
                    ${renderBar('Grooming Frequency', data.groom_frequency)}
                    ${renderBar('Drooling Level', data.drooling)}
                    ${renderBar('Adaptability', data.adaptability)}
                    ${renderBar('Trainability', data.trainability)}
                    ${renderBar('Energy Level', data.energy)}
                    ${renderBar('Barking Level', data.barking)}
                    ${renderBar('Stimulation Needs', data.stimulation_needs)}
                </div>

                <div class="flex-item">
                    <h2>Exercise tips</h2>
                    <ul>
                        <li>HELP</li>
                    </ul>
                </div>
            `;
            }
        })
}

// function to render an attribute with a loading bar
function renderBar(title, value) {
    const percentage = value * 20;  // Convert 1-5 scale to percentage
    return `
        <li>
            <strong>${title}:</strong> <br /> <em>${value}</em>
            <div class="loading-bar">
                <div class="bar" style="width: ${percentage}%;"></div>
            </div>
        </li>
    `;
}

// Function to change the URL, without a page-load
function updateURL(value) {
    var state = {breed: value};
    history.pushState(state, null, value);
}
