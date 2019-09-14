module.exports = {
  lintOnSave: false,
  runtimeCompiler: true,
  publicPath: process.env.NODE_ENV === 'production' ?
  '/ppfiles/dist/' :
  '/',
  devServer: {
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:8082',
        ws: true,
        changeOrigin: true,
        pathRewrite: {
          '^/api': ''
        }
      }
    }
  }
}
