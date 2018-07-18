<template>
  <section class="ManyFlipCards" @click="flip">

   <flip-card 
    v-if="showSingleCart"

    class="flip-card"
    ref="flipCard"
    :customFlipCount="flipCounts[0]"

    :bgImage="bgImage"
    :title="title"
    :subtitle="subtitle"
    :text="text"
   />

   <flip-card 
    v-else
    v-for="(n, index) in dividers"
    :key="index"

    :style="{width: `${flipWidth}px`}"
    :customFlipCount="flipCounts[index]"
    :imgStyle="imgStyles[index]"
    :sprite="true"

   />

  </section>
</template>

<script>
import html2canvas from 'html2canvas';
import FlipCard from '@/components/Home/FlipCard/FlipCard.vue';


export default {
  name: 'ManyFlipCards',

  props: {
    bgImage: {
      type: String,
      default: '',
    },
    title: {
      type: String,
      default: '',
    },
    subtitle: {
      type: String,
      default: '',
    },
    text: {
      type: String,
      default: '',
    },
  },

  data () {
    return {
      delay: 100,
      showSingleCart: true,

      flipCounts: {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
      },

      imgStyles: {
        0: {front: {}, back: {}},
        1: {front: {}, back: {}},
        2: {front: {}, back: {}},
        3: {front: {}, back: {}},
        4: {front: {}, back: {}},
        5: {front: {}, back: {}},
        6: {front: {}, back: {}},
        7: {front: {}, back: {}},
        8: {front: {}, back: {}},
        9: {front: {}, back: {}},
      },

      flipWidth: 0,
      dividers: 1,
    }
  },

  created() {
    this.dividers = this.getRandomInt(4, 10);  
  },

  mounted() {

    let debounce;
    window.addEventListener('resize', () => {

      clearTimeout(debounce);
      debounce = setTimeout(() => {
        this.flipWidth = 0;
        this.showSingleCart = true;
        Object.keys(this.flipCounts).forEach((key, index) => {
          this.flipCounts[key] = 0;
        });
      });
		});
  },

  methods: {

    flip() {

      if (this.flipCounts[0] == 0) 
        this.renderCanvases();

      const rotate = setInterval(() => {
        if (!this.showSingleCart) {
          this.rotateCards();
          clearInterval(rotate);
        }
      }, this.showSingleCart ? 200 : 0);

    },

    renderCanvases() {
      this.renderCanvas(this.$refs.flipCard.$refs.front);
      this.renderCanvas(this.$refs.flipCard.$refs.back);
    },

    rotateCards() {
      this.$emit('rotating', true);

      Object.keys(this.flipCounts).forEach((key, index) => {
        setTimeout(() => {
          this.flipCounts[key] += 1;
        }, this.delay * index);
      });

      setTimeout(() => {
        this.$emit('rotating', false);
      }, this.delay * Object.keys(this.flipCounts).length);
    },

    renderCanvas(element) {
      const face = element.getAttribute('face');
      this.flipWidth = element.offsetWidth / this.dividers;

      html2canvas(element).then((canvas) => {

        const dataURL = canvas.toDataURL("image/png");

        for (let i = 0; i < this.dividers; i++) {
          this.imgStyles[i][face] = {background: `url(${dataURL}) -${i * this.flipWidth}px 0`};
        }

        this.showSingleCart = false;

      });

    },

    getRandomInt(min, max) {
      return Math.floor(Math.random() * (max - min + 1) + min);
    },

  },

  components: {
    FlipCard,
  },

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="less" scoped>

.ManyFlipCards {

  width: 100%;
  height: 100%;

  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;

}

</style>
