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
                const breedInfo = data.breed_info;  // Access the nested breed_info object
                document.getElementById('breedInfo').innerHTML = `
                <div class="flex-item">
                    <img class="breed-image" src="/static/img/breeds/${breedName}.jpg" alt="Image of the ${breedName}">

                    <h2>Physical Attributes</h2>
                    <ul>
                        <li><strong>Height:</strong> <br /> <em>${breedInfo.height}</em></li>
                        <li><strong>Weight:</strong> <br /> <em>${breedInfo.weight}</em></li>
                        <li><strong>Life Expectancy:</strong> <br /> <em>${breedInfo.life}</em></li>
                        <li><strong>Coat Type:</strong> <br /> <em>${breedInfo.coat_type}</em></li>
                        <li><strong>Coat Length:</strong> <br /> <em>${breedInfo.coat_length}</em></li>
                    </ul>
                </div>

                <div class="flex-item">
                    <h2>Temperament</h2>
                    ${renderBar('Affectionate with Family', breedInfo.affectionate_family)}
                    ${renderBar('Good with Children', breedInfo.children)}
                    ${renderBar('Good with Other Dogs', breedInfo.other_dogs)}
                    ${renderBar('Friendliness with Strangers', breedInfo.strangers)}
                    ${renderBar('Playfulness Level', breedInfo.playfulness)}
                    ${renderBar('Protective Nature', breedInfo.protective)}
                </div>

                <div class="flex-item">
                    <h2>Care Requirements</h2>
                    ${renderBar('Shedding Level', breedInfo.shedding)}
                    ${renderBar('Grooming Frequency', breedInfo.groom_frequency)}
                    ${renderBar('Drooling Level', breedInfo.drooling)}
                    ${renderBar('Adaptability', breedInfo.adaptability)}
                    ${renderBar('Trainability', breedInfo.trainability)}
                    ${renderBar('Energy Level', breedInfo.energy)}
                    ${renderBar('Barking Level', breedInfo.barking)}
                    ${renderBar('Stimulation Needs', breedInfo.stimulation_needs)}
                </div>

                <div class="flex-item" id="tips_container">
                    <h2>Exercise tips</h2>
                    <ul>
                        ${Array.isArray(data.exercise_tips) ? data.exercise_tips.map(tip => `<li>${tip}</li>`).join('') : '<li>No exercise tips available</li>'}
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
