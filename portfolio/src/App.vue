<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import '@tensorflow/tfjs-core';
import '@tensorflow/tfjs-backend-cpu';
</script>

<template>
  <header>
    <div class="wrapper">
      <a class="codementor" target="_blank" href="https://www.codementor.io/@peter610?refer=badge"><img
          src="https://github.com/kongzii/kongzii/raw/master/im-a-cm-b-2.png" alt="Codementor badge"></a>
      <a class="badge-aws-ml" href="https://www.credly.com/badges/a27f28fe-9490-459d-a61b-0325b25e8533/public_url"
        target="_blank">
        <img class="badge-img" src="/AWS-Certified-Machine-Learning-Speciality.png" width="100" height="100" />
      </a>
      <a class="badge-aws-developer" href="https://www.credly.com/badges/2a77dc85-9063-4801-bc19-0690f33d43cd/public_url"
        target="_blank">
        <img class="badge-img" src="/AWS-Certified-Developer-Associate_badge.png" width="100" height="100" />
      </a>
      <a class="badge-aws-practitioner"
        href="https://www.credly.com/badges/ec6ba700-c48f-43fe-abac-738f67066d6f/public_url" target="_blank">
        <img class="badge-img" src="/AWS-Certified-Cloud-Practitioner_badge.png" width="100" height="100" />
      </a>
      <nav>
        <RouterLink to="/" class="link">Resume Bot</RouterLink>
        <RouterLink to="/photobooth" class="link">Photobooth</RouterLink>
        <RouterLink to="/game" class="link">Tic Tac Toe</RouterLink>
        <RouterLink to="/resume" class="link">Classic Resume</RouterLink>
        <a class="link" target="_blank" href="https://www.linkedin.com/in/jung-ninja/">LinkedIn</a>
        <a class="link" target="_blank" href="https://github.com/kongzii/">GitHub</a>
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
  max-width: 985px;
  width: 85vw;
}

.codementor {
  border-radius: 5px;
  position: absolute;
  top: 25px;
  left: 25px;
  padding: 0;
}

.codementor img {
  width: 125px;
  height: auto;
}

.badge-aws-ml {
  position: absolute;
  top: 25px;
  right: 25px;
  width: 100px;
  height: 100px;
  padding: 0;
}

.badge-aws-developer {
  position: absolute;
  top: 150px;
  right: 25px;
  width: 100px;
  height: 100px;
  padding: 0;
}

.badge-aws-practitioner {
  position: absolute;
  top: 275px;
  right: 25px;
  width: 100px;
  height: 100px;
  padding: 0;
}

.badge-img {
  width: 100%;
  height: 100%;
}


@media (max-width: 1000px) {
  .wrapper>nav {
    flex-direction: column;
    text-align: center;
  }

  .badge-aws-ml {
    width: 50px;
    height: 50px;
  }

  .badge-aws-developer {
    width: 50px;
    height: 50px;
    top: 85px;
  }

  .badge-aws-practitioner {
    width: 50px;
    height: 50px;
    top: 145px;
  }
}

a {
  color: var(--color-black);
  font-weight: bold;
  text-decoration: none;
  padding: 0.75em 1.25em;
  border-radius: 1em;
  margin: 0.1em 0;
  text-align: center;
  vertical-align: center;
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
