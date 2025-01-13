<template>
  <div>
    <ParentComponent></ParentComponent>
  </div>
  <div>
    <h1>Data Details</h1>
    <table>
      <thead>
        <tr>
          <th>Field</th>
          <th>Value</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>ID</td>
          <td>{{ data._id }}</td>
        </tr>
        <tr>
          <td>Date</td>
          <td>{{ formattedDate }}</td>
        </tr>
        <tr>
          <td>Hour</td>
          <td>{{ data.hour }}</td>
        </tr>
        <tr>
          <td>Month</td>
          <td>{{ data.month }}</td>
        </tr>
        <tr>
          <td>Year</td>
          <td>{{ data.year }}</td>
        </tr>
        <tr>
          <td>SMP</td>
          <td>{{ data.smp }}</td>
        </tr>
      </tbody>
    </table>
  </div>

</template>

<script>
import axios from 'axios';
import { ref, onMounted, computed } from 'vue';

import ParentComponent from './components/ParentComponent.vue';

export default {
  components: { ParentComponent },
  setup() {
    const data = ref({});
    const apiUrl = process.env.VUE_APP_API_URL; // .env에서 읽은 API URL

    // 날짜 포맷팅
    const formattedDate = computed(() => {
      if (!data.value.date) return '';
      return new Date(data.value.date).toLocaleString();
    });

    // API 호출
    onMounted(() => {
      axios
        .get(`${apiUrl}/api/data/`)
        .then((response) => {
          data.value = response.data;
        })
        .catch((error) => {
          console.error('There was an error!', error);
        });
    });

    return {
      data,
      formattedDate,
    };
  }
};
</script>

<style>
/* 간단한 스타일 */
table {
  width: 100%;
  border-collapse: collapse;
  margin: 20px 0;
}

table,
th,
td {
  border: 1px solid #ddd;
}

th,
td {
  padding: 10px;
  text-align: left;
}

th {
  background-color: #f4f4f4;
}
</style>