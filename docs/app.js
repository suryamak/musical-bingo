const app = Vue.createApp({
    data() {
        return {
            items: null
        }
    },
    mounted() {
        axios.get('https://musical-bingo.herokuapp.com/generate-board')
        .then(response => (this.items = response.data))
        // .then(response => (console.log(response.data)))
    }
})

app.mount('#bingo-board')