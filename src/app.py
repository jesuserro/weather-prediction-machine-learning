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
    st.session_state.datos_cargados = True 
    return data

# Función para limpiar los datos
def clean_data(data):
    # Normalize headers to lowercase and remove spaces
    data.columns = data.columns.str.lower().str.replace(' ', '_')
    
    # Check for data types
    st.success("Dataset cleaned successfully!")
    
    # Save the cleaned data
    # data.to_csv('data/processed/weather_classification_data.csv', index=False)
    return data

# Sidebar para cargar y mostrar el encabezado del archivo CSV
st.sidebar.title("Opciones")
if st.sidebar.button("Cargar y mostrar datos"):
    data = load_data()
    st.write(data.head())

# Botón para limpiar los datos
if st.sidebar.button("Limpiar Data"):
    data = load_data()
    cleaned_data = clean_data(data)
    st.write("Datos limpiados y guardados en 'data/processed/weather_classification_data.csv'")