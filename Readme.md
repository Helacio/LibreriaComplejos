# Librería básica de Números Complejos.
Se realizan las siguiente operaciones básicas sobre números complejos.
1. Suma.
2. Producto.
3. Resta.
4. División.
5. Módulo.
6. Conjugado.
7. Conversión entre coordenadas polar y cartesiana.
8. Retornar la fase de un número complejo.

Tenga en cuenta que algunas de las funciones mencionadas depende de la liberia 'math' para realizar operaciones de funciones trigonométricas.

## Libreria:
Todas las entradas de las funciones son de tipo de tupla(s) y los resultados a operaciones son del mismo tipo, adicionalmente considere que las respuestas a tipo flotantes no están aproximadas ni se limitan la cantidad de decimales.

Observe como en el siguiente fragmento de código se emplea la libreria 'math'.

```python
#Pasar de coordenadas cartesianas a polares
def cartopolar(a):
    lnght = (a[0] ** 2 + a[1] ** 2) ** (0.5)
    angle = math.atan2(a[1], a[0])
    return (lnght, angle)
```

1. Suma de Números Complejos.

Esta función suma dos números complejos a y b, donde cada número complejo se representa como una tupla (parte real, parte imaginaria). Retorna una tupla con la suma de las partes reales e imaginarias.
```python
def sum_cplx(a, b):
    real = a[0] + b[0]
    imag = a[1] + b[1]
    return (real, imag)
```
    
2. Multiplicación de Números Complejos.

Multiplica dos números complejos a y b aplicando la fórmula de multiplicación para números complejos.
```python
def mult_cplx(a,b):
    real = a[0]*b[0] - a[1]*b[1]
    imag = a[0]*b[1] + a[1]*b[0]
    return (real, imag)
```

3. Resta de Números Complejos.

Resta dos números complejos a y b devolviendo al usuario una tupla con la diferencia de las partes reales e imaginarias.
```python
def diferencia_cplx(a, b):
    real = a[0] - b[0]
    imag = a[1] - b[1]
    return (real, imag)
```

4.División de Números Complejos.

Se sigue la formula propuesta en el libro guia de lecutra.

```python
def division_cplx(a, b):  #a/b
    denom = b[0] ** 2 + b[1] ** 2
    real = (a[0]*b[0] + a[1]*b[1]) / denom
    imag = (a[1]*b[0] - a[0]*b[1]) / denom
    return (real, imag)
```

5. Módulo de un Número Complejo.

Calcula el módulo o magnitud de un número complejo a, que es la distancia desde el origen hasta el punto (a[0], a[1]) en el plano complejo.
```python
def modulo(a):
    return (a[0] ** 2 + a[1] ** 2) ** (0.5)
```

6. Conjugado de un Número Complejo.

Esta función retorna el conjugado de un número complejo a, invirtiendo el signo de su parte imaginaria.
```python
def conjugado(a):
    return (a[0], -a[1])
```

7. Conversión de Cartesiano a Polar.

Convierte un número complejo a de su forma cartesiana a su forma polar. El ángulo se calcula usando la función atan2, que maneja correctamente los cuadrantes.
```python
def cartopolar(a):
    lnght = (a[0] ** 2 + a[1] ** 2) ** (0.5)
    angle = math.atan2(a[1], a[0])
    return (lnght, angle)
```

8. Conversión de Polar a Cartesiano.

Convierte un número complejo de su forma polar a su forma cartesiana mediante funciones trigonométricas.

```python
def polartocart(a):
    x = a[0] * math.cos(a[1])
    y = a[0] * math.sin(a[1])
    return (x, y)
```

9. Fase de un Número Complejo.

Retorna el ángulo que forma en el plano real e imaginario.
```python
def fase(a):
    return math.atan2(a[1], a[0])
```

## Pruebas.
Se realizan las pruebas unitarias mediante 'uniitest' y el método 'assertAlmostEqual'.

Como puede observar se limitan algunas cifras decimales debido a limitantes con la calculadora física.
```python
    def test_cartopolar(self):
        cart1 = Bclib.cartopolar((3,4))
        self.assertAlmostEqual(cart1[0],5)
        self.assertAlmostEqual(cart1[1],0.9272, places=3)

        cart2 = Bclib.cartopolar((5, -2.18))
        self.assertAlmostEqual(cart2[0], 5.45457, places=4)
        self.assertAlmostEqual(cart2[1], -0.41115, places=4)
```

En la prueba de fase se 'forza' el resultado manual de verficación ya que la función lo arroja en terminos de radianes negativos, pero el resultado también es valido si se toma el angulo en radianes correcto en valor positivo.
```python
    def test_fase(self):
        fase1 = Bclib.fase((3,4))
        self.assertAlmostEqual(fase1, 0.9272952)

        fase2 = Bclib.fase((-1,-2))
        self.assertAlmostEqual(fase2, -2.03444393)  #Otra respuesta válida 4.2484

```