<template>
  <div class="bg-white p-6 md:p-8 rounded-xl shadow-lg flex flex-wrap md:flex-nowrap gap-16">
    <div class="w-full md:w-1/2 flex items-center justify-center">
      <div class="h-96 w-full rounded-lg overflow-hidden">
        <img 
          :src="room.image" 
          alt="" 
          class="w-full h-full object-cover" 
          loading="lazy"
        />  <!-- Alt text is empty because it's decorative only -->
      </div>
    </div>
    <div class="w-full md:w-1/2 flex flex-col justify-center">
      <h3 class="text-2xl font-bold text-primary mb-4">{{ room.name }}</h3>
      
      <!-- Description Paragraph -->
      <div class="prose prose-lg mb-6">
        <p>{{ room.description }}</p>
      </div>
      
      <!-- Features Paragraph -->
      <div v-if="room.features && room.features.length > 0" class="mb-6">
        <h4 class="text-lg font-semibold text-primary mb-2">Features:</h4>
        <ul class="list-disc pl-5 space-y-1">
          <li v-for="feature in room.features" :key="feature" class="text-gray-700">
            {{ feature }}
          </li>
        </ul>
      </div>
      
      <!-- Activities Paragraph -->
      <div v-if="room.activities && room.activities.length > 0" class="mb-6">
        <h4 class="text-lg font-semibold text-primary mb-2">Activities:</h4>
        <div class="flex flex-wrap gap-2">
          <nuxt-link 
            v-for="activity in room.activities" 
            :key="activity"
            :to="`/singleactivity?id=${activityIdsMap[activity] || ''}`"
            class="inline-flex items-center px-3 py-1 rounded-full bg-primary-light text-primary hover:bg-primary hover:text-white transition-colors"
          >
            {{ activity }}
          </nuxt-link>
        </div>
      </div>
      
      <!-- Quote -->
      <div v-if="room.quote" class="italic text-gray-600 mt-4">
        "{{ room.quote }}"
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  room: {
    type: Object,
    required: true
  },
  activityIdsMap: {
    type: Object,
    default: () => ({})
  }
})
</script>

<style scoped>
.text-primary {
  color: #006A71;
}

.bg-primary {
  background-color: #006A71;
}

.bg-primary-light {
  background-color: #e0f2f3;
}
</style> 