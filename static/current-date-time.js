function updateDateTime() {
    const currentDateElement = document.getElementById('current-date');
    const currentTimeElement = document.getElementById('current-time');

    // Get the current date and time
    const currentDateTime = new Date();

    // Format date as "YYYY-MM-DD"
    const formattedDate = currentDateTime.toISOString().slice(0, 10);

    // Format time as "HH:MM:SS"
    const formattedTime = currentDateTime.toLocaleTimeString();

    // Update the content of the elements
    currentDateElement.textContent = `Date: ${formattedDate}`;
    currentTimeElement.textContent = `Time: ${formattedTime}`;
}

// Call the function initially to display the date and time
updateDateTime();

// Update the date and time every second (1000 milliseconds)
//setInterval(updateDateTime, 1000);

