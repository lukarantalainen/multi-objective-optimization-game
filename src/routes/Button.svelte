<script lang="ts">
    let { text, callback } = $props();
</script>

<button class="button" onclick={callback}>
    {text}
</button>

<style>
    :root {
    --button-bg: rgb(102, 255, 0);
    }

    .button {
        background-color: var(--button-bg);
        color: white;
        padding: 5px 10px;
        cursor: pointer;
        border: none;
        text-align: center;
        border-radius: 10px;
    }
    
</style>