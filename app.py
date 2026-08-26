import streamlit as st
st.title("Especialización Python for Analytics - Evaluación 1")

# Menú lateral de navegación
st.sidebar.title("Menú")

seccion = st.sidebar.selectbox("Seleccione una sección:", ["Home","Ejercicio 1","Ejercicio 2","Ejercicio 3","Ejercicio 4"])

# Contenido según la sección seleccionada
if seccion == "Home":
    st.header("Home")
    st.write("Bienvenido a mi primera aplicación desarrollada en Streamlit.")

elif seccion == "Ejercicio 1":
    st.header("Ejercicio 1")

elif seccion == "Ejercicio 2":
    st.header("Ejercicio 2")

elif seccion == "Ejercicio 3":
    st.header("Ejercicio 3")

elif seccion == "Ejercicio 4":
    st.header("Ejercicio 4")

# Nombre del autor
st.write("Elaborado por Fidel Bringas")
