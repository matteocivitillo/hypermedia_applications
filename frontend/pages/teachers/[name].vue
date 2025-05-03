<template>
  <div class="flex flex-col min-h-screen">
    <NavBar />
    <BreadCrumbs :breadcrumbs="[
      { text: 'Home', url: '/' }, 
      { text: 'Teachers', url: '/teachers' }, 
      { text: teacher?.name || route.params.name }
    ]" />
    <main class="flex-grow">
      <!-- Teacher Profile Section -->
      <section class="bg-gray-50 py-14">
        <div class="container mx-auto px-4" v-if="teacher">
          <div class="flex flex-col lg:flex-row gap-20">
            <!-- Teacher Card -->
            <div class="w-full lg:w-1/3">
              <div class="bg-white rounded-xl shadow-lg overflow-hidden">
                <div class="h-96 relative">
                  <img :src="teacher.image" :alt="teacher.name" class="w-full h-full object-cover">
                  <div class="absolute inset-0 bg-black bg-opacity-10"></div>
                </div>
                <div class="p-6 space-y-4">
                  <div class="flex flex-wrap gap-2 items-center">
                    <span class="bg-primary bg-opacity-80 text-white px-3 py-1 rounded-full text-sm">
                      {{ teacher.role }}
                    </span>
                  </div>
                  <h3 class="text-2xl font-bold">{{ teacher.name }}</h3>
                  <div class="flex flex-wrap gap-2">
                    <span v-for="(specialty, index) in teacher.specialties" :key="index" class="bg-white bg-opacity-80 text-gray-600 border border-white px-3 py-1 rounded-full text-sm">
                      {{ specialty }}
                    </span>
                  </div>
                </div>
              </div>
            </div>
            
            <!-- Teacher Details -->
            <div class="w-full lg:w-2/3 space-y-8">
              <div class="space-y-1">
                <h1 class="text-4xl font-bold">{{ teacher.name }}</h1>
                <p class="text-2xl text-gray-600">{{ teacher.role }}</p>
              </div>
              
              <div class="space-y-2">
                <h2 class="text-3xl font-bold">Expertise</h2>
                <p class="text-xl text-gray-600">{{ teacher.expertise }}</p>
              </div>
              
              <div class="space-y-2">
                <h2 class="text-3xl font-bold">About</h2>
                <div v-html="teacher.bio" class="text-xl text-gray-600"></div>
              </div>
              
              <div class="space-y-4">
                <h2 class="text-3xl font-bold">Activities</h2>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <div v-for="(activity, index) in teacher.activities" :key="index" class="bg-gray-200 text-center py-3 px-6 rounded-xl">
                    <span class="font-bold">{{ activity }}</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div v-else class="text-center py-10">
          <p class="text-xl">Teacher not found</p>
          <NuxtLink to="/teachers" class="inline-block mt-4 px-6 py-2 bg-primary text-white rounded-lg hover:bg-opacity-90 transition-colors">
            Back to Teachers
          </NuxtLink>
        </div>
      </section>
    </main>
    <SiteFooter />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import NavBar from '~/components/home/NavBar.vue'
import BreadCrumbs from '~/components/home/BreadCrumbs.vue'
import SiteFooter from '~/components/home/SiteFooter.vue'

const route = useRoute()
const teacher = ref(null)

// Teacher data - in a real app, this would come from an API or database
const teacherData = {
  'sarah-mitchell': {
    name: 'Sarah Mitchell',
    role: 'Lead Yoga Instructor',
    image: '/images/teachers/sarah-mitchell.jpg',
    specialties: ['Vinyasa Flow', 'Meditation'],
    expertise: 'Vinyasa Flow & Meditation',
    bio: `<p>With over 15 years of experience in yoga practice and teaching, Sarah brings a wealth of knowledge in Vinyasa Flow and meditation techniques. Her classes focus on mindful movement and breath awareness.</p>
          <p class="mt-4">Sarah's approach combines traditional yoga with contemporary wellness practices, creating a unique experience for students at all levels. She believes in the transformative power of yoga to enhance both physical health and mental clarity.</p>
          <p class="mt-4">Certified in multiple yoga disciplines, Sarah continues to expand her knowledge through regular advanced training and workshops worldwide.</p>`,
    activities: ['Morning Vinyasa Flow', 'Mindful Meditation', 'Breathwork Workshop', 'Yoga for Beginners']
  },
  'michael-chen': {
    name: 'Michael Chen',
    role: 'Wellness Director',
    image: '/images/teachers/michael-chen.jpg',
    specialties: ['Traditional Yoga', 'Water Yoga'],
    expertise: 'Traditional Yoga & Water Yoga',
    bio: `<p>Michael has been practicing yoga for over 20 years and brings deep knowledge of traditional practices combined with innovative water-based techniques. His holistic approach to wellness integrates both physical and mental aspects of health.</p>
         <p class="mt-4">As our Wellness Director, Michael oversees the development of all programs at Serendipity, ensuring they meet the highest standards of quality and effectiveness.</p>`,
    activities: ['Traditional Yoga', 'Water Yoga Sessions', 'Wellness Workshops', 'Personal Coaching']
  },
  'emma-rodriguez': {
    name: 'Emma Rodriguez',
    role: 'Dance & Movement Specialist',
    image: '/images/teachers/emma-rodriguez.jpg',
    specialties: ['Zumba', 'Dynamic Flow'],
    expertise: 'Dance Fitness & Dynamic Yoga Flow',
    bio: `<p>Emma brings energy and rhythm to Serendipity with her background in professional dance and yoga instruction. Her classes are known for their joyful atmosphere and effective combinations of movement techniques.</p>
         <p class="mt-4">With certification in multiple dance and yoga disciplines, Emma creates uniquely engaging sessions that help participants discover the joy of movement.</p>`,
    activities: ['Zumba Classes', 'Dynamic Flow Yoga', 'Dance Meditation', 'Rhythm Workshops']
  },
  'david-kumar': {
    name: 'David Kumar',
    role: 'Meditation Guide',
    image: '/images/teachers/david-kumar.jpg',
    specialties: ['Mindfulness', 'Spiritual Wellness'],
    expertise: 'Mindfulness & Spiritual Practices',
    bio: `<p>David specializes in various meditation techniques and spiritual practices that enhance mental clarity and emotional balance. His gentle guidance helps students of all levels develop a consistent and rewarding meditation practice.</p>
         <p class="mt-4">Having studied with masters in India and Tibet, David brings authentic traditional practices and makes them accessible to modern practitioners.</p>`,
    activities: ['Daily Meditation Sessions', 'Mindfulness Workshops', 'Spiritual Retreats', 'One-on-One Guidance']
  },
  'sofia-bianchi': {
    name: 'Sofia Bianchi',
    role: 'Creative Arts Instructor',
    image: '/images/teachers/sofia-bianchi.jpg',
    specialties: ['Ceramics', 'Mindful Creation'],
    expertise: 'Creative Arts & Mindful Creation',
    bio: `<p>Sofia combines her background in fine arts with mindfulness practices to create uniquely therapeutic creative experiences. Her classes encourage self-expression through various artistic media while maintaining present-moment awareness.</p>
         <p class="mt-4">With a strong belief in the healing power of creativity, Sofia guides students to discover inner peace and personal insight through artistic expression.</p>`,
    activities: ['Ceramic Workshops', 'Mindful Art Sessions', 'Creative Meditation', 'Expressive Arts Therapy']
  }
}

onMounted(() => {
  // Get the teacher data based on the route parameter
  const teacherName = route.params.name
  teacher.value = teacherData[teacherName] || null
})
</script>

<style scoped>
.bg-primary {
  background-color: #006A71;
}
</style> 