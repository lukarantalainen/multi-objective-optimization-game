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

    .button:hover {
        box-shadow: 1px 1px 5px rgb(175, 255, 28);
    }

    .button:active {
        background-color: rgb(58, 146, 0);
        box-shadow: none;
    }
    
</style>