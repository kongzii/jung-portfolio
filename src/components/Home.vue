<template>
  <section class="home">

    <i-e-warning />

    <div class="about">
      <h1>Hi, I'm Peter.</h1>
      <h2>A full stack developer from Prague.</h2>
      <p>Le Lorem Ipsum est simplement du faux texte employé dans la composition et la mise en page avant impression. Le Lorem Ipsum est le faux texte standard de l'imprimerie depuis les années 1500, quand un imprimeur anonyme assembla ensemble des morceaux de texte pour réaliser un livre spécimen de polices de texte. Il n'a pas fait que survivre cinq siècles, mais s'est aussi adapté à la bureautique informatique, sans que son contenu n'en soit modifié. Il a été popularisé dans les années 1960 grâce à la vente de feuilles Letraset contenant des passages du Lorem Ipsum, et, plus récemment, par son inclusion dans des applications de mise en page de texte, comme Aldus PageMaker.</p>
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
