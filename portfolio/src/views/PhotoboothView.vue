<script setup lang="ts">
// @ts-nocheck
import Ask from '../components/Ask.vue';
import Bubble from '../components/Bubble.vue';
</script>

<template>
  <div class="photobooth">
    <loading v-model:active="isLoading" :can-cancel="true" :is-full-page="true" />
    <Bubble :text="intro" :is-recipient="false" :disableSenderClass="true" />
    <img :src="imageData" v-if="base64Image != ''" />
    <Ask v-on:enter="ask" :button-text="'Draw'" />
    <div class="examples" :class="{ disabled: disableAsking }">
      <div class="text"><b>You can try:</b></div>
      <div v-for="x in suggestedQuestions" class="example" @click="ask(x)">{{ x }}</div>
    </div>
  </div>
</template>

<script lang="ts">
import Loading from 'vue-loading-overlay';
import 'vue-loading-overlay/dist/css/index.css';

export default {
  components: {
    Loading,
  },
  data() {
    return {
      intro: "Get inspired and unleash your creativity! Below, you have access to an image generation model that can vividly portray me in a myriad of captivating contexts based on your prompt. Should you desire inspiration, feel free to explore some of the examples provided! Happy creating!",
      base64Image: "",
      userId: Math.random().toString(),
      isLoading: false,
      suggestedQuestions: [
        "As a pirate with a parrot",
        "As a cowboy with a dog",
      ],
    };
  },
  async created() {
    this.isLoading = false;
  },
  computed: {
    imageData() {
      return `data:image/png;base64,${this.base64Image}`;
    }
  },
  methods: {
    async ask(prompt: string) {
      prompt = prompt.trim();

      if (prompt == "")
        return;

      this.isLoading = true;
      let request = await fetch(`${api_host}/photo/?user_id=${this.userId}&prompt=${prompt}`, {
        method: "GET",
      });
      let response = await request.json();
      this.base64Image = response["image"];
      this.isLoading = false;
    },

  }
}

</script>


<style scoped>
.bubble {
  width: 80vw;
  max-width: 600px;
  align-self: center;
}

.photobooth {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-content: center;
  align-items: center;
}

img {
  border-radius: 22px;
}

.Ask {
  max-width: 600px;
}

.examples {
  display: flex;
  flex-direction: row;
  margin-top: 20px;
}

@media (max-width: 1000px) {
  .examples {
    flex-direction: column;
    width: 100%;
    max-width: 600px;
  }
}

.examples>div {
  margin: 0.25em 1em;
  padding: 0.5em 1em;
  border-radius: 1em;
}

.examples>.text {
  color: var(--bubble-text-color);
}

.examples>.example {
  cursor: pointer;
  color: var(--bubble-text-color);
  background: var(--color-bg-chat);
}

.examples>.example:hover {
  border-color: var(--color-bg-chat);
  background-color: var(--color-bg-buttons);
}
</style>