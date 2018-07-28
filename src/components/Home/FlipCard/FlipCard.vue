<template>
  <section class="scene">
    <div class="card" :style="{transform: `rotateX(${flipTimes * 180}deg)`}" @click="flip">
      <div class="face" face="front" ref="front" :style="{'background-image': `url(${bgImage})`}">
        <div class="normal" v-if="!sprite">
          <div class="title">
            <h2 v-if="title">{{title}}</h2>
            <h3 v-if="subtitle">{{subtitle}}</h3>
          </div>

          <p>{{text}}</p>
        </div>

        <div class="sprite" v-else :style="imgStyle.front"></div>
      </div>

      <div class="face" face="back" ref="back" :style="{'background-image': `url(${bgImageBack})`}">
        <div class="normal" v-if="!sprite">
          <div class="title back">
            <h2 v-if="backTitle">{{backTitle}}</h2>
            <h3 v-if="backSubtitle">{{backSubtitle}}</h3>
          </div>
          
          <!-- <p>Text Back</p> -->
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
    bgImageBack: {
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

        .title {
          background: fade(white, 90%);
          padding: 20px;
          width: 30%;
          border-bottom-right-radius: 20px;
          
          @media (max-width: 700px) {
            width: 40%;
          }

          @media (max-width: 600px) {
            width: 50%;
          }

          &.back {

          }
        }
      }

      &[face="front"] {
        background-color: transparent;
      }

      &[face="back"] {
        background-color: transparent;
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

      h2 {
        margin-bottom: 0;
        text-align: center;
      }

      p {
        margin-top: auto;
      }

      h3 {
        margin-bottom: 0;
        margin-top: 10px;
        text-align: center;
      }

      .sprite {
        height: 100%;
      }

    }
  }
}

</style>
