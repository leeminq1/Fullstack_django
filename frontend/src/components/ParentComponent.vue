<template>
    <div>
        <h1>Parent Component</h1>
        <ChildComponent v-model:db="selectedDb" v-model:resource="selectedResource" @update-query="updateQuery" />
        <DetailCompoent />
    </div>
</template>

<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import ChildComponent from './ChildComponent.vue';
import DetailCompoent from './DetailCompoent.vue';

export default {
    components: { ChildComponent, DetailCompoent },
    setup() {
        const router = useRouter();
        const selectedDb = ref('dev');
        const selectedResource = ref('total');

        const updateQuery = (db, resource) => {

            console.log("### Parent", db.value, resource.value)

            // router로 주소를 넣어서 다름 컴포넌트에서는 이 값을 받아서 url에서 값을 받아서 사용함
            // 하위 컴포넌트에서는 watch로 route.query를 감지함
            router.push({
                query: {
                    db: db,
                    resource: resource,
                },
            });
        };

        return {
            selectedDb,
            selectedResource,
            updateQuery,
        };
    },
};
</script>