import { defineStore } from 'pinia'
import { ref } from 'vue'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

export const useAuthStore = defineStore('auth', () => {
  const token = ref<string | null>(localStorage.getItem('token'))

  async function login(email: string, password: string) {
    const body = new URLSearchParams({ username: email, password })
    const response = await fetch(`${API_URL}/auth/login`, {
      method: 'POST',
      body,
    })
    if (!response.ok) throw new Error('Invalid email or password')
    const data = await response.json()
    token.value = data.access_token
    localStorage.setItem('token', data.access_token)
  }

  async function register(email: string, password: string) {
    const response = await fetch(`${API_URL}/auth/register`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password }),
    })
    if (!response.ok) {
      const error = await response.json().catch(() => ({ detail: 'Registration failed' }))
      throw new Error(error.detail)
    }
  }

  function logout() {
    token.value = null
    localStorage.removeItem('token')
  }

  return { token, login, register, logout }
})
