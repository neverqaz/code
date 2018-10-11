<template><!--template只能有一个外部的节点<div> -->
 <div id="app">
     <div id="cover"></div>
 </div>
   
</template>
<script>
export default {
    data(){
        return{
            text:'hello,word'
        }
    },
    // render(){//template中的html转换成js
    // createElement()

    // }
}
</script>
<style lang="stylus" scoped>
<!-- scoped 表示只在该vue组件里使用-->
#app
  position absolute
  left 0
  right 0
  top 0
  bottom 0

#cover
  position absolute
  left 0
  top 0
  right 0
  bottom 0
  background-color #999
  opacity .9
  z-index -1

</style>
