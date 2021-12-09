<template>
<div class="hello">
    <h1>{{msg}}</h1>
    <div class="DivBuscador-container">
        <form @submit.prevent="buscar" class="formBuscador">
            <div class="DivBuscador">
                <input @keypress="input" v-model="buscador" class="InputBuscador" />
                <label class="lblBuscador">Buscar</label>
            </div>
        </form>
    </div>
    <div class="listadoDivContainer" v-if="listado.length > 0">
        <div class="listadoDiv" v-for="item in listado" :key="item.title">
            <h1>{{item.title}}</h1>
            <p>{{item.pageid}} </p>
            <p v-html="item.snippet"></p>
        </div>
    </div>

    <div v-else>
        <h1>No hay búsquedas </h1>
    </div>

</div>
</template>

<script>
import axios from "axios";
export default {
    name: 'HelloWorld',
    props: {
        msg: String
    },
    data() {
        return {
            buscador: '',
            listado: [],
            lista_palabras: [],
            lista_existente: []
        }
    },
    mounted() {
        axios.get("http://localhost:8000/reportes/").then((response) => {

            this.lista_existente = response.data

        }).catch((error) => {
            console.log(error)
        })
    },
    methods: {
        agregarPalabra: function (val) {
            axios.post('http://localhost:8000/reportes/', val).then((response) => {
                console.log(response.data)
            }).catch((error) => {
                console.log(error)
            })
        },
        buscar: function () {
            if (this.buscador.length >= 1) {
                var url = "https://en.wikipedia.org/w/api.php?";
                var params = "action=query" +
                    "&list=search" +
                    "&srsearch=" + this.buscador +
                    "&utf8=" +
                    "&format=json" +
                    "&origin=*";
                var path = url + params;
                console.log(path)
                axios.get(path).then((response) => {
                        console.log(response.data.query.search)
                        this.listado = response.data.query.search
                        if (this.lista_palabras.length > 0) {
                            var bandera = false;
                            for (var i = 0; i < this.lista_palabras.length; i++) {
                                //console.log(" COMPROBAR ")
                                //console.log(this.lista_palabras[i].palabra == this.buscador)
                                //console.log("i: " + this.lista_palabras[i].palabra)
                                //console.log("buscador: " + this.buscador)
                                if (this.lista_palabras[i].palabra == this.buscador) {
                                    this.lista_palabras[i].cantidad = this.lista_palabras[i].cantidad + 1;

                                    if (this.lista_palabras[i].cantidad >= 5) {
                                        this.agregarPalabra({
                                            "palabra": this.lista_palabras[i].palabra,
                                            "busquedas_totales": this.lista_palabras[i].cantidad,
                                            "ultimos_resultados": response.data.query.search.length
                                        })

                                    }

                                    bandera = true;
                                    break;
                                }
                            }
                            if (!bandera) {
                                this.lista_palabras.push({
                                    "palabra": this.buscador,
                                    "cantidad": 1
                                })

                            }

                        } else {
                            this.lista_palabras.push({
                                "palabra": this.buscador,
                                "cantidad": 1
                            })

                        }

                        if (this.lista_palabras.length > 0 && this.lista_existente.length > 0) {
                            console.log("APLICA")
                            this.lista_existente.forEach(e => {
                                console.log("e :" + e.palabra)
                                for (var i = 0; i < this.lista_palabras.length; i++) {
                                    if (this.lista_palabras[i].palabra.toLowerCase() == e.palabra.toLowerCase()) {
                                        console.log("La palabra R: " + this.lista_palabras[i].palabra + " se parece a la palabra e: " + e.palabra)
                                        this.agregarPalabra({
                                            "palabra": this.lista_palabras[i].palabra,
                                            "busquedas_totales": this.lista_palabras[i].cantidad,
                                            "ultimos_resultados": response.data.query.search.length
                                        })
                                    }
                                }

                            })

                        }
                        //console.log("Tamaño de lista de palabras: " + this.lista_palabras.length + " Palabra agregada : " + this.buscador)
                        //console.log("this.lista_palabras: ")
                        //console.log(this.lista_palabras)
                        //console.log(this.listado.length)
                    })
                    .catch((error) => {
                        console.log(error);
                    })
            } else {
                this.listado = []
            }

        },
        input: function () {
            var input = document.getElementsByClassName("InputBuscador");
            if (input != null) {
                for (var i = 0; i < input.length; i++) {
                    input[i].addEventListener("keyup", function () {
                        if (this.value.length >= 1) {
                            this.nextElementSibling.classList.add("fijar");
                        } else {
                            this.nextElementSibling.classList.remove("fijar");
                        }
                    })
                }
            }
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->

<style src="@/assets/css/buscador.css"></style>
