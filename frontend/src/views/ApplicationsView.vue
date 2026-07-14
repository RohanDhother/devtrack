<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useApplicationsStore, type Status } from '@/stores/applications'

const store = useApplicationsStore()

const company = ref('')
const role = ref('')
const status = ref<Status>('applied')

onMounted(() => store.load())

async function handleCreate() {
  await store.create({ company: company.value, role: role.value, status: status.value })
  company.value = ''
  role.value = ''
  status.value = 'applied'
}
</script>

<template>
  <div>
    <h1>Applications</h1>

    <form @submit.prevent="handleCreate">
      <input v-model="company" placeholder="Company" required />
      <input v-model="role" placeholder="Role" required />
      <select v-model="status">
        <option value="applied">Applied</option>
        <option value="interviewing">Interviewing</option>
        <option value="offer">Offer</option>
        <option value="rejected">Rejected</option>
      </select>
      <button type="submit">Add</button>
    </form>

    <p v-if="store.loading">Loading...</p>
    <p v-if="store.error" class="error">{{ store.error }}</p>

    <ul v-if="!store.loading">
      <li v-for="app in store.applications" :key="app.id">
        {{ app.company }} — {{ app.role }} — {{ app.status }}
        <button @click="store.remove(app.id)">Delete</button>
      </li>
    </ul>
  </div>
</template>

<style scoped>
.error {
  color: red;
}
</style>