# Portfolio Page

<https://www.jung.ninja>

Below you will also find a section about how to customize the page for yourself and deploy it on Digitalocean.

## What's included

When you go to the [website](https://www.jung.ninja), you will see the following:

### Resume-bot

Two versions of chat-bot that talk about your resume.

The first version is a simple question-answering model, but the cool part is that it runs entirellly on the browser, using TensorFlow.js.

The second version is a more advanced chatbot, using OpenAI's `gpt-3.5-turbo`* model with infromation auto loaded from included PDF at `portfolio/public/Peter_Jung_CV_extended.pdf`.

### Photobooth

Tricked OpenAI's DALL·E* to generate your face in various scenarios according to the prompt.

** Why didn't I use open-source models and choose what OpenAI has? Because it's a portfolio page where I don't expect many visitors, yet I need it to be accessible non-stop, and running a server with strong enough GPUs is expensive.

### Tic tac toe game

A simple game made with [Defold](https://defold.com), it uses MCTS algorithm to play against you.

### Other stuff

- Classic resume in PDF format
- Link to LinkedIn
- Link to GitHub
- Dark/Light mode switcher

## Customization

### Resume-bot customization

- Replace `portfolio/public/Peter_Jung_CV_extended.pdf` with your resume in PDF format and `SYSTEM_MESSAGE` in `api/api.py` (for the LLM-based chat-bot)
- Replace `portfolio/src/model/resume.ts` with your resume in JSON format (for the question-answering chat-bot)
- Replace pre-written welcome phrases in `portfolio/src/components/Discussion.vue` (there is no need to always generate these)

### Photobooth customization

- Just place your pictures in `photobooth/jung` folder

### Classic resume customization

- Replace `./Peter_Jung_CV_extended.pdf` with name of your resume in `portfolio/src/components/ResumeView.vue`

### Hotjar tracking

- Replace with your own Hotjar tracking code in `portfolio/index.html`

## Local development

`docker-compose` with `docker` is used for local environment, use:

- `docker-compose up app api` to start the frontend and backend
- `docker-compose up tic` to start the tic tac toe server

## Deployment

To minimize total costs, everything is backed into a single Docker image.

There is a special Dockerfile `Dockerfile.deployment` that includes everything necessary:

- frontend using Vue.js
- backend using FastAPI
- tic tac toe game files
- nginx to proxy the traffic to the right server by the domain name

Once the image is built, one can use Digitalocean to host it for 5$ a month:

- create a new container registry and push the image there
  - to speed up the process, you can edit the `deploy.sh` script
- create a new app and deploy the image from the registry
  - set health check to be `HTTP` on path `/`
  - use HTTP port `8080` (configured in `nginx.conf`)
  - add your domains (and also set them in `nginx.conf`)
  - don't forget to set up the environment variables
    - `OPENAI_API_KEY` - your OpenAI API key
    - `ALLOW_ORIGINS` - your domain names separated by `,`, so that the frontend can access the backend
    - `AUTHOR_FIRST_NAME`
    - `AUTHOR_LAST_NAME`
    - `AUTHOR_LOCATION`
    - `SLACK_TOKEN` and `SLACK_NOTIFY_USER` - if you want notifications about the bot's questions and answers to be sent to Slack
