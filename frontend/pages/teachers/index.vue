<template>
  <div class="flex flex-col min-h-screen">
    <NavBar />
    <BreadCrumbs :breadcrumbs="[
      { text: 'Home', url: '/' }, 
      { text: 'Teachers' }
    ]" />
    <main class="flex-grow">
      <!-- Teachers Section -->
      <section class="bg-white py-14 px-4 md:px-20">
        <div class="container mx-auto">
          <!-- Section Header -->
          <div class="flex flex-col items-center gap-8 mb-12">
            <h1 class="text-3xl font-bold text-primary text-center">Our Teachers</h1>
            <p class="text-xl text-gray-600 text-center max-w-3xl">
              Meet our experienced instructors who bring their unique expertise and passion to Serendipity Yoga.
            </p>
          </div>

          <!-- Teachers Grid -->
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 justify-items-center">
            <!-- Teacher Card 1 - Sarah Mitchell -->
            <NuxtLink to="/teachers/sarah-mitchell" class="w-full max-w-sm bg-white rounded-xl shadow-lg overflow-hidden transition-transform hover:scale-105">
              <div class="h-80 relative">
                <img src="/images/teachers/sarah-mitchell.jpg" alt="Sarah Mitchell" class="w-full h-full object-cover">
                <div class="absolute inset-0 bg-black bg-opacity-10"></div>
              </div>
              <div class="p-6 space-y-4">
                <div class="flex flex-wrap gap-2 items-center">
                  <span class="bg-primary bg-opacity-80 text-white px-3 py-1 rounded-full text-sm">
                    Lead Yoga Instructor
                  </span>
                </div>
                <h3 class="text-2xl font-bold">Sarah Mitchell</h3>
                <div class="flex flex-wrap gap-2">
                  <span class="bg-white bg-opacity-80 text-gray-600 border border-white px-3 py-1 rounded-full text-sm">
                    Vinyasa Flow
                  </span>
                  <span class="bg-white bg-opacity-80 text-gray-600 border border-white px-3 py-1 rounded-full text-sm">
                    Meditation
                  </span>
                </div>
              </div>
            </NuxtLink>

            <!-- Teacher Card 2 - Michael Chen -->
            <NuxtLink to="/teachers/michael-chen" class="w-full max-w-sm bg-white rounded-xl shadow-lg overflow-hidden transition-transform hover:scale-105">
              <div class="h-80 relative">
                <img src="/images/teachers/michael-chen.jpg" alt="Michael Chen" class="w-full h-full object-cover">
                <div class="absolute inset-0 bg-black bg-opacity-10"></div>
              </div>
              <div class="p-6 space-y-4">
                <div class="flex flex-wrap gap-2 items-center">
                  <span class="bg-primary bg-opacity-80 text-white px-3 py-1 rounded-full text-sm">
                    Wellness Director
                  </span>
                </div>
                <h3 class="text-2xl font-bold">Michael Chen</h3>
                <div class="flex flex-wrap gap-2">
                  <span class="bg-white bg-opacity-80 text-gray-600 border border-white px-3 py-1 rounded-full text-sm">
                    Traditional Yoga
                  </span>
                  <span class="bg-white bg-opacity-80 text-gray-600 border border-white px-3 py-1 rounded-full text-sm">
                    Water Yoga
                  </span>
                </div>
              </div>
            </NuxtLink>

            <!-- Teacher Card 3 - Emma Rodriguez -->
            <NuxtLink to="/teachers/emma-rodriguez" class="w-full max-w-sm bg-white rounded-xl shadow-lg overflow-hidden transition-transform hover:scale-105">
              <div class="h-80 relative">
                <img src="/images/teachers/emma-rodriguez.jpg" alt="Emma Rodriguez" class="w-full h-full object-cover">
                <div class="absolute inset-0 bg-black bg-opacity-10"></div>
              </div>
              <div class="p-6 space-y-4">
                <div class="flex flex-wrap gap-2 items-center">
                  <span class="bg-primary bg-opacity-80 text-white px-3 py-1 rounded-full text-sm">
                    Dance & Movement Specialist
                  </span>
                </div>
                <h3 class="text-2xl font-bold">Emma Rodriguez</h3>
                <div class="flex flex-wrap gap-2">
                  <span class="bg-white bg-opacity-80 text-gray-600 border border-white px-3 py-1 rounded-full text-sm">
                    Zumba
                  </span>
                  <span class="bg-white bg-opacity-80 text-gray-600 border border-white px-3 py-1 rounded-full text-sm">
                    Dynamic Flow
                  </span>
                </div>
              </div>
            </NuxtLink>

            <!-- Teacher Card 4 - David Kumar -->
            <NuxtLink to="/teachers/david-kumar" class="w-full max-w-sm bg-white rounded-xl shadow-lg overflow-hidden transition-transform hover:scale-105">
              <div class="h-80 relative">
                <img src="/images/teachers/david-kumar.jpg" alt="David Kumar" class="w-full h-full object-cover">
                <div class="absolute inset-0 bg-black bg-opacity-10"></div>
              </div>
              <div class="p-6 space-y-4">
                <div class="flex flex-wrap gap-2 items-center">
                  <span class="bg-primary bg-opacity-80 text-white px-3 py-1 rounded-full text-sm">
                    Meditation Guide
                  </span>
                </div>
                <h3 class="text-2xl font-bold">David Kumar</h3>
                <div class="flex flex-wrap gap-2">
                  <span class="bg-white bg-opacity-80 text-gray-600 border border-white px-3 py-1 rounded-full text-sm">
                    Mindfulness
                  </span>
                  <span class="bg-white bg-opacity-80 text-gray-600 border border-white px-3 py-1 rounded-full text-sm">
                    Spiritual Wellness
                  </span>
                </div>
              </div>
            </NuxtLink>

            <!-- Teacher Card 5 - Sofia Bianchi -->
            <NuxtLink to="/teachers/sofia-bianchi" class="w-full max-w-sm bg-white rounded-xl shadow-lg overflow-hidden transition-transform hover:scale-105">
              <div class="h-80 relative">
                <img src="/images/teachers/sofia-bianchi.jpg" alt="Sofia Bianchi" class="w-full h-full object-cover">
                <div class="absolute inset-0 bg-black bg-opacity-10"></div>
              </div>
              <div class="p-6 space-y-4">
                <div class="flex flex-wrap gap-2 items-center">
                  <span class="bg-primary bg-opacity-80 text-white px-3 py-1 rounded-full text-sm">
                    Creative Arts Instructor
                  </span>
                </div>
                <h3 class="text-2xl font-bold">Sofia Bianchi</h3>
                <div class="flex flex-wrap gap-2">
                  <span class="bg-white bg-opacity-80 text-gray-600 border border-white px-3 py-1 rounded-full text-sm">
                    Ceramics
                  </span>
                  <span class="bg-white bg-opacity-80 text-gray-600 border border-white px-3 py-1 rounded-full text-sm">
                    Mindful Creation
                  </span>
                </div>
              </div>
            </NuxtLink>
          </div>
        </div>
      </section>
    </main>
    <SiteFooter />
  </div>
</template>

<script setup>
import NavBar from '~/components/home/NavBar.vue'
import BreadCrumbs from '~/components/home/BreadCrumbs.vue'
import SiteFooter from '~/components/home/SiteFooter.vue'
</script>

<style scoped>
.bg-primary {
  background-color: #006A71;
}
</style> 