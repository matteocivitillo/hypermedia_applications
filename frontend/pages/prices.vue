<template>
  <div class="flex flex-col min-h-screen dark:bg-gray-800">
    <NavBar />
    <BreadCrumbs :breadcrumbs="[
      { text: 'Home', url: '/' }, 
      { text: 'Prices' }
    ]" />
    <main class="flex-grow">
      
      <!-- Introduction Section -->
      <section class="py-10 px-8 md:px-20 bg-gradient-to-b dark:bg-gray-800">
        <div class="container mx-auto text-center">
          <h1 class="text-3xl font-bold text-primary dark:text-[#9ACBD0] mb-4">
            Our Membership Plans
          </h1>
          <p class="text-xl text-gray-600 dark:text-gray-200 mb-2">
            To activate any of our subscription plans, please visit our reception desk at our center.
          </p>
          <p class="text-xl text-gray-600 dark:text-gray-200 mb-2">
            Below you'll find all our available pricing options to suit your needs.
          </p>
        </div>
      </section>
      
      <!-- Subscription Plans by Type -->
      <section class="py-14 px-4 border-b border-gray-200 dark:border-gray-600 bg-white dark:bg-gray-700 animate-fade-in">
        <div class="container mx-auto">
          <h2 class="text-3xl font-bold text-gray-900 dark:text-white text-center mb-10 relative">
            <span class="inline-block relative">
              Yoga4You
            </span>
          </h2>
          
          <!-- Combined Features and Pricing -->
          <div class="flex flex-col lg:flex-row justify-between items-center max-w-6xl mx-auto">
            <!-- Features Box -->
            <div class="w-full lg:w-1/3 max-w-md animate-fade-in">
              <div class="bg-white dark:bg-gray-600 rounded-xl shadow-xl dark:shadow-gray-900/70 overflow-hidden border border-gray-100 dark:border-gray-500">
                <div class="bg-gradient-to-br from-primary/5 to-transparent dark:from-primary/10 dark:to-gray-600 p-5 rounded-t-xl">
                  <h3 class="text-xl font-bold text-primary dark:text-[#9ACBD0] mb-3 flex items-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" viewBox="0 0 20 20" fill="currentColor">
                      <path fill-rule="evenodd" d="M2.166 4.999A11.954 11.954 0 0010 1.944 11.954 11.954 0 0017.834 5c.11.65.166 1.32.166 2.001 0 5.225-3.34 9.67-8 11.317C5.34 16.67 2 12.225 2 7c0-.682.057-1.35.166-2.001zm11.541 3.708a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                    </svg>
                    Features included
                  </h3>
                  <div class="space-y-1 text-gray-600 dark:text-gray-200">
                    <p class="flex items-center text-gray-700 dark:text-gray-200">
                      <span class="inline-block w-5 h-5 rounded-full bg-primary/10 dark:bg-primary/20 text-primary dark:text-[#9ACBD0] mr-2 flex items-center justify-center text-xs">✓</span>
                      Unlimited access to all classes
                    </p>
                    <p class="flex items-center text-gray-700 dark:text-gray-200">
                      <span class="inline-block w-5 h-5 rounded-full bg-primary/10 dark:bg-primary/20 text-primary dark:text-[#9ACBD0] mr-2 flex items-center justify-center text-xs">✓</span>
                      Access to meditation room
                    </p>
                    <p class="flex items-center text-gray-700 dark:text-gray-200">
                      <span class="inline-block w-5 h-5 rounded-full bg-primary/10 dark:bg-primary/20 text-primary dark:text-[#9ACBD0] mr-2 flex items-center justify-center text-xs">✓</span>
                      Use of shower facilities
                    </p>
                  </div>
                </div>
              </div>
            </div>
            
            <!-- Pricing Comparison -->
            <div class="w-full lg:w-3/5 max-w-xl animate-fade-in mt-6 lg:mt-0">
              <div class="bg-white dark:bg-gray-600 rounded-xl shadow-xl dark:shadow-gray-900/70 overflow-hidden border border-gray-200 dark:border-gray-500">
                <table class="w-full text-left">
                  <thead>
                    <tr class="border-b-2 dark:border-gray-500">
                      <th class="px-4 py-3 font-bold text-white bg-primary">Plan Duration</th>
                      <th class="px-4 py-3 font-bold text-white bg-primary">Total Price</th>
                      <th class="px-4 py-3 font-bold text-white bg-primary">Monthly Equivalent</th>
                      <th class="px-4 py-3 font-bold text-white bg-primary">Savings</th>
                    </tr>
                  </thead>
                  <tbody class="divide-y divide-gray-300 dark:divide-gray-500">
                    <tr class="bg-gray-50 dark:bg-gray-700 transition-colors">
                      <td class="px-4 py-3 font-medium text-primary dark:text-[#9ACBD0]">Monthly</td>
                      <td class="px-4 py-3 font-bold text-gray-900 dark:text-white">25€</td>
                      <td class="px-4 py-3 text-gray-700 dark:text-gray-200">25€/month</td>
                      <td class="px-4 py-3 text-gray-700 dark:text-gray-200">-</td>
                    </tr>
                    <tr class="bg-white dark:bg-gray-600 transition-colors">
                      <td class="px-4 py-3 font-medium text-primary dark:text-[#9ACBD0]">6 Months</td>
                      <td class="px-4 py-3 font-bold text-gray-900 dark:text-white">140€</td>
                      <td class="px-4 py-3 text-gray-700 dark:text-gray-200">23.33€/month</td>
                      <td class="px-4 py-3">
                        <span class="text-green-600 dark:text-green-400 text-sm font-medium px-2 py-0.5 bg-green-50 dark:bg-green-900/30 rounded-md border border-green-100 dark:border-green-700">Save 10€</span>
                      </td>
                    </tr>
                    <tr class="bg-gray-50 dark:bg-gray-700 transition-colors">
                      <td class="px-4 py-3 font-medium text-primary dark:text-[#9ACBD0]">Yearly</td>
                      <td class="px-4 py-3 font-bold text-gray-900 dark:text-white">270€</td>
                      <td class="px-4 py-3 text-gray-700 dark:text-gray-200">22.50€/month</td>
                      <td class="px-4 py-3">
                        <span class="text-green-600 dark:text-green-400 text-sm font-medium px-2 py-0.5 bg-green-50 dark:bg-green-900/30 rounded-md border border-green-100 dark:border-green-700">Save 30€</span>
                      </td>
                    </tr>
                  </tbody>
                </table>
                <div class="p-3 bg-gradient-to-r from-primary/5 to-primary/10 dark:from-gray-500 dark:to-gray-600 border-t dark:border-gray-500">
                  <p class="italic text-gray-700 dark:text-gray-200 text-center text-sm">Unlock your yoga journey with our essential experience</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
      
      <!-- Standard Plans Section -->
      <section class="py-14 px-4 border-b border-gray-200 dark:border-gray-600 bg-white dark:bg-gray-700 animate-fade-in">
        <div class="container mx-auto">
          <h2 class="text-3xl font-bold text-gray-900 dark:text-white text-center mb-10 relative">
            <span class="inline-block relative">
              Standard
            </span>
          </h2>
          
          <!-- Combined Features and Pricing -->
          <div class="flex flex-col lg:flex-row justify-between items-center max-w-6xl mx-auto">
            <!-- Features Box -->
            <div class="w-full lg:w-1/3 max-w-md animate-fade-in">
              <div class="bg-white dark:bg-gray-600 rounded-xl shadow-xl dark:shadow-gray-900/70 overflow-hidden border border-gray-100 dark:border-gray-500">
                <div class="bg-gradient-to-br from-primary/5 to-transparent dark:from-primary/10 dark:to-gray-600 p-5 rounded-t-xl">
                  <h3 class="text-xl font-bold text-primary dark:text-[#9ACBD0] mb-3 flex items-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" viewBox="0 0 20 20" fill="currentColor">
                      <path fill-rule="evenodd" d="M2.166 4.999A11.954 11.954 0 0010 1.944 11.954 11.954 0 0017.834 5c.11.65.166 1.32.166 2.001 0 5.225-3.34 9.67-8 11.317C5.34 16.67 2 12.225 2 7c0-.682.057-1.35.166-2.001zm11.541 3.708a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                    </svg>
                    Features included
                  </h3>
                  <div class="space-y-1 text-gray-600 dark:text-gray-200">
                    <p class="flex items-center text-gray-700 dark:text-gray-200">
                      <span class="inline-block w-5 h-5 rounded-full bg-primary/10 dark:bg-primary/20 text-primary dark:text-[#9ACBD0] mr-2 flex items-center justify-center text-xs">✓</span>
                      Unlimited access to all classes
                    </p>
                    <p class="flex items-center text-gray-700 dark:text-gray-200">
                      <span class="inline-block w-5 h-5 rounded-full bg-primary/10 dark:bg-primary/20 text-primary dark:text-[#9ACBD0] mr-2 flex items-center justify-center text-xs">✓</span>
                      Access to meditation room
                    </p>
                    <p class="flex items-center text-gray-700 dark:text-gray-200">
                      <span class="inline-block w-5 h-5 rounded-full bg-primary/10 dark:bg-primary/20 text-primary dark:text-[#9ACBD0] mr-2 flex items-center justify-center text-xs">✓</span>
                      Use of shower facilities
                    </p>
                    <p class="flex items-center text-gray-700 dark:text-gray-200">
                      <span class="inline-block w-5 h-5 rounded-full bg-primary/10 dark:bg-primary/20 text-primary dark:text-[#9ACBD0] mr-2 flex items-center justify-center text-xs">✓</span>
                      Access to all activites under reservation
                    </p>
                    <p class="flex items-center text-gray-700 dark:text-gray-200">
                      <span class="inline-block w-5 h-5 rounded-full bg-primary/10 dark:bg-primary/20 text-primary dark:text-[#9ACBD0] mr-2 flex items-center justify-center text-xs">✓</span>
                      Access to all the areas
                    </p>
                    <p class="flex items-center text-gray-700 dark:text-gray-200">
                      <span class="inline-block w-5 h-5 rounded-full bg-primary/10 dark:bg-primary/20 text-primary dark:text-[#9ACBD0] mr-2 flex items-center justify-center text-xs">✓</span>
                      Spa access
                    </p>
                  </div>
                </div>
              </div>
            </div>
            
            <!-- Pricing Comparison -->
            <div class="w-full lg:w-3/5 max-w-xl animate-fade-in mt-6 lg:mt-0">
              <div class="bg-white dark:bg-gray-600 rounded-xl shadow-xl dark:shadow-gray-900/70 overflow-hidden border border-gray-200 dark:border-gray-500">
                <table class="w-full text-left">
                  <thead>
                    <tr class="border-b-2 dark:border-gray-500">
                      <th class="px-4 py-3 font-bold text-white bg-primary">Plan Duration</th>
                      <th class="px-4 py-3 font-bold text-white bg-primary">Total Price</th>
                      <th class="px-4 py-3 font-bold text-white bg-primary">Monthly Equivalent</th>
                      <th class="px-4 py-3 font-bold text-white bg-primary">Savings</th>
                    </tr>
                  </thead>
                  <tbody class="divide-y divide-gray-300 dark:divide-gray-500">
                    <tr class="bg-gray-50 dark:bg-gray-700 transition-colors">
                      <td class="px-4 py-3 font-medium text-primary dark:text-[#9ACBD0]">Monthly</td>
                      <td class="px-4 py-3 font-bold text-gray-900 dark:text-white">35€</td>
                      <td class="px-4 py-3 text-gray-700 dark:text-gray-200">35€/month</td>
                      <td class="px-4 py-3 text-gray-700 dark:text-gray-200">-</td>
                    </tr>
                    <tr class="bg-white dark:bg-gray-600 transition-colors">
                      <td class="px-4 py-3 font-medium text-primary dark:text-[#9ACBD0]">6 Months</td>
                      <td class="px-4 py-3 font-bold text-gray-900 dark:text-white">200€</td>
                      <td class="px-4 py-3 text-gray-700 dark:text-gray-200">33.33€/month</td>
                      <td class="px-4 py-3">
                        <span class="text-green-600 dark:text-green-400 text-sm font-medium px-2 py-0.5 bg-green-50 dark:bg-green-900/30 rounded-md border border-green-100 dark:border-green-700">Save 10€</span>
                      </td>
                    </tr>
                    <tr class="bg-gray-50 dark:bg-gray-700 transition-colors">
                      <td class="px-4 py-3 font-medium text-primary dark:text-[#9ACBD0]">Yearly</td>
                      <td class="px-4 py-3 font-bold text-gray-900 dark:text-white">380€</td>
                      <td class="px-4 py-3 text-gray-700 dark:text-gray-200">31.67€/month</td>
                      <td class="px-4 py-3">
                        <span class="text-green-600 dark:text-green-400 text-sm font-medium px-2 py-0.5 bg-green-50 dark:bg-green-900/30 rounded-md border border-green-100 dark:border-green-700">Save 40€</span>
                      </td>
                    </tr>
                  </tbody>
                </table>
                <div class="p-3 bg-gradient-to-r from-primary/5 to-primary/10 dark:from-gray-500 dark:to-gray-600 border-t dark:border-gray-500">
                  <p class="italic text-gray-700 dark:text-gray-200 text-center text-sm">Elevate your practice with comprehensive access</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
      
      <!-- Plus Plans Section -->
      <section class="py-14 px-4 bg-white dark:bg-gray-700 animate-fade-in">
        <div class="container mx-auto">
          <h2 class="text-3xl font-bold text-gray-900 dark:text-white text-center mb-10 relative">
            <span class="inline-block relative">
              Premium
            </span>
          </h2>
          
          <!-- Combined Features and Pricing -->
          <div class="flex flex-col lg:flex-row justify-between items-center max-w-6xl mx-auto">
            <!-- Features Box -->
            <div class="w-full lg:w-1/3 max-w-md animate-fade-in">
              <div class="bg-white dark:bg-gray-600 rounded-xl shadow-xl dark:shadow-gray-900/70 overflow-hidden border border-gray-100 dark:border-gray-500">
                <div class="bg-gradient-to-br from-primary/5 to-transparent dark:from-primary/10 dark:to-gray-600 p-5 rounded-t-xl">
                  <h3 class="text-xl font-bold text-primary dark:text-[#9ACBD0] mb-3 flex items-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" viewBox="0 0 20 20" fill="currentColor">
                      <path fill-rule="evenodd" d="M2.166 4.999A11.954 11.954 0 0010 1.944 11.954 11.954 0 0017.834 5c.11.65.166 1.32.166 2.001 0 5.225-3.34 9.67-8 11.317C5.34 16.67 2 12.225 2 7c0-.682.057-1.35.166-2.001zm11.541 3.708a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                    </svg>
                    Features included
                  </h3>
                  <div class="space-y-1 text-gray-600 dark:text-gray-200">
                    <p class="flex items-center text-gray-700 dark:text-gray-200">
                      <span class="inline-block w-5 h-5 rounded-full bg-primary/10 dark:bg-primary/20 text-primary dark:text-[#9ACBD0] mr-2 flex items-center justify-center text-xs">✓</span>
                      Unlimited access to all classes
                    </p>
                    <p class="flex items-center text-gray-700 dark:text-gray-200">
                      <span class="inline-block w-5 h-5 rounded-full bg-primary/10 dark:bg-primary/20 text-primary dark:text-[#9ACBD0] mr-2 flex items-center justify-center text-xs">✓</span>
                      Privileged access to meditation room
                    </p>
                    <p class="flex items-center text-gray-700 dark:text-gray-200">
                      <span class="inline-block w-5 h-5 rounded-full bg-primary/10 dark:bg-primary/20 text-primary dark:text-[#9ACBD0] mr-2 flex items-center justify-center text-xs">✓</span>
                      Use of shower facilities
                    </p>
                    <p class="flex items-center text-gray-700 dark:text-gray-200">
                      <span class="inline-block w-5 h-5 rounded-full bg-primary/10 dark:bg-primary/20 text-primary dark:text-[#9ACBD0] mr-2 flex items-center justify-center text-xs">✓</span>
                      Access to all activites without reservation
                    </p>
                    <p class="flex items-center text-gray-700 dark:text-gray-200">
                      <span class="inline-block w-5 h-5 rounded-full bg-primary/10 dark:bg-primary/20 text-primary dark:text-[#9ACBD0] mr-2 flex items-center justify-center text-xs">✓</span>
                      Access to all the areas
                    </p>
                    <p class="flex items-center text-gray-700 dark:text-gray-200">
                      <span class="inline-block w-5 h-5 rounded-full bg-primary/10 dark:bg-primary/20 text-primary dark:text-[#9ACBD0] mr-2 flex items-center justify-center text-xs">✓</span>
                      Spa access
                    </p>
                    <p class="flex items-center text-gray-700 dark:text-gray-200">
                      <span class="inline-block w-5 h-5 rounded-full bg-primary/10 dark:bg-primary/20 text-primary dark:text-[#9ACBD0] mr-2 flex items-center justify-center text-xs">✓</span>
                      Discounts and free drinks at the bar
                    </p>
                  </div>
                </div>
              </div>
            </div>
            
            <!-- Pricing Comparison -->
            <div class="w-full lg:w-3/5 max-w-xl animate-fade-in mt-6 lg:mt-0">
              <div class="bg-white dark:bg-gray-600 rounded-xl shadow-xl dark:shadow-gray-900/70 overflow-hidden border border-gray-200 dark:border-gray-500">
                <table class="w-full text-left">
                  <thead>
                    <tr class="border-b-2 dark:border-gray-500">
                      <th class="px-4 py-3 font-bold text-white bg-primary">Plan Duration</th>
                      <th class="px-4 py-3 font-bold text-white bg-primary">Total Price</th>
                      <th class="px-4 py-3 font-bold text-white bg-primary">Monthly Equivalent</th>
                      <th class="px-4 py-3 font-bold text-white bg-primary">Savings</th>
                    </tr>
                  </thead>
                  <tbody class="divide-y divide-gray-300 dark:divide-gray-500">
                    <tr class="bg-gray-50 dark:bg-gray-700 transition-colors">
                      <td class="px-4 py-3 font-medium text-primary dark:text-[#9ACBD0]">Monthly</td>
                      <td class="px-4 py-3 font-bold text-gray-900 dark:text-white">40€</td>
                      <td class="px-4 py-3 text-gray-700 dark:text-gray-200">40€/month</td>
                      <td class="px-4 py-3 text-gray-700 dark:text-gray-200">-</td>
                    </tr>
                    <tr class="bg-white dark:bg-gray-600 transition-colors">
                      <td class="px-4 py-3 font-medium text-primary dark:text-[#9ACBD0]">6 Months</td>
                      <td class="px-4 py-3 font-bold text-gray-900 dark:text-white">220€</td>
                      <td class="px-4 py-3 text-gray-700 dark:text-gray-200">36.67€/month</td>
                      <td class="px-4 py-3">
                        <span class="text-green-600 dark:text-green-400 text-sm font-medium px-2 py-0.5 bg-green-50 dark:bg-green-900/30 rounded-md border border-green-100 dark:border-green-700">Save 20€</span>
                      </td>
                    </tr>
                    <tr class="bg-gray-50 dark:bg-gray-700 transition-colors">
                      <td class="px-4 py-3 font-medium text-primary dark:text-[#9ACBD0]">Yearly</td>
                      <td class="px-4 py-3 font-bold text-gray-900 dark:text-white">420€</td>
                      <td class="px-4 py-3 text-gray-700 dark:text-gray-200">35.00€/month</td>
                      <td class="px-4 py-3">
                        <span class="text-green-600 dark:text-green-400 text-sm font-medium px-2 py-0.5 bg-green-50 dark:bg-green-900/30 rounded-md border border-green-100 dark:border-green-700">Save 60€</span>
                      </td>
                    </tr>
                  </tbody>
                </table>
                <div class="p-3 bg-gradient-to-r from-primary/5 to-primary/10 dark:from-gray-500 dark:to-gray-600 border-t dark:border-gray-500">
                  <p class="italic text-gray-700 dark:text-gray-200 text-center text-sm">Experience ultimate wellness with premium benefits</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
      
      <!-- Comparison Table Section -->
      <section class="py-14 px-4 bg-white dark:bg-gray-800 border-t border-gray-200 dark:border-gray-600 animate-fade-in">
        <div class="container mx-auto">
          <h1 class="text-3xl font-bold text-primary dark:text-[#9ACBD0] text-center mb-4">
            Compare Plans
          </h1>
          <p class="text-lg text-gray-600 dark:text-gray-200 text-center mb-6">
            Below is a table that highlights the main feature differences for each type of membership.
          </p>
          
          <div class="max-w-5xl mx-auto overflow-hidden border border-gray-200 dark:border-gray-500 rounded-xl shadow-xl dark:shadow-gray-900/70">
            <table class="w-full text-left">
              <thead>
                <tr class="bg-primary text-white">
                  <th class="px-6 py-4 font-semibold">Features</th>
                  <th class="px-6 py-4 font-semibold text-center">Yoga4You</th>
                  <th class="px-6 py-4 font-semibold text-center">Standard</th>
                  <th class="px-6 py-4 font-semibold text-center">Premium</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-gray-300 dark:divide-gray-500">
                <tr class="bg-white dark:bg-gray-600 transition-colors">
                  <td class="px-6 py-4 text-gray-800 dark:text-gray-200">Unlimited access to all classes</td>
                  <td class="px-6 py-4 text-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mx-auto text-green-500" viewBox="0 0 20 20" fill="currentColor">
                      <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                    </svg>
                  </td>
                  <td class="px-6 py-4 text-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mx-auto text-green-500" viewBox="0 0 20 20" fill="currentColor">
                      <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                    </svg>
                  </td>
                  <td class="px-6 py-4 text-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mx-auto text-green-500" viewBox="0 0 20 20" fill="currentColor">
                      <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                    </svg>
                  </td>
                </tr>
                <tr class="bg-gray-50 dark:bg-gray-700 transition-colors">
                  <td class="px-6 py-4 text-gray-800 dark:text-gray-200">Access to meditation room</td>
                  <td class="px-6 py-4 text-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mx-auto text-green-500" viewBox="0 0 20 20" fill="currentColor">
                      <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                    </svg>
                  </td>
                  <td class="px-6 py-4 text-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mx-auto text-green-500" viewBox="0 0 20 20" fill="currentColor">
                      <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                    </svg>
                  </td>
                  <td class="px-6 py-4 text-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mx-auto text-green-500" viewBox="0 0 20 20" fill="currentColor">
                      <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                    </svg>
                  </td>
                </tr>
                <tr class="bg-white dark:bg-gray-600 transition-colors">
                  <td class="px-6 py-4 text-gray-800 dark:text-gray-200">Use of shower facilities</td>
                  <td class="px-6 py-4 text-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mx-auto text-green-500" viewBox="0 0 20 20" fill="currentColor">
                      <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                    </svg>
                  </td>
                  <td class="px-6 py-4 text-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mx-auto text-green-500" viewBox="0 0 20 20" fill="currentColor">
                      <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                    </svg>
                  </td>
                  <td class="px-6 py-4 text-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mx-auto text-green-500" viewBox="0 0 20 20" fill="currentColor">
                      <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                    </svg>
                  </td>
                </tr>
                <tr class="bg-gray-50 dark:bg-gray-700 transition-colors">
                  <td class="px-6 py-4 text-gray-800 dark:text-gray-200">Access to all activities under reservation</td>
                  <td class="px-6 py-4 text-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mx-auto text-gray-300" viewBox="0 0 20 20" fill="currentColor">
                      <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" />
                    </svg>
                  </td>
                  <td class="px-6 py-4 text-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mx-auto text-green-500" viewBox="0 0 20 20" fill="currentColor">
                      <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                    </svg>
                  </td>
                  <td class="px-6 py-4 text-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mx-auto text-green-500" viewBox="0 0 20 20" fill="currentColor">
                      <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                    </svg>
                  </td>
                </tr>
                <tr class="bg-white dark:bg-gray-600 transition-colors">
                  <td class="px-6 py-4 text-gray-800 dark:text-gray-200">Access to all areas</td>
                  <td class="px-6 py-4 text-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mx-auto text-gray-300" viewBox="0 0 20 20" fill="currentColor">
                      <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" />
                    </svg>
                  </td>
                  <td class="px-6 py-4 text-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mx-auto text-green-500" viewBox="0 0 20 20" fill="currentColor">
                      <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                    </svg>
                  </td>
                  <td class="px-6 py-4 text-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mx-auto text-green-500" viewBox="0 0 20 20" fill="currentColor">
                      <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                    </svg>
                  </td>
                </tr>
                <tr class="bg-gray-50 dark:bg-gray-700 transition-colors">
                  <td class="px-6 py-4 text-gray-800 dark:text-gray-200">Spa access</td>
                  <td class="px-6 py-4 text-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mx-auto text-gray-300" viewBox="0 0 20 20" fill="currentColor">
                      <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" />
                    </svg>
                  </td>
                  <td class="px-6 py-4 text-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mx-auto text-green-500" viewBox="0 0 20 20" fill="currentColor">
                      <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                    </svg>
                  </td>
                  <td class="px-6 py-4 text-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mx-auto text-green-500" viewBox="0 0 20 20" fill="currentColor">
                      <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                    </svg>
                  </td>
                </tr>
                <tr class="bg-white dark:bg-gray-600 transition-colors">
                  <td class="px-6 py-4 text-gray-800 dark:text-gray-200">Privileged access to meditation room</td>
                  <td class="px-6 py-4 text-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mx-auto text-gray-300" viewBox="0 0 20 20" fill="currentColor">
                      <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" />
                    </svg>
                  </td>
                  <td class="px-6 py-4 text-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mx-auto text-gray-300" viewBox="0 0 20 20" fill="currentColor">
                      <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" />
                    </svg>
                  </td>
                  <td class="px-6 py-4 text-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mx-auto text-green-500" viewBox="0 0 20 20" fill="currentColor">
                      <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                    </svg>
                  </td>
                </tr>
                <tr class="bg-gray-50 dark:bg-gray-700 transition-colors">
                  <td class="px-6 py-4 text-gray-800 dark:text-gray-200">Access to all activities without reservation</td>
                  <td class="px-6 py-4 text-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mx-auto text-gray-300" viewBox="0 0 20 20" fill="currentColor">
                      <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" />
                    </svg>
                  </td>
                  <td class="px-6 py-4 text-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mx-auto text-gray-300" viewBox="0 0 20 20" fill="currentColor">
                      <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" />
                    </svg>
                  </td>
                  <td class="px-6 py-4 text-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mx-auto text-green-500" viewBox="0 0 20 20" fill="currentColor">
                      <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                    </svg>
                  </td>
                </tr>
                <tr class="bg-white dark:bg-gray-600 transition-colors">
                  <td class="px-6 py-4 text-gray-800 dark:text-gray-200">Discounts and free drinks at the bar</td>
                  <td class="px-6 py-4 text-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mx-auto text-gray-300" viewBox="0 0 20 20" fill="currentColor">
                      <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" />
                    </svg>
                  </td>
                  <td class="px-6 py-4 text-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mx-auto text-gray-300" viewBox="0 0 20 20" fill="currentColor">
                      <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" />
                    </svg>
                  </td>
                  <td class="px-6 py-4 text-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mx-auto text-green-500" viewBox="0 0 20 20" fill="currentColor">
                      <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                    </svg>
                  </td>
                </tr>
              </tbody>
            </table>
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

// SEO metadata for this page
useSeoMeta({
    title: 'Our Prices - Serendipity Yoga',
    description: 'Explore our pricing options for yoga classes, retreats, and spa services. Choose the perfect package to suit your needs and budget.',
  })
</script>

<style scoped>
.text-primary {
  color: #006A71;
}

/* Dark mode override */
:root.dark .text-primary {
  color: #9ACBD0;
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

/* Transition for theme switching */
.dark-transition {
  transition: background-color 0.3s ease, color 0.3s ease, border-color 0.3s ease;
}
</style> 