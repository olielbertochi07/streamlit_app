import base64
import streamlit as st
from db_functions import *
from app_functions import *
from app_lista_presupuestos import *
from app_nuevo_presupuesto import *
from app_lista_produtos import *
opcoes = ["Lista de Stock", "Presupuesto","Nuevo Presupuesto"]
def main():
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
    if st.session_state['logged_in']:
        choice = st.sidebar.selectbox("Seleccionar Menu", opcoes)
        st.sidebar.subheader("________________________________")
        if choice == "Lista de Stock":
            Listar_Produtos()
        if choice == "Presupuesto":
            Listar_Presupuesto()
        if choice == "Nuevo Presupuesto":
            Nuevo_Presupuesto()
    else:
        login_page()
def login_page():
    st.title("Bertochi Sistemas")
    username = st.text_input("", placeholder="Informe el Usuario", key="user-input")
    password = st.text_input("", placeholder="Informe la Contraseña", type="password")
    password = password.upper()
    username = username.upper()    
    if st.button("Iniciar Sesión"):
        if check_login(username, password):
            st.session_state['logged_in'] = True
            st.experimental_rerun()
        else:
            st.error("Login falhou. Verifique suas credenciais.")
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)  
if __name__ == "__main__":
    st.set_page_config( 
        page_title="Bertochi Sistemas",
        page_icon="📦",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    main()
