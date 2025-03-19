import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Título de la aplicación
st.title("¡Bienvenidas a Weather Prediction!")

# ...existing code...

# Cargar el archivo CSV
def load_data():
    data = pd.read_csv('data/raw/weather_classification_data.csv')
    return data

# Sidebar para cargar y mostrar el encabezado del archivo CSV
st.sidebar.title("Opciones")
if st.sidebar.button("Cargar y mostrar datos"):
    data = load_data()
    st.write(data.head())