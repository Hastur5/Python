Voy a partir de entre las similitudes y diferencias en Python con JS

**Variables**

JS: let fili = "perro";
PY: fili = "perro"

**array**

JS: perros = ["skip", "fili", "volcán"];
PY: perros = ["skip", "fili", "volcán"]

**objeto**

let perro = {"fili": "tonto"};
PY: perro = {"fili: "tonto"}

**IF**
JS:
    if (condicion) {
        // hacer algo
    } else if (otra_condicion) {
        // hacer algo
    } else {
        // hacer algo
    }
PY:
    if condicion:
    pass
    elif otra_condicion:
        pass
    else:
        pass

**Funciones**
JS: function funcion(argumento) {
        return argumento + 1;
    }
PY: def funcion(argumento):
    return argumento + 1

**Bucles**

1. Bucle for:
py: 

    for i in range(5):
        print(i)

    frutas = ['manzana', 'plátano', 'cereza']
    for fruta in frutas:
        print(fruta)

js: 

    for (let i = 0; i < 5; i++) {
        console.log(i);
    }

    let frutas = ['manzana', 'plátano', 'cereza'];
    for (let i = 0; i < frutas.length; i++) {
        console.log(frutas[i]);
    }

2. Bucle for...of (para iterar sobre valores):
Py:

    frutas = ['manzana', 'plátano', 'cereza']
    for fruta in frutas:
        print(fruta)

Js:

    let frutas = ['manzana', 'plátano', 'cereza'];
    for (let fruta of frutas) {
        console.log(fruta);
    }

3. Bucle for...in (para iterar sobre claves/índices):
Py (en diccionarios):

    diccionario = {'a': 1, 'b': 2, 'c': 3}
    for clave in diccionario:
        print(clave, diccionario[clave])

Js (en objetos):

    let objeto = {a: 1, b: 2, c: 3};
    for (let clave in objeto) {
        console.log(clave, objeto[clave]);
    }

4. Bucle while:
Py:

    contador = 0
    while contador < 5:
        print(contador)
        contador += 1

Js:

    let contador = 0;
    while (contador < 5) {
        console.log(contador);
        contador++;
    }
