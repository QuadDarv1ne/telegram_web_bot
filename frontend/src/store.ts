import { defineStore } from 'pinia'
import axios from 'axios'

export const useMainStore = defineStore('main', {
  state: () => ({
    message: '',
  }),
  actions: {
    async fetchMessage() {
      try {
        const response = await axios.get('http://localhost:8000/api/users/1')
        this.message = response.data.username || 'User not found'
      } catch (error) {
        console.error('Error fetching message:', error)
      }
    }
  }
})
