<script lang="ts">
  import { onMount } from 'svelte';
  import { money, target, day, values, spending, revenue } from './state';
  import { Chart } from 'chart.js/auto';

  let canvas: HTMLCanvasElement;
  let chart: Chart;

  onMount(() => {
    chart = new Chart(canvas, {
      type: 'line',
      data: {
        labels: [],
        datasets: [{
          label: 'Money',
          data: $values,
        }]
      },
      options: {
        plugins: {
          legend: {
            display: false,
          }
        },
        scales: {
          y: {
            beginAtZero: true,
            max: target,
          }
        }
      }
    });

  })

  $effect(() => {
    if (!chart) return;
      // eslint-disable-next-line no-useless-assignment
      chart.data.labels = Array.from(Array($day-1).keys().map(x => ++x));
      chart.data.datasets[0].data = $values;
      chart.update();
      console.log(chart.data.datasets[0].data.length);
  })

  let finished: boolean = $derived($money >= target);
    
</script>

<div class="container">
  <div class="stat-container">
    <h2>Progress</h2>
    <div class="progress-container">
      <progress class="progress" value={$money} max={target}></progress>
      <p class="progress-label">{$money}/{target}</p>
    </div>
    <p>Spending {$spending}</p>
    <p>Revenue {$revenue}</p>


  {#if finished}
    <span class="result-label">
      Congratulations! Reached {target} in {$day} days!
    </span>
  {/if} 
  </div>

  <div class="canvas-container">
    <canvas class="graph" bind:this={canvas}></canvas>
    
  </div>

</div>

<style>


  .container {
    display: flex;
    justify-content: space-between;
  }

  .progress-container {
    width: 100%;
    border-radius: 2px;
    overflow: hidden;
  }

  .progress-label {
    display: block;
    text-align: center;
    font-size: 0.8rem;
    margin-top: 0.2rem;
    z-index: 1;
  }

  .canvas-container {
    display: flex;
    flex-grow: 1;
    max-width: 600px;
    max-height: 600px;
  }

  .stat-container {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: left;
  }



  progress[value] {
    -webkit-appearance: none;
    appearance: none;
    width: 100%;
    height: 20px;
    overflow: hidden;
  }

  progress[value]::-webkit-progress-bar {
    background-color: gray;
  }

  progress[value]::-webkit-progress-value {
    background-color: greenyellow;
  }

</style>

