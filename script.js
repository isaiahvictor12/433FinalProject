// Initialize temperature chart with 24-hour view
var ctx = document.getElementById("temp-chart").getContext("2d");
var temp_chart = new Chart(ctx, {
  type: "line",
  data: {
    labels: ["12AM", "3AM", "6AM", "9AM", "12PM", "3PM", "6PM", "9PM"],
    datasets: [
      {
        label: "Temperature (°C)",
        data: [23, 22, 21, 24, 27, 26, 25, 22],
        borderColor: "#ff6384",
        fill: false,
      },
    ],
  },
});

// Show light chart for selected time period
function showTempChart(period) {
  // Update active tab
  var tabs = document
    .getElementById("temp-chart-tabs")
    .getElementsByTagName("button");
  for (var i = 0; i < tabs.length; i++) {
    tabs[i].classList.remove("active");
    if (tabs[i].id == period + "-tab") {
      tabs[i].classList.add("active");
    }
  }
  // Update chart data
  // Update chart data
  switch (period) {
    case "24hr":
      temp_chart.data.labels = [
        "12AM",
        "1AM",
        "2AM",
        "3AM",
        "4AM",
        "5AM",
        "6AM",
        "7AM",
        "8AM",
        "9AM",
        "10AM",
        "11AM",
        "12PM",
        "1PM",
        "2PM",
        "3PM",
        "4PM",
        "5PM",
        "6PM",
        "7PM",
        "8PM",
        "9PM",
        "10PM",
        "11PM",
      ];
      temp_chart.data.datasets[0].data = [
        23, 22, 21, 24, 27, 26, 25, 22, 23, 25, 26, 27, 28, 29, 30, 31, 32, 33,
        34, 33, 32, 31, 29, 28,
      ];
      break;
    case "7day":
      temp_chart.data.labels = [
        "Mon",
        "Tue",
        "Wed",
        "Thu",
        "Fri",
        "Sat",
        "Sun",
      ];
      temp_chart.data.datasets[0].data = [22, 23, 25, 24, 27, 26, 23];
      break;
    case "30day":
      temp_chart.data.labels = ["Week 1", "Week 2", "Week 3", "Week 4"];
      temp_chart.data.datasets[0].data = [24, 26, 23, 25];
      break;
  }

  temp_chart.update();
}

// Initialize temperature chart with 24-hour view
var ctx = document.getElementById("light-chart").getContext("2d");
var light_chart = new Chart(ctx, {
  type: "line",
  data: {
    labels: ["12AM", "3AM", "6AM", "9AM", "12PM", "3PM", "6PM", "9PM"],
    datasets: [
      {
        label: "Light",
        data: [23, 22, 21, 24, 27, 26, 25, 22],
        borderColor: "#ff6384",
        fill: false,
      },
    ],
  },
});

// Show chart for selected time period
function showLightChart(period) {
  // Update active tab
  var tabs = document
    .getElementById("light-chart-tabs")
    .getElementsByTagName("button");
  for (var i = 0; i < tabs.length; i++) {
    tabs[i].classList.remove("active");
    if (tabs[i].id == period + "-tab") {
      tabs[i].classList.add("active");
    }
  }

  // Update chart data
  switch (period) {
    case "24hr":
      light_chart.data.labels = [
        "12AM",
        "1AM",
        "2AM",
        "3AM",
        "4AM",
        "5AM",
        "6AM",
        "7AM",
        "8AM",
        "9AM",
        "10AM",
        "11AM",
        "12PM",
        "1PM",
        "2PM",
        "3PM",
        "4PM",
        "5PM",
        "6PM",
        "7PM",
        "8PM",
        "9PM",
        "10PM",
        "11PM",
      ];
      light_chart.data.datasets[0].data = [
        23, 22, 21, 24, 27, 26, 25, 22, 23, 25, 26, 27, 28, 29, 30, 31, 32, 33,
        34, 33, 32, 31, 29, 28,
      ];
      break;
    case "7day":
      light_chart.data.labels = [
        "Mon",
        "Tue",
        "Wed",
        "Thu",
        "Fri",
        "Sat",
        "Sun",
      ];
      light_chart.data.datasets[0].data = [22, 23, 25, 24, 27, 26, 23];
      break;
    case "30day":
      light_chart.data.labels = ["Week 1", "Week 2", "Week 3", "Week 4"];
      light_chart.data.datasets[0].data = [24, 26, 23, 25];
      break;
  }

  light_chart.update();
}

// Initialize temperature chart with 24-hour view
var ctx = document.getElementById("humidity-chart").getContext("2d");
var humidity_chart = new Chart(ctx, {
  type: "line",
  data: {
    labels: ["12AM", "3AM", "6AM", "9AM", "12PM", "3PM", "6PM", "9PM"],
    datasets: [
      {
        label: "Humidity",
        data: [23, 22, 21, 24, 27, 26, 25, 22],
        borderColor: "#ff6384",
        fill: false,
      },
    ],
  },
});

// Show chart for selected time period
function showHumidityChart(period) {
  // Update active tab
  var tabs = document
    .getElementById("humidity-chart-tabs")
    .getElementsByTagName("button");
  for (var i = 0; i < tabs.length; i++) {
    tabs[i].classList.remove("active");
    if (tabs[i].id == period + "-tab") {
      tabs[i].classList.add("active");
    }
  }

  // Update chart data
  // Update chart data
  switch (period) {
    case "24hr":
      humidity_chart.data.labels = [
        "12AM",
        "1AM",
        "2AM",
        "3AM",
        "4AM",
        "5AM",
        "6AM",
        "7AM",
        "8AM",
        "9AM",
        "10AM",
        "11AM",
        "12PM",
        "1PM",
        "2PM",
        "3PM",
        "4PM",
        "5PM",
        "6PM",
        "7PM",
        "8PM",
        "9PM",
        "10PM",
        "11PM",
      ];
      humidity_chart.data.datasets[0].data = [
        23, 22, 21, 24, 27, 26, 25, 22, 23, 25, 26, 27, 28, 29, 30, 31, 32, 33,
        34, 33, 32, 31, 29, 28,
      ];
      break;
    case "7day":
      humidity_chart.data.labels = [
        "Mon",
        "Tue",
        "Wed",
        "Thu",
        "Fri",
        "Sat",
        "Sun",
      ];
      humidity_chart.data.datasets[0].data = [22, 23, 25, 24, 27, 26, 23];
      break;
    case "30day":
      humidity_chart.data.labels = ["Week 1", "Week 2", "Week 3", "Week 4"];
      humidity_chart.data.datasets[0].data = [24, 26, 23, 25];
      break;
  }

  humidity_chart.update();
}
