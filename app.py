import streamlit as st

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
    st.header("Ejercicio 2")

elif seccion == "Ejercicio 3":
    st.header("Ejercicio 3")

elif seccion == "Ejercicio 4":
    st.header("Ejercicio 4")

# Nombre del autor
st.sidebar.write("---")
st.sidebar.write("Elaborado por Fidel Bringas")
