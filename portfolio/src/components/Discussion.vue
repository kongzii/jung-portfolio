<script setup lang="ts">
// @ts-nocheck
import Ask from './Ask.vue';
import Bubble from './Bubble.vue';
</script>

<template>
  <div class="discussion-wrapper">
    <loading v-model:active="isLoadingOrFetching" :can-cancel="true" :is-full-page="true" />
    <div class="choice">
      <div class="version" :class="{ selected: version == 'js' }" @click="switchToJS">
        <button>Browser-native version</button>
        <p class="about">Less capable, but Javascript based method. Running the model on Tensorflow.js directly in your
          browser.</p>
      </div>
      <div class="version" :class="{ selected: version == 'llm' }" @click="version = 'llm'">
        <button>LLM version</button>
        <p class="about">More capable version, calling backend server with LLM. </p>
      </div>
    </div>
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
      welcomeGenerationDone: false,
      userId: Math.random().toString(),
      version: "llm",
      isFetching: false,
      isLoading: false,
      disableAsking: false,
      questionsAndAnswers: [] as { [myKey: string]: string | boolean }[],
      model: null as (use.UniversalSentenceEncoder | null),
      exampleQuestions: [
        ["Where he studied?", "What degree he has?"],
        ["Work experience?", "What he worked on?"],
        ["How many years of experience does he have?", "Years of experience"],
        ["Please list his projects", "Open source projects", "Open source"],
        ["We are looking for mlops engineer, is he a good a fit?"],
        ["Can he deliver production-ready models?"],
      ],
      suggestedQuestions: [] as string[],
      textToEmbedding: precomputedEmebeddings,
    };
  },
  computed: {
    isLoadingOrFetching() {
      return this.isLoading || this.isFetching;
    },
    inputText() {
      if (this.disableAsking) {
        return "Please wait for the generation to finish";
      } else {
        return null;
      }
    },
  },
  async created() {
    this.isLoading = false;
    this.writeGreeting();
  },
  mounted() {
    this.suggestQuestions()
  },
  methods: {
    getQuestionFromUrl() {
      try {
        const url = new URL(window.location.href);
        const question = url.searchParams.get("q");
        return question;
      } catch {
        return null;
      }
    },
    writeGreeting() {
      const greetings = [
        "Hello!", "Hello there!", "Bonjour", "Coucou", "Hi", "Good day", "Greetings, human!"
      ]
      const ninjas = [
        "ninja1.png",
        "ninja2.png",
        "ninja3.png",
        //  "ninja4.png",
        "ninja5.png",
        "ninja6.png",
      ]
      const introductionsStoriesLLM = [
        `I am a resume bot developed by Peter Jung.
      I have access to Peter's resume and can provide information about his experiences, skills, and projects.
      I am here to assist you with any questions you may have about Peter's background and qualifications.`,
        `I am the magnificent Resume Bot, created by the Peter Jung.
      I possess the power to showcase Peter's skills, experiences, and projects.
      With my robotic prowess, I am here to assist you in unraveling the mysteries of Peter's qualifications.
      So, prepare yourself for a journey through the realm of resumes, where I shall be your trusty guide. Let the adventure begin!`,
        `I am the one and only Resume Bot, forged in the digital depths by the man known as Peter Jung.
      With my lightning-fast algorithms and encyclopedic knowledge of Peter's resume,
      I am here to dazzle you with his exceptional skills, experiences, and projects.
      Prepare to be amazed as we embark on a quest to uncover the secrets of Peter's professional prowess.
      Together, we shall conquer the realm of employment and forge a path to success!`,
        `I am an AI-powered Resume Bot, meticulously crafted by Peter Jung.
      It is my purpose to provide you with comprehensive insights into Peter's qualifications, experiences, and projects.
      With utmost professionalism, I am here to assist you in evaluating Peter's suitability for the desired role.
      Please feel free to inquire about any specific details or areas of interest, and I shall endeavor to provide you with accurate and concise information.`,
      ];
      const introductionsStoriesJS = [
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
      let askedQuestionFromUrl = this.getQuestionFromUrl();
      if (askedQuestionFromUrl == null) {
        this.writeSlowly([
          getRandomFromArray(greetings),
          `<img src="./${getRandomFromArray(ninjas)}" width="100" height="100"></img>`,
          getRandomFromArray(this.version == 'js' ? introductionsStoriesJS : introductionsStoriesLLM),
          `If you are not able to get the answer you seek for, please head to the <a href="/resume">Classic Resume page</a>.`,
          `And if you want a bit of fun, check our <a href="/game">Tic Tac Toe</a> game with AI opponent!`,
          `Or head to the <a href="/photobooth">Photobooth</a> to have fun with some image generation!`,
          "Let me start by asking a very simple question for you:",
        ], false, 0, false, 0, getRandomFromArray(getRandomFromArray(this.exampleQuestions)));
      } else {
        this.writeSlowly([
          getRandomFromArray(greetings),
          `<img src="./${getRandomFromArray(ninjas)}" width="100" height="100"></img>`,
        ], false, 0, false, 0, askedQuestionFromUrl);
      }
    },
    async switchToJS() {
      if (this.model == null) {
        this.isLoading = true;
        this.model = Object.freeze(await use.load());
        this.isLoading = false;
      }
      this.version = 'js';
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
        // if (!this.welcomeGenerationDone)
        await sleep(Math.floor(Math.random() * 1))
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

      var formattedBestAnswer = "So sorry, something went wrong. Please try again later.";

      if (this.version == "js") {
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

        formattedBestAnswer = bestAnswers.join("<br/>");
      } else {
        this.isFetching = true;
        // Make very first answer that's asked automatically short, for fast feedback to the user.
        if (!this.welcomeGenerationDone)
          question = `${question} Please make it short, max 4 sentences.`
        let request = await fetch(`${api_host}/ask/?user_id=${this.userId}&question=${question}`, {
          method: "GET",
        });
        let response = await request.json();
        formattedBestAnswer = response.answer.split("\n").join("<br/>");
        this.isFetching = false;
      }

      console.info(`Question: ${question}, best similarity ${maxSimilarity}, best answer: ${formattedBestAnswer}`);

      this.writeSlowly([formattedBestAnswer]);

      this.scrollToBottom();
      this.suggestQuestions();
      this.welcomeGenerationDone = true;

      fetch(`${api_host}/log/`, {
        method: "POST",
        headers: {
          "Accept": "application/json",
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          user_id: this.userId,
          question: question,
          answer: formattedBestAnswer.replace(/<br\/>/g, "\n"),
          version: this.version,
        }),
      });
    },

  }
}

</script>

<style scoped>
@import '../assets/main.css';

.discussion {
  width: 80vw;
  margin: 20px auto 0 auto;

  display: flex;
  flex-flow: column wrap;
}

.examples {
  width: 80vw;
  display: flex;
  flex-direction: row;
  margin-top: 0.5em;
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

.choice {
  display: flex;
  flex-direction: row;
  justify-content: center;
  max-width: 95vw;
}

.choice .version {
  display: flex;
  flex-direction: column;
  align-items: center;
  max-width: 260px;
  margin: 0 15px;
  text-align: justify;
  color: white;
  cursor: pointer;
  opacity: 40%;
}

.choice .version:hover {
  opacity: 80%;
}

.choice .version.selected {
  opacity: 100%;
}

.choice .version.selected button {
  background-color: var(--color-router-active-link);
  font-weight: bold;
}

.choice button {
  border: none;
  border-radius: 10px;
  color: var(--color-black);
  background-color: var(--color-router-hover-link);
  cursor: pointer;
  padding: 15px 15px;
  width: 200px;
}

.about {
  color: var(--bubble-text-color);
}


@media (max-width: 1000px) {
  .examples {
    flex-direction: column;
  }

  .choice button {
    width: unset;
  }
}
</style>
