<template>
  <button 
    @click="toggleTheme" 
    class="relative p-2 rounded-full focus:outline-none focus:ring-0 transition-colors duration-300"
    :class="isDark ? 'bg-gray-800 text-gray-200' : 'bg-gray-100 text-gray-600'"
    aria-label="Toggle dark mode"
  >
    <!-- Sun icon -->
    <svg 
      v-if="!isDark" 
      xmlns="http://www.w3.org/2000/svg" 
      class="h-5 w-5 transition-transform duration-500" 
      fill="none" 
      viewBox="0 0 24 24" 
      stroke="currentColor"
    >
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" />
    </svg>
    
    <!-- Moon icon -->
    <svg 
      v-else 
      xmlns="http://www.w3.org/2000/svg" 
      class="h-5 w-5 transition-transform duration-500" 
      fill="none" 
      viewBox="0 0 24 24" 
      stroke="currentColor"
    >
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" />
    </svg>
  </button>
</template>

<script setup>
import { useTheme } from '../../utils/theme';

// Usa il composable per la gestione del tema
const { isDark, toggleTheme } = useTheme();
</script>

<style scoped>
.text-primary {
  color: #006A71;
}
</style> 