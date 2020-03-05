import Vue from 'vue'
import App from './App.vue'

Vue.config.productionTip = false

console.log('hello')

function bar() {}

const baz = 'aflskdjsd' + 2

baz * baz

new Vue({
	render: h => h(App),
}).$mount('#app')
