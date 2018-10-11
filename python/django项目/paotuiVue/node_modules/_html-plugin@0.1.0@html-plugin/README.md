# HTML Plugin

[Here is the plugin](//github.com/jantimon/html-webpack-plugin) mentioned in the [offcial webpack guide](//webpack.js.org/guides/output-management/#setting-up-htmlwebpackplugin).

[![build status](https://travis-ci.org/dk00/html-plugin.svg)](//travis-ci.org/dk00/html-plugin)
[![coverage](https://codecov.io/gh/dk00/html-plugin/branch/master/graph/badge.svg)](//codecov.io/gh/dk00/html-plugin)
[![npm](https://img.shields.io/npm/v/html-plugin.svg)](//npm.im/html-plugin)
[![dependencies](https://david-dm.org/dk00/html-plugin/status.svg)](//david-dm.org/dk00/html-plugin)

This plugin aims to create `index.html` for PWAs, with good default template built-in, and let you customize with simple configuration.

You can also provide your own templates in the same way you compose apps - JSX and React components.

## Installation

Install the plugin with npm:

`$ npm i -D html-plugin vhtml`

# Usage

Add the plugin to webpack config:

```diff
+ const HtmlPlugin = require('html-plugin')
  module.exports = {
    entry: 'index.js',
    output: {
      path: __dirname + '/dist',
      filename: 'bundle.js'
    },
+   plugins: [
+     new HtmlPlugin({
+       title: 'My App'
+     })
+   ]
  }
```

This will generate `dist/index.html`:

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <title>My App</title>
  <meta charset="utf-8" />
  <meta name="mobile-web-app-capable" content="yes" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="theme-color" content="#000" />
  <meta name="apple-mobile-web-app-capable" content="yes" />
  <meta name="apple-mobile-web-app-status-bar-style" content="black" />
  <link rel="manifest" href="/manifest.json" />
  <link rel="shortcut icon" href="/favicon.png" />
</head>

<body>
  <div id="root"></div>
  <script src="bundle.js"></script>
</body>

</html>
```

## Options

- filename
- title / name
- lang
- themeColor
- manifest
- favicon
