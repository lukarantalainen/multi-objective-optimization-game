<script lang="ts">
    import Graph from './Graph.svelte';

    let price: number = $state(0);
    let value2: number = $state(0);
    let value3: number = $state(0);
    let value4: number = $state(0);
    let day: number = $state(1);
    let inventory: number = $state(0);
    let buyers: number = 0;
    let money: number = $state(0);


    function increase_day() {
        day += 1;
        if (inventory > 0 && buyers > 0) {
            inventory -= 1;
            buyers -= 1;
            money += price;
        }

        if (price < 50) {
            buyers += 1;
        }
        
    }

    function increment() {
        inventory += 1;
    }

    let dayInterval = setInterval(increase_day, 1000);
</script>

<div class="container">
    <div class="top-bar">
        <div class="left-container">
            <span>Day {day}</span>
            <span>Inventory {inventory}</span>
        </div>
        <div class="stat-container">
            <span>Sold</span>
            <span>Customers</span>
            <span>Money {money}</span>
            <span>Time</span>
        </div>
        
    </div>
    <div class="content">
        <div class="left">
        <h2>Options</h2>
            <div class="options-container">
                <button onclick={increment}>Make</button>
                <input type="range" name="weight" id="0" class="slider" bind:value={price}>
                <span>{price}</span>
                <input type="range" name="weight" id="1" class="slider" bind:value={value2}>
                <span>{value2}</span>
                <input type="range" name="weight" id="2" class="slider" bind:value={value3}>
                <span>{value3}</span>
                <input type="range" name="weight" id="3" class="slider" bind:value={value4}>
                <span>{value4}</span>
            </div>
        </div>
        <Graph/>
    </div>
    
</div>

<style>
    :global(body) {     
        margin: 0;
        padding: 0; 
    }

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

    .top-bar {
        display: flex;
        justify-content: space-between;
    }

    .stat-container {
        display: flex;
        gap: 1em;
    }
    

</style>
