
function handleBoxClick(event) {
    // Get the data-info attribute value
    const info = event.target.dataset.info;

    // Navigate to the other page
    window.location.href = 'commitee_member.html?info=${encodeURIComponent(info)}';
}

function fetchJSONData() {
    fetch('datasource/council_committee_JSON.json')
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
        const categories = ["Finance, Health, Transport, Staff Management, Housing, Order, Licensing, Health, Education"]
        const boxes = document.querySelectorAll('.box')
        try{
            // console.log(committee)
            boxes[idx].textContent = `${committee.Category}`;
            boxes[idx].setAttribute('data-info', `${committee.Category}`);
            boxes[idx].addEventListener('click', handleBoxClick);
        }
        catch{
            return
        };
            
    });
}

// Call the fetchJSONData function to fetch and display the JSON data
fetchJSONData();