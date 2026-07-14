<script setup lang="ts">
import { RouterView, useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const auth = useAuthStore()
const router = useRouter()

function handleLogout() {
  auth.logout()
  router.push({ name: 'login' })
}
</script>

<template>
  <nav>
    <router-link to="/">DevTrack</router-link>
    <span v-if="auth.token">
      <button @click="handleLogout">Logout</button>
    </span>
    <span v-else>
      <router-link to="/login">Login</router-link>
      <router-link to="/register">Register</router-link>
    </span>
  </nav>
  <RouterView />
</template>