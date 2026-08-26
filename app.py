import streamlit as st
import numpy as np
import pandas as pd

from libreria_funciones_proyecto1 import calcular_oro_recuperado

# Título principal de la aplicación
st.title("Especialización Python for Analytics - Evaluación 1")

# Menú lateral de navegación
st.sidebar.title("Menú")

seccion = st.sidebar.selectbox(
    "Seleccione una sección:",
    [
        "Home",
        "Ejercicio 1",
        "Ejercicio 2",
        "Ejercicio 3",
        "Ejercicio 4"
    ]
)

# Lista para conservar los movimientos registrados
if "movimientos" not in st.session_state:
    st.session_state.movimientos = []

# Arrays para conservar los productos del Ejercicio 2
if "nombres_productos" not in st.session_state:
    st.session_state.nombres_productos = np.array([], dtype=str)
    st.session_state.categorias = np.array([], dtype=str)
    st.session_state.precios = np.array([], dtype=float)
    st.session_state.cantidades = np.array([], dtype=int)
    st.session_state.totales = np.array([], dtype=float)

# Histórico para conservar los resultados del Ejercicio 3
if "historico_oro" not in st.session_state:
    st.session_state.historico_oro = []

# Contenido según la sección seleccionada
if seccion == "Home":
    st.image("logo-dmc-institute-01.png", width=200)
    st.title("Proyecto 1 – Aplicación en Streamlit")

    st.subheader("Especialización en Python for Analytics")
    st.write("**Módulo 1 – Python Fundamentals**")

    st.markdown("---")

    st.subheader("Datos del estudiante")

    st.write("**Nombre completo:** Fidel Napoleón Bringas Salazar")
    st.write("**Información general:** Estudiante interesado en el análisis de datos y el uso de herramientas tecnológicas.")
    st.write("**Año:** 2026")

    st.markdown("---")

    st.subheader("Descripción del proyecto")

    st.write(
        """
        Este proyecto consiste en desarrollar una aplicación interactiva
        utilizando GibHub, Python y Streamlit. La aplicación permitirá poner en
        práctica los conocimientos adquiridos durante la primera parte delcurso de Especializacion en Python for Analitics, como el
        uso de variables, estructuras de datos, control de flujo, funciones,
        programación funcional y programación orientada a objetos.
        """
    )

    st.subheader("Tecnologías utilizadas")

    st.markdown(
        """
        - **Python:** lenguaje de programación utilizado para desarrollar la aplicación.
        - **Streamlit:** herramienta utilizada para crear la interfaz interactiva.
        - **GitHub:** plataforma utilizada para almacenar y gestionar el código del proyecto.
        """
    )

elif seccion == "Ejercicio 1":
    st.title("Ejercicio 1 – Flujo de caja con listas")

    st.markdown(
        """
        En este ejercicio se registran movimientos financieros en una lista.
        Cada movimiento contiene un **concepto**, un **tipo de movimiento**
        y un **valor**.

        Al finalizar, la aplicación muestra los ingresos, los gastos, el saldo
        y el estado actual del flujo de caja.
        """
    )

    st.subheader("Registrar un movimiento")

    concepto = st.text_input(
        "Concepto del movimiento:",
        placeholder="Ejemplo: Pago de salario"
    )

    tipo_movimiento = st.selectbox(
        "Tipo de movimiento:",
        ["Ingreso", "Gasto"]
    )

    valor = st.number_input(
        "Valor del movimiento (S/):",
        min_value=0.0,
        value=0.0,
        step=10.0
    )

    if st.button("Agregar movimiento"):
        if concepto.strip() == "":
            st.error("Debe ingresar el concepto del movimiento.")

        elif valor <= 0:
            st.error("El valor del movimiento debe ser mayor que cero.")

        else:
            movimiento = {
                "Concepto": concepto,
                "Tipo": tipo_movimiento,
                "Valor": valor
            }

            st.session_state.movimientos.append(movimiento)
            st.success("Movimiento agregado correctamente.")

    st.markdown("---")
    st.subheader("Movimientos registrados")

    if len(st.session_state.movimientos) > 0:
        st.dataframe(
            st.session_state.movimientos,
            use_container_width=True
        )

        total_ingresos = sum(
            movimiento["Valor"]
            for movimiento in st.session_state.movimientos
            if movimiento["Tipo"] == "Ingreso"
        )

        total_gastos = sum(
            movimiento["Valor"]
            for movimiento in st.session_state.movimientos
            if movimiento["Tipo"] == "Gasto"
        )

        saldo_final = total_ingresos - total_gastos

        st.subheader("Resumen del flujo de caja")

        columna1, columna2, columna3 = st.columns(3)

        with columna1:
            st.metric(
                "Total de ingresos",
                f"S/ {total_ingresos:.2f}"
            )

        with columna2:
            st.metric(
                "Total de gastos",
                f"S/ {total_gastos:.2f}"
            )

        with columna3:
            st.metric(
                "Saldo final",
                f"S/ {saldo_final:.2f}"
            )

        if saldo_final >= 0:
            st.success(
                f"El flujo de caja está a favor con un saldo de "
                f"S/ {saldo_final:.2f}."
            )
        else:
            st.error(
                f"El flujo de caja está en contra con un saldo de "
                f"S/ {saldo_final:.2f}."
            )

    else:
        st.write("Todavía no se han registrado movimientos.")

elif seccion == "Ejercicio 2":
    st.title("Ejercicio 2 – Registro con NumPy, arrays y DataFrame")

    st.markdown(
        """
        En este ejercicio se registran productos utilizando **arrays de
        NumPy**. Cada producto contiene su nombre, categoría, precio,
        cantidad y total.

        Después de agregar un producto, los arrays se convierten en un
        **DataFrame** para mostrar la información actualizada.
        """
    )

    st.subheader("Formulario de registro")

    nombre_producto = st.text_input(
        "Nombre del producto:",
        placeholder="Ejemplo: Laptop"
    )

    categoria = st.selectbox(
        "Categoría:",
        [
            "Tecnología",
            "Alimentos",
            "Ropa",
            "Hogar",
            "Oficina",
            "Otros"
        ]
    )

    precio = st.number_input(
        "Precio unitario (S/):",
        min_value=0.0,
        value=0.0,
        step=1.0
    )

    cantidad = st.number_input(
        "Cantidad:",
        min_value=1,
        value=1,
        step=1
    )

    total = precio * cantidad

    st.write(f"**Total del registro:** S/ {total:.2f}")

    if st.button("Agregar producto"):
        if nombre_producto.strip() == "":
            st.error("Debe ingresar el nombre del producto.")

        elif precio <= 0:
            st.error("El precio debe ser mayor que cero.")

        else:
            st.session_state.nombres_productos = np.append(
                st.session_state.nombres_productos,
                nombre_producto
            )

            st.session_state.categorias = np.append(
                st.session_state.categorias,
                categoria
            )

            st.session_state.precios = np.append(
                st.session_state.precios,
                precio
            )

            st.session_state.cantidades = np.append(
                st.session_state.cantidades,
                cantidad
            )

            st.session_state.totales = np.append(
                st.session_state.totales,
                total
            )

            st.success("Producto agregado correctamente.")

    st.markdown("---")
    st.subheader("Productos registrados")

    if len(st.session_state.nombres_productos) > 0:
        tabla_productos = pd.DataFrame(
            {
                "Producto": st.session_state.nombres_productos,
                "Categoría": st.session_state.categorias,
                "Precio": st.session_state.precios,
                "Cantidad": st.session_state.cantidades,
                "Total": st.session_state.totales
            }
        )

        st.dataframe(
            tabla_productos,
            use_container_width=True
        )

    else:
        st.write("Todavía no se han registrado productos.")

elif seccion == "Ejercicio 3":
    st.title("Ejercicio 3 – Función desde una librería externa")

    st.markdown(
        """
        En este ejercicio se utiliza una función importada desde la librería
        externa `libreria_funciones_proyecto1.py`.

        La función seleccionada permite estimar la cantidad de **oro recuperado**
        a partir del tonelaje procesado, la ley de oro y el porcentaje de
        recuperación metalúrgica.
        """
    )

    st.subheader("Seleccionar función")

    funcion_seleccionada = st.selectbox(
        "Función disponible:",
        ["Calcular oro recuperado"]
    )

    if funcion_seleccionada == "Calcular oro recuperado":
        st.subheader("Ingresar parámetros")

        tonelaje = st.number_input(
            "Tonelaje procesado (t):",
            min_value=0.0,
            value=1000.0,
            step=100.0
        )

        ley_oro = st.number_input(
            "Ley de oro (g/t):",
            min_value=0.0,
            value=1.0,
            step=0.1
        )

        recuperacion = st.number_input(
            "Recuperación metalúrgica (%):",
            min_value=0.0,
            max_value=100.0,
            value=80.0,
            step=1.0
        )

        if st.button("Ejecutar función"):
            if tonelaje <= 0:
                st.error("El tonelaje debe ser mayor que cero.")

            elif ley_oro <= 0:
                st.error("La ley de oro debe ser mayor que cero.")

            elif recuperacion <= 0:
                st.error(
                    "La recuperación metalúrgica debe ser mayor que cero."
                )

            else:
                resultado = calcular_oro_recuperado(
                    tonelaje,
                    ley_oro,
                    recuperacion
                )

                gramos_contenidos = resultado["gramos_contenidos"]
                gramos_recuperados = resultado["gramos_recuperados"]
                onzas_recuperadas = resultado["onzas_recuperadas"]

                st.success("La función se ejecutó correctamente.")

                st.subheader("Resultado")

                columna1, columna2, columna3 = st.columns(3)

                with columna1:
                    st.metric(
                        "Oro contenido",
                        f"{gramos_contenidos:,.2f} g"
                    )

                with columna2:
                    st.metric(
                        "Oro recuperado",
                        f"{gramos_recuperados:,.2f} g"
                    )

                with columna3:
                    st.metric(
                        "Oro recuperado",
                        f"{onzas_recuperadas:,.2f} oz"
                    )

                nuevo_resultado = {
                    "Tonelaje (t)": tonelaje,
                    "Ley de oro (g/t)": ley_oro,
                    "Recuperación (%)": recuperacion,
                    "Oro contenido (g)": gramos_contenidos,
                    "Oro recuperado (g)": gramos_recuperados,
                    "Oro recuperado (oz)": onzas_recuperadas
                }

                st.session_state.historico_oro.append(nuevo_resultado)

    st.markdown("---")
    st.subheader("Histórico de resultados")

    if len(st.session_state.historico_oro) > 0:
        tabla_historica = pd.DataFrame(
            st.session_state.historico_oro
        )

        st.dataframe(
            tabla_historica,
            use_container_width=True
        )

    else:
        st.write("Todavía no se han realizado cálculos.")

elif seccion == "Ejercicio 4":
    st.header("Ejercicio 4")

# Nombre del autor
st.sidebar.write("---")
st.sidebar.write("Elaborado por Fidel Bringas")
