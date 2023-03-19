<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import '@tensorflow/tfjs-core';
import '@tensorflow/tfjs-backend-cpu';
</script>

<template>
  <header>
    <div class="wrapper">
      <!-- <img class="badge-aws-practitioner" src="/AWS-Certified-Cloud-Practitioner_badge.png" width="100" height="100" /> -->
      <nav>
        <RouterLink to="/" class="link">Resume Bot</RouterLink>
        <RouterLink to="/game" class="link">Tic Tac Toe</RouterLink>
        <RouterLink to="/resume" class="link">Classic Resume</RouterLink>
        <a class="link" target="_blank" href="https://www.linkedin.com/in/jung-ninja/">LinkedIn</a>
        <a class="link" href="mailto:peter@jung.ninja">Contact Me</a>
        <a class="link switch-theme" @click="switchTheme">Use {{ darkTheme ? "Light" : "Dark" }} Theme</a>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<script lang="ts">

export default {
  data: () => ({
    darkTheme: true,
  }),
  methods: {
    switchTheme() {
      const element = document.querySelector("html");

      if (element!.hasAttribute("theme")) {
        element!.removeAttribute("theme");
        this.darkTheme = false;
      }
      else {
        element!.setAttribute("theme", "dark");
        this.darkTheme = true;
      }
    }
  }
}

</script>

<style scoped>
@import './assets/main.css';

header {
  margin-bottom: 5vh;
}

.wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100vw;
}

.wrapper>nav {
  margin-top: 2em;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  max-width: 785px;
  width: 80vw;
}

.badge-aws-practitioner {
  position: absolute;
  top: 25px;
  right: 25px;
  width: 100px;
  height: 100px;
}


@media (max-width: 1000px) {
  .wrapper>nav {
    flex-direction: column;
    text-align: center;
  }

  .badge-aws-practitioner {
    width: 50px;
    height: 50px;
  }
}

a {
  color: var(--color-black);
  font-weight: bold;
  text-decoration: none;
  padding: 0.75em 1.25em;
  border-radius: 1em;
  margin: 0.1em 0;
}

a:hover {
  background: var(--color-router-hover-link);
}

.router-link-active {
  background: var(--color-router-active-link);
}

.switch-theme {
  cursor: pointer;
}
</style>
