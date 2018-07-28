<template>
  <section class="home">

    <i-e-warning />

    <div class="about">
      <h1>Ahoj, jsem Peter.</h1> 
      <h2>Full stack vývojář z Prahy.</h2> 
      <p>Níže jsou chronologicky seřazeny mé poslední projekty. Ať už soukromé nebo tímové z práce v M7. Mrknout můžete i na můj <a href="http://github.com/kongzii" target="_blank">github</a>.</p>
      <a class="resume-link" href="http://cv.jung.ninja" target="_blank">životopis</a>
    </div>

    <carousel-with-buttons class="carousel"  />

  </section>
</template>

<script>
import CarouselWithButtons from '@/components/Home/Carousel/CarouselWithButtons.vue';
import IEWarning from '@/components/IEWarning.vue';

export default {
  name: 'Home',

  data () {
    return {
    }
  },

  methods: {

  },

  components: {
    CarouselWithButtons,
    IEWarning,
  },

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="less" scoped>

.home {
  .about {
    position: relative;

    @media (min-width: 1000px) {
      padding: 0 50px;
    }

    h1,
    h2,
    p {
      font-family: monospace;
    }

    h1 {
      font-size: 50px;
      line-height: 50px;
      margin: 0;
    }

    .resume-link {
      font-weight: bold;
      font-size: 15px;
      transition: .25s;
      margin: 0;
      text-transform: uppercase;

      @media (min-width: 650px) {
        position: absolute;
        top: 10%;
        right: 0;
      }

      @media (min-width: 1000px) {
        right: 50px;
      }

      &:hover {
        // color: white;
        // text-shadow: 0 0 5px fade(grey, 50%);
        // text-decoration: none;
      }
    }

    h2 {
      margin-top: 0;
    }

    p {
      text-align: justify;
    }
  }

  .carousel {
    margin-top: 4vh;
  }
}

</style>
