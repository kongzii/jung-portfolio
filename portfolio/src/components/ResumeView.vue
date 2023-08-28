<script setup lang="ts">
</script>

<template>
    <div class="resume">
        <a :href="source" target="_blank">
            <div class="download">Download as PDF</div>
        </a>
        <vue-pdf-embed :source="source" :width="pdfWidth" v-if="render" class="pdf" />
    </div>
</template>

<script lang="ts">
import { nextTick } from 'vue';
import VuePdfEmbed from 'vue-pdf-embed'

export default {
    components: {
        VuePdfEmbed,
    },
    data() {
        return {
            render: true,
            source: "./Peter_Jung_CV.pdf",
            windowWidth: window.innerWidth,
        }
    },
    async mounted() {
        window.addEventListener('resize', async () => {
            this.render = false;
            this.windowWidth = window.innerWidth
            await nextTick();
            this.render = true;
        });
    },
    computed: {
        pdfWidth() {
            return Math.min(Math.ceil(this.windowWidth * 0.8), 800);
        }
    }
}

</script>


<style scoped>
@import '../assets/main.css';

.resume {
    margin: 0 auto 50px auto;
}

.download {
    cursor: pointer;
    background: var(--color-bg-chat);
    margin: 0.25em 1em;
    padding: 0.5em 1em;
    border-radius: 1em;
    text-align: center;
}

a {
    text-decoration: none;
    color: var(--color-black);
}

.download:hover {
    background: var(--color-router-hover-link);
}

.pdf {
    margin-top: 2.5em;
    border-radius: 1em;
}
</style>
