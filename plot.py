import base64
from io import BytesIO
import matplotlib.pyplot as plt

# Temperature plot
x_temp = [1, 2, 3, 4, 5]
y_temp = [10, 20, 30, 25, 20]

plt.plot(x_temp, y_temp)
plt.title('Temperature')
plt.xlabel('Time')
plt.ylabel('Temperature (C)')

buffer_temp = BytesIO()
plt.savefig(buffer_temp, format='png')
buffer_temp.seek(0)

plot_data_temp = base64.b64encode(buffer_temp.getvalue()).decode()

# Light plot
x_light = [1, 2, 3, 4, 5]
y_light = [800, 850, 900, 950, 1000]

plt.clf() # clear previous plot
plt.plot(x_light, y_light)
plt.title('Light')
plt.xlabel('Time')
plt.ylabel('Light (lux)')

buffer_light = BytesIO()
plt.savefig(buffer_light, format='png')
buffer_light.seek(0)

plot_data_light = base64.b64encode(buffer_light.getvalue()).decode()

# Humidity plot
x_humidity = [1, 2, 3, 4, 5]
y_humidity = [40, 50, 60, 55, 50]

plt.clf() # clear previous plot
plt.plot(x_humidity, y_humidity)
plt.title('Humidity')
plt.xlabel('Time')
plt.ylabel('Humidity (%)')

buffer_humidity = BytesIO()
plt.savefig(buffer_humidity, format='png')
buffer_humidity.seek(0)

plot_data_humidity = base64.b64encode(buffer_humidity.getvalue()).decode()

# Generate HTML code to display plots
html = f"""
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>433 Final Project</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <header>
      <h1>433 Final Project</h1>
    </header>
    <div class="container">
      <h2>Temperature Chart</h2>
      <div class="chart-container">
        <img src='data:image/png;base64,{plot_data_temp}'/>
      </div>

      <h2>Light Chart</h2>
      <div class="chart-container">
        <img src='data:image/png;base64,{plot_data_light}'/>
      </div>

      <h2>Humidity Chart</h2>
      <div class="chart-container">
        <img src='data:image/png;base64,{plot_data_humidity}'/>
      </div>
    </div>
  </body>
</html>
"""

# Write HTML code to file
with open('plot.html', 'w') as f:
    f.write(html)
