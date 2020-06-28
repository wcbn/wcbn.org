const webpack = require("webpack");
const path = require("path");

module.exports = {
  entry: ["./static/js/index.jsx", "./static/css/application.css"],
  output: {
    path: path.resolve(__dirname + "/static/", "dist"),
    filename: "bundle.js",
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
