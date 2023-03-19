<script setup lang="ts">
// @ts-nocheck
import Ask from './Ask.vue';
import Bubble from './Bubble.vue';
</script>

<template>
  <div class="discussion-wrapper">
    <loading v-model:active="isLoading" :can-cancel="true" :is-full-page="true" />
    <div v-if="questionsAndAnswers" class="discussion">
      <Bubble v-for="x in questionsAndAnswers" :text="x.message" :is-recipient="x.isRecipient" />
    </div>
    <Ask v-on:enter="ask" :class="{ disabled: disableAsking }" :default-text="inputText" />
    <div class="examples" :class="{ disabled: disableAsking }">
      <div class="text"><b>You can try:</b></div>
      <div v-for="x in suggestedQuestions" class="example" @click="ask(x)">{{ x }}</div>
    </div>
    <div ref="bottom" class="bottom"></div>
    <!-- <button @click="() => downloadObjectAsJson(textToEmbedding)">download embeddings</button> -->
  </div>
</template>
o
<script lang="ts">
import Loading from 'vue-loading-overlay';
import 'vue-loading-overlay/dist/css/index.css';
import { resumeArrayish } from "@/model/resume";
import { dotProduct, getRandomFromArray, sleep, downloadObjectAsJson, precomputedEmebeddings } from "@/model/tools";
import * as use from '@tensorflow-models/universal-sentence-encoder';
import { nextTick } from 'vue';

export default {
  components: {
    Loading,
  },
  data() {
    return {
      isLoading: true,
      disableAsking: false,
      questionsAndAnswers: [] as { [myKey: string]: string | boolean }[],
      model: null as (use.UniversalSentenceEncoder | null),
      exampleQuestions: [
        ["Where Peter studied?", "What degree he has?"],
        ["Work experience?", "What he worked on?"],
        ["How many years of experience does he have?", "Years of experience"],
        ["Please list Peter's projects", "Open source projects", "Open source"],
      ],
      suggestedQuestions: [] as string[],
      textToEmbedding: precomputedEmebeddings,
    };
  },
  computed: {
    inputText() {
      if (this.disableAsking) {
        return "Please wait for the generation to finish";
      } else {
        return null;
      }
    },
  },
  async created() {
    this.model = Object.freeze(await use.load());
    this.isLoading = false;
  },
  watch: {
    isLoading: function (val) {
      if (!val) {
        this.writeGreeting();
      }
    },
  },
  mounted() {
    this.suggestQuestions()
  },
  methods: {
    writeGreeting() {
      const greetings = [
        "Hello!", "Hello there!", "Bonjour", "Coucou", "Hi", "Good day"
      ]
      const ninjas = [
        "ninja1.png",
        "ninja2.png",
        "ninja3.png",
        //  "ninja4.png",
        "ninja5.png",
        "ninja6.png",
      ]
      const introductionsStories = [
        `I am a Resume Bot Ninja created by Peter.
      Please, do not expect ChatGPT-like narratives from me.
      Rather, I am powered by TensorFlow.js, a deep learning framework that runs a neural network trained for question answering directly in your browser.
      When you ask questions about Peter, I provide direct answers to your questions based on his resume.
      This means that no APIs are called, and your questions remains private.
      Additionally, there are many advantages to using a small task-focused neural network such as mine,
      including fast response rates and cost-effectiveness, as there is no need to pay for OpenAI's API.`,

        `I am Resume Bot Ninja made by Peter.
      Please, don't expect ChatGPT-like stories.
      Instead of just calling OpenAI's API with Peter's resume in the prompt, this is TensorFlow.js powered neural network trained on question answering dataset.
      Anything you ask is answered directly in your browser, no APIs called at all, the model is running in your browser.
      As such, there are many advantages:<br/>
      <br/>
        - fast response rate<br/>
        - privacy, no data are sent to any server<br/>
        - price, with small task-focused neural network, no need to pay for OpenAI's API<br/>`,

        `I'm a Resume Bot Ninja developed by Peter.
      Just to clarify, I won't be generating ChatGPT-style stories.
      Instead, I'm powered by TensorFlow.js, which means that I'm a tiny neural network running directly in your browser.
      When you ask question about Peter's resume, I can provide answers to your queries directly within your browser, without any need to call external APIs.
      This offers a number of advantages, including fast response rates, privacy (since no data is sent to external servers),
      and affordability (as we don't need to pay for OpenAI's API).
      Thanks for using my task-focused neural network!`,

        `
      I'm a Resume Bot Ninja designed by Peter.
      Just a heads up, my capabilities are different from ChatGPT's storytelling skills.
      Instead, I'm powered by TensorFlow.js - a neural network framework running model trained on a question answering dataset, directly in your browser.
      This allows me to provide you with direct answers to your Peter's resume-related questions, all within your browser.
      Plus, since I don't need to access any external APIs, you can enjoy fast response times and complete privacy. And, thanks to my task-focused neural network running in the browser, you don't need to worry about us paying for expensive OpenAI APIs.
      Thanks for using me!`
      ];
      this.writeSlowly([
        getRandomFromArray(greetings),
        `<img src="./${getRandomFromArray(ninjas)}" width="100" height="100"></img>`,
        getRandomFromArray(introductionsStories),
        `If you are not able to get the answer you seek for, please head to the <a href="/resume">Classic Resume page</a>.`,
        `And if you want a bit of fun, check our <a href="/game">Tic Tac Toe</a> game with AI opponent!`,
        "Let me start by asking a very simple question for you:",
      ], false, 0, false, 0, getRandomFromArray(["Please list Peter's projects", "Please tell me about Peter's work experience"]));
    },
    async embedText(text: string) {
      return (await Promise.all([(await this.model!.embed(text)).array()]))[0][0];
    },
    async embedTextCached(text: string) {
      if (text in this.textToEmbedding) {
        return this.textToEmbedding[text];
      }
      const embedding = await this.embedText(text);
      this.textToEmbedding[text] = embedding;
      return embedding;
    },
    suggestQuestions() {
      const shuffledNested = this.exampleQuestions.sort(() => 0.5 - Math.random()).slice(0, 3);
      const shuffled = shuffledNested.map(x => getRandomFromArray(x));
      this.suggestedQuestions = shuffled;
    },
    scrollToBottom() {
      this.$refs["bottom"].scrollIntoView({ behavior: "smooth" })
    },
    async writeSlowly(texts: string[], right: boolean = false, charIndex: number = 0, popLatest: boolean = false, textIndex: number = 0, ask: string = "") {
      this.disableAsking = true;

      if (popLatest)
        this.questionsAndAnswers.pop();

      const cropped = texts[textIndex].slice(0, charIndex)

      this.questionsAndAnswers.push({ "message": cropped, "isRecipient": right });

      if (charIndex < texts[textIndex].length) {
        await sleep(Math.floor(Math.random() * 5))
        this.writeSlowly(texts, right, charIndex + 1, true, textIndex, ask)
      } else if (textIndex < texts.length - 1) {
        this.writeSlowly(texts, right, 0, false, textIndex + 1, ask)
      } else if (ask != "") {
        await this.ask(ask);
      } else {
        this.disableAsking = false;
      }
    },
    async ask(question: string) {
      if (question.trim() == "")
        return;

      this.questionsAndAnswers.push({ "message": question, "isRecipient": true });
      await nextTick();

      const questionEmbedding = await this.embedText(question);

      var maxSimilarity = -2.0;
      var bestAnswers = [] as string[];

      for (let row of resumeArrayish) {
        const keys = row[0];
        const values = row[1];

        for (let key of keys) {
          const keyEmbedding = await this.embedTextCached(key);
          const similarity = dotProduct(questionEmbedding, keyEmbedding);

          if (similarity > maxSimilarity) {
            maxSimilarity = similarity;
            bestAnswers = values;
          }
        }
      }

      if (maxSimilarity < 0.1)
        bestAnswers = [
          "Sorry, I don't know what you mean, coud you rephrase?",
          "You can also try simplify the question, or provide just a few keywords, like 'experience' or 'projects'",
        ];

      const formattedBestAnswer = bestAnswers.join("<br/>");

      console.info(`Question: ${question}, best similarity ${maxSimilarity}, best answer: ${formattedBestAnswer}`);

      this.writeSlowly([formattedBestAnswer]);

      this.scrollToBottom();
      this.suggestQuestions();
    },

  }
}

</script>

<style scoped>
@import '../assets/main.css';

.discussion {
  width: 80vw;
  margin: 0 auto 0 auto;

  display: flex;
  flex-flow: column wrap;
}

.examples {
  width: 80vw;
  display: flex;
  flex-direction: row;
  margin-top: 0.5em;
}

@media (max-width: 1000px) {
  .examples {
    flex-direction: column;
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

.bottom {
  margin-top: 50px;
}

.disabled {
  pointer-events: none;
  opacity: 0.3;
}
</style>