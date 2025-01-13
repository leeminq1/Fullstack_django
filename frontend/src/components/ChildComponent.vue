<template>
    <div>
        <select v-model="localSelectedDb">
            <option value="dev">Dev</option>
            <option value="prod">Prod</option>
        </select>

        <select v-model="localSelectedResource">
            <option value="total">Total</option>
            <option value="partial">Partial</option>
        </select>

        <button @click="emitUpdate">Update Query</button>
    </div>
</template>

<script>
import { ref, defineComponent } from 'vue';

export default defineComponent({
    name: "ChildComponent",
    props: {
        selectedDb: {
            type: String,
            required: true,
        },
        selectedResource: {
            type: String,
            required: true,
        },
    },
    emits: ['update-query'],
    setup(props, { emit }) {
        const localSelectedDb = ref(props.selectedDb);
        const localSelectedResource = ref(props.selectedResource);

        // watch(
        //     () => props.selectedDb,
        //     (newValue) => {
        //         localSelectedDb.value = newValue;
        //     }
        // );

        // watch(
        //     () => props.selectedResource,
        //     (newValue) => {
        //         localSelectedResource.value = newValue;
        //     }
        // );

        const emitUpdate = () => {
            emit('update-query', localSelectedDb.value, localSelectedResource.value);
        };

        return {
            localSelectedDb,
            localSelectedResource,
            emitUpdate,
        };
    },
});
</script>