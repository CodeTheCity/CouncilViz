

function handleBoxClick(event) {
    // Get the data-info attribute value
    const info = event.target.dataset.info;
    // Navigate to the other page
    window.location.href = `commitee_member.html?info=${encodeURIComponent(info)}`;
}

function fetchJSONData(json_file) {
    fetch(json_file)
    .then(response => response.json())
    .then(data => {
        // Call a function to process the data
        displayCommittees(data);
    })
    .catch(error => console.error('Error fetching data:', error));
}

// Function to display the JSON data
function displayCommittees(data) {
    // Access the array of objects
    data.forEach((committee, idx) => {
        // Create list item for each committee
        const boxes = document.querySelectorAll('.box')
        try{
            // console.log(committee)
            boxes[idx].textContent = `${committee}`;
            boxes[idx].setAttribute('data-info', `${committee}`);
            boxes[idx].addEventListener('click', handleBoxClick);
        }
        catch{
            return
        };
            
    });
}

// Call the fetchJSONData function to fetch and display the JSON data
fetchJSONData('/council_committee_categories.json');