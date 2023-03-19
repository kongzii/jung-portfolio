<script setup lang="ts">
defineProps<{
    defaultText?: string
}>()
</script>

<template>
    <div class="Ask">
        <span class="point">></span>
        <input class="input" v-model="text" v-on:keyup.enter="onEnter" v-if="!defaultText" />
        <span class="span-input" v-else>{{ defaultText }}</span>
        <div class="button" @click="onEnter">Ask</div>
    </div>
</template>

<script lang="ts">

export default {
    data() {
        return {
            text: "",
        }
    },
    methods: {
        onEnter() {
            this.$emit("enter", this.text);
            this.text = "";
        }
    }
}

</script>


<style scoped>
@import '../assets/main.css';

.Ask {
    width: 80vw;
    margin: 25px auto 0 auto;
    padding: 10px 15px;
    display: flex;
    flex-direction: row;
    background-color: var(--color-bg-chat);
    border-radius: 1em;
}

.point {
    margin-top: 2px;
    margin-left: 0.25em;
    font-weight: bold;
    padding: 0.25em;
    color: var(--bubble-text-color);
}

.span-input,
.input {
    margin-left: 15px;
    width: 100%;
    background-color: transparent;
    border: none;
    color: var(--bubble-text-color);
    outline: none;
    font-size: 1em;
}

.span-input {
    margin-top: 5px;
}

.button {
    width: 20%;
    height: 100%;
    border: 1px solid var(--color-black);
    border-radius: 1em;
    cursor: pointer;
    background: transparent;
    text-align: center;
    padding: 0.25em;
    color: var(--bubble-text-color);
}

.button:hover {
    border-color: var(--color-bg-chat);
    background-color: var(--color-bg-buttons);
    color: var(--bubble-text-color-recipient);

}
</style>
