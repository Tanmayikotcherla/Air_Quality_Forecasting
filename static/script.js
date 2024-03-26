function predictAirQuality() {
    var temperature = document.getElementById("temperature").value;
    var humidity = document.getElementById("humidity").value;
    var windSpeed = document.getElementById("wind-speed").value;
    var pollutantEmissions = document.getElementById("pollutant-emissions").value;

    // Make sure all inputs are filled
    if (!temperature || !humidity || !windSpeed || !pollutantEmissions) {
        alert("Please fill all fields");
        return;
    }

    // Send prediction request to Flask backend
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            temperature: temperature,
            humidity: humidity,
            windSpeed: windSpeed,
            pollutantEmissions: pollutantEmissions
        }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("predicted-index").textContent = data.predictedIndex;
        document.getElementById("result-container").style.display = "block";
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}
