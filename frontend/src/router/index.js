import { createRouter, createWebHistory } from 'vue-router';

// Define your routes
const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: () => import('../components/ParentComponent.vue'),
  },
  {
    path: '/detail',
    name: 'DetailView',
    component: () => import('../components/DetailCompoent.vue'),
  },
];

// Create the router instance
const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
