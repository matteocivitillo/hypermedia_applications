<template>
  <section class="bg-white py-14">
    <div class="container mx-auto">
      <h2 class="text-3xl font-bold text-primary text-center mb-10">Our Yoga Classes</h2>
      
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <!-- Class Card 1 -->
        <div class="bg-secondary bg-opacity-50 rounded-xl shadow-custom p-6">
          <div class="mb-5">
            <span class="bg-primary bg-opacity-50 text-white text-sm font-normal py-1 px-3 rounded-full">
              Beginner
            </span>
          </div>
          
          <div class="mb-6">
            <h3 class="text-2xl font-bold text-primary mb-3">Hatha Yoga</h3>
            <p class="text-gray-600">
              A slow style, working on postures (asana), breathing (pranayama) and relaxation.
            </p>
          </div>
          
          <div class="flex items-center">
            <div class="w-10 h-10 rounded-full bg-gray-300 mr-3 overflow-hidden">
              <img src="/images/teacher-1.jpg" alt="Hatha Yoga Teacher" class="w-full h-full object-cover" />
            </div>
            <span class="text-gray-600">Teacher</span>
          </div>
        </div>
        
        <!-- Class Card 2 -->
        <div class="bg-secondary bg-opacity-50 rounded-xl shadow-custom p-6">
          <div class="mb-5">
            <span class="bg-primary bg-opacity-50 text-white text-sm font-normal py-1 px-3 rounded-full">
              Intermediate
            </span>
          </div>
          
          <div class="mb-6">
            <h3 class="text-2xl font-bold text-primary mb-3">Kundalini Yoga</h3>
            <p class="text-gray-600">
              Intense energy work with breathing, mantra, meditation and repetitive movements.
            </p>
          </div>
          
          <div class="flex items-center">
            <div class="w-10 h-10 rounded-full bg-gray-300 mr-3 overflow-hidden">
              <img src="/images/teacher-2.jpg" alt="Kundalini Yoga Teacher" class="w-full h-full object-cover" />
            </div>
            <span class="text-gray-600">Teacher</span>
          </div>
        </div>
        
        <!-- Class Card 3 -->
        <div class="bg-secondary bg-opacity-50 rounded-xl shadow-custom p-6">
          <div class="mb-5">
            <span class="bg-primary bg-opacity-50 text-white text-sm font-normal py-1 px-3 rounded-full">
              Advanced
            </span>
          </div>
          
          <div class="mb-6">
            <h3 class="text-2xl font-bold text-primary mb-3">Ashtanga Yoga</h3>
            <p class="text-gray-600">
              Fixed, intense sequences executed smoothly and quickly.
            </p>
          </div>
          
          <div class="flex items-center">
            <div class="w-10 h-10 rounded-full bg-gray-300 mr-3 overflow-hidden">
              <img src="/images/teacher-3.jpg" alt="Ashtanga Yoga Teacher" class="w-full h-full object-cover" />
            </div>
            <span class="text-gray-600">Teacher</span>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {}
</script> 