import streamlit as st
from db_functions import get_database_connection

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
def check_login(username, password):
    mydb = get_database_connection()
    mycursor = mydb.cursor()
    sql = "CALL `App_Consulta_Sessao`(%s, %s)"
    mycursor.execute(sql, (username, password))
    result = mycursor.fetchone()
    mycursor.close()
    mydb.close()
    return result
def get_lista_presupuesto(filtro_):  
    mydb = get_database_connection()
    mycursor = mydb.cursor()
    SQL ="CALL `App_Consulta_Presupuestos`(%s);"
    mycursor.execute(SQL, (f'{filtro_}'))
    results = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return results
def get_filtered_data(filtro_id, filtro_codigo, filtro_descricao):
    mydb = get_database_connection()
    mycursor = mydb.cursor()
    sql = "CALL `App_Consulta_Stock`(%s, %s, %s, '100')"
    mycursor.execute(sql, (filtro_id, f'%{filtro_codigo}%', f'%{filtro_descricao}%'))
    results = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return results