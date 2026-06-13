<script lang="ts">
	import favicon from '$lib/assets/favicon.svg';

	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
	<link rel="preconnect" href="https://fonts.googleapis.com">
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin=anonymous>
	<link href="https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&family=Roboto:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
</svelte:head>

<nav class="navbar">
    <div class="button-container">
        <button class="nav-button" id="button1">Button 1</button>
        <button class="nav-button" id="button2">Button 2</button>
        <button class="nav-button">Button 3</button>
    </div>

    <a href="dashboard.html">Dashboard</a>
</nav>
    

{@render children()}

<style>


	:global(*) {
		margin: 0;
		padding: 0; 
		font-family: "Roboto";
	}
	
	button {
		font-size: 20px;
	}

	.navbar {
        width: inherit;
        padding: 10px;
        display: flex;
        flex-grow: 1;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid gray;
    }

    .button-container {
        display: flex;
        width: fit-content;
        gap: 1em;
        justify-content: space-between;
        align-items: center;
    }
    
    .nav-button {
        border-radius: 10px;
        transition-duration: 200ms;
        border: none;
        padding: 4px 10px;
        background-color: white;
    }

    .nav-button:hover {
        background-color: lightskyblue;
    }

</style>
