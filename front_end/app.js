document.addEventListener("DOMContentLoaded", function() {
    const tripForm = document.getElementById("trip-form");
    tripForm.addEventListener("submit", function(event) {
        event.preventDefault();
        const startStation = document.getElementById("start-station").value;
        const endStation = document.getElementById("end-station").value;
        // Send the start and end station data to the backend for route planning
        // Display the result on the result page
        // You can use AJAX or fetch API for this purpose
        // Redirect to the result page once you have the route information
        window.location.href = `result.html?start=${startStation}&end=${endStation}`;
    });
});