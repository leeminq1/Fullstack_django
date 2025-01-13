<template>
  <div>
    <h1>detail Compoenet</h1>
  </div>
  <div>
    <p>Database: {{ queryDb }}</p>
    <p>Resource: {{ queryResource }}</p>
  </div>
</template>

<script>
import { ref, watch } from 'vue';
import { useRoute } from 'vue-router';

export default {
  setup() {
    const route = useRoute();
    const queryDb = ref('');
    const queryResource = ref('');

    const fetchApiData = async (db, resource) => {
      const response = await fetch(`/api/data?db=${db}&resource=${resource}`);
      const data = await response.json();
      console.log(data);
    };

    watch(
      () => route.query,
      (newQuery) => {
        queryDb.value = newQuery.db;
        queryResource.value = newQuery.resource;
        fetchApiData(newQuery.db, newQuery.resource);
      },
      { immediate: true }
    );

    return {
      queryDb,
      queryResource,
    };
  },
};
</script>