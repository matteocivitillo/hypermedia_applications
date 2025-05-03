<template>
  <div>
    <div class="container mx-auto py-3 pl-8">
      <p class="text-sm font-bold text-gray-500">
        <template v-for="(crumb, index) in breadcrumbs" :key="index">
          <template v-if="index > 0"> &gt; </template>
          <a v-if="crumb.url" :href="crumb.url" class="hover:text-primary">{{ crumb.text }}</a>
          <span v-else>{{ crumb.text }}</span>
        </template>
      </p>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    breadcrumbs: {
      type: Array,
      default: () => [
        { text: 'Home', url: '/' },
        { text: 'Category' },
        { text: 'Page' }
      ]
    }
  }
}
</script> 