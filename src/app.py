import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Título de la aplicación
st.title("¡Bienvenidas a Weather Prediction!")

# Cargar el archivo CSV
def load_data():
    data = pd.read_csv('data/raw/weather_classification_data.csv')
    st.session_state.datos_cargados = True 
    st.session_state.data = data
    return data

# Función para limpiar los datos
def clean_data(data):
    # Normalize headers to lowercase and remove spaces
    data.columns = data.columns.str.lower().str.replace(' ', '_')
    
    # Check for data types
    return data

# Sidebar para cargar y mostrar el encabezado del archivo CSV
st.sidebar.title("Opciones")
if st.sidebar.button("Cargar y mostrar datos"):
    data = load_data()
    st.write(data.head())

# Botón para limpiar los datos
if st.sidebar.button("Limpiar Data"):
    if 'data' in st.session_state:
        cleaned_data = clean_data(st.session_state.data)
        st.session_state.cleaned_data = cleaned_data
        st.write("Datos limpiados y guardados en 'data/processed/weather_classification_data.csv'")
        st.write(cleaned_data.head())
        st.success("Dataset cleaned successfully!")
    else:
        st.warning("Primero carga los datos.")
        
# Mostrar el DataFrame cargado si existe en session_state
if 'data' in st.session_state:
    st.write(st.session_state.data.head())