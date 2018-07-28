<template>
  <section class="IEWarning" v-if="isIE">
    <article class="">
      Unfortunately IE doesn't support transform: preserve-3d property yet. <br /><br />
      Please check at supported browsers like <b>Chrome</b> or <b>Firefox</b>, thanks.
      <br />
      <br />
      <b>Or you can at least download PDF version of my CV</b> <a :href="cvLink" class="download">here</a>.
    </article>
  </section>
</template>

<script>
import detectIe from 'detectIe';

export default {
  name: 'IEWarning',

  data () {
    return {
      isIE: false,
      cvLink: 'http://cv.jung.ninja/files/jung_cv_eng.pdf',
    }
  },

  mounted() {
    this.isIE = detectIe();
  },

  methods: {

  },

  components: {

  },

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="less" scoped>

.IEWarning {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: fade(black, 50%);
  z-index: 999;

  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

  article {
    border-radius: 10px;
    padding: 20px;
    background: white;
    text-align: justify;
  }
}

</style>
