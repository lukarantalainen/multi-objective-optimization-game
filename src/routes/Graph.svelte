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
      chart.data.labels = Array.from(Array($day).keys());
      chart.data.datasets[0].data = $values;
      chart.update();
  })

  let finished: boolean = $derived($money >= target);
    
</script>

<div class="container">
  <div class="progress-container">
    <h2>Progress</h2>
    <meter value={$money} max={target}></meter>
    <p>{$money}/{target   }</p>


  {#if finished}
    <span class="result-label">
      Congratulations! Reached {target} in {$day} days!
    </span>
  {/if} 
  </div>

  <canvas bind:this={canvas}></canvas>

</div>

<style>
  .container {
    display: flex;
  }

  .progress-container {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: left;
  }
</style>

