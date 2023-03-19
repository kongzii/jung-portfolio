<script setup lang="ts">

</script>

<template>
    <div>
        <!-- <img></img> -->
    </div>
</template>

<script lang="ts">
import { getRandomFromArray, randomIntFromInterval } from "@/model/tools";

export default {
    data() {
        return {
            ninjas: [
                "ninja1.png",
                "ninja2.png",
                "ninja3.png",
                // "ninja4.png",
                "ninja5.png",
                "ninja6.png",
            ],
        }
    },
    mounted() {

    },
}

</script>


<style >
@import '../assets/main.css';
</style>
