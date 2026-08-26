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

# Contenido según la sección seleccionada
if seccion == "Home":
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
        utilizando Python y Streamlit. La aplicación permitirá poner en
        práctica los conocimientos adquiridos durante el Módulo 1, como el
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
    st.header("Ejercicio 1")

elif seccion == "Ejercicio 2":
    st.header("Ejercicio 2")

elif seccion == "Ejercicio 3":
    st.header("Ejercicio 3")

elif seccion == "Ejercicio 4":
    st.header("Ejercicio 4")

# Nombre del autor
st.sidebar.write("---")
st.sidebar.write("Elaborado por Fidel Bringas")
