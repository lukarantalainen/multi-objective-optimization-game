<script lang="ts">
    import Graph from "./Graph.svelte";
    import Button from "./Button.svelte";
    //import Slider from "./Slider.svelte";
    import { onMount } from "svelte";
    // eslint-disable-next-line @typescript-eslint/no-unused-vars
    import { money, target, day, values, spending, revenue } from "./state";

    let id: ReturnType<typeof setInterval>;
    const interval: number = 100;
    let paused: boolean = false;
    let pauseButtonState: string = $state("Pause");
    function createInterval(): ReturnType<typeof setInterval> {
        return setInterval(handle_interval, interval);
    }

    function pause() {
        clearInterval(id);
        pauseButtonState = "Play";
        paused = true;
    }

    function play() {
        id = createInterval();
        pauseButtonState = "Pause";
        paused = false;
    }

    function playPause() {
        if (paused) play();
        else pause();
    }

    onMount(() => {
        id = createInterval();
        return () => clearInterval(id);
    });

    class Event {
        interval: number;
        next_trigger: number;
        constructor(interval: number) {
            this.interval = interval;
            this.next_trigger = interval;
        }
    }

    let inventory: number = $state(0);

    let customers: number = $state(0);
    let sold: number = $state(0);
    let time_cost: number = $state(1);

    let marketing: number = $state(0);
    let salary: number = $state(0);

    let price: number = $state(10);
    let comfort: number = $state(1);
    let production_cost: number = $derived(
        Math.round(5 * comfort ** 2 + marketing ** 1.05 + salary ** 1.05),
    );

    let queue: number = $state(0);

    let day_event = new Event(1);
    let make_event = new Event(0.5);
    let customer_event = new Event(0.7);

    const events: Event[] = [day_event, make_event, customer_event];

    function handle_interval() {
        if (day_event.next_trigger <= 0) {
            day_event.next_trigger = day_event.interval;
            $day += 1;
            values.update((items) => [...items, $money]);
        }

        if (make_event.next_trigger <= 0 && queue > 0) {
            make_event.next_trigger = make_event.interval;
            inventory += 1;
        }

        if (customer_event.next_trigger <= 0) {
            customer_event.next_trigger = Math.random() + 0.5;
            addCustomer();
        }

        for (let i = 0; i < events.length; ++i) {
            events[i].next_trigger -= interval / 1000;
        }
        sell();
    }

    function addCustomer() {
        const sum = production_cost / price + marketing;
        if (Math.random() * 5 < sum) {
            ++customers;
        }
    }

    function handleFinish() {
        pause();
    }

    function changeMoney(delta: number) {
        $money += delta;
        if (delta > 0) $revenue += delta;
        else $spending += Math.abs(delta);
        if ($money >= target) {
            handleFinish();
        }
    }

    function sell() {
        if (inventory > 0 && customers > 0) {
            inventory -= 1;
            customers -= 1;
            changeMoney(price);
            sold += 1;
        }
    }

    function make() {
        if ($money < production_cost) return;
        inventory += 1;
        changeMoney(-production_cost);
    }
</script>

<div class="container">
    <div class="top-bar">
        <div class="stat-container">
            <span class="top-bar-stat">Day {$day}</span>
            <span class="top-bar-stat">Inventory {inventory}</span>
            <span class="top-bar-stat">Money ${$money}</span>
        </div>
        <div class="stat-container">
            <span class="top-bar-stat">Sold {sold}</span>
            <span class="top-bar-stat">Customers {customers}</span>
            <span class="top-bar-stat">Time cost {time_cost}</span>
        </div>
    </div>
    <div class="content-container">
<div class="content">
        <div class="left">
            <div class="options-container">
                <h2>Options</h2>
                <div class="option">
                    <span>Cost {price} Production cost {production_cost}</span>
                    <input
                        type="range"
                        min="10"
                        max="500"
                        name="cost"
                        id="0"
                        class="slider"
                        bind:value={price}
                    />
                </div>
                <div class="option">
                    <span>Comfort {comfort}</span>
                    <input
                        type="range"
                        min="1"
                        max="10"
                        name="comfort"
                        id="1"
                        class="slider"
                        bind:value={comfort}
                    />
                </div>
                <div class="option">
                    <span>Marketing {marketing}</span>
                    <input
                        type="range"
                        name="weight"
                        id="2"
                        class="slider"
                        bind:value={marketing}
                    />
                </div>
                <div class="option">
                    <span>Salary {salary}</span>
                    <input
                        type="range"
                        name="weight"
                        id="3"
                        class="slider"
                        bind:value={salary}
                    />
                </div>

                <Button text="Make" callback={make} />
                <span>In queue: {queue}</span>
            </div>
        </div>
        <Graph />
    </div>
    <button class="pause-button" onclick={playPause}>{pauseButtonState}</button>
    </div>
    

</div>

<style>
    :global(html) {
        background-color: rgb(254, 255, 247);
    }

    .content-container {
        padding: 10px;
    }

    .content {
        width: inherit;
        display: grid;
        grid-template-columns: 1fr 2fr;
        gap: 1em;
    }

    h2 {
        font-weight: 600;
    }

    .options-container {
        display: flex;
        flex-direction: column;
        gap: 1em;
        border-radius: 10px;
        padding: 10px;
        background-color: #21471e;
        color: #b6ff51;
        font-weight: 600;
    }

    .option {
        display: flex;
        justify-content: space-between;
    }

    .top-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 12px 16px;
        background-color: #21471e;
        border-bottom: 1px solid lightgray;
    }

    .stat-container {
        display: flex;
        gap: 1em;
        align-items: center;
    }

    .top-bar-stat {
        transition-duration: 100ms;
        border-radius: 10px;
        padding: 4px 10px;
        font-weight: 600;
        color: #b6ff51;
    }

    .top-bar-stat:hover {
        background-color: rgb(60, 255, 0);
    }

    .footer {
        bottom: 0;
        width: 100%;
        bottom: 0;
    }

    .pause-button {
        border-radius: 10px;
        margin: 5px;
        border: none;
        background-color: black;
        color: yellow;
        font-weight: 600;
        padding: 4px 5px;
    }

</style>
