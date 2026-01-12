import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import math



# -------------------------------------------------
# CONFIGURAÇÃO DA PÁGINA
# -------------------------------------------------
st.set_page_config(
    page_title="Dashboard SAP | Vale",
    page_icon="🔷",
    layout="wide",
    initial_sidebar_state="expanded"
)




# -------------------------------------------------
# AUTENTICAÇÃO - LOGIN CORPORATIVO
# -------------------------------------------------

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

USUARIOS = {
    "admin": "vale123",
    "gestor": "sap2026",
    "analista": "dashboard"
}

def tela_login():

    st.markdown("""
    <style>
        .login-bg {
            position: fixed;
            inset: 0;
            background: linear-gradient(135deg, #004d4a, #00807C);
            z-index: -1;
        }

        @keyframes fadeUp {
            from { opacity: 0; transform: translateY(40px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .vale-logo {
            display: flex;
            justify-content: center;
            margin-bottom: 1.2rem;
        }

        .vale-logo img {
            width: 140px;
        }

        .login-title {
            text-align: center;
            font-size: 1.6rem;
            font-weight: 900;
            color: #004d4a;
            margin-bottom: 0.2rem;
        }

        .login-subtitle {
            text-align: center;
            font-size: 0.85rem;
            color: #666;
            margin-bottom: 1.8rem;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="login-bg"></div>', unsafe_allow_html=True)

    # CENTRALIZAÇÃO REAL COM COLUNAS
    col_esq, col_centro, col_dir = st.columns([1, 1.2, 1])

    with col_centro:
        st.markdown('<div class="login-card">', unsafe_allow_html=True)

        st.markdown("""
            <div class="vale-logo">
                <img src="https://cdn.cookielaw.org/logos/9ba68c80-813d-4500-99f7-c620c54620bc/4f5b6ac2-1b26-44a7-bce4-c9d6b6cf55fe/275110e4-d5dc-4ae2-a0ff-acaf61612a7a/MicrosoftTeams-image_(1).png">
            </div>
            <div class="login-title">Portal SAP Analytics</div>
            <div class="login-subtitle">Acesso Corporativo • Vale S.A.</div>
        """, unsafe_allow_html=True)

        usuario = st.text_input("Usuário", placeholder="Digite seu usuário")
        senha = st.text_input("Senha", type="password", placeholder="Digite sua senha")

        if st.button("Entrar", use_container_width=True):
            if usuario in USUARIOS and senha == USUARIOS[usuario]:
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Usuário ou senha inválidos")

        st.markdown('</div>', unsafe_allow_html=True)



# -------------------------------------------------
# BLOQUEIO DE ACESSO
# -------------------------------------------------
if not st.session_state.authenticated:
    tela_login()
    st.stop()


# -------------------------------------------------
# CORES OFICIAIS DA VALE - PALETA CORPORATIVA
# -------------------------------------------------
VALE_GREEN = "#00807C"
VALE_YELLOW = "#EEA722"
VALE_GREY = "#77787B"
VALE_DARK_GREEN = "#004d4a"
VALE_LIGHT_GREEN = "#00a896"

# Paleta corporativa profissional
PALETA_CORPORATIVA = [
    "#00807C",  # Verde Vale
    "#EEA722",  # Amarelo Vale
    "#004d4a",  # Verde escuro
    "#00a896",  # Turquesa
    "#77787B",  # Cinza Vale
    "#2a9d8f",  # Verde água
    "#f4a261",  # Laranja corporativo
    "#e76f51",  # Terra cota
    "#118ab2",  # Azul corporativo
    "#06d6a0"   # Verde menta
]

# -------------------------------------------------
# FUNÇÃO PARA CALCULAR EIXO Y COM 2 NÍVEIS ACIMA
# -------------------------------------------------
def calcular_y_max_com_margem(max_valor):
    """
    Calcula o limite superior do eixo Y com 2 níveis acima do maior valor
    Exemplo: se max=78 e escala é 10, retorna 100 (80, 90, 100)
    """
    if max_valor <= 10:
        tick_interval = 1
    elif max_valor <= 50:
        tick_interval = 5
    elif max_valor <= 100:
        tick_interval = 10
    elif max_valor <= 500:
        tick_interval = 50
    else:
        tick_interval = 100

    # Arredonda para o próximo tick + adiciona 2 níveis
    proximo_tick = math.ceil(max_valor / tick_interval) * tick_interval
    y_max = proximo_tick + (2 * tick_interval)

    return y_max, tick_interval

# CSS customizado - VISUAL CORPORATIVO COM ANIMAÇÕES
st.markdown(f"""
                                <style>
                                @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

                                * {{
                                    font-family: 'Inter', sans-serif;
                                }}

                                /* ========================================
                                   ANIMAÇÕES KEYFRAMES CORPORATIVAS
                                ======================================== */
                                @keyframes fadeInUp {{
                                    from {{
                                        opacity: 0;
                                        transform: translateY(30px);
                                    }}
                                    to {{
                                        opacity: 1;
                                        transform: translateY(0);
                                    }}
                                }}

                                @keyframes fadeIn {{
                                    from {{
                                        opacity: 0;
                                    }}
                                    to {{
                                        opacity: 1;
                                    }}
                                }}

                                @keyframes slideInRight {{
                                    from {{
                                        opacity: 0;
                                        transform: translateX(-30px);
                                    }}
                                    to {{
                                        opacity: 1;
                                        transform: translateX(0);
                                    }}
                                }}

                                @keyframes slideInLeft {{
                                    from {{
                                        opacity: 0;
                                        transform: translateX(30px);
                                    }}
                                    to {{
                                        opacity: 1;
                                        transform: translateX(0);
                                    }}
                                }}

                                @keyframes pulse {{
                                    0%, 100% {{
                                        transform: scale(1);
                                    }}
                                    50% {{
                                        transform: scale(1.02);
                                    }}
                                }}

                                @keyframes bounceIn {{
                                    0% {{
                                        opacity: 0;
                                        transform: scale(0.3);
                                    }}
                                    50% {{
                                        opacity: 1;
                                        transform: scale(1.05);
                                    }}
                                    70% {{
                                        transform: scale(0.9);
                                    }}
                                    100% {{
                                        transform: scale(1);
                                    }}
                                }}

                                @keyframes slideDown {{
                                    from {{
                                        opacity: 0;
                                        transform: translateY(-20px);
                                    }}
                                    to {{
                                        opacity: 1;
                                        transform: translateY(0);
                                    }}
                                }}

                                /* ========================================
                                   BACKGROUND CORPORATIVO
                                ======================================== */
                                [data-testid="stAppViewContainer"] {{
                                    background: var(--background-color) !important;
                                    animation: fadeIn 0.8s ease-out;
                                }}

                                [data-testid="stHeader"] {{
                                    background: transparent !important;
                                }}

                                .main .block-container {{
                                    padding-top: 2rem;
                                    animation: fadeInUp 0.6s ease-out;
                                }}

                                /* ========================================
                                   HEADERS CORPORATIVOS COM ANIMAÇÃO
                                ======================================== */
                                .main-header {{
                                    font-size: 2.8rem;
                                    font-weight: 800;
                                    background: linear-gradient(135deg, {VALE_GREEN} 0%, {VALE_DARK_GREEN} 100%);
                                    -webkit-background-clip: text;
                                    -webkit-text-fill-color: transparent;
                                    background-clip: text;
                                    margin-bottom: 0.5rem;
                                    letter-spacing: -0.5px;
                                    animation: slideInRight 0.8s ease-out;
                                }}

                                .subtitle {{
                                    font-size: 1.1rem;
                                    color: {VALE_GREY};
                                    margin-bottom: 2rem;
                                    font-weight: 500;
                                    letter-spacing: 0.3px;
                                    animation: slideInLeft 1s ease-out;
                                }}

                                /* ========================================
                                   MÉTRICAS CORPORATIVAS COM ANIMAÇÃO
                                ======================================== */
                                div[data-testid="stMetric"] {{
                                    background: linear-gradient(135deg, rgba(0,128,124,0.08) 0%, rgba(0,128,124,0.04) 100%);
                                    padding: 1.8rem;
                                    border-radius: 16px;
                                    border: 2px solid rgba(0,128,124,0.15);
                                    transition: all 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
                                    text-align: center;
                                    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
                                    animation: bounceIn 0.8s ease-out backwards;
                                }}

                                div[data-testid="stMetric"]:nth-child(1) {{
                                    animation-delay: 0.1s;
                                }}

                                div[data-testid="stMetric"]:nth-child(2) {{
                                    animation-delay: 0.2s;
                                }}

                                div[data-testid="stMetric"]:nth-child(3) {{
                                    animation-delay: 0.3s;
                                }}

                                div[data-testid="stMetric"]:nth-child(4) {{
                                    animation-delay: 0.4s;
                                }}

                                div[data-testid="stMetric"]:hover {{
                                    transform: translateY(-12px) scale(1.03);
                                    border-color: {VALE_GREEN};
                                    box-shadow: 0 20px 60px rgba(0,128,124,0.3);
                                    background: linear-gradient(135deg, rgba(0,128,124,0.15) 0%, rgba(0,128,124,0.08) 100%);
                                }}

                                div[data-testid="stMetricValue"] {{
                                    font-size: 2.5rem;
                                    font-weight: 800;
                                    background: linear-gradient(135deg, {VALE_GREEN} 0%, {VALE_DARK_GREEN} 100%);
                                    -webkit-background-clip: text;
                                    -webkit-text-fill-color: transparent;
                                    background-clip: text;
                                    letter-spacing: -1px;
                                    transition: all 0.3s ease;
                                }}

                                div[data-testid="stMetric"]:hover div[data-testid="stMetricValue"] {{
                                    transform: scale(1.1);
                                }}

                                div[data-testid="stMetricLabel"] {{
                                    color: {VALE_GREY};
                                    font-weight: 700;
                                    font-size: 0.85rem;
                                    text-transform: uppercase;
                                    letter-spacing: 1.5px;
                                    transition: all 0.3s ease;
                                }}

                                div[data-testid="stMetric"]:hover div[data-testid="stMetricLabel"] {{
                                    color: {VALE_GREEN};
                                }}

                                /* ========================================
                                   ABAS CORPORATIVAS COM ANIMAÇÃO
                                ======================================== */
                                .stTabs [data-baseweb="tab-list"] {{
                                    gap: 12px;
                                    background: linear-gradient(135deg, rgba(0,128,124,0.06) 0%, rgba(0,128,124,0.03) 100%);
                                    padding: 1rem;
                                    border-radius: 16px;
                                    box-shadow: inset 0 1px 3px rgba(0,0,0,0.05);
                                    animation: slideDown 0.8s ease-out;
                                }}

                                .stTabs [data-baseweb="tab"] {{
                                    padding: 14px 32px;
                                    font-weight: 700;
                                    border-radius: 12px;
                                    background: transparent;
                                    border: 2px solid transparent;
                                    transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
                                    font-size: 0.95rem;
                                    letter-spacing: 0.5px;
                                    position: relative;
                                    overflow: hidden;
                                }}

                                .stTabs [data-baseweb="tab"]::before {{
                                    content: '';
                                    position: absolute;
                                    top: 0;
                                    left: -100%;
                                    width: 100%;
                                    height: 100%;
                                    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
                                    transition: left 0.6s ease;
                                }}

                                .stTabs [data-baseweb="tab"]:hover::before {{
                                    left: 100%;
                                }}

                                .stTabs [data-baseweb="tab"]::after {{
                                    content: '';
                                    position: absolute;
                                    bottom: 0;
                                    left: 50%;
                                    width: 0;
                                    height: 3px;
                                    background: {VALE_GREEN};
                                    transition: all 0.4s ease;
                                    transform: translateX(-50%);
                                }}

                                .stTabs [data-baseweb="tab"]:hover::after {{
                                    width: 80%;
                                }}

                                .stTabs [data-baseweb="tab"]:hover {{
                                    background: linear-gradient(135deg, rgba(0,128,124,0.12) 0%, rgba(0,128,124,0.08) 100%);
                                    border-color: {VALE_GREEN};
                                    transform: translateY(-5px) scale(1.02);
                                    box-shadow: 0 10px 20px rgba(0,128,124,0.2);
                                }}

                                .stTabs [aria-selected="true"] {{
                                    background: linear-gradient(135deg, {VALE_GREEN} 0%, {VALE_DARK_GREEN} 100%) !important;
                                    color: white !important;
                                    border: 2px solid {VALE_GREEN} !important;
                                    transform: translateY(-5px) scale(1.02);
                                    box-shadow: 0 12px 30px rgba(0,128,124,0.35);
                                }}

                                /* ========================================
                                   CARDS CORPORATIVOS COM ANIMAÇÃO
                                ======================================== */
                                .info-card {{
                                    background: linear-gradient(135deg, rgba(0,128,124,0.06) 0%, rgba(0,128,124,0.03) 100%);
                                    padding: 2.2rem;
                                    border-radius: 16px;
                                    border-left: 6px solid {VALE_GREEN};
                                    margin: 0.8rem 0;
                                    box-shadow: 0 4px 16px rgba(0,128,124,0.12);
                                    transition: all 0.6s cubic-bezier(0.68, -0.55, 0.265, 1.55);
                                    text-align: center;
                                    animation: fadeInUp 0.7s ease-out;
                                    position: relative;
                                    overflow: hidden;
                                }}

                                .info-card::before {{
                                    content: '';
                                    position: absolute;
                                    top: 0;
                                    left: -100%;
                                    width: 100%;
                                    height: 100%;
                                    background: linear-gradient(90deg, transparent, rgba(0,128,124,0.1), transparent);
                                    transition: left 0.8s ease;
                                }}

                                .info-card:hover::before {{
                                    left: 100%;
                                }}

                                .info-card:hover {{
                                    transform: translateY(-10px) scale(1.03);
                                    border-left-width: 12px;
                                    box-shadow: 0 25px 60px rgba(0,128,124,0.3);
                                    background: linear-gradient(135deg, rgba(0,128,124,0.12) 0%, rgba(0,128,124,0.06) 100%);
                                }}

                                .info-card h3 {{
                                    margin: 0.5rem 0;
                                    word-wrap: break-word;
                                    font-weight: 700;
                                    transition: all 0.3s ease;
                                }}

                                .info-card:hover h3 {{
                                    transform: scale(1.05);
                                    color: {VALE_GREEN};
                                }}

                                .info-card-label {{
                                    color: {VALE_GREY};
                                    font-size: 0.85rem;
                                    font-weight: 700;
                                    text-transform: uppercase;
                                    letter-spacing: 1.5px;
                                    margin-bottom: 0.8rem;
                                    display: block;
                                }}

                                /* ========================================
                                   ESCOPO CORPORATIVO COM ANIMAÇÃO
                                ======================================== */
                                .escopo-container {{
                                    background: linear-gradient(135deg, rgba(0,128,124,0.06) 0%, rgba(0,128,124,0.03) 100%);
                                    padding: 1.8rem;
                                    border-radius: 16px;
                                    border: 2px solid rgba(0,128,124,0.15);
                                    margin: 1rem 0;
                                    transition: all 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
                                    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
                                    animation: fadeIn 0.8s ease-out;
                                }}

                                .escopo-container:hover {{
                                    border-color: {VALE_GREEN};
                                    box-shadow: 0 15px 40px rgba(0,128,124,0.25);
                                    transform: translateY(-6px);
                                    border-width: 3px;
                                }}

                                .escopo-label {{
                                    color: {VALE_GREEN};
                                    font-weight: 800;
                                    font-size: 1rem;
                                    text-transform: uppercase;
                                    letter-spacing: 1.5px;
                                    margin-bottom: 1rem;
                                    display: block;
                                    transition: all 0.3s ease;
                                }}

                                .escopo-container:hover .escopo-label {{
                                    letter-spacing: 2px;
                                }}

                                .escopo-text {{
                                    font-size: 1rem;
                                    line-height: 1.7;
                                    text-align: justify;
                                    opacity: 0.9;
                                    font-weight: 400;
                                    transition: all 0.3s ease;
                                }}

                                .escopo-container:hover .escopo-text {{
                                    opacity: 1;
                                }}

                                /* ========================================
                                   BOTÕES CORPORATIVOS COM ANIMAÇÃO
                                ======================================== */
                                .stButton>button {{
                                    background: linear-gradient(135deg, {VALE_GREEN} 0%, {VALE_DARK_GREEN} 100%);
                                    color: white !important;
                                    border: none;
                                    padding: 1rem 3rem;
                                    border-radius: 12px;
                                    font-weight: 800;
                                    font-size: 1rem;
                                    text-transform: uppercase;
                                    letter-spacing: 1.5px;
                                    transition: all 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
                                    box-shadow: 0 6px 20px rgba(0,128,124,0.25);
                                    position: relative;
                                    overflow: hidden;
                                }}

                                .stButton>button::before {{
                                    content: '';
                                    position: absolute;
                                    top: 50%;
                                    left: 50%;
                                    width: 0;
                                    height: 0;
                                    border-radius: 50%;
                                    background: rgba(255,255,255,0.3);
                                    transform: translate(-50%, -50%);
                                    transition: width 0.6s ease, height 0.6s ease;
                                }}

                                .stButton>button:hover::before {{
                                    width: 400px;
                                    height: 400px;
                                }}

                                .stButton>button:hover {{
                                    background: linear-gradient(135deg, {VALE_YELLOW} 0%, #d69619 100%);
                                    transform: translateY(-6px) scale(1.05);
                                    box-shadow: 0 15px 40px rgba(238,167,34,0.5);
                                }}

                                .stButton>button:active {{
                                    transform: translateY(-2px) scale(0.98);
                                }}

                                /* ========================================
                                   TABELAS CORPORATIVAS COM ANIMAÇÃO
                                ======================================== */
                                .stDataFrame {{
                                    transition: all 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
                                    border-radius: 16px;
                                    animation: fadeInUp 0.8s ease-out;
                                }}

                                .stDataFrame:hover {{
                                    transform: scale(1.02);
                                    box-shadow: 0 20px 50px rgba(0,128,124,0.25);
                                }}

                                div[data-testid="stDataFrame"] > div {{
                                    border-radius: 16px;
                                    border: 2px solid rgba(0,128,124,0.15);
                                    transition: all 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
                                    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
                                }}

                                div[data-testid="stDataFrame"]:hover > div {{
                                    border-color: {VALE_GREEN};
                                    border-width: 3px;
                                }}

                                /* ========================================
                                   INPUTS CORPORATIVOS
                                ======================================== */
                                .stTextInput input {{
                                    background: rgba(255,255,255,0.05) !important;
                                    border: 2px solid rgba(0,128,124,0.2) !important;
                                    border-radius: 12px !important;
                                    padding: 1rem 1.2rem !important;
                                    transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
                                    font-weight: 500;
                                }}

                                .stTextInput input:focus {{
                                    border-color: {VALE_GREEN} !important;
                                    box-shadow: 0 0 0 6px rgba(0,128,124,0.15) !important;
                                    transform: translateY(-3px) scale(1.02);
                                    border-width: 3px !important;
                                }}

                                .stMultiSelect div[data-baseweb="select"] {{
                                    background: rgba(255,255,255,0.05);
                                    border: 2px solid rgba(0,128,124,0.2);
                                    border-radius: 12px;
                                    transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
                                }}

                                .stMultiSelect div[data-baseweb="select"]:hover {{
                                    border-color: {VALE_GREEN};
                                    box-shadow: 0 6px 16px rgba(0,128,124,0.2);
                                    transform: translateY(-2px);
                                }}

                                .stMultiSelect span[data-baseweb="tag"] {{
                                    background: linear-gradient(135deg, {VALE_GREEN} 0%, {VALE_DARK_GREEN} 100%) !important;
                                    color: white !important;
                                    border-radius: 8px !important;
                                    padding: 0.4rem 1rem !important;
                                    font-weight: 600;
                                    animation: bounceIn 0.4s ease-out;
                                    transition: all 0.3s ease;
                                }}

                                .stMultiSelect span[data-baseweb="tag"]:hover {{
                                    transform: scale(1.1);
                                    box-shadow: 0 4px 12px rgba(0,128,124,0.3);
                                }}

                                .stSelectbox div[data-baseweb="select"] {{
                                    background: rgba(255,255,255,0.05);
                                    border: 2px solid rgba(0,128,124,0.2);
                                    border-radius: 12px;
                                    transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
                                }}

                                .stSelectbox div[data-baseweb="select"]:hover {{
                                    border-color: {VALE_GREEN};
                                    box-shadow: 0 6px 16px rgba(0,128,124,0.2);
                                    transform: translateY(-2px);
                                }}

                                /* ========================================
                                   FILE UPLOADER - MODO LIGHT CORRIGIDO
                                ======================================== */
                                [data-testid="stFileUploader"] {{
                                    background: rgba(0,128,124,0.06) !important;
                                    border: 2px dashed rgba(0,128,124,0.3) !important;
                                    border-radius: 12px;
                                    padding: 1.5rem;
                                    transition: all 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
                                    animation: fadeIn 0.6s ease-out;
                                }}

                                [data-testid="stFileUploader"]:hover {{
                                    border-color: {VALE_GREEN} !important;
                                    background: rgba(0,128,124,0.12) !important;
                                    box-shadow: 0 8px 20px rgba(0,128,124,0.2);
                                    transform: translateY(-4px) scale(1.02);
                                    border-style: solid !important;
                                }}

                                [data-testid="stFileUploader"] section {{
                                    background: transparent !important;
                                }}

                                [data-testid="stFileUploader"] button {{
                                    background: linear-gradient(135deg, {VALE_GREEN} 0%, {VALE_DARK_GREEN} 100%) !important;
                                    color: white !important;
                                    border: none !important;
                                    font-weight: 600;
                                    padding: 0.6rem 1.5rem;
                                    border-radius: 8px;
                                    transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
                                }}

                                [data-testid="stFileUploader"] button:hover {{
                                    background: linear-gradient(135deg, {VALE_YELLOW} 0%, #d69619 100%) !important;
                                    transform: translateY(-3px) scale(1.05);
                                    box-shadow: 0 8px 20px rgba(238,167,34,0.4);
                                }}

                                /* ========================================
                                   SIDEBAR CORPORATIVA
                                ======================================== */
                                section[data-testid="stSidebar"] {{
                                    background: linear-gradient(180deg, {VALE_GREEN} 0%, {VALE_DARK_GREEN} 100%) !important;
                                    box-shadow: 8px 0 32px rgba(0,0,0,0.2);
                                    animation: slideInRight 0.5s ease-out;
                                }}

                                section[data-testid="stSidebar"] > div {{
                                    padding-top: 2rem;
                                }}

                                section[data-testid="stSidebar"] * {{
                                    color: white !important;
                                }}

                                section[data-testid="stSidebar"] .stButton>button {{
                                    background: rgba(255,255,255,0.15) !important;
                                    color: white !important;
                                    border: 2px solid rgba(255,255,255,0.4);
                                    backdrop-filter: blur(10px);
                                    transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
                                }}

                                section[data-testid="stSidebar"] .stButton>button:hover {{
                                    background: white !important;
                                    color: {VALE_GREEN} !important;
                                    border-color: white;
                                    transform: translateY(-3px) scale(1.05);
                                }}

                                section[data-testid="stSidebar"] [data-testid="stFileUploader"] {{
                                    background: rgba(255,255,255,0.1) !important;
                                    border-color: rgba(255,255,255,0.3) !important;
                                }}

                                section[data-testid="stSidebar"] [data-testid="stFileUploader"]:hover {{
                                    background: rgba(255,255,255,0.2) !important;
                                    border-color: white !important;
                                }}

                                /* ========================================
                                   MENSAGENS CORPORATIVAS
                                ======================================== */
                                .stSuccess {{
                                    border-radius: 12px;
                                    border-left-width: 6px;
                                    background-color: rgba(0,128,124,0.1);
                                    box-shadow: 0 2px 8px rgba(0,128,124,0.15);
                                    animation: slideInLeft 0.5s ease-out;
                                    transition: all 0.3s ease;
                                }}

                                .stSuccess:hover {{
                                    transform: translateX(5px);
                                    box-shadow: 0 6px 20px rgba(0,128,124,0.25);
                                }}

                                .stInfo {{
                                    border-radius: 12px;
                                    border-left-width: 6px;
                                    background-color: rgba(0,128,200,0.1);
                                    box-shadow: 0 2px 8px rgba(0,128,200,0.15);
                                    animation: slideInLeft 0.5s ease-out;
                                    transition: all 0.3s ease;
                                }}

                                .stInfo:hover {{
                                    transform: translateX(5px);
                                    box-shadow: 0 6px 20px rgba(0,128,200,0.25);
                                }}

                                .stWarning {{
                                    border-radius: 12px;
                                    border-left-width: 6px;
                                    background-color: rgba(238,167,34,0.1);
                                    box-shadow: 0 2px 8px rgba(238,167,34,0.15);
                                    animation: slideInLeft 0.5s ease-out;
                                    transition: all 0.3s ease;
                                }}

                                .stWarning:hover {{
                                    transform: translateX(5px);
                                    box-shadow: 0 6px 20px rgba(238,167,34,0.25);
                                }}

                                /* ========================================
                                   SCROLLBAR CORPORATIVA
                                ======================================== */
                                ::-webkit-scrollbar {{
                                    width: 12px;
                                    height: 12px;
                                }}

                                ::-webkit-scrollbar-track {{
                                    background: rgba(0,0,0,0.03);
                                    border-radius: 10px;
                                }}

                                ::-webkit-scrollbar-thumb {{
                                    background: linear-gradient(135deg, {VALE_GREEN} 0%, {VALE_DARK_GREEN} 100%);
                                    border-radius: 10px;
                                    border: 2px solid transparent;
                                    background-clip: padding-box;
                                    transition: all 0.3s ease;
                                }}

                                ::-webkit-scrollbar-thumb:hover {{
                                    background: linear-gradient(135deg, {VALE_DARK_GREEN} 0%, {VALE_GREEN} 100%);
                                    background-clip: padding-box;
                                }}

                                /* ========================================
                                   CONTAINERS DE PESQUISA
                                ======================================== */
                                .search-container {{
                                    background: linear-gradient(135deg, rgba(0,128,124,0.06) 0%, rgba(0,128,124,0.03) 100%);
                                    padding: 2.5rem;
                                    border-radius: 16px;
                                    border: 2px solid rgba(0,128,124,0.15);
                                    margin: 1rem 0;
                                    box-shadow: 0 4px 16px rgba(0,128,124,0.12);
                                    animation: fadeInUp 0.7s ease-out;
                                    transition: all 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
                                }}

                                .search-container:hover {{
                                    border-color: {VALE_GREEN};
                                    box-shadow: 0 12px 35px rgba(0,128,124,0.2);
                                    transform: translateY(-5px);
                                }}

                                .search-title {{
                                    color: {VALE_GREEN};
                                    font-size: 1.6rem;
                                    font-weight: 800;
                                    margin-bottom: 1.5rem;
                                    text-align: center;
                                    letter-spacing: 0.5px;
                                    transition: all 0.3s ease;
                                }}

                                .search-container:hover .search-title {{
                                    transform: scale(1.05);
                                    letter-spacing: 1px;
                                }}

                                /* ========================================
                                   CARDS DE RESULTADO
                                ======================================== */
                                .result-card {{
                                    background: linear-gradient(135deg, rgba(0,128,124,0.06) 0%, rgba(0,128,124,0.03) 100%);
                                    padding: 2.5rem;
                                    border-radius: 16px;
                                    border: 2px solid {VALE_GREEN};
                                    margin: 1.5rem 0;
                                    box-shadow: 0 8px 24px rgba(0,128,124,0.18);
                                    transition: all 0.6s cubic-bezier(0.68, -0.55, 0.265, 1.55);
                                    animation: fadeInUp 0.6s ease-out;
                                }}

                                .result-card:hover {{
                                    transform: translateY(-10px) scale(1.02);
                                    box-shadow: 0 30px 70px rgba(0,128,124,0.35);
                                    border-width: 4px;
                                }}

                                .result-header {{
                                    text-align: center;
                                    font-size: 1.9rem;
                                    color: {VALE_GREEN};
                                    font-weight: 800;
                                    margin-bottom: 1.5rem;
                                    padding-bottom: 1rem;
                                    border-bottom: 3px solid rgba(0,128,124,0.2);
                                    letter-spacing: 0.5px;
                                    transition: all 0.3s ease;
                                }}

                                .result-card:hover .result-header {{
                                    letter-spacing: 1.5px;
                                    transform: scale(1.05);
                                }}

                                /* ========================================
                                   EXPANDER CORPORATIVO
                                ======================================== */
                                .streamlit-expanderHeader {{
                                    background: linear-gradient(135deg, rgba(0,128,124,0.06) 0%, rgba(0,128,124,0.03) 100%) !important;
                                    border: 2px solid rgba(0,128,124,0.15) !important;
                                    border-radius: 12px !important;
                                    transition: all 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55) !important;
                                    font-weight: 600;
                                }}

                                .streamlit-expanderHeader:hover {{
                                    border-color: {VALE_GREEN} !important;
                                    box-shadow: 0 8px 20px rgba(0,128,124,0.25) !important;
                                    transform: translateY(-3px) scale(1.01);
                                }}

                                /* ========================================
                                   CONTAINER DE GRÁFICOS - SEM PISCAR
                                ======================================== */
                                .js-plotly-plot {{
                                    border-radius: 20px;
                                    padding: 1.5rem;
                                    background: linear-gradient(135deg, rgba(0,128,124,0.02) 0%, rgba(0,128,124,0.01) 100%);
                                    box-shadow: 0 4px 20px rgba(0,0,0,0.08);
                                }}

                                .js-plotly-plot:hover {{
                                    box-shadow: 0 15px 40px rgba(0,128,124,0.2);
                                }}

                                /* Desabilitar TODAS animações nos gráficos */
                                .js-plotly-plot * {{
                                    animation: none !important;
                                }}

                                .js-plotly-plot text {{
                                    animation: none !important;
                                }}

                                .js-plotly-plot .legendtext {{
                                    animation: none !important;
                                }}

                                .js-plotly-plot .legend {{
                                    animation: none !important;
                                }}

                                .js-plotly-plot svg {{
                                    animation: none !important;
                                }}

                                .js-plotly-plot svg * {{
                                    animation: none !important;
                                }}

                                /* ========================================
                                   MARKDOWN HEADERS
                                ======================================== */
                                h1, h2, h3, h4, h5, h6 {{
                                    color: inherit !important;
                                    font-weight: 700;
                                    transition: all 0.3s ease;
                                }}

                                h2, h3 {{
                                    animation: fadeInUp 0.6s ease-out;
                                }}

                                h2:hover, h3:hover {{
                                    transform: translateX(5px);
                                    color: {VALE_GREEN} !important;
                                }}

                                /* ========================================
                                   PADDING AJUSTADO
                                ======================================== */
                                .main > div {{
                                    padding-top: 1rem;
                                }}
                                </style>
                            """, unsafe_allow_html=True)

# -------------------------------------------------
# SIDEBAR - CONFIGURAÇÕES
# -------------------------------------------------
with st.sidebar:
    st.markdown(f"<h2 style='color: white; text-align: center; margin-bottom: 2rem; font-weight: 800; letter-spacing: 1px;'>⚙️ CONFIGURAÇÕES</h2>", unsafe_allow_html=True)

    if 'file_uploaded' not in st.session_state:
        st.session_state.file_uploaded = False
    if 'df_completo' not in st.session_state:
        st.session_state.df_completo = None
    if 'show_database' not in st.session_state:
        st.session_state.show_database = False

    if not st.session_state.file_uploaded:
        uploaded_file = st.file_uploader(
            "📂 Upload da Planilha",
            type=["xlsx", "xls"],
            help="Selecione um arquivo Excel com os dados dos projetos SAP"
        )

        if uploaded_file:
            st.session_state.file_uploaded = True
            st.session_state.uploaded_file = uploaded_file
            st.rerun()
    else:
        st.success("✅ Planilha carregada")

        if st.button("🔄 Carregar Nova Planilha"):
            st.session_state.file_uploaded = False
            st.session_state.df_completo = None
            st.session_state.uploaded_file = None
            st.session_state.show_database = False
            st.rerun()

    st.markdown("---")

    with st.expander("ℹ️ Sobre o Dashboard", expanded=False):
        st.markdown("""
                                    **Dashboard SAP Analytics Vale**

                                    Funcionalidades:
                                    - 📊 Análise de projetos PEP
                                    - 📈 Análise de projetos por Código
                                    - 🔍 Busca detalhada (PEP e Código)
                                    - 📥 Exportação de dados
                                    - 💰 Análise de Economia (2026-2056)
                                    - 📅 Detalhamento Mensal (2026-2028)

                                    **Versão:** 6.0  
                                    **Atualizado:** Jan/2026
                                    """)

    if st.session_state.file_uploaded:
        st.markdown("---")
        if st.button("📊 Visualizar Base de Dados Completa", use_container_width=True):
            st.session_state.show_database = True
            st.rerun()

# -------------------------------------------------
# CABEÇALHO PRINCIPAL
# -------------------------------------------------
col_logo, col_title = st.columns([1, 4])

with col_logo:
    st.markdown(f"""
                                    <div style='background: transparent; padding: 0.5rem 0;'>
                                        <img src='https://cdn.cookielaw.org/logos/9ba68c80-813d-4500-99f7-c620c54620bc/4f5b6ac2-1b26-44a7-bce4-c9d6b6cf55fe/275110e4-d5dc-4ae2-a0ff-acaf61612a7a/MicrosoftTeams-image_(1).png' 
                                             style='width: 150px; height: auto; background: transparent; filter: drop-shadow(0 0 20px rgba(0,128,124,0.5));'>
                                    </div>
                                """, unsafe_allow_html=True)

with col_title:
    st.markdown('<p class="main-header">Dashboard de Análise de Projetos SAP</p>',
                unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Sistema Integrado de Gestão de Projetos | Vale S.A.</p>',
                unsafe_allow_html=True)

# -------------------------------------------------
# MODAL DE BASE DE DADOS
# -------------------------------------------------
if st.session_state.get('show_database', False) and st.session_state.get('df_completo') is not None:
    st.markdown("---")
    st.markdown("## 📊 Base de Dados Completa")

    col_info, col_close = st.columns([4, 1])
    with col_info:
        st.info(f"📋 Total de **{len(st.session_state.df_completo):,}** registros na base de dados")
    with col_close:
        if st.button("❌ Fechar", use_container_width=True):
            st.session_state.show_database = False
            st.rerun()

    col_f1, col_f2 = st.columns(2)
    with col_f1:
        empresas_filtro = st.multiselect(
            "Filtrar por Empresa:",
            options=sorted(st.session_state.df_completo["Empresa"].unique()),
            key="filtro_empresa_db"
        )
    with col_f2:
        if "Status" in st.session_state.df_completo.columns:
            status_filtro = st.multiselect(
                "Filtrar por Status:",
                options=sorted(st.session_state.df_completo["Status"].dropna().unique()),
                key="filtro_status_db"
            )
        else:
            status_filtro = []

    df_exibir = st.session_state.df_completo.copy()
    if empresas_filtro:
        df_exibir = df_exibir[df_exibir["Empresa"].isin(empresas_filtro)]
    if status_filtro:
        df_exibir = df_exibir[df_exibir["Status"].isin(status_filtro)]

    st.dataframe(
        df_exibir.reset_index(drop=True),
        use_container_width=True,
        height=500
    )

    col_d1, col_d2, col_d3 = st.columns([1, 1, 1])
    with col_d2:
        csv = df_exibir.to_csv(index=False).encode('utf-8-sig')
        st.download_button(
            label="📥 Baixar Dados Filtrados (CSV)",
            data=csv,
            file_name="base_dados_filtrada.csv",
            mime="text/csv",
            use_container_width=True
        )

    st.markdown("---")

# -------------------------------------------------
# PROCESSAMENTO DOS DADOS
# -------------------------------------------------
if st.session_state.file_uploaded and 'uploaded_file' in st.session_state:

    try:
        df_original = pd.read_excel(st.session_state.uploaded_file, header=0)

        colunas_necessarias = {
            0: "Código",
            1: "Código PEP",
            3: "Empresa",
            6: "Status",
            21: "Escopo",
            470: "Total Econ Pluri",
            471: "Total Exc Econ 2016 à 2025"
        }

        # Meses de 2026
        meses_2026 = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
        for i, mes in enumerate(meses_2026):
            colunas_necessarias[403 + i] = f"2026_{mes}"

        colunas_necessarias[415] = "Total_2026"

        # Meses de 2027
        for i, mes in enumerate(meses_2026):
            colunas_necessarias[416 + i] = f"2027_{mes}"

        colunas_necessarias[428] = "Total_2027"

        # Meses de 2028
        for i, mes in enumerate(meses_2026):
            colunas_necessarias[429 + i] = f"2028_{mes}"

        colunas_necessarias[441] = "Total_2028"

        # Anos de 2029 a 2056
        for i, ano in enumerate(range(2029, 2057)):
            colunas_necessarias[442 + i] = f"Total_{ano}"

        df_completo = pd.DataFrame()

        for idx, nome_col in colunas_necessarias.items():
            if idx < len(df_original.columns):
                df_completo[nome_col] = df_original.iloc[:, idx]
            else:
                df_completo[nome_col] = None

        df_completo = df_completo.dropna(subset=["Código", "Empresa"])
        st.session_state.df_completo = df_completo

        # =================================================
        # ABAS PRINCIPAIS REESTRUTURADAS
        # =================================================
        tab_analise_pep, tab_analise_codigo = st.tabs(
            ["📊 Análise por PEP", "🔢 Análise por Código"]
        )

        # =================================================
        # ABA 1 - ANÁLISE POR PEP
        # =================================================
        with tab_analise_pep:

            df_pep = df_completo[df_completo["Código PEP"].notna()].copy()
            df_pep = df_pep[df_pep["Código PEP"].astype(str).str.strip() != ""]

            st.markdown("### 🔎 Filtros de Análise")
            col_filtro1, col_filtro2 = st.columns(2)

            with col_filtro1:
                empresas_disponiveis_pep = sorted(df_pep["Empresa"].unique())
                empresas_selecionadas_pep = st.multiselect(
                    "Filtrar por empresas:",
                    options=empresas_disponiveis_pep,
                    default=empresas_disponiveis_pep,
                    help="Selecione uma ou mais empresas para análise",
                    key="filtro_empresas_pep"
                )

            with col_filtro2:
                if "Status" in df_pep.columns and df_pep["Status"].notna().any():
                    status_disponiveis_pep = sorted(df_pep["Status"].dropna().unique())
                    status_selecionados_pep = st.multiselect(
                        "Filtrar por status:",
                        options=status_disponiveis_pep,
                        default=status_disponiveis_pep,
                        help="Selecione um ou mais status para análise",
                        key="filtro_status_pep"
                    )
                else:
                    status_selecionados_pep = []

            df_pep_filtrado = df_pep[df_pep["Empresa"].isin(empresas_selecionadas_pep)]
            if status_selecionados_pep:
                df_pep_filtrado = df_pep_filtrado[df_pep_filtrado["Status"].isin(status_selecionados_pep)]

            st.markdown("---")

            st.markdown("### 📈 Indicadores Principais")

            kpi1, kpi2, kpi3, kpi4 = st.columns(4)

            with kpi1:
                total_projetos_pep = df_pep_filtrado["Código PEP"].nunique()
                st.metric(
                    label="🎯 Total de Códigos PEP",
                    value=f"{total_projetos_pep:,}",
                    help="Número total de códigos PEP únicos"
                )

            with kpi2:
                total_empresas_pep = df_pep_filtrado["Empresa"].nunique()
                st.metric(
                    label="🏢 Empresas com PEP",
                    value=total_empresas_pep,
                    help="Quantidade de empresas com códigos PEP"
                )

            with kpi3:
                media_pep = total_projetos_pep / total_empresas_pep if total_empresas_pep > 0 else 0
                st.metric(
                    label="📊 Média PEP/Empresa",
                    value=f"{media_pep:.1f}",
                    help="Média de códigos PEP por empresa"
                )

            with kpi4:
                total_status_pep = df_pep_filtrado["Status"].nunique() if "Status" in df_pep_filtrado.columns else 0
                st.metric(
                    label="📋 Status Diferentes",
                    value=total_status_pep,
                    help="Quantidade de status diferentes"
                )

            st.markdown("---")

            subtab_dashboard_pep, subtab_status_pep, subtab_busca_pep = st.tabs(
                ["📊 Dashboard Empresas", "📈 Dashboard Status", "🔎 Buscar PEP"]
            )

            # ========== SUB-ABA: DASHBOARD EMPRESAS (PEP) ==========
            with subtab_dashboard_pep:

                resumo_pep = (
                    df_pep_filtrado
                    .groupby("Empresa")["Código PEP"]
                    .nunique()
                    .reset_index()
                    .sort_values(by="Código PEP", ascending=False)
                )
                resumo_pep.rename(columns={"Código PEP": "Qtd PEP"}, inplace=True)
                resumo_pep["Percentual"] = (resumo_pep["Qtd PEP"] / resumo_pep["Qtd PEP"].sum() * 100).round(1)

                col_g1, col_g2 = st.columns(2)

                with col_g1:
                    st.markdown("#### 📊 Códigos PEP por Empresa")

                    max_valor = resumo_pep["Qtd PEP"].max()
                    y_max, tick_interval = calcular_y_max_com_margem(max_valor)

                    fig_bar = go.Figure()

                    fig_bar.add_trace(go.Bar(
                        x=resumo_pep["Empresa"],
                        y=resumo_pep["Qtd PEP"],
                        text=resumo_pep["Qtd PEP"],
                        textposition='outside',
                        textfont=dict(size=16, family="Inter", color=VALE_GREEN),
                        marker=dict(
                            color=resumo_pep["Qtd PEP"],
                            colorscale=[
                                [0, VALE_YELLOW],
                                [0.5, VALE_LIGHT_GREEN],
                                [1, VALE_GREEN]
                            ],
                            showscale=False,
                            line=dict(color=VALE_GREEN, width=2),
                        ),
                        hovertemplate='<b style="font-size:17px">%{x}</b><br>' +
                                      '<b>Códigos PEP:</b> %{y:,}<br>' +
                                      '<b>Participação:</b> %{customdata:.1f}%<br>' +
                                      '<extra></extra>',
                        customdata=resumo_pep["Percentual"],
                        hoverlabel=dict(
                            bgcolor=VALE_GREEN,
                            font_size=16,
                            font_family="Inter",
                            font_color="white",
                            bordercolor="white"
                        )
                    ))

                    fig_bar.update_layout(
                        height=620,
                        margin=dict(l=100, r=100, t=150, b=160),
                        xaxis_title="",
                        yaxis_title="Quantidade de PEP",
                        plot_bgcolor='rgba(0,0,0,0)',
                        paper_bgcolor='rgba(0,0,0,0)',
                        font=dict(size=14, family="Inter"),
                        xaxis=dict(
                            tickangle=-45,
                            automargin=True,
                            showgrid=False,
                            tickfont=dict(size=13, family="Inter"),
                            linecolor='rgba(0,128,124,0.2)',
                            linewidth=2
                        ),
                        yaxis=dict(
                            automargin=True,
                            showgrid=True,
                            gridcolor='rgba(0,128,124,0.08)',
                            gridwidth=2,
                            tickfont=dict(size=13, family="Inter"),
                            linecolor='rgba(0,128,124,0.2)',
                            linewidth=2,
                            range=[0, y_max],
                            dtick=tick_interval
                        )
                    )

                    st.plotly_chart(fig_bar, use_container_width=True, config={
                        'displayModeBar': True,
                        'displaylogo': False,
                        'modeBarButtonsToRemove': ['pan2d', 'lasso2d', 'select2d'],
                        'toImageButtonOptions': {
                            'format': 'png',
                            'filename': 'grafico_pep_empresas_vale',
                            'height': 1200,
                            'width': 1800,
                            'scale': 3
                        }
                    })

                with col_g2:
                    st.markdown("#### 🎯 Distribuição Percentual")

                    fig_pie = go.Figure()

                    fig_pie.add_trace(go.Pie(
                        labels=resumo_pep["Empresa"],
                        values=resumo_pep["Qtd PEP"],
                        hole=0.5,
                        marker=dict(
                            colors=PALETA_CORPORATIVA[:len(resumo_pep)],
                            line=dict(color='white', width=4)
                        ),
                        textinfo='percent',
                        textfont=dict(size=15, family="Inter", color='white'),
                        textposition='inside',
                        hovertemplate='<b style="font-size:17px">%{label}</b><br>' +
                                      '<b>Códigos PEP:</b> %{value:,}<br>' +
                                      '<b>Participação:</b> %{percent}<br>' +
                                      '<extra></extra>',
                        hoverlabel=dict(
                            bgcolor=VALE_GREEN,
                            font_size=16,
                            font_family="Inter",
                            font_color="white",
                            bordercolor="white"
                        ),
                        pull=[0.08] + [0.02] * (len(resumo_pep) - 1),
                        rotation=45,
                        direction='clockwise'
                    ))

                    fig_pie.update_layout(
                        height=620,
                        margin=dict(l=20, r=20, t=60, b=40),
                        showlegend=True,
                        paper_bgcolor='rgba(0,0,0,0)',
                        font=dict(size=13, family="Inter"),
                        legend=dict(
                            orientation="h",
                            yanchor="bottom",
                            y=-0.3,
                            xanchor="center",
                            x=0.5,
                            bgcolor='rgba(0,128,124,0.06)',
                            bordercolor=VALE_GREEN,
                            borderwidth=2,
                            font=dict(size=12, family="Inter")
                        ),
                        annotations=[dict(
                            text=f'<b>{total_projetos_pep:,}</b><br><span style="font-size:16px">PEPs</span>',
                            x=0.5, y=0.5,
                            font_size=24,
                            showarrow=False,
                            font=dict(family="Inter", color=VALE_GREEN)
                        )]
                    )

                    st.plotly_chart(fig_pie, use_container_width=True, config={
                        'displayModeBar': True,
                        'displaylogo': False,
                        'modeBarButtonsToRemove': ['pan2d', 'lasso2d', 'select2d'],
                        'toImageButtonOptions': {
                            'format': 'png',
                            'filename': 'grafico_distribuicao_pep_vale',
                            'height': 1200,
                            'width': 1800,
                            'scale': 3
                        }
                    })

                st.markdown("---")
                st.markdown("#### 📊 Resumo Estatístico")

                col_stats = st.columns([1, 2, 1])[1]

                with col_stats:
                    if len(resumo_pep) > 0:
                        st.markdown(f"""
                                                    <div style='text-align: center; padding: 2rem; background: linear-gradient(135deg, rgba(0,128,124,0.06) 0%, rgba(0,128,124,0.03) 100%); 
                                                         border-radius: 16px; border: 2px solid rgba(0,128,124,0.15);'>
                                                        <h3 style='color: {VALE_GREEN}; margin-bottom: 1.5rem;'>📈 Estatísticas Gerais</h3>
                                                        <div style='font-size: 1.1rem; line-height: 2;'>
                                                            <p><strong>Maior volume:</strong> {resumo_pep['Empresa'].iloc[0]}</p>
                                                            <p><strong>Códigos PEP:</strong> {resumo_pep['Qtd PEP'].iloc[0]:,}</p>
                                                            <p><strong>Participação:</strong> {resumo_pep['Percentual'].iloc[0]:.1f}%</p>
                                                            <hr style="border: 1px solid rgba(0,128,124,0.2); margin: 1rem 0;">
                                                            <p><strong>Total geral:</strong> {resumo_pep['Qtd PEP'].sum():,} PEPs</p>
                                                            <p style="margin: 0;"><strong>Empresas:</strong> {len(resumo_pep)}</p>
                                                        </div>
                                                    </div>
                                                    """, unsafe_allow_html=True)

            # ========== SUB-ABA: DASHBOARD STATUS (PEP) ==========
            with subtab_status_pep:

                st.markdown("#### 📈 Análise de Status dos Projetos PEP")

                if "Status" in df_pep_filtrado.columns and df_pep_filtrado["Status"].notna().any():

                    resumo_status_pep = (
                        df_pep_filtrado
                        .groupby("Status")["Código PEP"]
                        .nunique()
                        .reset_index()
                        .sort_values(by="Código PEP", ascending=False)
                    )
                    resumo_status_pep.rename(columns={"Código PEP": "Qtd PEP"}, inplace=True)
                    resumo_status_pep["Percentual"] = (resumo_status_pep["Qtd PEP"] / resumo_status_pep["Qtd PEP"].sum() * 100).round(1)

                    col_kpi1, col_kpi2, col_kpi3 = st.columns(3)

                    with col_kpi1:
                        st.metric(
                            label="📊 Status Diferentes",
                            value=len(resumo_status_pep),
                            help="Quantidade de status únicos"
                        )

                    with col_kpi2:
                        status_principal_pep = resumo_status_pep.iloc[0]["Status"] if len(resumo_status_pep) > 0 else "N/A"
                        st.metric(
                            label="🎯 Status Principal",
                            value=status_principal_pep,
                            help="Status com mais projetos"
                        )

                    with col_kpi3:
                        perc_principal_pep = resumo_status_pep.iloc[0]["Percentual"] if len(resumo_status_pep) > 0 else 0
                        st.metric(
                            label="📈 Concentração",
                            value=f"{perc_principal_pep:.1f}%",
                            help="Percentual do status principal"
                        )

                    st.markdown("---")

                    col_g1, col_g2 = st.columns(2)

                    with col_g1:
                        st.markdown("#### 📊 PEP por Status")

                        max_valor_status_pep = resumo_status_pep["Qtd PEP"].max()
                        y_max_status_pep, tick_interval_status_pep = calcular_y_max_com_margem(max_valor_status_pep)

                        fig_status_bar_pep = go.Figure()

                        fig_status_bar_pep.add_trace(go.Bar(
                            x=resumo_status_pep["Status"],
                            y=resumo_status_pep["Qtd PEP"],
                            text=resumo_status_pep["Qtd PEP"],
                            textposition='outside',
                            textfont=dict(size=16, family="Inter", color=VALE_YELLOW),
                            marker=dict(
                                color=resumo_status_pep["Qtd PEP"],
                                colorscale=[
                                    [0, "#f4a261"],
                                    [0.5, VALE_YELLOW],
                                    [1, VALE_GREEN]
                                ],
                                showscale=False,
                                line=dict(color=VALE_YELLOW, width=2)
                            ),
                            hovertemplate='<b style="font-size:17px">%{x}</b><br>' +
                                          '<b>Códigos PEP:</b> %{y:,}<br>' +
                                          '<b>Percentual:</b> %{customdata:.1f}%<br>' +
                                          '<extra></extra>',
                            customdata=resumo_status_pep["Percentual"],
                            hoverlabel=dict(
                                bgcolor=VALE_YELLOW,
                                font_size=16,
                                font_family="Inter",
                                font_color="white",
                                bordercolor="white"
                            )
                        ))

                        fig_status_bar_pep.update_layout(
                            height=620,
                            margin=dict(l=100, r=100, t=150, b=160),
                            xaxis_title="",
                            yaxis_title="Quantidade de PEP",
                            plot_bgcolor='rgba(0,0,0,0)',
                            paper_bgcolor='rgba(0,0,0,0)',
                            font=dict(size=14, family="Inter"),
                            xaxis=dict(
                                tickangle=-45,
                                automargin=True,
                                showgrid=False,
                                tickfont=dict(size=13, family="Inter"),
                                linecolor='rgba(238,167,34,0.2)',
                                linewidth=2
                            ),
                            yaxis=dict(
                                automargin=True,
                                showgrid=True,
                                gridcolor='rgba(238,167,34,0.08)',
                                gridwidth=2,
                                tickfont=dict(size=13, family="Inter"),
                                linecolor='rgba(238,167,34,0.2)',
                                linewidth=2,
                                range=[0, y_max_status_pep],
                                dtick=tick_interval_status_pep
                            )
                        )

                        st.plotly_chart(fig_status_bar_pep, use_container_width=True, config={
                            'displayModeBar': True,
                            'displaylogo': False,
                            'modeBarButtonsToRemove': ['pan2d', 'lasso2d', 'select2d'],
                            'toImageButtonOptions': {
                                'format': 'png',
                                'filename': 'grafico_status_pep_vale',
                                'height': 1200,
                                'width': 1800,
                                'scale': 3
                            }
                        })

                    with col_g2:
                        st.markdown("#### 🎯 Distribuição por Status")

                        fig_status_pie_pep = go.Figure()

                        fig_status_pie_pep.add_trace(go.Pie(
                            labels=resumo_status_pep["Status"],
                            values=resumo_status_pep["Qtd PEP"],
                            hole=0.5,
                            marker=dict(
                                colors=PALETA_CORPORATIVA[:len(resumo_status_pep)],
                                line=dict(color='white', width=4)
                            ),
                            textinfo='percent',
                            textfont=dict(size=15, family="Inter", color='white'),
                            textposition='inside',
                            hovertemplate='<b style="font-size:17px">%{label}</b><br>' +
                                          '<b>Códigos PEP:</b> %{value:,}<br>' +
                                          '<b>Percentual:</b> %{percent}<br>' +
                                          '<extra></extra>',
                            hoverlabel=dict(
                                bgcolor=VALE_YELLOW,
                                font_size=16,
                                font_family="Inter",
                                font_color="white",
                                bordercolor="white"
                            ),
                            pull=[0.08] + [0.02] * (len(resumo_status_pep) - 1),
                            rotation=45,
                            direction='clockwise'
                        ))

                        fig_status_pie_pep.update_layout(
                            height=620,
                            margin=dict(l=20, r=20, t=60, b=40),
                            showlegend=True,
                            paper_bgcolor='rgba(0,0,0,0)',
                            font=dict(size=13, family="Inter"),
                            legend=dict(
                                orientation="h",
                                yanchor="bottom",
                                y=-0.3,
                                xanchor="center",
                                x=0.5,
                                bgcolor='rgba(238,167,34,0.06)',
                                bordercolor=VALE_YELLOW,
                                borderwidth=2,
                                font=dict(size=12, family="Inter")
                            ),
                            annotations=[dict(
                                text=f'<b>{len(resumo_status_pep)}</b><br><span style="font-size:16px">Status</span>',
                                x=0.5, y=0.5,
                                font_size=24,
                                showarrow=False,
                                font=dict(family="Inter", color=VALE_YELLOW)
                            )]
                        )

                        st.plotly_chart(fig_status_pie_pep, use_container_width=True, config={
                            'displayModeBar': True,
                            'displaylogo': False,
                            'modeBarButtonsToRemove': ['pan2d', 'lasso2d', 'select2d'],
                            'toImageButtonOptions': {
                                'format': 'png',
                                'filename': 'grafico_status_distribuicao_vale',
                                'height': 1200,
                                'width': 1800,
                                'scale': 3
                            }
                        })

                    st.markdown("---")
                    st.markdown("#### 📋 Detalhamento por Status")

                    st.dataframe(
                        resumo_status_pep.style.format({
                            "Qtd PEP": "{:,}",
                            "Percentual": "{:.1f}%"
                        }).background_gradient(cmap='Greens', subset=['Qtd PEP']),
                        use_container_width=True,
                        height=350
                    )

                    st.markdown("---")
                    st.markdown("#### 🔄 Status x Empresa")

                    pivot_status_empresa_pep = df_pep_filtrado.groupby(["Status", "Empresa"])["Código PEP"].nunique().reset_index()
                    pivot_table_pep = pivot_status_empresa_pep.pivot(index="Status", columns="Empresa", values="Código PEP").fillna(0)

                    st.dataframe(
                        pivot_table_pep.style.background_gradient(cmap='Greens'),
                        use_container_width=True,
                        height=350
                    )

                    csv_status_pep = resumo_status_pep.to_csv(index=False).encode('utf-8-sig')
                    st.download_button(
                        label="📥 Exportar Análise de Status (CSV)",
                        data=csv_status_pep,
                        file_name="analise_status_pep.csv",
                        mime="text/csv",
                    )

                else:
                    st.warning("⚠️ Não há informações de status disponíveis para análise.")

            # ========== SUB-ABA: BUSCAR PEP (COM DETALHES COMPLETOS) ==========
            with subtab_busca_pep:

                st.markdown('<div class="search-container">', unsafe_allow_html=True)
                st.markdown('<p class="search-title">🔎 Busca Detalhada por Código PEP</p>', unsafe_allow_html=True)

                col_busca1, col_busca2 = st.columns([3, 1])

                with col_busca1:
                    codigo_pep_busca = st.text_input(
                        "Digite o código PEP:",
                        placeholder="Ex: C144044",
                        help="Busca inteligente - não diferencia maiúsculas/minúsculas",
                        key="busca_pep_detalhado"
                    )

                with col_busca2:
                    tipo_busca_pep = st.selectbox(
                        "Tipo:",
                        ["Contém", "Começa com", "Termina com", "Exato"],
                        key="tipo_busca_pep_detalhado"
                    )

                st.markdown('</div>', unsafe_allow_html=True)

                if codigo_pep_busca:
                    codigo_str_pep = df_pep_filtrado["Código PEP"].astype(str)

                    if tipo_busca_pep == "Contém":
                        resultado_pep = df_pep_filtrado[codigo_str_pep.str.contains(codigo_pep_busca, case=False, na=False)]
                    elif tipo_busca_pep == "Começa com":
                        resultado_pep = df_pep_filtrado[codigo_str_pep.str.startswith(codigo_pep_busca, na=False)]
                    elif tipo_busca_pep == "Termina com":
                        resultado_pep = df_pep_filtrado[codigo_str_pep.str.endswith(codigo_pep_busca, na=False)]
                    else:
                        resultado_pep = df_pep_filtrado[codigo_str_pep.str.lower() == codigo_pep_busca.lower()]

                    if not resultado_pep.empty:
                        st.success(f"✅ **{len(resultado_pep)} projeto(s) encontrado(s)**")
                        st.markdown("---")

                        for idx, row in resultado_pep.iterrows():
                            st.markdown(f'''
                                                            <div class="result-card" style="padding: 1.5rem;">
                                                                <div style="width: 100%; text-align: center; margin-bottom: 1.5rem; padding: 1.3rem; 
                                                                     background: linear-gradient(135deg, rgba(0,128,124,0.08) 0%, rgba(0,128,124,0.04) 100%); 
                                                                     border-radius: 12px; border: 2px solid rgba(0,128,124,0.2);">
                                                                    <p style="margin: 0 auto 0.6rem auto; font-size: 0.75rem; font-weight: 700; 
                                                                       color: {VALE_GREY}; text-transform: uppercase; letter-spacing: 2px; 
                                                                       display: block; width: 100%;">
                                                                        🔢 CÓDIGO PEP
                                                                    </p>
                                                                    <h2 style="color: {VALE_GREEN}; margin: 0 auto; font-size: 2.2rem; font-weight: 900; 
                                                                        letter-spacing: 0.5px; display: block; width: 100%;">
                                                                        {row["Código PEP"]}
                                                                    </h2>
                                                                </div>
                                                        ''', unsafe_allow_html=True)

                            col1, col2 = st.columns(2)

                            with col1:
                                empresa_text = row['Empresa'] if pd.notna(row['Empresa']) else 'Não informado'
                                st.markdown(f'''
                                                                <div class="info-card">
                                                                    <span class="info-card-label">🏢 Empresa Responsável</span>
                                                                    <h3 style='color: {VALE_GREEN}; margin: 0.5rem 0;'>{empresa_text}</h3>
                                                                </div>
                                                            ''', unsafe_allow_html=True)

                                status_texto = row['Status'] if pd.notna(row['Status']) else 'Não informado'
                                st.markdown(f'''
                                                                <div class="info-card">
                                                                    <span class="info-card-label">📊 Status do Projeto</span>
                                                                    <h3 style='color: {VALE_YELLOW}; margin: 0.5rem 0;'>{status_texto}</h3>
                                                                </div>
                                                            ''', unsafe_allow_html=True)

                            with col2:
                                codigo_projeto_texto = row['Código'] if pd.notna(row['Código']) else 'Não informado'
                                st.markdown(f'''
                                                                <div class="info-card">
                                                                    <span class="info-card-label">📄 Código do Projeto</span>
                                                                    <h3 style='color: {VALE_GREEN}; margin: 0.5rem 0;'>{codigo_projeto_texto}</h3>
                                                                </div>
                                                            ''', unsafe_allow_html=True)

                            st.markdown('<div class="escopo-container">', unsafe_allow_html=True)
                            st.markdown('<span class="escopo-label">📝 Escopo do Projeto</span>', unsafe_allow_html=True)
                            if pd.notna(row['Escopo']) and str(row['Escopo']).strip() != "":
                                st.markdown(f'<div class="escopo-text">{row["Escopo"]}</div>', unsafe_allow_html=True)
                            else:
                                st.markdown('<div class="escopo-text"><i>Escopo não informado para este projeto.</i></div>', unsafe_allow_html=True)
                            st.markdown('</div>', unsafe_allow_html=True)

                            # GRÁFICO DE ECONOMIA - TOTAIS ANUAIS
                            st.markdown("---")
                            st.markdown("### 💰 Análise de Economia Projetada (2026-2056)")

                            anos = list(range(2026, 2057))
                            valores_anuais = []

                            for ano in [2026, 2027, 2028]:
                                col_total = f"Total_{ano}"
                                if col_total in row.index and pd.notna(row[col_total]):
                                    try:
                                        valores_anuais.append(float(row[col_total]))
                                    except:
                                        valores_anuais.append(0)
                                else:
                                    valores_anuais.append(0)

                            for ano in range(2029, 2057):
                                col_total = f"Total_{ano}"
                                if col_total in row.index and pd.notna(row[col_total]):
                                    try:
                                        valores_anuais.append(float(row[col_total]))
                                    except:
                                        valores_anuais.append(0)
                                else:
                                    valores_anuais.append(0)

                            fig_economia = go.Figure()

                            fig_economia.add_trace(go.Scatter(
                                x=anos,
                                y=valores_anuais,
                                mode='lines+markers',
                                name='Economia Anual',
                                line=dict(color=VALE_GREEN, width=4),
                                marker=dict(size=10, color=VALE_GREEN, symbol='circle',
                                            line=dict(color='white', width=2)),
                                fill='tozeroy',
                                fillcolor='rgba(0,128,124,0.15)',
                                hovertemplate='<b>Ano:</b> %{x}<br>' +
                                              '<b>Economia:</b> R$ %{y:,.2f}<br>' +
                                              '<extra></extra>',
                                hoverlabel=dict(
                                    bgcolor=VALE_GREEN,
                                    font_size=15,
                                    font_family="Inter",
                                    font_color="white"
                                )
                            ))

                            fig_economia.update_layout(
                                height=700,
                                margin=dict(l=100, r=100, t=120, b=100),
                                xaxis_title="Ano",
                                yaxis_title="Economia (R$)",
                                plot_bgcolor='rgba(0,0,0,0)',
                                paper_bgcolor='rgba(0,0,0,0)',
                                font=dict(size=14, family="Inter"),
                                xaxis=dict(
                                    showgrid=True,
                                    gridcolor='rgba(0,128,124,0.08)',
                                    tickfont=dict(size=13, family="Inter"),
                                    linecolor='rgba(0,128,124,0.2)',
                                    linewidth=2,
                                    dtick=2,
                                    tickangle=-45
                                ),
                                yaxis=dict(
                                    showgrid=True,
                                    gridcolor='rgba(0,128,124,0.08)',
                                    tickfont=dict(size=13, family="Inter"),
                                    linecolor='rgba(0,128,124,0.2)',
                                    linewidth=2,
                                    tickformat=',.0f'
                                ),
                                hovermode='x unified',
                                title=dict(
                                    text=f"<b>Projeção de Economia Anual - PEP {row['Código PEP']}</b>",
                                    font=dict(size=20, family="Inter", color=VALE_GREEN),
                                    x=0.5,
                                    xanchor='center'
                                )
                            )

                            st.plotly_chart(fig_economia, use_container_width=True, config={
                                'displayModeBar': True,
                                'displaylogo': False,
                                'modeBarButtonsToRemove': ['pan2d', 'lasso2d', 'select2d'],
                                'toImageButtonOptions': {
                                    'format': 'png',
                                    'filename': f'economia_anual_pep_{row["Código PEP"]}',
                                    'height': 1400,
                                    'width': 2400,
                                    'scale': 3
                                }
                            })

                            # DETALHAMENTO MENSAL
                            st.markdown("---")
                            st.markdown("### 📅 Detalhamento Mensal (2026-2028)")

                            col_ano_sel = st.columns([1, 2, 1])[1]
                            with col_ano_sel:
                                ano_selecionado = st.selectbox(
                                    "Selecione o ano para ver detalhamento mensal:",
                                    [2026, 2027, 2028],
                                    key=f"ano_mensal_pep_{idx}"
                                )

                            meses_nomes = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
                            valores_mensais = []

                            for mes in meses_nomes:
                                col_mes = f"{ano_selecionado}_{mes}"
                                if col_mes in row.index and pd.notna(row[col_mes]):
                                    try:
                                        valores_mensais.append(float(row[col_mes]))
                                    except:
                                        valores_mensais.append(0)
                                else:
                                    valores_mensais.append(0)

                            fig_mensal = go.Figure()

                            fig_mensal.add_trace(go.Bar(
                                x=meses_nomes,
                                y=valores_mensais,
                                text=[f"R$ {v:,.2f}" for v in valores_mensais],
                                textposition='outside',
                                textfont=dict(size=12, family="Inter", color=VALE_YELLOW),
                                marker=dict(
                                    color=valores_mensais,
                                    colorscale=[
                                        [0, VALE_YELLOW],
                                        [0.5, VALE_LIGHT_GREEN],
                                        [1, VALE_GREEN]
                                    ],
                                    showscale=False,
                                    line=dict(color=VALE_YELLOW, width=2)
                                ),
                                hovertemplate=f'<b>%{{x}}/{ano_selecionado}</b><br>' +
                                              '<b>Economia:</b> R$ %{y:,.2f}<br>' +
                                              '<extra></extra>',
                                hoverlabel=dict(
                                    bgcolor=VALE_YELLOW,
                                    font_size=14,
                                    font_family="Inter",
                                    font_color="white"
                                )
                            ))

                            fig_mensal.update_layout(
                                height=550,
                                margin=dict(l=80, r=80, t=100, b=80),
                                xaxis_title="Mês",
                                yaxis_title="Economia (R$)",
                                plot_bgcolor='rgba(0,0,0,0)',
                                paper_bgcolor='rgba(0,0,0,0)',
                                font=dict(size=13, family="Inter"),
                                xaxis=dict(
                                    showgrid=False,
                                    tickfont=dict(size=12, family="Inter"),
                                    linecolor='rgba(238,167,34,0.2)',
                                    linewidth=2
                                ),
                                yaxis=dict(
                                    showgrid=True,
                                    gridcolor='rgba(238,167,34,0.08)',
                                    tickfont=dict(size=12, family="Inter"),
                                    linecolor='rgba(238,167,34,0.2)',
                                    linewidth=2,
                                    tickformat=',.0f'
                                ),
                                title=dict(
                                    text=f"<b>Detalhamento Mensal - {ano_selecionado}</b>",
                                    font=dict(size=18, family="Inter", color=VALE_YELLOW),
                                    x=0.5,
                                    xanchor='center'
                                )
                            )

                            st.plotly_chart(fig_mensal, use_container_width=True, config={
                                'displayModeBar': True,
                                'displaylogo': False,
                                'modeBarButtonsToRemove': ['pan2d', 'lasso2d', 'select2d'],
                                'toImageButtonOptions': {
                                    'format': 'png',
                                    'filename': f'economia_mensal_{ano_selecionado}_pep_{row["Código PEP"]}',
                                    'height': 1200,
                                    'width': 2000,
                                    'scale': 3
                                }
                            })

                            # Métricas de totais
                            st.markdown("---")
                            st.markdown("#### 📊 Totais de Economia")
                            col_econ1, col_econ2, col_econ3 = st.columns(3)

                            with col_econ1:
                                total_econ_pluri = row['Total Econ Pluri'] if pd.notna(row['Total Econ Pluri']) else 0
                                try:
                                    total_econ_pluri = float(total_econ_pluri)
                                except:
                                    total_econ_pluri = 0
                                st.metric(
                                    label="💰 Total Econ Plurianual",
                                    value=f"R$ {total_econ_pluri:,.2f}",
                                    help="Coluna RC - Total de economia plurianual"
                                )

                            with col_econ2:
                                total_exc_econ = row['Total Exc Econ 2016 à 2025'] if pd.notna(row['Total Exc Econ 2016 à 2025']) else 0
                                try:
                                    total_exc_econ = float(total_exc_econ)
                                except:
                                    total_exc_econ = 0
                                st.metric(
                                    label="📈 Total Exc Econ 2016-2025",
                                    value=f"R$ {total_exc_econ:,.2f}",
                                    help="Coluna RD - Total exceto economia 2016 a 2025"
                                )

                            with col_econ3:
                                total_mes_selecionado = sum(valores_mensais)
                                st.metric(
                                    label=f"📅 Total {ano_selecionado}",
                                    value=f"R$ {total_mes_selecionado:,.2f}",
                                    help=f"Total mensal de {ano_selecionado}"
                                )

                            st.markdown('</div>', unsafe_allow_html=True)

                        st.markdown("---")
                        st.markdown("### 📋 Resumo de Todos os Resultados")
                        st.dataframe(
                            resultado_pep[["Código", "Código PEP", "Empresa", "Status", "Escopo"]].reset_index(drop=True),
                            use_container_width=True,
                            height=300
                        )

                        csv_resultado_pep = resultado_pep.to_csv(index=False).encode('utf-8-sig')
                        st.download_button(
                            label="📥 Baixar Todos os Resultados (CSV)",
                            data=csv_resultado_pep,
                            file_name=f"busca_pep_{codigo_pep_busca}.csv",
                            mime="text/csv",
                        )
                    else:
                        st.warning("⚠️ Nenhum código PEP encontrado com esse critério.")
                else:
                    st.info("💡 **Como usar:** Digite o código PEP no campo acima para visualizar todas as informações detalhadas, incluindo análise de economia anual e mensal.")

                    with st.expander("📋 Ver exemplos de códigos PEP disponíveis"):
                        exemplos_pep = df_pep["Código PEP"].head(10).tolist()
                        st.markdown("**Códigos PEP de exemplo na base:**")
                        for cod in exemplos_pep:
                            st.markdown(f"- `{cod}`")

        # =================================================
        # ABA 2 - ANÁLISE POR CÓDIGO
        # =================================================
        with tab_analise_codigo:

            st.markdown("### 🔎 Filtros de Análise")
            col_filtro1_cod, col_filtro2_cod = st.columns(2)

            with col_filtro1_cod:
                empresas_disponiveis_cod = sorted(df_completo["Empresa"].unique())
                empresas_selecionadas_cod = st.multiselect(
                    "Filtrar por empresas:",
                    options=empresas_disponiveis_cod,
                    default=empresas_disponiveis_cod,
                    help="Selecione uma ou mais empresas para análise",
                    key="filtro_empresas_codigo"
                )

            with col_filtro2_cod:
                if "Status" in df_completo.columns and df_completo["Status"].notna().any():
                    status_disponiveis_cod = sorted(df_completo["Status"].dropna().unique())
                    status_selecionados_cod = st.multiselect(
                        "Filtrar por status:",
                        options=status_disponiveis_cod,
                        default=status_disponiveis_cod,
                        help="Selecione um ou mais status para análise",
                        key="filtro_status_codigo"
                    )
                else:
                    status_selecionados_cod = []

            df_codigo_filtrado = df_completo[df_completo["Empresa"].isin(empresas_selecionadas_cod)]
            if status_selecionados_cod:
                df_codigo_filtrado = df_codigo_filtrado[df_codigo_filtrado["Status"].isin(status_selecionados_cod)]

            st.markdown("---")

            st.markdown("### 📈 Indicadores Principais")

            kpi1_cod, kpi2_cod, kpi3_cod, kpi4_cod = st.columns(4)

            with kpi1_cod:
                total_projetos_cod = df_codigo_filtrado["Código"].nunique()
                st.metric(
                    label="🎯 Total de Códigos",
                    value=f"{total_projetos_cod:,}",
                    help="Número total de códigos únicos"
                )

            with kpi2_cod:
                total_empresas_cod = df_codigo_filtrado["Empresa"].nunique()
                st.metric(
                    label="🏢 Empresas",
                    value=total_empresas_cod,
                    help="Quantidade de empresas"
                )

            with kpi3_cod:
                media_cod = total_projetos_cod / total_empresas_cod if total_empresas_cod > 0 else 0
                st.metric(
                    label="📊 Média Código/Empresa",
                    value=f"{media_cod:.1f}",
                    help="Média de códigos por empresa"
                )

            with kpi4_cod:
                total_status_cod = df_codigo_filtrado["Status"].nunique() if "Status" in df_codigo_filtrado.columns else 0
                st.metric(
                    label="📋 Status Diferentes",
                    value=total_status_cod,
                    help="Quantidade de status diferentes"
                )

            st.markdown("---")

            subtab_dashboard_cod, subtab_status_cod, subtab_busca_cod = st.tabs(
                ["📊 Dashboard Empresas", "📈 Dashboard Status", "🔎 Buscar por Código"]
            )

            # ========== SUB-ABA: DASHBOARD EMPRESAS (CÓDIGO) ==========
            with subtab_dashboard_cod:

                resumo_cod = (
                    df_codigo_filtrado
                    .groupby("Empresa")["Código"]
                    .nunique()
                    .reset_index()
                    .sort_values(by="Código", ascending=False)
                )
                resumo_cod.rename(columns={"Código": "Qtd Código"}, inplace=True)
                resumo_cod["Percentual"] = (resumo_cod["Qtd Código"] / resumo_cod["Qtd Código"].sum() * 100).round(1)

                col_g1, col_g2 = st.columns(2)

                with col_g1:
                    st.markdown("#### 📊 Códigos por Empresa")

                    max_valor_cod = resumo_cod["Qtd Código"].max()
                    y_max_cod, tick_interval_cod = calcular_y_max_com_margem(max_valor_cod)

                    fig_bar_cod = go.Figure()

                    fig_bar_cod.add_trace(go.Bar(
                        x=resumo_cod["Empresa"],
                        y=resumo_cod["Qtd Código"],
                        text=resumo_cod["Qtd Código"],
                        textposition='outside',
                        textfont=dict(size=16, family="Inter", color=VALE_GREEN),
                        marker=dict(
                            color=resumo_cod["Qtd Código"],
                            colorscale=[
                                [0, VALE_YELLOW],
                                [0.5, VALE_LIGHT_GREEN],
                                [1, VALE_GREEN]
                            ],
                            showscale=False,
                            line=dict(color=VALE_GREEN, width=2),
                        ),
                        hovertemplate='<b style="font-size:17px">%{x}</b><br>' +
                                      '<b>Códigos:</b> %{y:,}<br>' +
                                      '<b>Participação:</b> %{customdata:.1f}%<br>' +
                                      '<extra></extra>',
                        customdata=resumo_cod["Percentual"],
                        hoverlabel=dict(
                            bgcolor=VALE_GREEN,
                            font_size=16,
                            font_family="Inter",
                            font_color="white",
                            bordercolor="white"
                        )
                    ))

                    fig_bar_cod.update_layout(
                        height=620,
                        margin=dict(l=100, r=100, t=150, b=160),
                        xaxis_title="",
                        yaxis_title="Quantidade de Códigos",
                        plot_bgcolor='rgba(0,0,0,0)',
                        paper_bgcolor='rgba(0,0,0,0)',
                        font=dict(size=14, family="Inter"),
                        xaxis=dict(
                            tickangle=-45,
                            automargin=True,
                            showgrid=False,
                            tickfont=dict(size=13, family="Inter"),
                            linecolor='rgba(0,128,124,0.2)',
                            linewidth=2
                        ),
                        yaxis=dict(
                            automargin=True,
                            showgrid=True,
                            gridcolor='rgba(0,128,124,0.08)',
                            gridwidth=2,
                            tickfont=dict(size=13, family="Inter"),
                            linecolor='rgba(0,128,124,0.2)',
                            linewidth=2,
                            range=[0, y_max_cod],
                            dtick=tick_interval_cod
                        )
                    )

                    st.plotly_chart(fig_bar_cod, use_container_width=True, config={
                        'displayModeBar': True,
                        'displaylogo': False,
                        'modeBarButtonsToRemove': ['pan2d', 'lasso2d', 'select2d'],
                        'toImageButtonOptions': {
                            'format': 'png',
                            'filename': 'grafico_codigo_empresas_vale',
                            'height': 1200,
                            'width': 1800,
                            'scale': 3
                        }
                    })

                with col_g2:
                    st.markdown("#### 🎯 Distribuição Percentual")

                    fig_pie_cod = go.Figure()

                    fig_pie_cod.add_trace(go.Pie(
                        labels=resumo_cod["Empresa"],
                        values=resumo_cod["Qtd Código"],
                        hole=0.5,
                        marker=dict(
                            colors=PALETA_CORPORATIVA[:len(resumo_cod)],
                            line=dict(color='white', width=4)
                        ),
                        textinfo='percent',
                        textfont=dict(size=15, family="Inter", color='white'),
                        textposition='inside',
                        hovertemplate='<b style="font-size:17px">%{label}</b><br>' +
                                      '<b>Códigos:</b> %{value:,}<br>' +
                                      '<b>Participação:</b> %{percent}<br>' +
                                      '<extra></extra>',
                        hoverlabel=dict(
                            bgcolor=VALE_GREEN,
                            font_size=16,
                            font_family="Inter",
                            font_color="white",
                            bordercolor="white"
                        ),
                        pull=[0.08] + [0.02] * (len(resumo_cod) - 1),
                        rotation=45,
                        direction='clockwise'
                    ))

                    fig_pie_cod.update_layout(
                        height=620,
                        margin=dict(l=20, r=20, t=60, b=40),
                        showlegend=True,
                        paper_bgcolor='rgba(0,0,0,0)',
                        font=dict(size=13, family="Inter"),
                        legend=dict(
                            orientation="h",
                            yanchor="bottom",
                            y=-0.3,
                            xanchor="center",
                            x=0.5,
                            bgcolor='rgba(0,128,124,0.06)',
                            bordercolor=VALE_GREEN,
                            borderwidth=2,
                            font=dict(size=12, family="Inter")
                        ),
                        annotations=[dict(
                            text=f'<b>{total_projetos_cod:,}</b><br><span style="font-size:16px">Códigos</span>',
                            x=0.5, y=0.5,
                            font_size=24,
                            showarrow=False,
                            font=dict(family="Inter", color=VALE_GREEN)
                        )]
                    )

                    st.plotly_chart(fig_pie_cod, use_container_width=True, config={
                        'displayModeBar': True,
                        'displaylogo': False,
                        'modeBarButtonsToRemove': ['pan2d', 'lasso2d', 'select2d'],
                        'toImageButtonOptions': {
                            'format': 'png',
                            'filename': 'grafico_distribuicao_codigo_vale',
                            'height': 1200,
                            'width': 1800,
                            'scale': 3
                        }
                    })

                st.markdown("---")
                st.markdown("#### 📊 Resumo Estatístico")

                col_stats_cod = st.columns([1, 2, 1])[1]

                with col_stats_cod:
                    if len(resumo_cod) > 0:
                        st.markdown(f"""
                        <div style='text-align: center; padding: 2rem; background: linear-gradient(135deg, rgba(0,128,124,0.06) 0%, rgba(0,128,124,0.03) 100%); 
                             border-radius: 16px; border: 2px solid rgba(0,128,124,0.15);'>
                            <h3 style='color: {VALE_GREEN}; margin-bottom: 1.5rem;'>📈 Estatísticas Gerais</h3>
                            <div style='font-size: 1.1rem; line-height: 2;'>
                                <p><strong>Maior volume:</strong> {resumo_cod['Empresa'].iloc[0]}</p>
                                <p><strong>Códigos:</strong> {resumo_cod['Qtd Código'].iloc[0]:,}</p>
                                <p><strong>Participação:</strong> {resumo_cod['Percentual'].iloc[0]:.1f}%</p>
                                <hr style="border: 1px solid rgba(0,128,124,0.2); margin: 1rem 0;">
                                <p><strong>Total geral:</strong> {resumo_cod['Qtd Código'].sum():,} Códigos</p>
                                <p style="margin: 0;"><strong>Empresas:</strong> {len(resumo_cod)}</p>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)

            # ========== SUB-ABA: DASHBOARD STATUS (CÓDIGO) ==========
            with subtab_status_cod:

                st.markdown("#### 📈 Análise de Status dos Projetos por Código")

                if "Status" in df_codigo_filtrado.columns and df_codigo_filtrado["Status"].notna().any():

                    resumo_status_cod = (
                        df_codigo_filtrado
                        .groupby("Status")["Código"]
                        .nunique()
                        .reset_index()
                        .sort_values(by="Código", ascending=False)
                    )
                    resumo_status_cod.rename(columns={"Código": "Qtd Código"}, inplace=True)
                    resumo_status_cod["Percentual"] = (resumo_status_cod["Qtd Código"] / resumo_status_cod["Qtd Código"].sum() * 100).round(1)

                    col_kpi1_cod, col_kpi2_cod, col_kpi3_cod = st.columns(3)

                    with col_kpi1_cod:
                        st.metric(
                            label="📊 Status Diferentes",
                            value=len(resumo_status_cod),
                            help="Quantidade de status únicos"
                        )

                    with col_kpi2_cod:
                        status_principal_cod = resumo_status_cod.iloc[0]["Status"] if len(resumo_status_cod) > 0 else "N/A"
                        st.metric(
                            label="🎯 Status Principal",
                            value=status_principal_cod,
                            help="Status com mais projetos"
                        )

                    with col_kpi3_cod:
                        perc_principal_cod = resumo_status_cod.iloc[0]["Percentual"] if len(resumo_status_cod) > 0 else 0
                        st.metric(
                            label="📈 Concentração",
                            value=f"{perc_principal_cod:.1f}%",
                            help="Percentual do status principal"
                        )

                    st.markdown("---")

                    col_g1_cod, col_g2_cod = st.columns(2)

                    with col_g1_cod:
                        st.markdown("#### 📊 Códigos por Status")

                        max_valor_status_cod = resumo_status_cod["Qtd Código"].max()
                        y_max_status_cod, tick_interval_status_cod = calcular_y_max_com_margem(max_valor_status_cod)

                        fig_status_bar_cod = go.Figure()

                        fig_status_bar_cod.add_trace(go.Bar(
                            x=resumo_status_cod["Status"],
                            y=resumo_status_cod["Qtd Código"],
                            text=resumo_status_cod["Qtd Código"],
                            textposition='outside',
                            textfont=dict(size=16, family="Inter", color=VALE_YELLOW),
                            marker=dict(
                                color=resumo_status_cod["Qtd Código"],
                                colorscale=[
                                    [0, "#f4a261"],
                                    [0.5, VALE_YELLOW],
                                    [1, VALE_GREEN]
                                ],
                                showscale=False,
                                line=dict(color=VALE_YELLOW, width=2)
                            ),
                            hovertemplate='<b style="font-size:17px">%{x}</b><br>' +
                                          '<b>Códigos:</b> %{y:,}<br>' +
                                          '<b>Percentual:</b> %{customdata:.1f}%<br>' +
                                          '<extra></extra>',
                            customdata=resumo_status_cod["Percentual"],
                            hoverlabel=dict(
                                bgcolor=VALE_YELLOW,
                                font_size=16,
                                font_family="Inter",
                                font_color="white",
                                bordercolor="white"
                            )
                        ))

                        fig_status_bar_cod.update_layout(
                            height=620,
                            margin=dict(l=100, r=100, t=150, b=160),
                            xaxis_title="",
                            yaxis_title="Quantidade de Códigos",
                            plot_bgcolor='rgba(0,0,0,0)',
                            paper_bgcolor='rgba(0,0,0,0)',
                            font=dict(size=14, family="Inter"),
                            xaxis=dict(
                                tickangle=-45,
                                automargin=True,
                                showgrid=False,
                                tickfont=dict(size=13, family="Inter"),
                                linecolor='rgba(238,167,34,0.2)',
                                linewidth=2
                            ),
                            yaxis=dict(
                                automargin=True,
                                showgrid=True,
                                gridcolor='rgba(238,167,34,0.08)',
                                gridwidth=2,
                                tickfont=dict(size=13, family="Inter"),
                                linecolor='rgba(238,167,34,0.2)',
                                linewidth=2,
                                range=[0, y_max_status_cod],
                                dtick=tick_interval_status_cod
                            )
                        )

                        st.plotly_chart(fig_status_bar_cod, use_container_width=True, config={
                            'displayModeBar': True,
                            'displaylogo': False,
                            'modeBarButtonsToRemove': ['pan2d', 'lasso2d', 'select2d'],
                            'toImageButtonOptions': {
                                'format': 'png',
                                'filename': 'grafico_status_codigo_vale',
                                'height': 1200,
                                'width': 1800,
                                'scale': 3
                            }
                        })

                    with col_g2_cod:
                        st.markdown("#### 🎯 Distribuição por Status")

                        fig_status_pie_cod = go.Figure()

                        fig_status_pie_cod.add_trace(go.Pie(
                            labels=resumo_status_cod["Status"],
                            values=resumo_status_cod["Qtd Código"],
                            hole=0.5,
                            marker=dict(
                                colors=PALETA_CORPORATIVA[:len(resumo_status_cod)],
                                line=dict(color='white', width=4)
                            ),
                            textinfo='percent',
                            textfont=dict(size=15, family="Inter", color='white'),
                            textposition='inside',
                            hovertemplate='<b style="font-size:17px">%{label}</b><br>' +
                                          '<b>Códigos:</b> %{value:,}<br>' +
                                          '<b>Percentual:</b> %{percent}<br>' +
                                          '<extra></extra>',
                            hoverlabel=dict(
                                bgcolor=VALE_YELLOW,
                                font_size=16,
                                font_family="Inter",
                                font_color="white",
                                bordercolor="white"
                            ),
                            pull=[0.08] + [0.02] * (len(resumo_status_cod) - 1),
                            rotation=45,
                            direction='clockwise'
                        ))

                        fig_status_pie_cod.update_layout(
                            height=620,
                            margin=dict(l=20, r=20, t=60, b=40),
                            showlegend=True,
                            paper_bgcolor='rgba(0,0,0,0)',
                            font=dict(size=13, family="Inter"),
                            legend=dict(
                                orientation="h",
                                yanchor="bottom",
                                y=-0.3,
                                xanchor="center",
                                x=0.5,
                                bgcolor='rgba(238,167,34,0.06)',
                                bordercolor=VALE_YELLOW,
                                borderwidth=2,
                                font=dict(size=12, family="Inter")
                            ),
                            annotations=[dict(
                                text=f'<b>{len(resumo_status_cod)}</b><br><span style="font-size:16px">Status</span>',
                                x=0.5, y=0.5,
                                font_size=24,
                                showarrow=False,
                                font=dict(family="Inter", color=VALE_YELLOW)
                            )]
                        )

                        st.plotly_chart(fig_status_pie_cod, use_container_width=True, config={
                            'displayModeBar': True,
                            'displaylogo': False,
                            'modeBarButtonsToRemove': ['pan2d', 'lasso2d', 'select2d'],
                            'toImageButtonOptions': {
                                'format': 'png',
                                'filename': 'grafico_status_distribuicao_codigo_vale',
                                'height': 1200,
                                'width': 1800,
                                'scale': 3
                            }
                        })

                    st.markdown("---")
                    st.markdown("#### 📋 Detalhamento por Status")

                    st.dataframe(
                        resumo_status_cod.style.format({
                            "Qtd Código": "{:,}",
                            "Percentual": "{:.1f}%"
                        }).background_gradient(cmap='Greens', subset=['Qtd Código']),
                        use_container_width=True,
                        height=350
                    )

                    st.markdown("---")
                    st.markdown("#### 🔄 Status x Empresa")

                    pivot_status_empresa_cod = df_codigo_filtrado.groupby(["Status", "Empresa"])["Código"].nunique().reset_index()
                    pivot_table_cod = pivot_status_empresa_cod.pivot(index="Status", columns="Empresa", values="Código").fillna(0)

                    st.dataframe(
                        pivot_table_cod.style.background_gradient(cmap='Greens'),
                        use_container_width=True,
                        height=350
                    )

                    csv_status_cod = resumo_status_cod.to_csv(index=False).encode('utf-8-sig')
                    st.download_button(
                        label="📥 Exportar Análise de Status (CSV)",
                        data=csv_status_cod,
                        file_name="analise_status_codigo.csv",
                        mime="text/csv",
                    )

                else:
                    st.warning("⚠️ Não há informações de status disponíveis para análise.")

            # ========== SUB-ABA: BUSCAR POR CÓDIGO (COM DETALHES COMPLETOS) ==========
            with subtab_busca_cod:

                st.markdown('<div class="search-container">', unsafe_allow_html=True)
                st.markdown('<p class="search-title">🔎 Busca Detalhada por Código do Projeto</p>', unsafe_allow_html=True)

                col_busca_cod1, col_busca_cod2 = st.columns([3, 1])

                with col_busca_cod1:
                    codigo_busca = st.text_input(
                        "Digite o código do projeto:",
                        placeholder="Ex: 2358",
                        help="Busca pelo código da Coluna A",
                        key="busca_codigo_projeto"
                    )

                with col_busca_cod2:
                    tipo_busca_codigo = st.selectbox(
                        "Tipo:",
                        ["Contém", "Começa com", "Termina com", "Exato"],
                        key="tipo_busca_codigo"
                    )

                st.markdown('</div>', unsafe_allow_html=True)

                if codigo_busca:
                    codigo_str = df_codigo_filtrado["Código"].astype(str)

                    if tipo_busca_codigo == "Contém":
                        resultado_codigo = df_codigo_filtrado[codigo_str.str.contains(codigo_busca, case=False, na=False)]
                    elif tipo_busca_codigo == "Começa com":
                        resultado_codigo = df_codigo_filtrado[codigo_str.str.startswith(codigo_busca, na=False)]
                    elif tipo_busca_codigo == "Termina com":
                        resultado_codigo = df_codigo_filtrado[codigo_str.str.endswith(codigo_busca, na=False)]
                    else:
                        resultado_codigo = df_codigo_filtrado[codigo_str.str.lower() == codigo_busca.lower()]

                    if not resultado_codigo.empty:
                        st.success(f"✅ **{len(resultado_codigo)} projeto(s) encontrado(s)**")
                        st.markdown("---")

                        for idx, row in resultado_codigo.iterrows():
                            st.markdown(f'''
                                <div class="result-card" style="padding: 1.5rem;">
                                    <div style="width: 100%; text-align: center; margin-bottom: 1.5rem; padding: 1.3rem; 
                                         background: linear-gradient(135deg, rgba(0,128,124,0.08) 0%, rgba(0,128,124,0.04) 100%); 
                                         border-radius: 12px; border: 2px solid rgba(0,128,124,0.2);">
                                        <p style="margin: 0 auto 0.6rem auto; font-size: 0.75rem; font-weight: 700; 
                                           color: {VALE_GREY}; text-transform: uppercase; letter-spacing: 2px; 
                                           display: block; width: 100%;">
                                            📄 PROJETO
                                        </p>
                                        <h2 style="color: {VALE_GREEN}; margin: 0 auto; font-size: 2.2rem; font-weight: 900; 
                                            letter-spacing: 0.5px; display: block; width: 100%;">
                                            {row["Código"]}
                                        </h2>
                                    </div>
                            ''', unsafe_allow_html=True)

                            col1, col2 = st.columns(2)

                            with col1:
                                empresa_text = row['Empresa'] if pd.notna(row['Empresa']) else 'Não informado'
                                st.markdown(f'''
                                    <div class="info-card">
                                        <span class="info-card-label">🏢 Empresa Responsável</span>
                                        <h3 style='color: {VALE_GREEN}; margin: 0.5rem 0;'>{empresa_text}</h3>
                                    </div>
                                ''', unsafe_allow_html=True)

                                status_texto = row['Status'] if pd.notna(row['Status']) else 'Não informado'
                                st.markdown(f'''
                                    <div class="info-card">
                                        <span class="info-card-label">📊 Status do Projeto</span>
                                        <h3 style='color: {VALE_YELLOW}; margin: 0.5rem 0;'>{status_texto}</h3>
                                    </div>
                                ''', unsafe_allow_html=True)

                            with col2:
                                if pd.notna(row['Código PEP']) and str(row['Código PEP']).strip() != "":
                                    pep_texto = row['Código PEP']
                                    pep_color = VALE_GREEN
                                else:
                                    pep_texto = "⚠️ Sem código PEP"
                                    pep_color = VALE_GREY

                                st.markdown(f'''
                                    <div class="info-card">
                                        <span class="info-card-label">🔢 Código PEP Vinculado</span>
                                        <h3 style='color: {pep_color}; margin: 0.5rem 0;'>{pep_texto}</h3>
                                    </div>
                                ''', unsafe_allow_html=True)

                            st.markdown('<div class="escopo-container">', unsafe_allow_html=True)
                            st.markdown('<span class="escopo-label">📝 Escopo do Projeto</span>', unsafe_allow_html=True)
                            if pd.notna(row['Escopo']) and str(row['Escopo']).strip() != "":
                                st.markdown(f'<div class="escopo-text">{row["Escopo"]}</div>', unsafe_allow_html=True)
                            else:
                                st.markdown('<div class="escopo-text"><i>Escopo não informado para este projeto.</i></div>', unsafe_allow_html=True)
                            st.markdown('</div>', unsafe_allow_html=True)

                            # GRÁFICO DE ECONOMIA - TOTAIS ANUAIS
                            st.markdown("---")
                            st.markdown("### 💰 Análise de Economia Projetada (2026-2056)")

                            anos = list(range(2026, 2057))
                            valores_anuais = []

                            for ano in [2026, 2027, 2028]:
                                col_total = f"Total_{ano}"
                                if col_total in row.index and pd.notna(row[col_total]):
                                    try:
                                        valores_anuais.append(float(row[col_total]))
                                    except:
                                        valores_anuais.append(0)
                                else:
                                    valores_anuais.append(0)

                            for ano in range(2029, 2057):
                                col_total = f"Total_{ano}"
                                if col_total in row.index and pd.notna(row[col_total]):
                                    try:
                                        valores_anuais.append(float(row[col_total]))
                                    except:
                                        valores_anuais.append(0)
                                else:
                                    valores_anuais.append(0)

                            fig_economia = go.Figure()

                            fig_economia.add_trace(go.Scatter(
                                x=anos,
                                y=valores_anuais,
                                mode='lines+markers',
                                name='Economia Anual',
                                line=dict(color=VALE_GREEN, width=4),
                                marker=dict(size=10, color=VALE_GREEN, symbol='circle',
                                            line=dict(color='white', width=2)),
                                fill='tozeroy',
                                fillcolor='rgba(0,128,124,0.15)',
                                hovertemplate='<b>Ano:</b> %{x}<br>' +
                                              '<b>Economia:</b> R$ %{y:,.2f}<br>' +
                                              '<extra></extra>',
                                hoverlabel=dict(
                                    bgcolor=VALE_GREEN,
                                    font_size=15,
                                    font_family="Inter",
                                    font_color="white"
                                )
                            ))

                            fig_economia.update_layout(
                                height=700,
                                margin=dict(l=100, r=100, t=120, b=100),
                                xaxis_title="Ano",
                                yaxis_title="Economia (R$)",
                                plot_bgcolor='rgba(0,0,0,0)',
                                paper_bgcolor='rgba(0,0,0,0)',
                                font=dict(size=14, family="Inter"),
                                xaxis=dict(
                                    showgrid=True,
                                    gridcolor='rgba(0,128,124,0.08)',
                                    tickfont=dict(size=13, family="Inter"),
                                    linecolor='rgba(0,128,124,0.2)',
                                    linewidth=2,
                                    dtick=2,
                                    tickangle=-45
                                ),
                                yaxis=dict(
                                    showgrid=True,
                                    gridcolor='rgba(0,128,124,0.08)',
                                    tickfont=dict(size=13, family="Inter"),
                                    linecolor='rgba(0,128,124,0.2)',
                                    linewidth=2,
                                    tickformat=',.0f'
                                ),
                                hovermode='x unified',
                                title=dict(
                                    text=f"<b>Projeção de Economia Anual - Projeto {row['Código']}</b>",
                                    font=dict(size=20, family="Inter", color=VALE_GREEN),
                                    x=0.5,
                                    xanchor='center'
                                )
                            )

                            st.plotly_chart(fig_economia, use_container_width=True, config={
                                'displayModeBar': True,
                                'displaylogo': False,
                                'modeBarButtonsToRemove': ['pan2d', 'lasso2d', 'select2d'],
                                'toImageButtonOptions': {
                                    'format': 'png',
                                    'filename': f'economia_anual_projeto_{row["Código"]}',
                                    'height': 1400,
                                    'width': 2400,
                                    'scale': 3
                                }
                            })

                            # DETALHAMENTO MENSAL
                            st.markdown("---")
                            st.markdown("### 📅 Detalhamento Mensal (2026-2028)")

                            col_ano_sel = st.columns([1, 2, 1])[1]
                            with col_ano_sel:
                                ano_selecionado = st.selectbox(
                                    "Selecione o ano para ver detalhamento mensal:",
                                    [2026, 2027, 2028],
                                    key=f"ano_mensal_{idx}"
                                )

                            meses_nomes = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
                            valores_mensais = []

                            for mes in meses_nomes:
                                col_mes = f"{ano_selecionado}_{mes}"
                                if col_mes in row.index and pd.notna(row[col_mes]):
                                    try:
                                        valores_mensais.append(float(row[col_mes]))
                                    except:
                                        valores_mensais.append(0)
                                else:
                                    valores_mensais.append(0)

                            fig_mensal = go.Figure()

                            fig_mensal.add_trace(go.Bar(
                                x=meses_nomes,
                                y=valores_mensais,
                                text=[f"R$ {v:,.2f}" for v in valores_mensais],
                                textposition='outside',
                                textfont=dict(size=12, family="Inter", color=VALE_YELLOW),
                                marker=dict(
                                    color=valores_mensais,
                                    colorscale=[
                                        [0, VALE_YELLOW],
                                        [0.5, VALE_LIGHT_GREEN],
                                        [1, VALE_GREEN]
                                    ],
                                    showscale=False,
                                    line=dict(color=VALE_YELLOW, width=2)
                                ),
                                hovertemplate=f'<b>%{{x}}/{ano_selecionado}</b><br>' +
                                              '<b>Economia:</b> R$ %{y:,.2f}<br>' +
                                              '<extra></extra>',
                                hoverlabel=dict(
                                    bgcolor=VALE_YELLOW,
                                    font_size=14,
                                    font_family="Inter",
                                    font_color="white"
                                )
                            ))

                            fig_mensal.update_layout(
                                height=550,
                                margin=dict(l=80, r=80, t=100, b=80),
                                xaxis_title="Mês",
                                yaxis_title="Economia (R$)",
                                plot_bgcolor='rgba(0,0,0,0)',
                                paper_bgcolor='rgba(0,0,0,0)',
                                font=dict(size=13, family="Inter"),
                                xaxis=dict(
                                    showgrid=False,
                                    tickfont=dict(size=12, family="Inter"),
                                    linecolor='rgba(238,167,34,0.2)',
                                    linewidth=2
                                ),
                                yaxis=dict(
                                    showgrid=True,
                                    gridcolor='rgba(238,167,34,0.08)',
                                    tickfont=dict(size=12, family="Inter"),
                                    linecolor='rgba(238,167,34,0.2)',
                                    linewidth=2,
                                    tickformat=',.0f'
                                ),
                                title=dict(
                                    text=f"<b>Detalhamento Mensal - {ano_selecionado}</b>",
                                    font=dict(size=18, family="Inter", color=VALE_YELLOW),
                                    x=0.5,
                                    xanchor='center'
                                )
                            )

                            st.plotly_chart(fig_mensal, use_container_width=True, config={
                                'displayModeBar': True,
                                'displaylogo': False,
                                'modeBarButtonsToRemove': ['pan2d', 'lasso2d', 'select2d'],
                                'toImageButtonOptions': {
                                    'format': 'png',
                                    'filename': f'economia_mensal_{ano_selecionado}_projeto_{row["Código"]}',
                                    'height': 1200,
                                    'width': 2000,
                                    'scale': 3
                                }
                            })

                            # Métricas de totais
                            st.markdown("---")
                            st.markdown("#### 📊 Totais de Economia")
                            col_econ1, col_econ2, col_econ3 = st.columns(3)

                            with col_econ1:
                                total_econ_pluri = row['Total Econ Pluri'] if pd.notna(row['Total Econ Pluri']) else 0
                                try:
                                    total_econ_pluri = float(total_econ_pluri)
                                except:
                                    total_econ_pluri = 0
                                st.metric(
                                    label="💰 Total Econ Plurianual",
                                    value=f"R$ {total_econ_pluri:,.2f}",
                                    help="Coluna RC - Total de economia plurianual"
                                )

                            with col_econ2:
                                total_exc_econ = row['Total Exc Econ 2016 à 2025'] if pd.notna(row['Total Exc Econ 2016 à 2025']) else 0
                                try:
                                    total_exc_econ = float(total_exc_econ)
                                except:
                                    total_exc_econ = 0
                                st.metric(
                                    label="📈 Total Exc Econ 2016-2025",
                                    value=f"R$ {total_exc_econ:,.2f}",
                                    help="Coluna RD - Total exceto economia 2016 a 2025"
                                )

                            with col_econ3:
                                total_mes_selecionado = sum(valores_mensais)
                                st.metric(
                                    label=f"📅 Total {ano_selecionado}",
                                    value=f"R$ {total_mes_selecionado:,.2f}",
                                    help=f"Total mensal de {ano_selecionado}"
                                )

                            st.markdown('</div>', unsafe_allow_html=True)

                        st.markdown("---")
                        st.markdown("### 📋 Resumo de Todos os Resultados")
                        st.dataframe(
                            resultado_codigo[["Código", "Empresa", "Status", "Código PEP", "Escopo"]].reset_index(drop=True),
                            use_container_width=True,
                            height=300
                        )

                        csv_resultado = resultado_codigo.to_csv(index=False).encode('utf-8-sig')
                        st.download_button(
                            label="📥 Baixar Todos os Resultados (CSV)",
                            data=csv_resultado,
                            file_name=f"busca_projeto_{codigo_busca}.csv",
                            mime="text/csv",
                        )
                    else:
                        st.warning("⚠️ Nenhum projeto encontrado com esse código.")
                else:
                    st.info("💡 **Como usar:** Digite o código do projeto no campo acima para visualizar todas as informações detalhadas, incluindo análise de economia anual e mensal.")

                    with st.expander("📋 Ver exemplos de códigos disponíveis"):
                        exemplos = df_completo["Código"].head(10).tolist()
                        st.markdown("**Códigos de exemplo na base:**")
                        for cod in exemplos:
                            st.markdown(f"- `{cod}`")

    except Exception as e:
        st.error(f"❌ **Erro ao processar o arquivo:** {str(e)}")
        st.info("💡 Verifique se o arquivo Excel está no formato correto.")

        import traceback
        with st.expander("🔍 Ver detalhes do erro (para debug)"):
            st.code(traceback.format_exc())

else:
    col_centro = st.columns([1, 2, 1])[1]

    with col_centro:
        st.markdown(f"""
        <div style='text-align: center; padding: 3rem;'>
            <h2 style='color: {VALE_GREEN};'>👋 Bem-vindo ao Dashboard SAP Vale</h2>
            <p style='font-size: 1.1rem; color: {VALE_GREY}; margin: 1.5rem 0;'>
                Faça o upload de uma planilha Excel na barra lateral para iniciar a análise
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")

        st.markdown("""
        ### 📊 Funcionalidades do Sistema

        **Análise por PEP**
        - Dashboard gerencial por empresa
        - Dashboard de status dos projetos
        - Busca avançada com gráficos de economia

        **Análise por Código**
        - Dashboard gerencial por empresa
        - Dashboard de status dos projetos
        - Busca detalhada com gráficos de economia

        **Recursos Especiais**
        - 📊 Visualização da base de dados completa
        - 🎨 Interface moderna e intuitiva
        - 🔍 Buscas inteligentes
        - 📥 Exportação facilitada
        - 📈 Gráficos interativos anuais e mensais
        - 💰 Análise de Economia (2026-2056)
        - 📅 Detalhamento Mensal (2026-2028)
        """)

st.markdown("---")
st.markdown(f"""
    <div style='text-align: center; color: {VALE_GREY}; font-size: 0.9rem; padding: 1rem;'>
        <strong style='color: {VALE_GREEN};'>Dashboard SAP Analytics</strong> | Vale S.A. © 2026<br>
        Sistema Integrado de Gestão de Projetos | <strong>Versão 6.0</strong>
    </div>
""", unsafe_allow_html=True)

