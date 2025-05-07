<template>
  <div class="flex flex-col min-h-screen bg-gray-100">
    <NavBar />
    <BreadCrumbs v-if="activity" :breadcrumbs="[
      { text: 'Home', url: '/' }, 
      { text: 'Activities', url: '/activities' }, 
      { text: activity.title || activity.name, url: '/singleactivity' }
    ]" />
    <main class="flex-grow">
      <!-- Activity Title Section -->
      <section class="py-14 px-10">
        <div class="container mx-auto">
          <h1 v-if="isLoading" class="loading-title text-center animate-fade-in">Loading...</h1>
          <h1 v-else-if="activity" class="text-4xl font-bold text-primary text-center">
            {{ activity.title || activity.name }}
          </h1>
        </div>
      </section>

      <!-- Activity Details Section -->
      <section class="bg-white py-14 px-10">
        <div class="container mx-auto">
          <!-- Loading State -->
          <div v-if="isLoading" class="flex justify-center items-center h-96">
            <div class="loading-spinner animate-fade-in">
              <div class="spinner"></div>
              <p class="mt-4 text-xl text-gray-600 animate-fade-in">Loading activity data...</p>
            </div>
          </div>
          
          <!-- Error State -->
          <div v-else-if="error" class="flex justify-center items-center h-96">
            <p class="text-xl text-red-600">{{ error }}</p>
          </div>
          
          <!-- Activity Data Display -->
          <div v-else-if="activity" class="bg-beige bg-opacity-50 rounded-xl p-6 sm:p-8 shadow-lg">
            <div class="flex flex-col lg:flex-row gap-12 items-center lg:items-start">
              <!-- Activity Content Section -->
              <div class="flex flex-col gap-8 lg:w-2/3">
                <!-- Level Badge -->
                <div class="flex items-center">
                  <span class="bg-primary bg-opacity-50 text-white px-4 py-2 rounded-full text-sm">
                    {{ activity.level || activity.difficulty || 'All Levels' }}
                  </span>
                </div>
                
                <!-- Activity Details -->
                <div class="space-y-4">
                  <h2 class="text-3xl font-bold text-primary">{{ activity.title || activity.name }}</h2>
                  <p class="text-xl text-gray-600">{{ activity.short_description || activity.description }}</p>
                </div>
                
                <!-- Teacher Info (if available) -->
                <div v-if="teacher && teacher.length > 0" class="mt-2">
                  <h3 class="text-xl font-bold text-black">Teachers:</h3>
                  <div v-for="(t, index) in teacher" :key="index" class="flex items-center gap-3 mt-2">
                    <img 
                      :src="t.image" 
                      alt="" 
                      class="w-10 h-10 rounded-full" 
                      v-if="t.image" 
                    />  <!-- Alt text is empty because it's decorative only -->
                    <div v-else class="w-10 h-10 bg-gray-300 rounded-full"></div> <!-- Placeholder if no image -->
                    <span class="text-gray-600">{{ t.name }} {{ t.surname }}</span> <!-- Display teacher's name and surname -->
                  </div>
                </div>
                
                <div v-else-if="teacher" class="flex items-center gap-3 mt-2">
                  <div class="w-12 h-12 bg-gray-300 rounded-full overflow-hidden border-2 border-primary">
                    <img 
                      :src="teacher.image ? (teacher.image.startsWith('http') ? teacher.image : `http://localhost:8000${teacher.image}`) : '/images/teacher-placeholder.jpg'" 
                      alt="" 
                      class="w-full h-full object-cover object-center" 
                      onerror="this.src='/images/teacher-placeholder.jpg'"
                    />  <!-- Alt text is empty because it's decorative only -->
                  </div>
                  <div>
                    <p class="text-gray-800 font-medium">{{ teacher.name }}</p>
                    <p class="text-gray-500 text-sm">{{ teacher.experience || 'Expert Teacher' }}</p>
                  </div>
                </div>
                
                <!-- About -->
                <div v-if="activity.about || activity.description" class="space-y-3 mt-6">
                  <h3 class="text-2xl font-bold text-black">About</h3>
                  <p v-if="activity.about" class="text-lg text-gray-600" v-html="activity.about"></p>
                  <p v-else class="text-lg text-gray-600">{{ activity.description }}</p>
                </div>
                
                <!-- Additional Sections -->
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-6">
                  <!-- Ideal For -->
                  <div v-if="activity.ideal_for" class="space-y-2">
                    <h3 class="text-xl font-bold text-black">Ideal For</h3>
                    <p class="text-base text-gray-600" v-html="activity.ideal_for"></p>
                  </div>
                  
                  <!-- Main Benefit -->
                  <div v-if="activity.main_benefit" class="space-y-2">
                    <h3 class="text-xl font-bold text-black">Main Benefit</h3>
                    <p class="text-base text-gray-600" v-html="activity.main_benefit"></p>
                  </div>
                </div>

                <!-- Additional Info -->
                <div v-if="activity.additional_info" class="space-y-2 mt-2">
                  <h3 class="text-xl font-bold text-black">Additional Information</h3>
                  <p class="text-base text-gray-600" v-html="activity.additional_info"></p>
                </div>
                
                <!-- Schedule -->
                <div v-if="activity.schedule" class="space-y-2 mt-2">
                  <h3 class="text-xl font-bold text-black">Schedule</h3>
                  <p class="text-base text-gray-600">{{ activity.schedule }}</p>
                </div>
                
                <!-- Room -->
                <div v-if="activity.roomid" class="space-y-2 mt-2">
                  <h3 class="text-xl font-bold text-black">Location</h3>
                  <p class="text-base text-gray-600">Room {{ activity.roomid }}</p>
                </div>
              </div>
              
              <!-- Activity Image -->
              <div class="lg:w-1/3">
                <div class="rounded-xl overflow-hidden shadow-lg h-80 md:h-96">
                  <img 
                    :src="activity.image ? activity.image : `/images/activities/default-activity.jpg`" 
                    alt="" 
                    class="w-full h-full object-cover" 
                    :class="{ 'opacity-0': !imageLoaded }" 
                    @load="imageLoaded = true" 
                    @error="handleImageError"
                  />  <!-- Alt text is empty because it's decorative only -->
                  <div v-if="!imageLoaded && !imageError" class="absolute inset-0 flex items-center justify-center bg-gray-200">
                    <p class="text-gray-600">Loading image...</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
      
      <!-- Other Activities Section -->
      <section v-if="activity" class="py-14 px-10">
        <div class="container mx-auto">
          <h2 class="text-3xl font-bold text-primary text-center mb-10">Other Activities You Might Like</h2>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <!-- This would contain similar activities, could be implemented later -->
          </div>
        </div>
      </section>
    </main>
    <SiteFooter />
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import NavBar from '~/components/home/NavBar.vue'
import BreadCrumbs from '~/components/home/BreadCrumbs.vue'
import SiteFooter from '~/components/home/SiteFooter.vue'

// Query parameters to get activity ID
const route = useRoute()
const activityId = ref(route.query.id)

// Data refs
const activity = ref(null)
const teacher = ref(null)
const isLoading = ref(true)
const error = ref(null)
const imageLoaded = ref(false)
const imageError = ref(false)

// Handle image loading error
const handleImageError = () => {
  imageError.value = true
  imageLoaded.value = true // Consider the image "loaded" even if it's an error
}

// Fetch teacher data
const fetchTeacher = async (teacherId) => {
  if (!teacherId) return null
  
  try {
    const response = await fetch(`http://localhost:8000/teacher/${teacherId}`)
    
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`)
    }
    
    const data = await response.json()
    console.log("Loaded teacher:", data.teacher);
    return data.teacher
  } catch (err) {
    console.error('Error fetching teacher:', err)
    return null
  }
}

// Fetch activity data from the API
const fetchActivity = async () => {
  if (!activityId.value) {
    error.value = 'No activity ID specified'
    isLoading.value = false
    return
  }
  
  try {
    console.log("Fetching activity with ID:", activityId.value)
    const response = await fetch(`http://localhost:8000/activity/${activityId.value}`)
    
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`)
    }
    
    const data = await response.json()
    
    if (data.activity) {
      activity.value = data.activity
      console.log("Loaded activity:", activity.value)
      
      // If the activity has a teacher_id, fetch the teacher
      if (activity.value.teacher_id) {
        teacher.value = await fetchTeacher(activity.value.teacher_id)
      }
    } else {
      error.value = 'Activity not found'
    }
  } catch (err) {
    console.error('Error fetching activity:', err)
    error.value = 'Failed to load activity data'
  } finally {
    isLoading.value = false
  }
}

// Fetch teacher data when the activity is loaded
const fetchTeacherByActivity = async () => {
  if (!activityId.value) {
    error.value = 'No activity ID specified'
    isLoading.value = false
    return
  }

  try {
    const response = await fetch(`http://localhost:8000/teacher/activity/${activityId.value}`);

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`)
    }

    const data = await response.json();

    if (data.teacher) {
      // Store the teacher data in a ref or reactive variable
      teacher.value = data.teacher;
    } else {
      error.value = 'Teacher not found'
    }
  } catch (err) {
    console.error('Error fetching teacher:', err)
    error.value = 'Failed to load teacher data'
  } finally {
    isLoading.value = false
  }
};

// Call this function after fetching the activity
onMounted(() => {
  fetchActivity();
  fetchTeacherByActivity();
});
// Fetch data when component mounts or when activityId changes
onMounted(fetchActivity)
watch(activityId, fetchActivity)

// SEO metadata for this page
watch(activity, (newActivity) => {
  if (newActivity) {
    useSeoMeta({
      title: `${newActivity.title || newActivity.name} - Serendipity Yoga`, // Use template literals
      description: 'Discover the details of our activities, including the teachers, schedule, and more.',
    });
  }
});
</script>

<style scoped>
.text-primary {
  color: #006A71;
}

.bg-primary {
  background-color: #006A71;
}

.bg-beige {
  background-color: #F2EFE7;
}

/* Loading spinner */
.loading-spinner {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  opacity: 0; /* Start hidden */
  animation: fadeIn 0.8s ease forwards; /* Adjust duration */
}

.spinner {
  width: 50px;
  height: 50px;
  border: 5px solid rgba(0, 106, 113, 0.2);
  border-radius: 50%;
  border-top-color: #006A71;
  animation: spin 1s ease-in-out infinite, scale 0.5s ease-in-out forwards; /* Add scale effect */
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes scale {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.1); /* Slightly scale up */
  }
  100% {
    transform: scale(1);
  }
}

/* Animations */
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-fade-in {
  animation: fadeIn 0.6s ease-out forwards;
}
</style> 