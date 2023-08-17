<script setup lang="ts">
defineProps<{
    text: string,
    isRecipient?: boolean
}>()
</script>

<template>
    <div class="bubble" :class="{ sender: !isRecipient, recipient: isRecipient }" v-html="text">
    </div>
</template>


<style >
@import '../assets/main.css';

.bubble>a,
.bubble>a:visited {
    text-decoration: none;
    color: var(--color-bg-recipient);
}

.bubble {
    color: var(--bubble-text-color);
    border-radius: 1em;
    padding: 0.75em 1.5em;
    margin: 0.2em;
    max-width: 90%;
}

.bubble.sender {
    align-self: flex-start;
    background-color: var(--color-bg-chat);
}

.bubble.recipient {
    align-self: flex-end;
    background-color: var(--color-bg-recipient);
    color: var(--bubble-text-color-recipient);
}

.bubble.sender.first {
    border-bottom-left-radius: 0.1em;
}

.bubble.sender.last {
    border-top-left-radius: 0.1em;
}

.bubble.sender.middle {
    border-bottom-left-radius: 0.1em;
    border-top-left-radius: 0.1em;
}

.bubble.recipient.first {
    border-bottom-right-radius: 0.1em;
}

.bubble.recipient.last {
    border-top-right-radius: 0.1em;
}

.discussion>.bubble.recipient.middle {
    border-bottom-right-radius: 0.1em;
    border-top-right-radius: 0.1em;
}
</style>
