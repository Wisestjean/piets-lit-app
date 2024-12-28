import streamlit as st
import pandas as pd
import numpy as np
st.title('🎈 Piets Greetings')

st.write('Piets first App with pietslit')
st.markdown(
    """
    <style>
    body {
        background-color: white;
        color: black;
    }
    [data-testid="stSidebar"] {
        background-color: lightblue;
        border-top-right-radius:25px;
        border-bottom-right-radius:25px;
    }
    /* Optional: Add some padding or shadow for better aesthetics */
    [data-testid="stSidebar"]::after {
        box-shadow: 30px 15px 10px rgba(1, 0, 0, 0.7);
    }
    .stSubheader {
        background-color: #f0f8ff; /* Light blue background */
        padding: 10px;
        border-radius: 5px;
        font-weight: bold;
    }

    .stApp {
        background-color: white;
        color: black;
    }
    
    </style>
    """,
    unsafe_allow_html=True,
)
with st.sidebar:
    st.header("HOME")
    st.header("LOGIN")
    st.header("About Piets")
    st.write("Piets first App with pietslit")
st.header("My piets header and divider",divider=True)

st.markdown("Piets markdown created")

st.subheader("st.columns")
col1, col2 = st.columns(2)

with col1:
    x = st.slider("Choose x value", 1,15)
with col2:
    st.write("vale :red[ ***x*** ] se", x)

st.markdown(''' 
            :red[Piets] :blue[puede] :orange[escribir] :rainbow[text] &mdash; :tulip::cherry_blossom:
            :rose: :sunflower: :blossom: :red-background[Piets Highlight]
            ''')
multi = ''' Si puede terminar una linea con dos esoacios,
        un suave retorno es utilizado para la siguiente linea.
        Dos o mas caracteres ien una nueva fila

'''
st.markdown(multi)
st.subheader("st.area_chart")
chart_data = pd.DataFrame(np.random.randn(20,3),columns=["a","b","c"])
st.area_chart(chart_data)

