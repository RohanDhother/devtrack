<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const email = ref('')
const password = ref('')
const error = ref<string | null>(null)
const loading = ref(false)
const success = ref(false)

const auth = useAuthStore()
const router = useRouter()

async function handleSubmit() {
  loading.value = true
  error.value = null
  try {
    await auth.register(email.value, password.value)
    success.value = true
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
    <h1>Register</h1>
    <input v-model="email" type="email" placeholder="Email" required />
    <input v-model="password" type="password" placeholder="Password (min 8 chars)" minlength="8" required />
    <button type="submit" :disabled="loading">{{ loading ? 'Registering...' : 'Register' }}</button>
    <p v-if="error" class="error">{{ error }}</p>
    <router-link to="/login">Already have an account? Login</router-link>
  </form>
</template>

<style scoped>
.error {
  color: red;
}
</style>