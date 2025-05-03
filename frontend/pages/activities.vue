<template>
  <div class="flex flex-col min-h-screen">
    <NavBar />
    <BreadCrumbs :breadcrumbs="[
      { text: 'Home', url: '/' }, 
      { text: 'Activities' }
    ]" />
    <main class="flex-grow">
      <!-- Activities Section -->
      <section class="bg-white py-14 px-20">
        <div class="container mx-auto">
          <!-- Section Header -->
          <div class="flex flex-col items-center gap-5 mb-12">
            <h1 class="text-3xl font-bold text-primary text-center">Our Activities</h1>
            <p class="text-xl text-gray-600 text-center max-w-3xl">
              Discover our diverse range of activities designed to nurture your body, mind, and spirit.
            </p>
          </div>

          <!-- Activities Grid -->
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            <!-- Activity Card 1 - Yoga Classes -->
            <div class="relative rounded-xl overflow-hidden shadow-lg h-80 group">
              <div class="absolute inset-0 bg-cover bg-center" style="background-image: url('/images/activities/yoga-classes.jpg');"></div>
              <div class="absolute inset-0 bg-black bg-opacity-30"></div>
              <div class="absolute bottom-0 left-0 right-0 p-6 text-white">
                <h3 class="text-2xl font-bold mb-2 bg-white bg-opacity-90 text-primary p-2 rounded-md">
                  Yoga Classes
                </h3>
                <p class="text-base bg-white bg-opacity-90 text-gray-600 p-2 rounded-md">
                  Traditional and modern yoga styles for all.
                </p>
              </div>
            </div>

            <!-- Activity Card 2 - Water Yoga -->
            <div class="relative rounded-xl overflow-hidden shadow-lg h-80 group">
              <div class="absolute inset-0 bg-cover bg-center" style="background-image: url('/images/activities/water-yoga.jpg');"></div>
              <div class="absolute inset-0 bg-black bg-opacity-30"></div>
              <div class="absolute bottom-0 left-0 right-0 p-6 text-white">
                <h3 class="text-2xl font-bold mb-2 bg-white bg-opacity-90 text-primary p-2 rounded-md">
                  Water Yoga
                </h3>
                <p class="text-base bg-white bg-opacity-90 text-gray-600 p-2 rounded-md">
                  Gentle yoga practice in our therapeutic pool.
                </p>
              </div>
            </div>

            <!-- Activity Card 3 - Meditation -->
            <div class="relative rounded-xl overflow-hidden shadow-lg h-80 group">
              <div class="absolute inset-0 bg-cover bg-center" style="background-image: url('/images/activities/meditation.jpg');"></div>
              <div class="absolute inset-0 bg-black bg-opacity-30"></div>
              <div class="absolute bottom-0 left-0 right-0 p-6 text-white">
                <h3 class="text-2xl font-bold mb-2 bg-white bg-opacity-90 text-primary p-2 rounded-md">
                  Meditation
                </h3>
                <p class="text-base bg-white bg-opacity-90 text-gray-600 p-2 rounded-md">
                  Guided sessions for inner peace.
                </p>
              </div>
            </div>

            <!-- Activity Card 4 - Workshops -->
            <div class="relative rounded-xl overflow-hidden shadow-lg h-80 group">
              <div class="absolute inset-0 bg-cover bg-center" style="background-image: url('/images/activities/workshops.jpg');"></div>
              <div class="absolute inset-0 bg-black bg-opacity-30"></div>
              <div class="absolute bottom-0 left-0 right-0 p-6 text-white">
                <h3 class="text-2xl font-bold mb-2 bg-white bg-opacity-90 text-primary p-2 rounded-md">
                  Workshops
                </h3>
                <p class="text-base bg-white bg-opacity-90 text-gray-600 p-2 rounded-md">
                  Special sessions on various wellness topics.
                </p>
              </div>
            </div>

            <!-- Activity Card 5 - Zumba -->
            <div class="relative rounded-xl overflow-hidden shadow-lg h-80 group">
              <div class="absolute inset-0 bg-cover bg-center" style="background-image: url('/images/activities/zumba.jpg');"></div>
              <div class="absolute inset-0 bg-black bg-opacity-30"></div>
              <div class="absolute bottom-0 left-0 right-0 p-6 text-white">
                <h3 class="text-2xl font-bold mb-2 bg-white bg-opacity-90 text-primary p-2 rounded-md">
                  Zumba
                </h3>
                <p class="text-base bg-white bg-opacity-90 text-gray-600 p-2 rounded-md">
                  High-energy dance fitness classes.
                </p>
              </div>
            </div>

            <!-- Activity Card 6 - Retreats -->
            <div class="relative rounded-xl overflow-hidden shadow-lg h-80 group">
              <div class="absolute inset-0 bg-cover bg-center" style="background-image: url('/images/activities/retreats.jpg');"></div>
              <div class="absolute inset-0 bg-black bg-opacity-40"></div>
              <div class="absolute bottom-0 left-0 right-0 p-6 text-white">
                <h3 class="text-2xl font-bold mb-2 bg-white bg-opacity-90 text-primary p-2 rounded-md">
                  Retreats
                </h3>
                <p class="text-base bg-white bg-opacity-90 text-gray-600 p-2 rounded-md">
                  Immersive wellness experiences.
                </p>
              </div>
            </div>

            <!-- Activity Card 7 - Aperitif Yoga -->
            <div class="relative rounded-xl overflow-hidden shadow-lg h-80 group">
              <div class="absolute inset-0 bg-cover bg-center" style="background-image: url('/images/activities/aperitif-yoga.jpg');"></div>
              <div class="absolute inset-0 bg-black bg-opacity-30"></div>
              <div class="absolute bottom-0 left-0 right-0 p-6 text-white">
                <h3 class="text-2xl font-bold mb-2 bg-white bg-opacity-90 text-primary p-2 rounded-md">
                  Aperitif Yoga
                </h3>
                <p class="text-base bg-white bg-opacity-90 text-gray-600 p-2 rounded-md">
                  Combine yoga with social connection.
                </p>
              </div>
            </div>

            <!-- Activity Card 8 - Ceramics -->
            <div class="relative rounded-xl overflow-hidden shadow-lg h-80 group">
              <div class="absolute inset-0 bg-cover bg-center" style="background-image: url('/images/activities/ceramics.jpg');"></div>
              <div class="absolute inset-0 bg-black bg-opacity-30"></div>
              <div class="absolute bottom-0 left-0 right-0 p-6 text-white">
                <h3 class="text-2xl font-bold mb-2 bg-white bg-opacity-90 text-primary p-2 rounded-md">
                  Ceramics
                </h3>
                <p class="text-base bg-white bg-opacity-90 text-gray-600 p-2 rounded-md">
                  Creative expression through pottery.
                </p>
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