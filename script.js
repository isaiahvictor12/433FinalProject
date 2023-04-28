// Define data for the temperature chart
const temperatureData = {
  labels: [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
  ],
  datasets: [
    {
      label: "Temperature",
      data: [18, 19, 20, 22, 24, 27, 29, 30, 28, 25, 21, 19],
      backgroundColor: "rgba(255, 99, 132, 0.2)",
      borderColor: "rgba(255, 99, 132, 1)",
      borderWidth: 1,
    },
  ],
};

// Define data for the light chart
const lightData = {
  labels: [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
  ],
  datasets: [
    {
      label: "Light",
      data: [120, 125, 130, 140, 150, 160, 170, 180, 170, 160, 150, 140],
      backgroundColor: "rgba(255, 205, 86, 0.2)",
      borderColor: "rgba(255, 205, 86, 1)",
      borderWidth: 1,
    },
  ],
};

// Define data for the humidity chart
const humidityData = {
  labels: [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
  ],
  datasets: [
    {
      label: "Humidity",
      data: [75, 72, 70, 68, 65, 63, 60, 58, 60, 63, 68, 72],
      backgroundColor: "rgba(54, 162, 235, 0.2)",
      borderColor: "rgba(54, 162, 235, 1)",
      borderWidth: 1,
    },
  ],
};

// Create the temperature chart
const temperatureChart = new Chart(
  document.getElementById("temperatureChart"),
  {
    type: "line",
    data: temperatureData,
    options: {
      scales: {
        yAxes: [
          {
            ticks: {
              beginAtZero: true,
            },
          },
        ],
      },
    },
  }
);

// Create the light chart
const lightChart = new Chart(document.getElementById("lightChart"), {
  type: "line",
  data: lightData,
  options: {
    scales: {
      yAxes: [
        {
          ticks: {
            beginAtZero: true,
          },
        },
      ],
    },
  },
});

// Create the humidity chart
const humidityChart = new Chart(document.getElementById("humidityChart"), {
  type: "line",
  data: humidityData,
  options: {
    scales: {
      yAxes: [
        {
          ticks: {
            beginAtZero: true,
          },
        },
      ],
    },
  },
});
