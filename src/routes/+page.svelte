    <script lang="ts">
        import Graph from './Graph.svelte';
        import { onMount } from 'svelte';
        import { money, target, day, finished } from './state';

        let id: number;
        const interval: number = 100;
        let paused: boolean = false;
        let pauseButtonState: string = $state("Pause");
        function createInterval() {
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
        })

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

        let price: number = $state(10);
        let comfort: number = $state(1);
        let production_cost: number = $derived(5 * comfort ** 2);
        
        let marketing: number = $state(0);
        let salary: number = $state(0);
        
        let queue: number = $state(0);

        let day_event = new Event(1);
        let make_event = new Event(0.5);
        let customer_event = new Event(0.7);


        const events: Event[] = [day_event, make_event, customer_event];

        function handle_interval() {
            if (day_event.next_trigger <= 0) {
                day_event.next_trigger = day_event.interval;
                $day += 1;
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
                events[i].next_trigger -= interval/1000;
            }
            sell();
        }

        function addCustomer() {
            if (price > production_cost * 2) {
                return;
            } else if (price > production_cost * 1.5) {
                customers += 1;
            } else if (price > production_cost * 1.3) {
                customers += 2;
            } else if (price > production_cost) {
                customers += 3;
            }
        }

        function handleFinish() {
            pause();
            $finished = true;
        }

        function changeMoney(delta: number) {
            $money += delta;
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

        function add_to_queue() {
            if ($money < production_cost) return;
            queue += 1;
            changeMoney(-production_cost);
        }

    </script>

    <div class="container">
        <div class="top-bar">
            <div class="left-container">
                <span class="counter">Day {$day}</span>
                <span class="counter">Inventory {inventory}</span>
                <span class="counter">Money ${$money}</span>
            </div>
            <div class="stat-container">
                <span class="counter">Sold {sold}</span>
                <span class="counter">Customers {customers}</span>
                <span class="counter">Time cost {time_cost}</span>
            </div>
            
        </div>
        <div class="content">
            <div class="left">
            <h2>Options</h2>
                <div class="options-container">
                    <div class="option">
                        <span>Cost {price} Production cost {production_cost}</span>
                        <input type="range" min=10 max=500 name="cost" id="0" class="slider" bind:value={price}>
                        
                    </div>
                    <div class="option">
                        <span>Comfort {comfort}</span>
                        <input type="range" min=1 max=10 name="comfort" id="1" class="slider" bind:value={comfort}>
                    </div>
                    <div class="option">
                        <span>Marketing {marketing}</span>
                        <input type="range" name="weight" id="2" class="slider" bind:value={marketing}>
                    </div>
                    <div class="option">
                        <span>Salary {salary}</span>
                        <input type="range" name="weight" id="3" class="slider" bind:value={salary}>
                    </div>
                </div>
                <button onclick={make}>Make</button>
                <span>In queue: {queue}</span>
            </div>
            <Graph/>            
        </div>
        <footer class="footer">
            <button onclick={playPause}>{pauseButtonState}</button>
        </footer>
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

    .footer {
        width: 100%;
        position: absolute;
        bottom: 0;
    }

</style>
