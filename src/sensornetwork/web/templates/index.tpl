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

        <div class="chart-container">
          <canvas id="temp-chart" class="chart"></canvas>
        </div>
      </div>

      <h2>Light Chart</h2>
      <div class="light-chart-wrapper">

        <div class="chart-container">
          <canvas id="light-chart" class="chart"></canvas>
        </div>
      </div>

      <h2>Humidity Chart</h2>
      <div class="humidity-chart-wrapper">

        <div class="chart-container">
          <canvas id="humidity-chart" class="chart"></canvas>
        </div>
      </div>
    </div>
    <script src="/static/script.js"></script>
  </body>
</html>
