import { createRouter, createWebHistory } from 'vue-router'
import DiscussionView from '../views/DiscussionView.vue'
import GameView from '../views/GameView.vue'
import ResumeView from '../views/ResumeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'discussion',
      component: DiscussionView
    },
    {
      path: '/game',
      name: 'game',
      component: GameView
    },
    {
      path: '/resume',
      name: 'resume',
      component: ResumeView
    }
  ]
})

export default router
