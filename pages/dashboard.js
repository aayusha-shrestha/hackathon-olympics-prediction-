function showContent(boxId) {
    // Hide all content boxes
    const boxes = document.querySelectorAll('.content-box');
    boxes.forEach(box => box.style.display = 'none');
    
    // Show the selected content box
    const selectedBox = document.getElementById(boxId);
    if (selectedBox) {
        selectedBox.style.display = 'flex';
    }
}

