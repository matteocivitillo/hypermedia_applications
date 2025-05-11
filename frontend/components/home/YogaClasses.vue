<template>
  <section class="py-20 bg-gray-50">
    <div class="container mx-auto px-8 sm:px-12 md:px-16 lg:px-24 xl:px-32">
      <h2 class="text-4xl font-bold text-primary text-center mb-16">Our Yoga Classes</h2>
      
      <div v-if="isLoading" class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div v-for="i in 3" :key="i" class="animate-pulse bg-white rounded-xl p-8 shadow-custom">
          <div class="h-4 bg-gray-200 rounded w-1/4 mb-8"></div>
          <div class="h-6 bg-gray-300 rounded w-3/4 mb-4"></div>
          <div class="h-20 bg-gray-200 rounded mb-8"></div>
          <div class="flex items-center mb-6">
            <div class="rounded-full bg-gray-300 h-12 w-12 mr-4"></div>
            <div>
              <div class="h-4 bg-gray-300 rounded w-24 mb-2"></div>
            </div>
          </div>
          <div class="h-10 bg-gray-200 rounded w-full"></div>
        </div>
      </div>
      
      <div v-else-if="hasError" class="text-center py-12">
        <p class="text-xl text-gray-600 mb-4">Could not load yoga classes. Please try again later.</p>
      </div>
      
      <div v-else-if="yogaClasses.length > 0" class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <!-- Class Card -->
        <div 
          v-for="yogaClass in yogaClasses" 
          :key="yogaClass.id"
          class="bg-white rounded-xl shadow-custom p-8 transform hover:-translate-y-2 transition-all duration-300"
        >
          <div class="mb-5">
            <span class="bg-primary bg-opacity-70 text-white text-sm font-medium py-1.5 px-4 rounded-full">
              {{ yogaClass.difficulty }}
            </span>
          </div>
          
          <div class="mb-8">
            <h3 class="text-2xl font-bold text-primary mb-4">{{ yogaClass.name }}</h3>
            <p class="text-gray-600 leading-relaxed">
              {{ yogaClass.description }}
            </p>
          </div>
          
          <div class="flex items-center">
            <div class="w-12 h-12 rounded-full bg-gray-300 mr-4 overflow-hidden border-2 border-primary">
              <img 
                :src="yogaClass.teacher_image" 
                alt=""  
                class="w-full h-full object-cover object-center"
                onerror="this.src='/images/teacher-placeholder.jpg'"
              />  <!-- Alt text is empty because it's decorative only -->
            </div>
            <div>
              <NuxtLink 
                v-if="yogaClass.teacher_id" 
                :to="`/singleteacher?id=${yogaClass.teacher_id}`" 
                class="text-gray-800 font-medium hover:text-primary transition-colors"
              >
                {{ yogaClass.teacher_name || 'Yoga Teacher' }}
              </NuxtLink>
              <p v-else class="text-gray-800 font-medium">{{ yogaClass.teacher_name || 'Yoga Teacher' }}</p>
            </div>
          </div>
          
          <NuxtLink 
            :to="`/singleactivity?id=${yogaClass.id}`" 
            class="mt-6 block w-full bg-secondary hover:bg-secondary-dark text-primary font-medium py-3 px-6 rounded-lg text-center transition-colors duration-300"
          >
            View Details
          </NuxtLink>
        </div>
      </div>
      
      <div v-else class="text-center py-12">
        <p class="text-xl text-gray-600">No yoga classes found.</p>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { API_URL } from '../../utils/api';

const yogaClasses = ref([]);
const isLoading = ref(true);
const hasError = ref(false);

// List of yoga class types we want to display
const targetYogaTypes = ['hatha', 'kundalini', 'ashtanga'];

onMounted(async () => {
  try {
    const response = await fetch(`${API_URL}/activities`);
    
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    
    const data = await response.json();
    
    if (data.activities && data.activities.length > 0) {
      // Cerchiamo specificamente Hatha, Kundalini e Ashtanga Yoga
      
      // Filter per trovare queste specifiche classi di yoga
      let selectedYogaClasses = [];
      
      // Prima proviamo a trovare attività che hanno specificamente questi nomi
      targetYogaTypes.forEach(yogaType => {
        const matchingActivity = data.activities.find(activity => 
          (activity.name?.toLowerCase().includes(yogaType) || 
           activity.title?.toLowerCase().includes(yogaType))
        );
        
        if (matchingActivity) {
          selectedYogaClasses.push(matchingActivity);
        }
      });
      
      // Se non abbiamo trovato nessuna classe, segnaliamo un errore
      if (selectedYogaClasses.length === 0) {
        hasError.value = true;
        return;
      }
      
      // Fetch teachers
      try {
        const teacherResponse = await fetch(`${API_URL}/teachers`);
        
        if (!teacherResponse.ok) {
          throw new Error(`HTTP error! Status: ${teacherResponse.status}`);
        }
        
        const teacherData = await teacherResponse.json();
        const teachers = teacherData.teachers || [];
        
        // Assegna insegnanti fissi per ogni tipo di yoga
        const teacherAssignments = {
          'hatha': 'Michael Chen',
          'kundalini': 'Sara Johnson',
          'ashtanga': 'Diego Martinez'
        };
        
        // Process yoga classes with teacher data
        yogaClasses.value = selectedYogaClasses.map(yoga => {
          // Ottieni nome della classe in modo che corrisponda alle specifiche richieste
          let yogaName = yoga.name || yoga.title || "Yoga Class";
          let yogaType = '';
          
          for (const type of targetYogaTypes) {
            if (yogaName.toLowerCase().includes(type)) {
              // Capitalize first letter of each word
              yogaName = type.charAt(0).toUpperCase() + type.slice(1) + " Yoga";
              yogaType = type;
              break;
            }
          }
          
          // Trova l'insegnante giusto in base al tipo di yoga
          let teacherName = teacherAssignments[yogaType] || 'Yoga Teacher';
          let teacher = teachers.find(t => t.name === teacherName);
          
          // Se non troviamo l'insegnante specifico, usiamo il primo disponibile
          if (!teacher && teachers.length > 0) {
            teacher = teachers[0];
          }
          
          return {
            id: yoga.id,
            name: yogaName,
            difficulty: getDifficultyFromType(yogaName) || yoga.level || yoga.difficulty,
            description: yoga.short_description || yoga.description || getDefaultDescription(yogaName),
            teacher_name: teacherName,
            teacher_image: teacher ? (teacher.image?.startsWith('http') ? teacher.image : `/images/teacher-${yogaType === 'hatha' ? '1' : yogaType === 'kundalini' ? '2' : '3'}.jpg`) : '/images/teacher-placeholder.jpg',
            teacher_id: teacher ? teacher.id : yoga.teacher_id || null
          };
        });
        
      } catch (error) {
        console.error('Failed to fetch teachers:', error);
        // If we can't get teacher info, we'll still show the yoga classes but without teacher data
        yogaClasses.value = selectedYogaClasses.map(yoga => {
          let yogaName = yoga.name || yoga.title || "Yoga Class";
          let yogaType = '';
          
          for (const type of targetYogaTypes) {
            if (yogaName.toLowerCase().includes(type)) {
              yogaName = type.charAt(0).toUpperCase() + type.slice(1) + " Yoga";
              yogaType = type;
              break;
            }
          }
          
          return {
            id: yoga.id,
            name: yogaName,
            difficulty: getDifficultyFromType(yogaName) || yoga.level || yoga.difficulty,
            description: yoga.short_description || yoga.description || getDefaultDescription(yogaName),
            teacher_name: 'Yoga Teacher',
            teacher_image: '/images/teacher-placeholder.jpg',
            teacher_id: null
          };
        });
      }
    } else {
      // No activities found in the response
      hasError.value = true;
    }
  } catch (error) {
    console.error('Failed to fetch yoga classes:', error);
    hasError.value = true;
  } finally {
    isLoading.value = false;
  }
});

// Helper function to assign a difficulty level based on yoga type
function getDifficultyFromType(yogaName) {
  const lowerName = yogaName.toLowerCase();
  if (lowerName.includes('hatha')) return 'Beginner';
  if (lowerName.includes('kundalini')) return 'Intermediate';
  if (lowerName.includes('ashtanga')) return 'Advanced';
  return null;
}

// Helper function to provide default descriptions
function getDefaultDescription(yogaName) {
  const lowerName = yogaName.toLowerCase();
  if (lowerName.includes('hatha')) {
    return 'A slow-paced style of yoga focusing on postures (asana), breathing (pranayama) and deep relaxation.';
  }
  if (lowerName.includes('kundalini')) {
    return 'Intense energy work incorporating breathing, mantra, meditation and repetitive movements.';
  }
  if (lowerName.includes('ashtanga')) {
    return 'A dynamic, physically demanding practice that synchronizes breath with a progressive series of postures.';
  }
  return 'A transformative yoga practice for mind, body and spirit.';
}
</script>

<style scoped>
.shadow-custom {
  box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1);
}

.text-primary {
  color: #006A71;
}

.bg-primary {
  background-color: #006A71;
}

.bg-secondary {
  background-color: #F2EFE7;
}

.bg-secondary-dark {
  background-color: #e7e3d2;
}
</style> 