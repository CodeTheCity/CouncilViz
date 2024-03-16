
function handleBoxClick(event) {
    // Get the data-info attribute value
    const info = event.target.dataset.info;

    // Navigate to the other page
    window.location.href = 'commitee_member.html/?info=${encodeURIComponent(info)}';
}

document.querySelectorAll('.box').addEventListener('click', handleBoxClick);

// Call the fetchJSONData function to fetch and display the JSON data
fetchJSONData();