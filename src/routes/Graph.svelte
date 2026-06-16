<script lang="ts">
  import { money, target, day, finished } from './state';

</script>

<div class="container">
  <div class="progress-container">
    <progress value={$money} max={target}></progress>


  {#if $finished}
    <span class="result-label">
      Congratulations! Reached {target} in {$day} days!
    </span>
  {/if} 
  </div>
  
  
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

