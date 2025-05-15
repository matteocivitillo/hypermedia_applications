<template>
  <div>
    <!-- This is just a redirect page -->
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { API_URL } from '~/utils/api'

// Query parameters to get activity ID
const route = useRoute()
const activityId = ref(route.query.id)
//const isLoading = ref(true) non lo usiamo

// Function to redirect to the new URL format
const redirectToNewFormat = async () => {
  if (!activityId.value) {
    navigateTo('/activities')
    return
  }
  
  try {
    // Fetch the activity data to get the name
    const response = await fetch(`${API_URL}/activity/${activityId.value}`)
    
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`)
    }
    
    const data = await response.json()
    
    if (data.activity) {
      const activityName = data.activity.title || data.activity.name
      // Create the slug and redirect
      const slug = activityName.toLowerCase().replace(/\s+/g, '-')
      navigateTo(`/activity/${slug}`, { redirectCode: 301 })
    } else {
      // If activity not found, redirect to activities list
      navigateTo('/activities')
    }
  } catch (err) {
    console.error('Error redirecting:', err)
    navigateTo('/activities')
  }
}

// Redirect when component mounts
onMounted(redirectToNewFormat)
</script> 