<template>
  <section class="scene" ref="scene">
    <div class="carousel" ref="carousel" :style="{transform: `translateZ(${-sceneRadius}px) rotateY(${angle}deg)`}">

			<div 
				class="cell"
				:class="{current: index == (currentCell - 1), hover: !isRotating}"
				v-for="(item, index) in cells"
				:key="index"
				:style="{transform: `rotateY(${theta * (index)}deg) translateZ(${cellRadius}px)`}"
			>
				<many-flip-cards @rotating="rotating" :bgImage="item.image" :bgImageBack="item.backImage" :title="item.title" :subtitle="item.subtitle" :text="item.text" />
			</div>

    </div>
			<p class="pagination"><span>{{currentCell}}</span> z <span>{{cellCount}}</span></p>

  </section>
</template>

<script>
import ManyFlipCards from '@/components/Home/FlipCard/ManyFlipCards.vue';

export default {
	name: 'Carousel',
	
	props: {
		cell: {
			type: Number,
			default: 1,
		},
		cells: {
			type: Array,
		},
	},

  data () {
    return {
			carouselHeight: 0,
			carouselWidth: 0,

			windowHeight: 0,
			windowWidth: 0,

			cellRadius: 1,
			isRotating: false,
    }
	},
	
	computed: {

		currentCell() {
			return this.cell - this.round * this.cellCount;
		},

		sceneRadius() {
			return Math.round( (this.carouselWidth / 2) / Math.tan( Math.PI / this.cellCount) );
		},

		theta() {
			return 360 / this.cellCount;
		},

		angle() {
			return this.theta * (this.cell - 1) * -1;
		},

		cellCount() {
			return this.cells.length;
		},

		round() {
			return Math.floor((this.cell - 1) / (this.cellCount));
		}

	},

	created() {
	
	},

  mounted() {
		this.$nextTick(() => {
			this.compCarouselSize();
		});

		window.addEventListener('resize', () => {
			this.windowHeight = window.innerHeight;
			this.windowWidth = window.innerWidth;
		});
  },

  methods: {

		toRadians(deg) {
			return deg * Math.PI / 180;
		},

		rotating(isRotating) {
			console.log(isRotating);
			this.isRotating = isRotating;
		},

		compCarouselSize() {
			this.$nextTick(() => {
				this.carouselHeight = this.$refs.carousel.offsetHeight;
				this.carouselWidth = this.$refs.carousel.offsetWidth;
	
				this.cellRadius = (this.$refs.scene.offsetWidth / 2) / Math.tan(this.toRadians(this.theta / 2));
				this.$refs.scene.style.height = `${window.innerHeight / 4 * 2}px`;
			});
		},
	},
	
	watch: {

		windowHeight(newHeight, oldHeight) {
			this.compCarouselSize();
		},

		windowWidth(newWidth, oldWidth) {
			this.compCarouselSize();
		},
		
	},

  components: {
		ManyFlipCards,
  },

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="less" scoped>

.scene {
	width: 100%;
	position: relative;
	perspective: 1000px;
	// height: 500px;
	// border: 1px solid black;

	.carousel {
		width: 100%;
		height: 100%;
		position: absolute;
		transform-style: preserve-3d;
		transition: transform 1s;

		.cell {
			position: absolute;
			width: ~"calc(100% - 20px)";
			height: ~"calc(100% - 20px)";
			left: 10px;
			top: 10px;
			pointer-events: none;

			transition: .75s opacity, .3s box-shadow;
			border-radius: 15px;
			overflow: hidden;

			&:not(.current) {

				opacity: .3;

			}

			&.current {

				pointer-events: all;
				cursor: pointer;
				opacity: 1;

				&.hover {
					&:hover {
						box-shadow: 0 0 30px 1px fade(black, 30%);
					}
				}

			}

			img {
				width: 100%;
			}

		}
	}

	.pagination {
			position: absolute;
			bottom: -40px;
			right: 20px;
			font-size: 17px;

			span {
				font-size: 20px;
			}
		}
}

</style>
