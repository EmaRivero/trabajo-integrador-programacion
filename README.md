# Trabajo Práctico Integrador - Programación I

## Análisis de eficiencia en algoritmos de validación de IDs duplicados

**Autores:** Julio Roja - Emmanuel Rivero

---

### 🔹 Problema

Dadas dos listas de IDs numéricos:

* `ids_registrados`: representa los usuarios ya almacenados en una base de datos.
* `ids_formulario`: representa nuevos registros ingresados desde un formulario.

El objetivo es determinar si alguno de los nuevos IDs ya está presente en la base existente. Para ello, se implementan y comparan dos estrategias:

* Una solución con **bucles anidados** (complejidad **O(n × m)**).
* Una solución optimizada usando **sets** (complejidad **O(n + m)**).

---

### 🌐 Tecnologías utilizadas

* **Lenguaje:** Python 3.12
* **Editor:** Visual Studio Code
* **Librerías:** `time`, `random`

---

### 🔹 Archivos incluidos

* `validacion_ids.py`: script principal con ambos algoritmos, generación de datos y medición de tiempos.
* `README.md`: este archivo.
* Captura de pantalla y video demostrativo incluidos en el informe PDF entregado.

---

### 🔧 Cómo ejecutar

1. Asegurarse de tener Python 3 instalado.
2. Ejecutar desde terminal o VS Code:

```bash
python validacion_ids.py
```

3. Se mostrarán los resultados de ambos algoritmos con y sin duplicados en las listas.

---

### 🔢 Resultados esperados

* En el primer caso (listas aleatorias), puede haber coincidencias y ambos algoritmos terminan rápidamente.
* En el segundo caso (listas sin coincidencias), el algoritmo con bucles anidados tarda considerablemente más, confirmando su complejidad O(n × m).
* El algoritmo con `set()` es rápido y constante en ambos escenarios.

---

### 📊 Conclusión

Este trabajo permitió evidenciar que dos soluciones al mismo problema pueden tener desempeños muy distintos. La notación Big-O fue clave para analizar el comportamiento teórico, mientras que las pruebas empíricas ayudaron a validar estos conceptos en la práctica. La diferencia de tiempo en el peor caso resulta decisiva para elegir algoritmos más eficientes.

---

### 📅 Enlace al video explicativo

*Disponible en el informe PDF entregado.*
