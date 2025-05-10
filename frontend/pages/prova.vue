<template>
    <div class="p-4">
      <h1 class="text-2xl mb-4">Messaggi dal database</h1>
      <ul v-if="messaggi.length">
        <li
          v-for="msg in messaggi"
          :key="msg.id"
          class="mb-2 p-2 border rounded"
        >
          {{ msg.testo }}
        </li>
      </ul>
      <p v-else>Caricamento in corso…</p>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import { API_URL } from '../utils/api'
  
  const messaggi = ref([])
  
  async function fetchMessaggi() {
    try {
      // Se usi proxy Vite -> '/api/messaggi'
      // Altrimenti fetch('http://localhost:8000/messaggi')
      const res = await fetch(`${API_URL}/messaggi`)
      const json = await res.json()
      console.log("DEBUG /messaggi ->", json)
      messaggi.value = json.messaggi
    } catch (err) {
      console.error('Errore fetch messaggi:', err)
    }
  }
  
  onMounted(fetchMessaggi)
  </script>
  