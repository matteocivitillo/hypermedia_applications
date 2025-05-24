<template>
  <div>
    <!-- This is just a redirect page -->
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { API_URL } from '~/utils/api'

// Query parameters to get teacher ID
const route = useRoute()
const teacherId = ref(route.query.id)
//const isLoading = ref(true) non lo usiamo

// Function to redirect to the new URL format
const redirectToNewFormat = async () => {
  console.log("singleteacher.vue - redirectToNewFormat called");
  console.log("teacherId from query:", teacherId.value);
  
  if (!teacherId.value) {
    console.log("No teacher ID provided, redirecting to /teachers");
    navigateTo('/teachers')
    return
  }
  
  try {
    // Fetch the teacher data to get the name and surname
    console.log(`Fetching teacher with ID: ${teacherId.value}`);
    const response = await fetch(`${API_URL}/teacher/${teacherId.value}`)
    
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`)
    }
    
    const data = await response.json()
    console.log("Teacher data received:", data);
    
    if (data.teacher) {
      const { name, surname } = data.teacher
      console.log(`Teacher found: ${name} ${surname}`);
      // Create the slug and redirect
      const slug = `${name.toLowerCase()}-${surname.toLowerCase()}`.replace(/\s+/g, '-')
      console.log(`Redirecting to: /teacher/${slug}`);
      navigateTo(`/teacher/${slug}`, { redirectCode: 301 })
    } else {
      // If teacher not found, redirect to teachers list
      console.log("Teacher not found in API response");
      navigateTo('/teachers')
    }
  } catch (err) {
    console.error('Error redirecting:', err)
    navigateTo('/teachers')
  }
}

// Redirect when component mounts
onMounted(redirectToNewFormat)
</script> 