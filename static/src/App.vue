<template>
  <div class="container">
    <form class="mt-2 mb-0">
      <div class="form-group">
        <input class="form-control" type="search" @input="debouncedSearch" v-model="query" placeholder="Entrez votre recherche. Entreprises, associations..." />
      </div>
    </form>
    <div class="text-center mb-2">
      <small v-if="datasets.length === 0 && !loading" >Pas de résultats</small>
      <small v-if="loading">Chargement...</small>
    </div>
    <div class="row row-cols-1 row-cols-md-2">
      <div v-for="dataset in datasets" v-bind:key="dataset._id" class="col mb-4">
        <div class="card h-100">
          <div class="card-body">
            <h5 class="card-title">{{ dataset.title }}</h5>
            <p class="card-text">{{ dataset.description }}</p>
          </div>
          <div class="card-footer">{{ dataset.organization }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Vue from 'vue'
import debounce from 'lodash.debounce'

export default Vue.extend({
  data() {
    return {
      query: '',
      datasets: [],
      loading: false
    }
  },
  mounted () {
    const urlparams = new URLSearchParams(window.location.search)
    const q = urlparams.get('q')
    if (q) {
      this.query = q
      this.search()
    }
  },
  methods: {
    search () {
      if (this.query === '') return this.datasets = []
      if (this.query.length < 4) return
      this.loading = true
      this.$http.get(`/api?q=${this.query}`).then((res) => {
        this.datasets = res.data.data
        this.loading = false
      })
    },
    debouncedSearch: debounce(function () {
      this.search()
      window.history.pushState({}, '', `?q=${this.query}`)
    }, 250)
  }
})
</script>
