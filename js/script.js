
function handleBoxClick(event) {
    // Get the data-info attribute value
    const info = event.target.dataset.info;

    // Navigate to the other page
    window.location.href = 'commitee_member.html?info=${encodeURIComponent(info)}';
}

document.querySelectorAll('.box').forEach((box,idx) => {
    box.setAttribute('data-info', jsonobj[idx]);
    box.addEventListener('click', handleBoxClick);
});