<template>
  <div class="bg-gray-50 rounded-xl shadow-custom p-8 h-full">
    <h3 class="text-2xl font-bold text-primary mb-6 text-center">{{ title }}</h3>

    <form class="space-y-6" @submit.prevent="handleSubmit">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div class="space-y-2">
          <label for="name" class="text-gray-600 block">Your Name</label>
          <input 
            type="text" 
            id="name" 
            v-model="formData.name"
            class="w-full px-4 py-3 rounded-lg border border-gray-200 focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none transition" 
            placeholder="John Doe" 
          />
        </div>

        <div class="space-y-2">
          <label for="email" class="text-gray-600 block">Your Email</label>
          <input 
            type="email" 
            id="email" 
            v-model="formData.email"
            class="w-full px-4 py-3 rounded-lg border border-gray-200 focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none transition" 
            placeholder="john@example.com" 
          />
        </div>
      </div>

      <div class="space-y-2">
        <label for="message" class="text-gray-600 block">Message</label>
        <textarea 
          id="message" 
          rows="4" 
          v-model="formData.message"
          class="w-full px-4 py-3 rounded-lg border border-gray-200 focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none transition resize-none" 
          placeholder="How can we help you?"
        ></textarea>
      </div>

      <button 
        type="submit" 
        class="w-full bg-primary hover:bg-primary-dark text-white font-medium py-3 px-4 rounded-lg transition-colors duration-300"
      >
        Send Message
      </button>
    </form>
  </div>
</template>

<script setup>
import { ref, defineProps } from 'vue'

const props = defineProps({
  title: {
    type: String,
    default: 'Send Us a Message' // Default value if no title is provided
  }
})

const formData = ref({
  name: '',
  email: '',
  message: ''
})

const handleSubmit = () => {
  // Here you would typically send the form data to a server
  // For now, we'll just log it to the console
  console.log('Form submitted:', formData.value)
  
  // Reset form after submission
  formData.value = {
    name: '',
    surname: '',
    email: '',
    message: ''
  }
  
  // You could also show a success message to the user
  alert('Message sent successfully!')
}
</script>

<style scoped>
.text-primary {
  color: #006A71;
}

.bg-primary {
  background-color: #006A71;
}

.bg-primary-dark {
  background-color: #004d52;
}

.shadow-custom {
  box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
}
</style> 