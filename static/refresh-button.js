document.addEventListener('DOMContentLoaded', function() {
    const refreshButton = document.getElementById('refresh-button');

    refreshButton.addEventListener('click', function() {
        // Add your refresh logic here
        location.reload(); // Example: Reload the page
    });
});
