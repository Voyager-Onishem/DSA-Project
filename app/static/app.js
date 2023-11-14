document.addEventListener("DOMContentLoaded", function() {
    const tripForm = document.getElementById("trip-form");
    tripForm.addEventListener("submit", function(event) {
        event.preventDefault();
        const startStation = document.getElementById("start-station").value;
        const endStation = document.getElementById("end-station").value;

        const data = {
            start: startStation,
            end: endStation
        };

        fetch("/route-planning-endpoint", {  // <-- Correct URL
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(result => {
            // Handle the route information received from the backend
            const routeInformation = result.route; // Assuming the result object has a 'route' property

            // Display the result on the result page
            const routeList = document.getElementById("route");
            routeList.innerHTML = ''; // Clear any previous content

            for (const station of routeInformation) {
                const listItem = document.createElement("li");
                listItem.textContent = station;
                routeList.appendChild(listItem);
            }

            // Redirect to the result page with route information
            window.location.href = `result.html?start=${startStation}&end=${endStation}&route=${routeInformation.join('-')}`;
        })
        .catch(error => {
            console.error("Error:", error);
        });
    });
});
