//解决跨域
module.exports = {
    devServer: {
//同webpack,设置服务器代理
        proxy: {
            '/api': {
                target: `http://127.0.0.1:8000/api`,
                changeOrigin: true,
                pathRewrite: {
                    '^/api': ''
                }
            }
        }
    }
};