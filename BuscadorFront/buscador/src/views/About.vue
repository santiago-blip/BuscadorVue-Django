<template>
<div class="about">
    <div class="container-fluid">
        <table class="table table-striped">
            <thead>
                <tr>
                    <th scope="col">ID</th>
                    <th scope="col">PALABRA</th>
                    <th scope="col">BÚSQUEDAS TOTALES</th>
                    <th scope="col">ÚLTIMOS RESULTADOS</th>
                    <th scope="col">PRIMER BÚSQUEDA</th>
                    <th scope="col">ÚLTIMA BÚSQUEDA</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="item in listado" :key="item.id">
                    <td>{{item.id}}</td>
                    <td>{{item.palabra}}</td>
                    <td>{{item.busquedas_totales}}</td>
                    <td>{{item.ultimos_resultados}}</td>
                    <td>{{item.primer_busqueda}}</td>
                    <td>{{item.ultima_busqueda}}</td>
                </tr>
            </tbody>
            <tfoot>
                <tr>
                    <td colspan="6">El total de palabras más buscadas es: {{listado.length}}</td>
                </tr>
            </tfoot>
        </table>
    </div>
</div>
</template>

<script>
import axios from "axios";
export default {
    name: 'About',
    data() {
        return {
            listado: []
        }
    },
    mounted() {
        this.cargarData()
    },
    methods: {
        cargarData() {
            axios.get('http://localhost:8000/reportes/').then((response) => {
                console.log(response.data)
                this.listado = response.data
            }).catch((error) => {
                console.log(error)
            })
        }
    }
}
</script>

<style src="@/assets/css/reportes.css"></style>
