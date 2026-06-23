<script lang="ts">
	import favicon from '$lib/assets/favicon.png';

	let { children } = $props();    
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
	<link rel="preconnect" href="https://fonts.googleapis.com">
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin=anonymous>
	<link href="https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&family=Roboto:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
</svelte:head>
    
{@render children()}

<style>
	:global(*) {
		margin: 0;
		padding: 0;
		font-family: "Roboto";
	}
</style>
