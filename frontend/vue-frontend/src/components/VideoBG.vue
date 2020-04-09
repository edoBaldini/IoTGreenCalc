<template>
<div id="home-top-video" class="VideoBg">
<video autoplay playsinline loop :muted="muted" ref="video">
   <source class="VideoBg_color" :src='require("@/assets/mp4/bg.mp4")' type='video/mp4'>
</video>
</div>
</template>

<script>
export default {
  name: 'VideoBG',
  props: {
    sources: {
      type: Array,
      required: false,
    },
    img: {
      type: String,
    },
    muted: {
      type: Boolean,
      default: true,
    },
  },
  data() {
    return {
      videoRatio: null,
    };
  },
  mounted() {
    this.setImageUrl();
    this.setContainerHeight();
    if (this.videoCanPlay()) {
      this.$refs.video.oncanplay = () => {
        if (!this.$refs.video) return;
        this.videoRatio = this.$refs.video.videoWidth / this.$refs.video.videoHeight;
        this.setVideoSize();
        this.$refs.video.style.visibility = 'visible';
      };
    }
    window.addEventListener('resize', this.resize);
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.resize);
  },
  methods: {
    resize() {
      this.setContainerHeight();
      if (this.videoCanPlay()) {
        this.setVideoSize();
      }
    },
    videoCanPlay() {
      return !!this.$refs.video.canPlayType;
    },
    setImageUrl() {
      if (this.img) {
        this.$el.style.backgroundImage = `url(${this.img})`;
      }
    },
    setContainerHeight() {
      this.$el.style.height = `${window.innerHeight}px`;
    },
    setVideoSize() {
      let width;
      let height;
      const containerRatio = this.$el.offsetWidth / this.$el.offsetHeight;
      if (containerRatio > this.videoRatio) {
        width = this.$el.offsetWidth;
      } else {
        height = this.$el.offsetHeight;
      }
      this.$refs.video.style.width = width ? `${width}px` : 'auto';
      this.$refs.video.style.height = height ? `${height}px` : 'auto';
    },
    getMediaType(src) {
      return `video/, ${src.split('.').pop()}`;
    },
  },
};
</script>

<style>

  /* .VideoBg {
    position: relative;
    background-size: cover;
    background-position: center;
    overflow: hidden;
  }
  .VideoBg video {
    position: absolute;
    top: 50%;
    left: 50%;
    visibility: hidden;
    transform: translate(-50%, -50%);
  }
  .VideoBg__content {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
  }

  .VideoBg_color {
    background-color: black !important;
  } */

  .VideoBg video {
    position: fixed;
    top: 50%;
    left: 50%;
    min-width: 100%;
    min-height: 100%;
    width: auto;
    height: auto;
    z-index: -100;
    transform: translateX(-50%) translateY(-50%);
    background-size: cover;
    transition: 1s opacity;
  }
  .font-set{
    font-family: Elianto;
    font-size: 60px;
    text-align: center;
    color:#eaffef;
  }
  .b-card-header-color{
    background-color:rgba(126, 211, 134, 0);
    color:#eaffef;
  }
  .b-card-text-color{
    background-color: rgba(28,55,101,.96);
    color:#eaffef;
  }

#home-top-video:before {
  content:"";
  position: fixed;
  top:0;
  right:0;
  left:0;
  bottom:0;
  z-index:1;
  background: rgba(0, 46, 102, .8);
}

#home-top-video {
  left: 0%;
  top: 0%;
  height: 100vh;
  width: 100%;
  overflow: hidden;
  position: absolute;
  z-index: -1;
}
</style>
