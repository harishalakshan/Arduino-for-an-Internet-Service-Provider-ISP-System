import React from 'react';
import Chart from 'chart.js/auto';

function Dashboard() {
  React.useEffect(() => {
    const ctx = document.getElementById("myChart");
    new Chart(ctx, {
      type: "line",
      data: {
        labels: ["Jan", "Feb", "Mar", "Apr"],
        datasets: [{
          label: "Temperature",
          data: [20, 21, 19, 23],
          borderColor: "rgba(75,192,192,1)",
          fill: false
        }]
      }
    });
  }, []);

  return (
    <div>
      <h2>Real-Time Sensor Dashboard</h2>
      <canvas id="myChart" width="400" height="200"></canvas>
    </div>
  );
}

export default Dashboard;
