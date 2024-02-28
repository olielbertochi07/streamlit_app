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
    formatted_results = [{"Id": row[0], "Codigo": row[1], "Descripcion": row[2], "Stock": row[3], "Min": row[4], "Mayorista": row[5], "Venta": row[6]} for row in results]
    for idx, row in enumerate(formatted_results):
        btnImg = st.button(f"Imagen Nº: {row["Id"]}")
        st.text("")
        e = 0
        if btnImg:   
            e = row["Id"] 
        else:
            e = 0

        id_format = (f'ID: {row["Id"]}')
        codigo_format = (f'{row["Codigo"]}')
        st.markdown(f'<div style="float: left;">{id_format}</div>', unsafe_allow_html=True)
        st.markdown(f'<div style="float: left;">{codigo_format}</div>', unsafe_allow_html=True)     
        descripcion_format = (f'{row["Descripcion"]}')
        st.markdown(f'<div style="text-align; font-weight: bold;">{descripcion_format}</div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align; font-weight: bold;">' '</div>', unsafe_allow_html=True) 
        if row['Stock'] <= row['Min']:
            stock_formatted = "<span style='color: red;'>Stock: {:,} UN</span>".format(int(row['Stock'])).replace(",", ".")
        else:
            stock_formatted = "<span style='color: green;'>Stock: {:,} UN</span>".format(int(row['Stock'])).replace(",", ".")

        st.markdown(f'{stock_formatted}', unsafe_allow_html=True)
        may_formatted = "Mayorista: " + "{:,} Gs".format(int(row['Mayorista'])).replace(",", ".")
        vent_formatted ="Venta: " + "{:,} Gs".format(int(row['Venta'])).replace(",", ".")     
        st.markdown(f'<div style="float: left;">{may_formatted}</div><div style="float: right;">{vent_formatted}</div>', unsafe_allow_html=True)  

        if e > 0:
            st.markdown("teste")  
            vlvbtn = st.button("Vovler")
            if vlvbtn:
                e=0

        st.markdown('<hr class="linha-presupuesto">', unsafe_allow_html=True)
        st.markdown("<style> .linha-presupuesto {margin: 0px 0;}</style>",unsafe_allow_html=True)
