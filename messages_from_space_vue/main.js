import './style.css'

document.querySelector('#app').innerHTML = `
  <h1>Клиент</h1>
  <p>Здесь будут выводиться сообщения</p>

`
const ComponentsApp = {
  data() {
    return {
      groceryList: [
        { id: 0, text: 'Vegetables' },
        { id: 1, text: 'Cheese' },
        { id: 2, text: 'Whatever else humans are supposed to eat' }
      ]
    }
  }
}

const app = Vue.createApp(ComponentsApp)

app.component('todo-item', {
  props: ['todo', 'text'],
  template: `<li>{{ text }} </li>`
})

app.mount('#components-app')

const counter = {
  data() {
    return {
      counter: 0
    }

  }
}

Vue.createApp(counter).mount('#counter')
