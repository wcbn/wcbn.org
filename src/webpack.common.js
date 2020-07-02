const webpack = require("webpack");
const path = require("path");

module.exports = {
  entry: {
    index: "./static/js/index.jsx",
    player: "./static/js/player.jsx",
    styles: "./static/css/application.css",
  },
  output: {
    path: path.resolve(__dirname + "/static/", "dist"),
    filename: "[name].bundle.js",
    publicPath: "/assets/",
  },
  module: {
    rules: [
      {
        test: /\.jsx?/,
        exclude: /node_modules/,
        loader: "babel-loader",
      },
      {
        test: /\.(png|gif|jpe?g|svg|ico|webp)$/i,
        loader: "url-loader?limit=100000",
      },
    ],
  },
  resolve: {
    extensions: [".js", ".jsx", ".css"],
    alias: {},
  },
};
