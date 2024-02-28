import base64
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
        if idx > 0:
            st.markdown('<hr class="linha-presupuesto">', unsafe_allow_html=True)
            st.markdown("<style> .linha-presupuesto {margin: 0px 0;}</style>",unsafe_allow_html=True)
        left_column, right_column = st.columns([1, 3])

        btnImg = st.button(f"Imagen Nº: {row["Id"]}")
        st.text("")
        if btnImg:   
            e = row["Id"] 
        else:
            e = 0

        with left_column:


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
        with right_column:
            may_formatted = "Mayorista: " + "{:,} Gs".format(int(row['Mayorista'])).replace(",", ".")
            vent_formatted ="Venta: " + "{:,} Gs".format(int(row['Venta'])).replace(",", ".")     
            st.markdown(f'<div style="float: left;">{may_formatted}</div><div style="float: right;">{vent_formatted}</div>', unsafe_allow_html=True)     
        if e > 0:
                with st.form(key='frm_img'):
                    st.markdown(row["Descripcion"])   
                    mydb = get_database_connection() 
                    myc = mydb.cursor()
                    SQL = "SELECT img, n_img FROM v_app_lista_imagens_produtos WHERE id_producto = %s;"
                    myc.execute(SQL, (row["Id"],))
                    images = myc.fetchall()
                    for img_data in images:
                        encoded_img = base64.b64encode(img_data[0]).decode("utf-8")
                        img_tag = f'<img src="data:image/png;base64,{encoded_img}" alt="product_image" style="max-width:100%; margin-bottom: 10px;">'
                        st.markdown(img_tag, unsafe_allow_html=True)
                    submit_button = st.form_submit_button(label='Volver')     