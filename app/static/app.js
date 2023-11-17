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

        fetch("/route-planning-endpoint", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(result => {
            // Handle the route information received from the backend
            const routeInformation = result.route;

            // Display the result on the result page
            let resultContainer = document.getElementById("result");

            // Clear previous results
            resultContainer.innerHTML = "";
            console.log(routeInformation);
            let tracker=1;
            for (const station of routeInformation) {
                const stationDiv = document.createElement("div");
                stationDiv.className = "station";
                stationDiv.textContent = station;
                if(tracker!==routeInformation.length){
                    stationDiv.textContent+="  -->";
                }
                resultContainer.append(stationDiv);
                tracker++;
            }
            // Redirect to the result page with route information
            // window.location.href = `result?start=${startStation}&end=${endStation}&route=${routeInformation.join('-')}`
        })
        .catch(error => {
            console.error("Error:", error);
        });
    });
});

