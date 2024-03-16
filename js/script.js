
function handleBoxClick(event) {
    // Get the data-info attribute value
    const info = event.target.dataset.info;

    // Navigate to the other page
    window.location.href = 'commitee_member.html?info=${encodeURIComponent(info)}';
}

document.querySelectorAll('.box').forEach(box => {
    box.addEventListener('click', handleBoxClick);
});