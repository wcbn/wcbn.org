const webpack = require("webpack");
const path = require("path");

module.exports = {
  entry: {
    index: "./static/js/index.js",
    styles: "./static/css/application.css",
    stream: "./static/svelte/index.js"
  },
  output: {
    path: path.resolve(__dirname + "/static/", "dist"),
    filename: "[name].bundle.js",
    publicPath: "/assets/",
  },
  module: {
    rules: [
      {
        test: /\.js/,
        exclude: /node_modules/,
        loader: "babel-loader",
      },
      {
        test: /\.(png|gif|jpe?g|svg|ico|webp)$/i,
        loader: "url-loader?limit=100000",
      },
      {
				test: /\.svelte$/,
				use: {
					loader: 'svelte-loader',
					options: {
						emitCss: false,
						hotReload: false
					}
				}
			},
    ],
  },
  resolve: {
    extensions: ['.mjs', '.js', '.svelte', ".css"],
    mainFields: ['svelte', 'browser', 'module', 'main'],
    alias: {
			svelte: path.resolve('node_modules', 'svelte')
		},
  },
};
