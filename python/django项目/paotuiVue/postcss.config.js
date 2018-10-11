const autoprefixer=require('autoprefixer')
//postcss是将编译完成之后的静态文件进行优化css代码
module.exports={
    plugins:[
        autoprefixer()//需要加css前缀的属性（没有被正式应用的css文件）
    ]
}