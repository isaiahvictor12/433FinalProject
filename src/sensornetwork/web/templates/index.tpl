<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>433 Final Project</title>
    <script>
    var s = "{{data}}".replace(/\&quot\;/g, "\"");
    var myData = JSON.parse(s);
    </script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link rel="stylesheet" href="/static/style.css" />
  </head>
  <body>
    <header>
      <h1>433 Final Project</h1>
    </header>
    <div class="container">
      <h2>Temperature Chart</h2>
      <div class="temp-chart-wrapper">
        <div class="chart-tabs" id="temp-chart-tabs">
          <button class="active" onclick="showTempChart('24hr')" id="24hr-tab">
            24-hr
          </button>
          <button onclick="showTempChart('7day')" id="7day-tab">7-day</button>
          <button onclick="showTempChart('30day')" id="30day-tab">
            30-day
          </button>
        </div>
        <div class="chart-container">
          <canvas id="temp-chart" class="chart"></canvas>
        </div>
      </div>

      <h2>Light Chart</h2>
      <div class="light-chart-wrapper">
        <div class="chart-tabs" id="light-chart-tabs">
          <button class="active" onclick="showLightChart('24hr')" id="24hr-tab">
            24-hr
          </button>
          <button onclick="showLightChart('7day')" id="7day-tab">7-day</button>
          <button onclick="showLightChart('30day')" id="30day-tab">
            30-day
          </button>
        </div>
        <div class="chart-container">
          <canvas id="light-chart" class="chart"></canvas>
        </div>
      </div>

      <h2>Humidity Chart</h2>
      <div class="humidity-chart-wrapper">
        <div class="chart-tabs" id="humidity-chart-tabs">
          <button
            class="active"
            onclick="showHumidityChart('24hr')"
            id="24hr-tab"
          >
            24-hr
          </button>
          <button onclick="showHumidityChart('7day')" id="7day-tab">
            7-day
          </button>
          <button onclick="showHumidityChart('30day')" id="30day-tab">
            30-day
          </button>
        </div>
        <div class="chart-container">
          <canvas id="humidity-chart" class="chart"></canvas>
        </div>
      </div>
    </div>
    <script src="/static/script.js"></script>
  </body>
</html>
