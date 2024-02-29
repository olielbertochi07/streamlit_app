import streamlit as st
from app_functions import get_filtered_data
from db_functions import get_database_connection
def Listar_Produtos():
    st.subheader("Lista de Productos")
    st.subheader("")
    filtro_id = st.sidebar.text_input("Cód. Int.", key="filtro_id")
    filtro_codigo = st.sidebar.text_input("Código", key="filtro_codigo")
    filtro_descricao = st.sidebar.text_input("Descripción", key="filtro_descricao")
    if filtro_id == "":
        filtro_id = '%'
    results = get_filtered_data(filtro_id, f'%{filtro_codigo}%', f'%{filtro_descricao}%')

    if results:
        for row in results:
            btnImg = st.button(f"Imagen Nº: {row[0]}")
            st.text("")
            e = 0
            if btnImg:   
                e = row[0] 
            else:
                e = 0

            id_format = (f'ID: {row[0]}')
            codigo_format = (f'{row[1]}')
            st.markdown(f'<div style="float: left;">{id_format}</div>', unsafe_allow_html=True)
            st.markdown(f'<div style="float: left;">{codigo_format}</div>', unsafe_allow_html=True)     
            descripcion_format = (f'{row[2]}')
            st.markdown(f'<div style="text-align; font-weight: bold;">{descripcion_format}</div>', unsafe_allow_html=True)
            st.markdown(f'<div style="text-align; font-weight: bold;">' '</div>', unsafe_allow_html=True) 
            if row[3] <= row[4]:
                stock_formatted = "<span style='color: red;'>Stock: {:,} UN</span>".format(int(row[3])).replace(",", ".")
            else:
                stock_formatted = "<span style='color: green;'>Stock: {:,} UN</span>".format(int(row[3])).replace(",", ".")

            st.markdown(f'{stock_formatted}', unsafe_allow_html=True)
            may_formatted = "Mayorista: " + "{:,} Gs".format(int(row[5])).replace(",", ".")
            vent_formatted ="Venta: " + "{:,} Gs".format(int(row[6])).replace(",", ".")     
            st.markdown(f'<div style="float: left;">{may_formatted}</div><div style="float: right;">{vent_formatted}</div>', unsafe_allow_html=True)  

            if e > 0:
                st.markdown("teste")  
                vlvbtn = st.button("Vovler")
                if vlvbtn:
                    e=0

            st.markdown('<hr class="linha-presupuesto">', unsafe_allow_html=True)
            st.markdown("<style> .linha-presupuesto {margin: 0px 0;}</style>",unsafe_allow_html=True)
    else:
        st.warning("Nenhum resultado encontrado.")
