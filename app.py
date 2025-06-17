import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from io import BytesIO

# =================================================================================================================
DB_SECUNDARIA = [{'FASES': 3, 'CABO': 120, 'VAO_M': 5, 'Y_DAN': 10}, {'FASES': 3, 'CABO': 120, 'VAO_M': 10, 'Y_DAN': 40}]
DB_COMPACTA = [{'TENSAO': 15, 'FASES': 3, 'CABO': 35, 'VAO_M': 15, 'Y_DAN': 342}]
DB_ILUMINACAO = [{'FASES': 1, 'CABO': 16, 'VAO_M': 5, 'Y_DAN': 5}]

TODOS_OS_CABOS = {
    'COMPACTA': DB_COMPACTA,
    'SECUNDARIA': DB_SECUNDARIA,
    'ILUMINACAO PUBLICA': DB_ILUMINACAO
}

# =================================================================================================================

def find_effort(db, vao_usuario, cabo_selecionado, **kwargs):
    opcoes_cabo_filtrado = [c for c in db if c['CABO'] == cabo_selecionado and all(c.get(k) == v for k, v in kwargs.items())]
    opcoes_vao_validas = [c for c in opcoes_cabo_filtrado if c['VAO_M'] >= vao_usuario]
    
    if not opcoes_vao_validas:
        return None, None 
        
    linha_selecionada = min(opcoes_vao_validas, key=lambda x: x['VAO_M'])
    return linha_selecionada['Y_DAN'], linha_selecionada['VAO_M']

def create_ui():
    st.set_page_config(layout="wide", page_title="Calculadora de Esforços em Poste")
    st.title("⚙️ Calculadora de Esforços em Poste")

    if 'resultados' not in st.session_state:
        st.session_state.resultados = []

    with st.sidebar:
        st.header("Configuração do Projeto")
        if 'num_postes' not in st.session_state:
            st.session_state.num_postes = 1

        # Use um callback para resetar os resultados se o número de postes mudar
        def update_num_postes():
            st.session_state.num_postes = st.session_state.num_postes_input
            st.session_state.resultados = [] # Reseta os resultados

        st.number_input("Quantidade de postes a serem calculados:", min_value=1, max_value=50, 
                        value=st.session_state.num_postes, step=1, key="num_postes_input", on_change=update_num_postes)

    all_postes_data = []

    with st.form(key='projeto_form'):
        for i in range(st.session_state.num_postes):
            with st.expander(f"Dados para o Poste #{i+1}", expanded=True):
                nome_poste = st.text_input("Nome/Identificador do Poste:", key=f"nome_poste_{i}")
                
                # Gerenciamento de estado para número de direções
                if f"num_dir_{i}" not in st.session_state:
                    st.session_state[f"num_dir_{i}"] = 1
                
                num_direcoes = st.number_input(
                    "Número de Direções:", 
                    min_value=1, 
                    value=st.session_state[f"num_dir_{i}"], 
                    step=1, 
                    key=f"num_dir_input_{i}"
                )
                st.session_state[f"num_dir_{i}"] = num_direcoes
                
                direcoes = []
                tem_compacta_poste = False

                for j in range(num_direcoes):
                    st.markdown(f"**Direção {j+1}**")
                    cols = st.columns([1, 2])
                    angulo = cols[0].number_input(f"Ângulo (0-360°):", min_value=0.0, max_value=360.0, value=0.0, step=1.0, key=f"angulo_{i}_{j}")
                    
                    tipos_selecionados = cols[1].multiselect(
                        "Selecione os tipos de cabo:",
                        options=list(TODOS_OS_CABOS.keys()),
                        key=f"tipos_{i}_{j}"
                    )

                    # Exibe o botão "Inserir" para atualizar o formulário de cabos
                    if tipos_selecionados:
                        if st.button(f"Inserir Direção {j+1}", key=f"inserir_{i}_{j}"):
                            # Quando o botão "Inserir" é pressionado, exibe os campos para inserir informações dos cabos
                            esforco_total_direcao = 0
                            for tipo in tipos_selecionados:
                                db = TODOS_OS_CABOS[tipo]
                                sub_cols = st.columns(3)
                                
                                if tipo == 'COMPACTA':
                                    tem_compacta_poste = True
                                    opcoes_tensao = sorted(list(set(c['TENSAO'] for c in db)))
                                    tensao_sel = sub_cols[0].selectbox("Tensão:", opcoes_tensao, key=f"tensao_{i}_{j}_{tipo}")
                                    db_filtrado = [c for c in db if c['TENSAO'] == tensao_sel]
                                    opcoes_cabo = sorted(list(set(c['CABO'] for c in db_filtrado)))
                                    cabo_sel = sub_cols[1].selectbox(f"Cabo ({tipo}):", opcoes_cabo, key=f"cabo_{i}_{j}_{tipo}")
                                    vao_sel = sub_cols[2].number_input("Vão (m):", min_value=1, step=1, key=f"vao_{i}_{j}_{tipo}")
                                    esforco, _ = find_effort(db, vao_sel, cabo_sel, TENSAO=tensao_sel)
                                else: 
                                    opcoes_fases = sorted(list(set(c['FASES'] for c in db)))
                                    fases_sel = sub_cols[0].selectbox("Fases:", opcoes_fases, key=f"fases_{i}_{j}_{tipo}")
                                    db_filtrado = [c for c in db if c['FASES'] == fases_sel]
                                    opcoes_cabo = sorted(list(set(c['CABO'] for c in db_filtrado)))
                                    cabo_sel = sub_cols[1].selectbox(f"Cabo ({tipo}):", opcoes_cabo, key=f"cabo_{i}_{j}_{tipo}")
                                    vao_sel = sub_cols[2].number_input("Vão (m):", min_value=1, step=1, key=f"vao_{i}_{j}_{tipo}")
                                    esforco, _ = find_effort(db, vao_sel, cabo_sel, FASES=fases_sel)

                                if esforco is not None:
                                    esforco_total_direcao += esforco
                            
                            direcoes.append({'id': str(j + 1), 'angulo': angulo, 'esforco_total': esforco_total_direcao})
                
                all_postes_data.append({'nome_poste': nome_poste, 'direcoes': direcoes, 'tem_compacta': tem_compacta_poste})

        submitted = st.form_submit_button("Calcular Projeto", type="primary")

    if submitted:
        st.session_state.resultados = []
        for poste_data in all_postes_data:
            if not poste_data['nome_poste']: continue
            
            resultante_mag, resultante_angulo, grafico_buffer = plotar_e_salvar_grafico(poste_data['direcoes'], poste_data['nome_poste'])
            poste_rec = recomendar_poste(resultante_mag, poste_data['tem_compacta'])
            
            relatorio_poste = {'ID do Poste': poste_data['nome_poste']}
            for k, direcao in enumerate(poste_data['direcoes']):
                relatorio_poste[f'Esforço Direção {k+1} (daN)'] = f"{direcao['esforco_total']:.2f}"
                relatorio_poste[f'Ângulo Direção {k+1} (°)'] = f"{direcao['angulo']:.1f}"
            
            relatorio_poste['Resultante Final (daN)'] = f"{resultante_mag:.2f}"
            relatorio_poste['Ângulo da Resultante (°)'] = f"{resultante_angulo:.1f}"
            relatorio_poste['Poste Recomendado'] = poste_rec
            relatorio_poste['grafico_buffer'] = grafico_buffer
            
            st.session_state.resultados.append(relatorio_poste)

    if st.session_state.resultados:
        st.header("Resultados do Projeto")
        
        for res in st.session_state.resultados:
            st.subheader(f"Resultados para o Poste: '{res['ID do Poste']}'")
            col1, col2 = st.columns(2)
            with col1:
                st.metric(label="Força Resultante Calculada", value=f"{float(res['Resultante Final (daN)']):.2f} daN")
                st.metric(label="Ângulo da Resultante", value=f"{float(res['Ângulo da Resultante (°)']):.2f} °")
                st.success(f"**Poste Recomendado:** {res['Poste Recomendado']}")
            with col2:
                st.image(res['grafico_buffer'], caption=f"Diagrama Vetorial para '{res['ID do Poste']}'")
            st.download_button(
                label=f"Baixar Gráfico de '{res['ID do Poste']}'",
                data=res['grafico_buffer'],
                file_name=f"grafico_{res['ID do Poste'].replace(' ', '_')}.png",
                mime="image/png",
                key=f"download_{res['ID do Poste']}"
            )
        
        st.markdown("---")
        st.header("Relatório Final Consolidado")
        
        df_export_data = []
        for res in st.session_state.resultados:
            export_item = res.copy()
            export_item.pop('grafico_buffer', None)
            df_export_data.append(export_item)
            
        df_resultados = pd.DataFrame(df_export_data)
        st.dataframe(df_resultados)
        
        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df_resultados.to_excel(writer, index=False, sheet_name='Relatorio')
        processed_data = output.getvalue()

        st.download_button(
            label="📥 Baixar Relatório Completo em Excel",
            data=processed_data,
            file_name="relatorio_esforcos_postes.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            key="download_excel"
        )

if __name__ == "__main__":
    create_ui()
