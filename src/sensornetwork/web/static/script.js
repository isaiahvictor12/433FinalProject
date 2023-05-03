// Initialize temperature chart with 24-hour view
var t_ctx = document.getElementById("temp-chart").getContext("2d");
var tdata = {
  labels: myData['labels'],
  datasets: [{
    data: myData['temperature']
  }],
  options: {
    scales: {
      yAxes: [{
          display: true,
          ticks: {
              suggestedMin: 15,    // minimum will be 0, unless there is a lower value.
              // OR //
              suggestMax: 30   // minimum value will be 0.
          }
      }]
    }
  }
}
var temp_chart = new Chart(t_ctx, {
  type: "line",
  data: tdata
});
temp_chart.update();
var h_ctx = document.getElementById("humidity-chart").getContext("2d");
var hdata = {
  labels: myData['labels'],
  datasets: [{
    data: myData['humidity']
  }]
}
var humidity_chart = new Chart(h_ctx, {
  type: "line",
  data: hdata,
  options: {
    scales: {
      yAxes: [{
          display: true,
          ticks: {
              suggestedMin: 0,    // minimum will be 0, unless there is a lower value.
              // OR //
              suggestMax: 1   // minimum value will be 0.
          }
      }]
    }
  }
});
humidity_chart.update();
var l_ctx = document.getElementById("light-chart").getContext("2d");
var ldata = {
  labels: myData['labels'],
  datasets: [{
    data: myData['light']
  }]
}
var light_chart = new Chart(l_ctx, {
  type: "line",
  data: ldata,
  options: {
    scales: {
      yAxes: [{
          display: true,
          ticks: {
              suggestedMin: 0,    // minimum will be 0, unless there is a lower value.
              // OR //
              suggestMax: 1   // minimum value will be 0.
          }
      }]
    }
  }
});
light_chart.update();