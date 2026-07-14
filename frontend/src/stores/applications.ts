import { defineStore } from 'pinia'
import { ref } from 'vue'
import { api } from '@/api/client'

export type Status = 'applied' | 'interviewing' | 'offer' | 'rejected'

export interface Application {
  id: number
  company: string
  role: string
  status: Status
  date_applied: string
  notes: string | null
}

export interface ApplicationCreate {
  company: string
  role: string
  status?: Status
  notes?: string | null
}

export const useApplicationsStore = defineStore('applications', () => {
  const applications = ref<Application[]>([])
  const loading = ref(false)
  const error = ref<string | null>(null)

  async function load() {
    loading.value = true
    error.value = null
    try {
      applications.value = await api.get<Application[]>('/applications/')
    } catch (e) {
      error.value = (e as Error).message
    } finally {
      loading.value = false
    }
  }

  async function create(payload: ApplicationCreate) {
    const application = await api.post<Application>('/applications/', payload)
    applications.value.push(application)
  }

  async function update(id: number, payload: Partial<ApplicationCreate>) {
    const updated = await api.patch<Application>(`/applications/${id}`, payload)
    const index = applications.value.findIndex((a) => a.id === id)
    if (index !== -1) applications.value[index] = updated
  }

  async function remove(id: number) {
    await api.delete(`/applications/${id}`)
    applications.value = applications.value.filter((a) => a.id !== id)
  }

  return { applications, loading, error, load, create, update, remove }
})
