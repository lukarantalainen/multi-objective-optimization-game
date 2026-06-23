<script lang="ts">
  import { onMount } from 'svelte';
  import { money, target, day, values } from './state';
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
            beginAtZero: true
          }
        }
      }
    });

  })

  $effect(() => {
    if (!chart) return;
      // eslint-disable-next-line no-useless-assignment
      chart.data.labels = Array.from(Array(10).keys().map(x => ++x));
      chart.data.datasets[0].data = $values;
      chart.update();
  })

  let finished: boolean = $derived($money >= target);
    
</script>

<div class="container">
  <div class="progress-container">
    <h2>Progress</h2>
    <progress class="progress" value={$money} max={target}></progress>
    <p>{$money}/{target   }</p>


  {#if finished}
    <span class="result-label">
      Congratulations! Reached {target} in {$day} days!
    </span>
  {/if} 
  </div>

  <canvas width="500" class="graph" bind:this={canvas}></canvas>

</div>

<style>


  .container {
    display: flex;
    justify-content: space-between;
  }

  .progress-container {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: left;
  }

  progress {
    width: 100%;
    appearance: none;
    border-radius: 10px;
  }

  progress::-webkit-progress-bar {
      background: #ddd;
      border-radius: 10px;
  }

  progress::-webkit-progress-value {
      background: limegreen;
      border-radius: 10px;
  }

  progress::-moz-progress-bar {
      background: limegreen;
      border-radius: 10px;
  }

</style>

