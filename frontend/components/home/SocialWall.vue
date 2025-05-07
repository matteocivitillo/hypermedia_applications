<template>
  <section class="py-20 bg-gray-50">
    <div class="container mx-auto px-8 sm:px-12 md:px-16 lg:px-24 xl:px-32">
      <h2 class="text-4xl font-bold text-primary text-center mb-6">Yoga Stories</h2>
      <p class="text-lg text-gray-600 text-center max-w-3xl mx-auto mb-8">See what our community members have to say about their transformative experiences with us.</p>
      
      <!-- Social Media Links - spostato sopra le recensioni -->
      <div class="mb-12 text-center">
        <h3 class="text-xl font-bold text-gray-700 mb-4">Follow Us</h3>
        <div class="flex justify-center space-x-6">
          <a href="#" class="text-gray-500 hover:text-primary transition-colors duration-300">
            <svg class="w-7 h-7" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
              <path fill-rule="evenodd" d="M22 12c0-5.523-4.477-10-10-10S2 6.477 2 12c0 4.991 3.657 9.128 8.438 9.878v-6.987h-2.54V12h2.54V9.797c0-2.506 1.492-3.89 3.777-3.89 1.094 0 2.238.195 2.238.195v2.46h-1.26c-1.243 0-1.63.771-1.63 1.562V12h2.773l-.443 2.89h-2.33v6.988C18.343 21.128 22 16.991 22 12z" clip-rule="evenodd"></path>
            </svg>
          </a>
          <a href="#" class="text-gray-500 hover:text-primary transition-colors duration-300">
            <svg class="w-7 h-7" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
              <path fill-rule="evenodd" d="M12.315 2c2.43 0 2.784.013 3.808.06 1.064.049 1.791.218 2.427.465a4.902 4.902 0 011.772 1.153 4.902 4.902 0 011.153 1.772c.247.636.416 1.363.465 2.427.048 1.067.06 1.407.06 4.123v.08c0 2.643-.012 2.987-.06 4.043-.049 1.064-.218 1.791-.465 2.427a4.902 4.902 0 01-1.153 1.772 4.902 4.902 0 01-1.772 1.153c-.636.247-1.363.416-2.427.465-1.067.048-1.407.06-4.123.06h-.08c-2.643 0-2.987-.012-4.043-.06-1.064-.049-1.791-.218-2.427-.465a4.902 4.902 0 01-1.772-1.153 4.902 4.902 0 01-1.153-1.772c-.247-.636-.416-1.363-.465-2.427-.047-1.024-.06-1.379-.06-3.808v-.63c0-2.43.013-2.784.06-3.808.049-1.064.218-1.791.465-2.427a4.902 4.902 0 011.153-1.772A4.902 4.902 0 015.45 2.525c.636-.247 1.363-.416 2.427-.465C8.901 2.013 9.256 2 11.685 2h.63zm-.081 1.802h-.468c-2.456 0-2.784.011-3.807.058-.975.045-1.504.207-1.857.344-.467.182-.8.398-1.15.748-.35.35-.566.683-.748 1.15-.137.353-.3.882-.344 1.857-.047 1.023-.058 1.351-.058 3.807v.468c0 2.456.011 2.784.058 3.807.045.975.207 1.504.344 1.857.182.466.399.8.748 1.15.35.35.683.566 1.15.748.353.137.882.3 1.857.344 1.054.048 1.37.058 4.041.058h.08c2.597 0 2.917-.01 3.96-.058.976-.045 1.505-.207 1.858-.344.466-.182.8-.398 1.15-.748.35-.35.566-.683.748-1.15.137-.353.3-.882.344-1.857.048-1.055.058-1.37.058-4.041v-.08c0-2.597-.01-2.917-.058-3.96-.045-.976-.207-1.505-.344-1.858a3.097 3.097 0 00-.748-1.15 3.098 3.098 0 00-1.15-.748c-.353-.137-.882-.3-1.857-.344-1.023-.047-1.351-.058-3.807-.058zM12 6.865a5.135 5.135 0 110 10.27 5.135 5.135 0 010-10.27zm0 1.802a3.333 3.333 0 100 6.666 3.333 3.333 0 000-6.666zm5.338-3.205a1.2 1.2 0 110 2.4 1.2 1.2 0 010-2.4z" clip-rule="evenodd"></path>
            </svg>
          </a>
          <a href="#" class="text-gray-500 hover:text-primary transition-colors duration-300">
            <svg class="w-7 h-7" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
              <path d="M8.29 20.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0022 5.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.072 4.072 0 012.8 9.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84"></path>
            </svg>
          </a>
        </div>
      </div>
      
      <!-- Masonry Layout for Reviews - più recensioni per riga e più piccole -->
      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-5">
        <!-- Review Cards -->
        <div 
          v-for="(review, index) in reviews" 
          :key="index"
          class="bg-white rounded-lg p-5 shadow-custom transform transition-all duration-300 hover:-translate-y-1"
          :class="{'md:col-span-2': review.featured && index < 2}"
        >
          <div class="flex items-center mb-3">
            <div class="w-10 h-10 rounded-full overflow-hidden mr-3 border-2 border-secondary">
              <img :src="review.image" alt="" class="w-full h-full object-cover" />  <!-- Alt text is empty because it's decorative only -->
            </div>
            <div>
              <p class="text-gray-800 font-medium text-sm">{{ review.name }}</p>
              <p class="text-gray-500 text-xs">{{ review.title }}</p>
            </div>
          </div>
          
          <div class="space-y-3">
            <div class="flex items-center">
              <template v-for="star in 5" :key="star">
                <svg 
                  class="w-4 h-4" 
                  :class="star <= review.rating ? 'text-yellow-400' : 'text-gray-300'"
                  fill="currentColor" 
                  viewBox="0 0 20 20"
                >
                  <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path>
                </svg>
              </template>
              <span class="text-gray-500 ml-2 text-xs">{{ review.date }}</span>
            </div>
            
            <p class="text-gray-700 text-sm leading-relaxed line-clamp-4">
              {{ review.text }}
            </p>
            
            <div v-if="review.image_url && review.featured" class="mt-2 rounded-lg overflow-hidden">
              <img :src="review.image_url" alt="" class="w-full h-auto" />  <!-- Alt text is empty because it's decorative only -->
            </div>
            
            <div v-if="review.class_attended" class="flex items-center mt-2 text-xs text-gray-500">
              <span class="bg-secondary bg-opacity-20 text-primary py-1 px-2 rounded-full">
                {{ review.class_attended }}
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue';

// Recensioni statiche per garantire che siano visualizzate correttamente
const reviews = ref([
  {
    name: 'Emma Rossi',
    title: 'Regular Practitioner',
    image: '/images/profile-1.jpg',
    rating: 5,
    date: 'July 15, 2023',
    text: "I've been practicing yoga for years, but joining Serendipity has truly transformed my practice. The instructors are incredibly knowledgeable and create a supportive environment where I can deepen my practice. The Hatha classes have helped me improve my flexibility and find balance in my busy life.",
    class_attended: 'Hatha Yoga',
    featured: true
  },
  {
    name: 'Marco Bianchi',
    title: 'Beginner Yogi',
    image: '/images/profile-2.jpg',
    rating: 4,
    date: 'September 3, 2023',
    text: "As a complete beginner, I was nervous about trying yoga, but the instructors at Serendipity made me feel welcome from day one. The beginner classes are perfectly paced, and they take time to explain proper alignment. After just two months, I'm already noticing improvements in my posture and overall well-being.",
    class_attended: 'Yoga for Beginners'
  },
  {
    name: 'Sofia Esposito',
    title: 'Advanced Practitioner',
    image: '/images/profile-3.jpg',
    rating: 5,
    date: 'August 12, 2023',
    text: "The Ashtanga classes here are challenging in the best way possible. I appreciate how the teachers provide modifications for different levels while still encouraging us to push our boundaries. The studio's peaceful atmosphere makes it my favorite place to practice and grow.",
    class_attended: 'Ashtanga Yoga',
    image_url: '/images/yoga-class-review.jpg'
  },
  {
    name: 'Luca Moretti',
    title: 'Wellness Enthusiast',
    image: '/images/profile-4.jpg',
    rating: 5,
    date: 'October 5, 2023',
    text: "I started coming to Serendipity for yoga but discovered their meditation sessions, which have been life-changing. Learning to quiet my mind and focus on my breath has helped me manage stress much better. The instructors create such a calming environment - it's my sanctuary in the middle of a hectic week.",
    class_attended: 'Meditation'
  },
  {
    name: 'Alessia Conti',
    title: 'Yoga Therapy Participant',
    image: '/images/profile-5.jpg',
    rating: 5,
    date: 'November 8, 2023',
    text: "After a back injury, I was recommended to try yoga therapy at Serendipity. The personalized approach and gentle guidance from my instructor have made a significant difference in my recovery. I've gained strength, mobility, and most importantly, confidence in my body again. Forever grateful for this amazing studio!",
    class_attended: 'Yoga Therapy',
    featured: true
  },
  {
    name: 'Giovanni Romano',
    title: 'Regular Member',
    image: '/images/profile-6.jpg',
    rating: 4,
    date: 'December 1, 2023',
    text: "The variety of classes offered at Serendipity keeps my practice interesting and challenging. I particularly enjoy the Kundalini yoga sessions which have helped me develop both physical strength and mental clarity. The community here is supportive and welcoming - it feels like a second home.",
    class_attended: 'Kundalini Yoga'
  }
]);

// In una versione reale, qui si potrebbero recuperare le recensioni dal server
onMounted(() => {
  console.log('Social Wall mounted with', reviews.value.length, 'reviews');
  // Assicurarsi che il component sia montato correttamente e che le recensioni siano disponibili
});
</script>

<style scoped>
.shadow-custom {
  box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1);
}

.line-clamp-4 {
  display: -webkit-box;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style> 