import streamlit as st
import pandas as pd
import plotly.graph_objects as go

car_data = pd.read_csv('/home/telneto/scripts/triplex/triple7_proyect/vehicles_us.csv')

hist_button = st.button('Construir histograma')
disp_button= st.button('Construir gráfico de dispersión')
st.write('Escoge aquí el gráfico de tu preferncia')

build_histogram = st.checkbox('Construir un histograma')
if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)

build_histogram = st.checkbox('Construir un gráfico de dispersión')
if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Creación de un gráfico de dispersión para el dataset de anuncios de ventas de autos')
    fig=go.Figure(data=[go.Scatter(x=car_data['odometer'],y=car_data['price'],mode='markers')])
    fig.update_layout(title_text='Dispersión del odómetro')
    st.plotly_chart(fig, use_container_width=True)



if disp_button:
    st.write('Creación de un gráfico de dispersión para el dataset de anuncios de ventas de autos')
    fig=go.Figure(data=[go.Scatter(x=car_data['odometer'],y=car_data['price'],mode='markers')])
    fig.update_layout(title_text='Dispersión del odómetro')
    st.plotly_chart(fig, use_container_width=True)

# Lógica a ejecutar cuando se hace clic en el botón
if hist_button:
    # Escribir un mensaje en la aplicación
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)


