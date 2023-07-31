<script setup lang="ts">
import Bubble from './Bubble.vue';
</script>

<template>
    <div class="game">
        <Bubble :text="intro" :is-recipient="false" :disableSenderClass="true" />
        <div class="iframe-wrapper">
            <iframe :src="ticTacToeUrl" v-if="render"></iframe>
            <div class="restart" @click="restart">Restart</div>
        </div>
    </div>
</template>

<script lang="ts">
import { nextTick } from 'vue';

export default {
    data() {
        return {
            render: true,
            intro: `

            Take a look at the Tic Tac Toe game I created using <a href="https://defold.com/" target="_blank">Defold</a>!
            Although I had no prior experience with the Defold engine or the <a href="https://www.lua.org/" target="_blank">LUA language</a>,
            the game effectively employs an algorithm that even AlphaGo utilizes to beat world's best players, or Spotify to recommend you the best songs.
            The game showcases an impressive AI opponent that utilizes the advanced MCTS algorithm to make its moves.
            As a result, the AI continuously improves after every game, making it quite challenging to beat.
            <br /> <br />
            Are you up for the challenge? Try it out and please share your experience with me.<br />
            `,
        }
    },
    computed: {
        ticTacToeUrl() {
            const protocol = location.protocol;
            return `${protocol}//tictactoe.jung.ninja`;
        }
    },
    methods: {
        async restart() {
            this.render = false;
            await nextTick();
            this.render = true;
        }
    }
}

</script>


<style scoped>
@import '../assets/main.css';

a {
    color: var(--color-black);
}

.intro {
    width: 80vw;
    max-width: 485px;
    text-align: justify;
    margin-top: 2em;
}

.game {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 0 auto 50px auto;
}

iframe {
    margin-top: 2em;
    border-radius: 1em;
    overflow: hidden;
    max-width: 500px;
    max-height: 500px;
    width: 80vw;
    height: 80vw;
}

.iframe-wrapper {
    cursor: pointer;

}

.bubble.sender {
    align-self: center;
}

.restart {
    cursor: pointer;
    color: var(--color-black);
    background: var(--color-bg-chat);
    margin: 0.25em 1em;
    padding: 0.5em 1em;
    border-radius: 1em;
    text-align: center;
}

.restart:hover {
    background: var(--color-router-hover-link);
}
</style>
