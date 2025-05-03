<template>
  <div class="flex flex-col min-h-screen">
    <NavBar />
    <BreadCrumbs :breadcrumbs="[{ text: 'Home', url: '/' }, { text: 'Teachers', url: '/teachers' }, { text: 'Sarah Mitchell', url: '/teacher/sarah-mitchell' }]" />
    <main class="flex-grow">
      <!-- Teacher Details Section -->
      <section class="bg-gray-50 py-14 border-b border-gray-200">
        <div class="container mx-auto px-6 md:px-20">
          <div class="flex flex-col md:flex-row gap-16 lg:gap-24">
            <!-- Teacher Card Preview -->
            <div class="w-full md:w-1/3">
              <div class="rounded-xl shadow-lg overflow-hidden">
                <div class="h-96 relative">
                  <img src="/images/teachers/sarah-mitchell.jpg" alt="Sarah Mitchell" class="w-full h-full object-cover">
                  <div class="absolute inset-0 bg-black bg-opacity-30"></div>
                  <div class="absolute inset-x-0 bottom-0 p-6">
                    <div class="flex flex-wrap gap-2 items-center mb-2">
                      <span class="bg-primary bg-opacity-80 text-white px-3 py-1 rounded-full text-sm">
                        Lead Yoga Instructor
                      </span>
                    </div>
                    <h3 class="text-2xl font-bold text-white">Sarah Mitchell</h3>
                    <div class="flex flex-wrap gap-2 mt-2">
                      <span class="bg-white bg-opacity-80 text-gray-600 px-3 py-1 rounded-full text-sm">
                        Vinyasa Flow
                      </span>
                      <span class="bg-white bg-opacity-80 text-gray-600 px-3 py-1 rounded-full text-sm">
                        Meditation
                      </span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            
            <!-- Teacher Information -->
            <div class="w-full md:w-2/3 flex flex-col gap-8">
              <!-- Teacher Name and Title -->
              <div class="space-y-1">
                <h1 class="text-4xl font-bold text-primary">Sarah Mitchell</h1>
                <p class="text-2xl text-gray-600">Lead Yoga Instructor</p>
              </div>
              
              <!-- Expertise -->
              <div class="space-y-2">
                <h2 class="text-3xl font-bold text-black">Expertise</h2>
                <p class="text-xl text-gray-600">Vinyasa Flow & Meditation</p>
              </div>
              
              <!-- About -->
              <div class="space-y-2">
                <h2 class="text-3xl font-bold text-black">About</h2>
                <p class="text-xl text-gray-600">
                  With over 15 years of experience in yoga practice and teaching, Sarah brings a wealth of knowledge in Vinyasa Flow and meditation techniques. Her classes focus on mindful movement and breath awareness.
                </p>
              </div>
              
              <!-- Activities -->
              <div class="space-y-6">
                <h2 class="text-3xl font-bold text-black">Activities</h2>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
                  <NuxtLink to="/activities" class="block bg-gray-200 rounded-xl px-6 py-4 text-center font-bold hover:bg-gray-300 transition">
                    Morning Vinyasa
                  </NuxtLink>
                  <NuxtLink to="/activities" class="block bg-gray-200 rounded-xl px-6 py-4 text-center font-bold hover:bg-gray-300 transition">
                    Mindful Meditation
                  </NuxtLink>
                  <NuxtLink to="/activities" class="block bg-gray-200 rounded-xl px-6 py-4 text-center font-bold hover:bg-gray-300 transition">
                    Advanced Flow
                  </NuxtLink>
                  <NuxtLink to="/activities" class="block bg-gray-200 rounded-xl px-6 py-4 text-center font-bold hover:bg-gray-300 transition">
                    Yoga for Beginners
                  </NuxtLink>
                </div>
              </div>
            </div>
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
.text-primary {
  color: #006A71;
}
</style> 