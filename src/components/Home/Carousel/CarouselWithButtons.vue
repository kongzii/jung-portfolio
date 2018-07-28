<template>
  <section class="CarouselWithButtons">

    <button @click="previous"><md-icon>navigate_before</md-icon></button>
    <carousel :cell="cell" :cells="cells" />
    <button @click="next"><md-icon>navigate_next</md-icon></button>

  </section>
</template>

<script>
import Carousel from '@/components/Home/Carousel/Carousel.vue';

import ggt from '@/assets/ggt.jpg';
import avon from '@/assets/avon.jpg';
import cosmed from '@/assets/cosmed.jpg';
import etelka from '@/assets/etelka.jpg';
import korpi from '@/assets/korpi.jpg';
import lod from '@/assets/lod.jpg';
import lod2 from '@/assets/lod2.jpg';
import logo from '@/assets/logo.png';
import planetary from '@/assets/planetary.jpg';
import projectstars from '@/assets/projectstars.jpg';
import robot from '@/assets/robot.jpg';
import sanaclis from '@/assets/sanaclis.jpg';

export default {
  name: 'CarouselWithButtons',


  data () {
    return {
      cell: 1,
      cells: [
				{
					image: ggt,
					// backImage: avon,
					title: 'GGT',
					// // subtitle: 'subtitle',
					// text: 'text',
				},
				{
					image: avon,
					// backImage: avon,
					url: 'http://avon.express',
					title: 'AVON',
					// // subtitle: 'subtitle',
					// text: 'text',
				},
				{
					image: cosmed,
					url: 'http://cosmed.sitelab.sk',
					title: 'COSMED',
					// // subtitle: 'subtitle',
					// text: 'text',
				},
				{
					image: sanaclis,
					url: 'http://sanaclis.eu',
					title: 'SANACLIS',
					// // subtitle: 'subtitle',
					// text: 'text',
				},
				{
					image: planetary,
					title: 'Planetary',
					// // subtitle: 'subtitle',
					// text: 'text',
				},
				{
					image: projectstars,
					url: 'http://project-stars.com',
					title: 'Project Stars',
					// // subtitle: 'subtitle',
					// text: 'text',
				},
				{
					image: korpi,
					url: 'https://github.com/kongzii/korpi',
					title: 'Korpi',
					// // subtitle: 'subtitle',
					// text: 'text',
				},
				{
					image: lod,
					backImage: lod2,
					title: '3D loďka',
					// // subtitle: 'subtitle',
					// text: 'text',
				},
				{
					image: robot,
					title: '3D robot',
					// // subtitle: 'subtitle',
					// text: 'text',
				},
				{
					image: etelka,
					title: 'eTelka',
					// // subtitle: 'subtitle',
					// text: 'text',
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
