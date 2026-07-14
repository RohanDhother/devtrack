<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const email = ref('')
const password = ref('')
const error = ref<string | null>(null)
const loading = ref(false)

const auth = useAuthStore()
const router = useRouter()

async function handleSubmit() {
  loading.value = true
  error.value = null
  try {
    await auth.login(email.value, password.value)
    router.push({ name: 'applications' })
  } catch (e) {
    error.value = (e as Error).message
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <form @submit.prevent="handleSubmit">
    <h1>Login</h1>
    <input v-model="email" type="email" placeholder="Email" required />
    <input v-model="password" type="password" placeholder="Password" required />
    <button type="submit" :disabled="loading">{{ loading ? 'Logging in...' : 'Login' }}</button>
    <p v-if="error" class="error">{{ error }}</p>
    <router-link to="/register">Need an account? Register</router-link>
  </form>
</template>

<style scoped>
.error {
  color: red;
}
</style>