<template>
  <section class="CarouselWithButtons">

    <button @click="previous"><md-icon>navigate_before</md-icon></button>
    <carousel :cell="cell" :cells="cells" />
    <button @click="next"><md-icon>navigate_next</md-icon></button>

  </section>
</template>

<script>
import Carousel from '@/components/Home/Carousel/Carousel.vue';

import sanaclis from '@/assets/sanaclis.jpg';

export default {
  name: 'CarouselWithButtons',


  data () {
    return {
      cell: 1,
      cells: [
				{
					image: sanaclis,
					url: '#',
					title: 'Bla',
					subtitle: 'subtitle',
					text: 'text',
				},
				{
					image: 'https://www.sikovnamamina.sk/wp-content/uploads/2016/04/anthus_spinoletta-0822_r.jpg',
					url: '#',
					title: 'Bla',
					subtitle: 'subtitle',
					text: 'text',
				},
				{
					image: 'https://www.sikovnamamina.sk/wp-content/uploads/2016/04/anthus_spinoletta-0822_r.jpg',
					url: '#',
					title: 'Bla',
					subtitle: 'subtitle',
					text: 'text',
				},
				{
					image: 'https://www.sikovnamamina.sk/wp-content/uploads/2016/04/anthus_spinoletta-0822_r.jpg',
					url: '#',
					title: 'Bla',
					subtitle: 'subtitle',
					text: 'text',
				},
				{
					image: 'https://www.sikovnamamina.sk/wp-content/uploads/2016/04/anthus_spinoletta-0822_r.jpg',
					url: '#',
					title: 'Bla',
					subtitle: 'subtitle',
					text: 'text',
				},
				{
					image: 'https://www.sikovnamamina.sk/wp-content/uploads/2016/04/anthus_spinoletta-0822_r.jpg',
					url: '#',
					title: 'Bla',
					subtitle: 'subtitle',
					text: 'text',
				},
				{
					image: 'https://www.sikovnamamina.sk/wp-content/uploads/2016/04/anthus_spinoletta-0822_r.jpg',
					url: '#',
					title: 'Bla',
					subtitle: 'subtitle',
					text: 'text',
				},
				{
					image: 'https://www.sikovnamamina.sk/wp-content/uploads/2016/04/anthus_spinoletta-0822_r.jpg',
					url: '#',
					title: 'Bla',
					subtitle: 'subtitle',
					text: 'text',
				},
				{
					image: 'https://www.sikovnamamina.sk/wp-content/uploads/2016/04/anthus_spinoletta-0822_r.jpg',
					url: '#',
					title: 'Bla',
					subtitle: 'subtitle',
					text: 'text',
				},
			],
    }
  },

  mounted() {

  },

  methods: {
    next() {
			this.cell += 1;
    },
    previous() {  
			this.cell -= 1;
    },
  },

  components: {
    Carousel,
  },

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="less" scoped>

.CarouselWithButtons {
  width: 100%;

  display: flex;
  flex-direction: row;
  justify-content: space-between;

  button {
    background: transparent;
    border: 1px solid transparent;
    cursor: pointer;
    z-index: 99;

    i {
      font-size: 60px !important;
    }
  }

}

</style>
