<template>
  <div class="bg-gray-100 border-b border-gray-200">
    <div class="container mx-auto py-3 px-8 sm:px-12 md:px-16 lg:px-24 xl:px-32">
      <p class="text-sm font-bold text-gray-600">
        <template v-for="(crumb, index) in breadcrumbs" :key="index">
          <template v-if="index > 0"> 
            <span class="mx-2 text-gray-400">&gt;</span> 
          </template>
          <NuxtLink 
            v-if="crumb.url && index < breadcrumbs.length - 1" 
            :to="crumb.url" 
            class="hover:text-primary transition-colors duration-200"
          >
            {{ crumb.text }}
          </NuxtLink>
          <span v-else class="text-primary">{{ crumb.text }}</span>
        </template>
      </p>
    </div>
  </div>
</template>

<script setup>
defineProps({
  breadcrumbs: {
    type: Array,
    default: () => [
      { text: 'Home', url: '/' }
    ]
  }
})
</script>

<style scoped>
.text-primary {
  color: #006A71;
}
.hover\:text-primary:hover {
  color: #006A71;
}
</style> 