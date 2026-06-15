<script lang="ts">
    import Graph from './Graph.svelte';

    let cost: number = $state(0);
    let comfort: number = $state(0);
    let value3: number = $state(0);
    let value4: number = $state(0);
    let day: number = $state(1);
    let inventory: number = $state(0);
    let money: number = $state(50);
    let production_cost: number = $state(10);

    let time: number = $state(1);
    // svelte-ignore state_referenced_locally
    let delta: number = 1; 

    let sold: number = $state(0);

    let queue: number = $state(0);

    function handle_interval() {
        day += 1;
        delta -= 1;
        sell();
        check_queue();
    }

    function sell() {
        if (inventory > 0) {
            inventory -= 1;
            money += cost;
            sold += 1;
        }
    }

    function check_queue() {
        if (delta == 0) {
            inventory += 1;
            delta = time;
        }
    }

    function make() {
        if (money < production_cost) {
            return;
        }
        queue += 1;
        money -= production_cost;
    }

    let dayInterval = setInterval(handle_interval, 1000);
</script>

<div class="container">
    <div class="top-bar">
        <div class="left-container">
            <span class="counter">Day {day}</span>
            <span class="counter">Inventory {inventory}</span>
        </div>
        <div class="stat-container">
            <span class="counter">Sold {sold}</span>
            <span class="counter">Customers</span>
            <span class="counter">Money {money}</span>
            <span class="counter">Time {time}</span>
        </div>
        
    </div>
    <div class="content">
        <div class="left">
        <h2>Options</h2>
            <div class="options-container">
                <div class="option">
                    <span>Cost {cost} Production cost {production_cost * comfort}</span>
                    <input type="range" min=10 max=400 name="cost" id="0" class="slider" bind:value={cost}>
                    
                </div>
                <div class="option">
                    <span>Comfort {comfort}</span>
                    <input type="range" min=1 max=10 name="comfort" id="1" class="slider" bind:value={comfort}>
                </div>
                <div class="option">
                    <span>{value3}</span>
                    <input type="range" name="weight" id="2" class="slider" bind:value={value3}>
                </div>
                <div class="option">
                    <span>{value4}</span>
                    <input type="range" name="weight" id="3" class="slider" bind:value={value4}>
                </div>
            </div>
            <button onclick={make}>Make</button>
            <span>In queue: {queue}</span>
        </div>
        <Graph/>
    </div>
    
</div>

<style>
    .content {
        padding: 10px;
        width: inherit;
        display: grid;
        grid-template-columns: 1fr 2fr;
        gap: 1em;   
    }

    .options-container {
        display: flex;
        flex-direction: column;
        gap: 1em;
    }
    
    .option {
        display: flex;
        justify-content: space-between;
    }

    .top-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1em;
        border-bottom: 1px solid lightgray;
    }

    .stat-container {
        display: flex;
        gap: 1em;
    }

    .counter {
        border-radius: 10px;
        padding: 4px 10px;
    }

    .counter:hover {
        background-color: lightblue;
    }

</style>
