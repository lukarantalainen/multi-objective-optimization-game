<script lang="ts">
    import { onMount } from 'svelte';
  import { money, target, day, finished } from './state';
  import { Chart } from 'chart.js/auto';

  let canvas: HTMLCanvasElement;

  onMount(() => {
    new Chart(canvas, {
      type: 'bar',
      data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [{
          label: '# of Votes',
          data: [12, 19, 3, 5, 2, 3],
          borderWidth: 1
        }]
      },
      options: {
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    });

  })
    
</script>

<div class="container">
  <div class="progress-container">
    <h2>Progress</h2>
    <meter value={$money} max={target}></meter>
    <p>{$money}/{target   }</p>


  {#if $finished}
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

