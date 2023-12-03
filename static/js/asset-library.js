document.addEventListener('DOMContentLoaded', function () {
    // Get references to the elements
    var viewMoreButton = document.querySelector('.view-more');
    var codeContent = document.querySelector('.code-content');

    // Set the initial state to hidden
    codeContent.style.display = 'none';

    // Add click event listener to the "View More" button
    viewMoreButton.addEventListener('click', function () {
        // Toggle the display property of the code content
        if (codeContent.style.display === 'none') {
            codeContent.style.display = 'block';
        } else {
            codeContent.style.display = 'none';
        }
    });
});