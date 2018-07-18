<template>
  <section class="scene">
    <div class="card" :style="{transform: `rotateX(${flipTimes * 180}deg)`}" @click="flip">
      <div class="face" face="front" ref="front" :style="{'background-image': `url(${bgImage})`}">
        <div class="normal" v-if="!sprite">
          <h2>{{title}}</h2>
          <h3>{{subtitle}}</h3>
          <p>{{text}}</p>
        </div>

        <div class="sprite" v-else :style="imgStyle.front"></div>
      </div>

      <div class="face" face="back" ref="back">
        <div class="normal" v-if="!sprite">
          <h2>Title Back</h2>
          <h3>Subtitle Back Back Back Back Back</h3>
          <p>Text Back</p>
        </div>

        <div class="sprite" v-else :style="imgStyle.back"></div>
      </div>
    </div>
  </section>
</template>

<script>
import html2canvas from 'html2canvas';

export default {
  name: 'FlipCard',

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
    imgStyle: {
      type: Object,
      default: () => {},
    },
    customFlipCount: {
      type: Number,
      default: -1,
    },
    sprite: {
      type: Boolean,
      default: false,
    },
  },

  data () {
    return {
      localFlipCount: 0,
    }
  },

  computed: {
    flipTimes() {

      if (this.customFlipCount >= 0)
        return this.customFlipCount;
      
      else
        return this.localFlipCount;

    },
  },

  created() {

  },

  mounted() {

  },

  methods: {

    flip() {
      this.localFlipCount += 1;
    },

  },

  components: {

  },

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="less" scoped>

.scene {
  width: 100%;
  height: 100%;
  perspective: 600px;

  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;

  .card {
    width: 100%;
    height: 100%;
    position: relative;
    transition: transform .75s, .3s box-shadow;
    transform-style: preserve-3d;

    &:hover {
      box-shadow: 0 0 30px 1px fade(black, 30%);
    }

    .face {
      position: absolute;
      height: 100%;
      width: 100%;
      backface-visibility: hidden;
      overflow: hidden;
      background-position: center center;
      background-size: cover;

      .normal {
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        width: 100%;
        height: 100%;
        padding: 20px;
      }

      &[face="front"] {
        background-color: transparent;
      }

      &[face="back"] {
        background-color: blue;
        transform: rotateX( 180deg );

        .sprite {
          transform: scaleY(-1);
        }
      }

      h2,
      h3,
      p {
        z-index: 2;
        margin-top: 0;
      }

      p {
        margin-top: auto;
      }

      .sprite {
        height: 100%;
      }

    }
  }
}

</style>
