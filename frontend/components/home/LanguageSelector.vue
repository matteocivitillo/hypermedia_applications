<template>
  <div class="relative inline-block text-left">
    <button
      @click="isOpen = !isOpen"
      type="button"
      class="flex items-center text-base font-medium bg-transparent text-white rounded-md focus:outline-none px-2 py-1"
    >
      <span class="text-lg mr-1">{{ current.flag }}</span>
      <span>{{ getCountryCode(current.code) }}</span>
      <svg class="w-4 h-4 ml-1" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
      </svg>
    </button>
    <div v-if="isOpen" class="origin-top-right absolute right-0 mt-2 w-24 rounded-md shadow-lg bg-white dark:bg-gray-700 ring-1 ring-black ring-opacity-5 z-50">
      <div class="py-1">
        <button
          v-for="lang in languages"
          :key="lang.code"
          @click="select(lang.code)"
          class="flex items-center w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600"
          :class="{ 'bg-gray-100 dark:bg-gray-600': lang.code === modelValue }"
        >
          <span class="text-lg mr-2">{{ lang.flag }}</span>
          <span>{{ getCountryCode(lang.code) }}</span>
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';

const props = defineProps({
  modelValue: { type: String, required: true },
  languages: { type: Array, required: true }
});
const emit = defineEmits(['update:modelValue']);

const isOpen = ref(false);
const current = computed(() => props.languages.find(l => l.code === props.modelValue) || props.languages[0]);

function select(code) {
  emit('update:modelValue', code);
  isOpen.value = false;
}

function getCountryCode(code) {
  if (code === 'en') return 'GB';
  if (code === 'zh') return 'CN';
  return code.toUpperCase();
}

// Chiudi il menu se clicchi fuori
function handleClickOutside(event) {
  if (isOpen.value && !event.target.closest('.relative')) {
    isOpen.value = false;
  }
}
if (typeof window !== 'undefined') {
  window.addEventListener('click', handleClickOutside);
}
</script> 