
const VueLoaderPlugin = require('vue-loader/lib/plugin')//vue-loader加载过来
const path = require('path')//加载一工程绝对路径
const HTMLPlugin=require('html-webpack-plugin')//引入html-webpack-plugin插件
const webpack=require('webpack')
const isDev = process.env.NODE_ENV ==='development'//我们所设置的package.json中的变量都是在process.env里
//静态文件的加载和把vue文件进行打包成能在浏览器中运行的代码
const config={
    target:'web',//webpack-dev-server编译目标是web
    mode: 'none',
    
    entry:path.join(__dirname,'src/index.js'),//所在目录下的地址
    output:{
        filename : 'bundle.js',
        path:path.join(__dirname,'dist')
    },
    module:{
          rules:[
              {
               test: /\.vue$/,//正则表达式中的‘.’需要转义
               loader:'vue-loader'
            },
            {
                test:/\.jsx/,
                loader: 'babel-loader'
            },
            {
                test:/\.css$/,
                use:[
                    'style-loader',//读取之后写到新文件还是其他
                    'css-loader'//读取出css文件
                ]
            },
            {
                test:/\.styl$/,//读取css预处理文件工具的css
                use:[
                    'style-loader',
                    'css-loader',
                    {
                        loader:'postcss-loader',
                        options:{
                            sourceMap:true,
                        }
                    },
                    'stylus-loader'//该解析会生成SourceMap
                ]
            },
            {
                test:/\.(gif|jpg|jpeg|png|svg)/, //加载图片
                use:[
                    {
                    loader:'url-loader',//url-loader依赖于file-loader
                    options:{//指定方式给url-loader进行处理
                        limit:1024,//把一些小于1024的图片代码经过url-loader编码
                        name:'[name].[ext]'//进来时的名字与出去时的名字一样[ext]文件扩展名


                    }
                }
            ]
            }

             
        ]

    },
    plugins:[//配置webpack 插件的地方
        new webpack.DefinePlugin({//process.env.NODE_ENV =='development'类似
            'process.env':{
                NODE_ENV:isDev ? '"development"':'"production"'//如果是development环境 则不变，否则传入production环境
            }
        }),
        new HTMLPlugin(),
        new VueLoaderPlugin(),
        
    ]
    
}
if (isDev){
    config.devtool='#cheap-module-eval-source-map'//在浏览器中完整映射代码好调试工具
    config.devServer ={
        port:'8000',
        host:'0.0.0.0',
        overlay:{

            errors:true,//有错误可以直接显示在网页上
            
        },
        // historyFallback:{//没有路由的地址都全部映射到index.html去

        // }
        //open:true//启动之后自动打开浏览器
        hot:true//只会重新加载当前修改的组件，而不会加载整个页面
    }
    config.plugins.push(//在config中plugins添加插件
        new webpack.HotModuleReplacementPlugin(),//不刷新页面
        new webpack.NoEmitOnErrorsPlugin()//不需要的信息展示的问题
    )

}
module.exports=config