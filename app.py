import streamlit as st
import requests

# Configuração da Página do Streamlit
st.set_page_config(
    page_title="Gerador de Landing Pages - Odontologia",
    page_icon="🦷",
    layout="centered"
)

st.title("🦷 Gerador de Landing Pages para Clínicas Odontológicas")
st.write("Preencha os dados abaixo para gerar e baixar a landing page profissional da clínica.")

# Formulário de Entrada de Dados
with st.form("dental_form"):
    st.subheader("📋 Informações da Clínica")
    
    clinic_name = st.text_input("Nome da Clínica", value="Clínica São Paulo Dental Studio")
    city = st.text_input("Cidade / Região", value="São Paulo - SP")
    address = st.text_input("Endereço Completo", value="Av. Angélica, 2582 - 1° andar - Higienópolis, São Paulo - SP")
    whatsapp = st.text_input("WhatsApp (com DDI e DDD)", value="5511945068360")
    phone_display = st.text_input("Telefone Formatado para Exibição", value="(11) 94506-8360")
    
    submit_button = st.form_submit_button(label="Gerar Landing Page 🚀")

if submit_button:
    # URL do template HTML bruto hospedado no seu repositório do GitHub
    # ATENÇÃO: Substitua 'seu-usuario' e 'seu-repositorio' pelo seu GitHub real
    github_template_url = "https://raw.githubusercontent.com/wikizzcomunicacao-byte/template/main/template.html"
    
    try:
        # Baixa o template do GitHub
        response = requests.get(github_template_url)
        
        if response.status_code == 200:
            html_content = response.text
            
            # Substitui as variáveis do template pelos dados preenchidos no formulário
            html_content = html_content.replace("{{CLINIC_NAME}}", clinic_name)
            html_content = html_content.replace("{{CITY}}", city)
            html_content = html_content.replace("{{ADDRESS}}", address)
            html_content = html_content.replace("{{WHATSAPP}}", whatsapp)
            html_content = html_content.replace("{{PHONE_DISPLAY}}", phone_display)
            
            st.success("✨ Landing Page gerada com sucesso!")
            
            # Botão para baixar o arquivo HTML pronto
            st.download_button(
                label="📥 Baixar arquivo index.html",
                data=html_content,
                file_name="index.html",
                mime="text/html"
            )
        else:
            st.error(f"Erro ao buscar o template no GitHub. Código de status: {response.status_code}")
            st.info("Verifique se o arquivo `template.html` está público e no branch principal (`main`) do seu repositório.")
            
    except Exception as e:
        st.error(f"Ocorreu um erro de conexão: {e}")
