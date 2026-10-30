import random
from datetime import date

import streamlit as st

# ---------------------------------------------------------------
# PERSONALIZE AQUI
# ---------------------------------------------------------------
NOME_NO_SITE = "Tizi"
DIA_ANIVERSARIO = 29
MES_ANIVERSARIO = 10
ASSINATURA = "Letícia Lívia"

# Nos dias seguintes ao aniversário, o site mostra "Atrasei X dias" em vez da contagem.
DIAS_DE_PARABENS_ATRASADO = 10

CARTA = """
Minha querida Letícia Lacerda,

Feliz aniversário!

Apesar de ainda não termos nos encontrado pessoalmente, isso nunca diminuiu o carinho enorme que sinto por você, muito menos a proximidade que sinto sempre que conversamos. Queria te dar algo feito com muito cuidado e carinho, e este cantinho é uma pequena forma de demonstrar o quanto você é especial e importante pra mim.

Fico genuinamente feliz e empolgada só de imaginar os planos que temos para nós e que espero, do fundo do meu coração, que a gente consiga tirar do papel. Mal posso esperar para transformar essas ideias em lembranças, conhecer lugares juntas, fazer nossas comprinhas e viver todos aqueles momentos que, por enquanto, só conseguimos imaginar. E, sinceramente, independentemente do programa, o que mais quero é ter você por perto e aproveitar sua companhia.

Espero que a vida seja cada vez mais gentil com você, que nunca faltem motivos para sorrir, pessoas que te façam bem e experiências que aqueçam seu coração. Que você receba todo o carinho e a bondade que espalha por aí, porque merece cada pedacinho disso.

Tenho muita sorte de ter você na minha vida. Você é luz! 🩷
"""

PLANOS = [
    ("🍊", "Laranjada no Centro"),
    ("🍻", "Tomar umas no bar do Bill"),
    ("🛍️", "Comprinhas em Madureira"),
    ("🏖️", "Praia da Barra de havaianas"),
    ("🏟️", "Conhecer o Maracanã"),
    ("⭐", "E infinitas possibilidades!"),
]
FRASE_PLANOS = "O que importa mesmo é a sua companhia."

MOTIVOS = [
    "Você faz qualquer dia ficar mais leve.",
    "Você escuta com atenção e carinho.",
    "Qualquer programa fica bom quando é com você.",
    "Só de pensar em passar o dia fazendo comprinhas com você, o dia já melhora.",
    "Você tem um jeito único de enxergar o mundo.",
    "Você me entende de um jeito que nem sempre consigo explicar.",
    "Você desperta em mim alguns dos sentimentos mais puros e bonitos que existem.",
    "Você me faz enxergar mais bondade no mundo e acreditar que ainda existem pessoas genuinamente boas.",
    "Você me ajuda a gostar um pouquinho mais de quem eu sou, porque, se alguém tão incrível quanto você gosta de mim, talvez eu seja mesmo uma pessoa tão boa quanto você me faz sentir.",
    "Sua companhia é daquelas que dão saudade, mesmo de longe, e você merece todas as coisas boas que estão chegando."
]

MENSAGEM_FINAL = (
    "Que seus dias sejam leves, seus sonhos encontrem caminhos e nunca faltem amor, "
    "carinho e boas surpresas na sua vida. "
    f"Feliz aniversário, {NOME_NO_SITE}!"
)
# ---------------------------------------------------------------

st.set_page_config(
    page_title=f"Feliz aniversário, {NOME_NO_SITE}!",
    page_icon="🧁",
    layout="centered",
)

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@600;700&family=Quicksand:wght@500;600;700&display=swap');

.stApp {
    background:
        radial-gradient(circle at 10% 8%, #ffd9e8 0, transparent 45%),
        radial-gradient(circle at 92% 20%, #e6d9ff 0, transparent 45%),
        radial-gradient(circle at 15% 70%, #d6eeff 0, transparent 45%),
        radial-gradient(circle at 90% 92%, #ffe9d6 0, transparent 45%),
        #fff8fb;
    background-attachment: fixed;
}

[data-testid="stHeader"] { display: none; }
#MainMenu, footer { visibility: hidden; }

.block-container,
[data-testid="stMainBlockContainer"] {
    max-width: 700px;
    padding-top: 3rem;
    padding-bottom: 4rem;
    position: relative;
    z-index: 1;
}

.baloes span {
    position: fixed;
    bottom: -80px;
    font-size: 2rem;
    opacity: 0.75;
    pointer-events: none;
    z-index: 0;
    animation: subir linear infinite;
}
@keyframes subir {
    from { transform: translateY(0) rotate(-6deg); }
    to { transform: translateY(-125vh) rotate(8deg); }
}
@media (prefers-reduced-motion: reduce) {
    .baloes { display: none; }
}

.titulo {
    font-family: 'Dancing Script', cursive;
    font-weight: 700;
    font-size: clamp(3rem, 13vw, 5.2rem);
    line-height: 1.05;
    text-align: center;
    color: #d9558f;
    margin: 0.4rem 0 0.8rem;
}
.subtitulo {
    text-align: center;
    font-family: 'Quicksand', sans-serif;
    font-weight: 600;
    font-size: 1.1rem;
    color: #7a6a99;
}
.pilula {
    display: table;
    margin: 1.3rem auto 0;
    background: #ffffff;
    border-radius: 999px;
    padding: 0.45rem 1.2rem;
    font-family: 'Quicksand', sans-serif;
    font-weight: 700;
    font-size: 0.95rem;
    color: #8a5fc9;
    box-shadow: 0 4px 14px rgba(138, 95, 201, 0.15);
}
.secao {
    font-family: 'Dancing Script', cursive;
    font-weight: 700;
    font-size: 2.1rem;
    color: #8a5fc9;
    text-align: center;
    margin: 3rem 0 1.2rem;
}

.carta {
    position: relative;
    background: #fffdf8;
    border-radius: 6px;
    padding: 2rem 1.8rem 1.5rem;
    font-family: 'Quicksand', sans-serif;
    font-weight: 500;
    font-size: 1.05rem;
    line-height: 1.85;
    color: #5a4a78;
    box-shadow: 0 12px 28px rgba(122, 106, 153, 0.18);
    transform: rotate(-0.8deg);
}
.carta::before {
    content: "";
    position: absolute;
    top: -14px;
    left: 50%;
    width: 110px;
    height: 28px;
    margin-left: -55px;
    background: rgba(255, 182, 213, 0.75);
    transform: rotate(3deg);
}
.carta p { margin: 0 0 1rem; }
.carta .assinatura {
    font-family: 'Dancing Script', cursive;
    font-weight: 700;
    font-size: 1.9rem;
    text-align: right;
    color: #d9558f;
    margin: 0.4rem 0 0;
}

.plano {
    display: flex;
    align-items: center;
    gap: 0.9rem;
    background: #ffffff;
    border-left: 8px solid #ffa6cb;
    border-radius: 4px 18px 18px 4px;
    padding: 0.95rem 1.3rem;
    margin-bottom: 0.8rem;
    font-family: 'Quicksand', sans-serif;
    font-weight: 700;
    font-size: 1.05rem;
    color: #5a4a78;
    box-shadow: 0 6px 16px rgba(122, 106, 153, 0.14);
}
.plano:nth-child(2) { border-left-color: #c9b2ff; }
.plano:nth-child(3) { border-left-color: #a8d8ff; }
.plano .icone { font-size: 1.6rem; }
.frase-planos {
    margin-top: 1.4rem;
    text-align: center;
    font-family: 'Dancing Script', cursive;
    font-weight: 700;
    font-size: 1.9rem;
    color: #d9558f;
}

.bilhete {
    background: #fff3b8;
    border-radius: 4px;
    padding: 1.6rem 1.5rem;
    text-align: center;
    font-family: 'Quicksand', sans-serif;
    font-weight: 600;
    font-size: 1.15rem;
    line-height: 1.6;
    color: #6b5a2e;
    box-shadow: 0 10px 22px rgba(160, 130, 40, 0.18);
    transform: rotate(1deg);
}
.bilhete.vazio { color: #9c8e62; }

.final {
    margin-top: 1.5rem;
    background: linear-gradient(135deg, #ffb3d1, #c9b2ff);
    border-radius: 28px;
    padding: 1.8rem 1.6rem;
    text-align: center;
    font-family: 'Dancing Script', cursive;
    font-weight: 700;
    font-size: 1.8rem;
    line-height: 1.4;
    color: #ffffff;
    box-shadow: 0 12px 26px rgba(201, 178, 255, 0.45);
}

.rodape {
    text-align: center;
    margin-top: 3.5rem;
    font-family: 'Quicksand', sans-serif;
    font-weight: 600;
    color: #9a8bb8;
}

.stButton { display: flex; justify-content: center; margin-top: 1.1rem; }
.stButton > button {
    background: #d9558f;
    border: 0;
    border-radius: 999px;
    padding: 0.65rem 1.8rem;
    box-shadow: 0 8px 18px rgba(217, 85, 143, 0.3);
}
.stButton > button p {
    color: #ffffff;
    font-family: 'Quicksand', sans-serif;
    font-weight: 700;
    font-size: 1.02rem;
}
.stButton > button:hover { background: #c94782; border: 0; }
.stButton > button:focus-visible { outline: 3px solid #8a5fc9; outline-offset: 3px; }
</style>
"""

BALOES = [
    ("🎀", 6, 17, -4),
    ("🐇", 22, 21, -12),
    ("🌸", 38, 15, -8),
    ("☁️", 55, 19, -2),
    ("🧸", 70, 23, -15),
    ("🌷", 84, 16, -6),
    ("🫧", 94, 20, -10),
]


def html(texto: str) -> None:
    """Renderiza HTML compactado (evita que o Markdown quebre o bloco)."""
    compacto = " ".join(l.strip() for l in texto.splitlines() if l.strip())
    st.markdown(compacto, unsafe_allow_html=True)


def dias_desde_e_ate_aniversario() -> tuple[int, int]:
    """Dias desde o último aniversário e dias até o próximo."""
    hoje = date.today()
    deste_ano = date(hoje.year, MES_ANIVERSARIO, DIA_ANIVERSARIO)
    if deste_ano <= hoje:
        anterior = deste_ano
        proximo = date(hoje.year + 1, MES_ANIVERSARIO, DIA_ANIVERSARIO)
    else:
        anterior = date(hoje.year - 1, MES_ANIVERSARIO, DIA_ANIVERSARIO)
        proximo = deste_ano
    return (hoje - anterior).days, (proximo - hoje).days


def sortear_motivo() -> None:
    atual = st.session_state.get("motivo")
    opcoes = [m for m in MOTIVOS if m != atual] or MOTIVOS
    st.session_state["motivo"] = random.choice(opcoes)


html(CSS)

baloes_html = "".join(
    f'<span style="left:{left}%; animation-duration:{dur}s; animation-delay:{delay}s">{emoji}</span>'
    for emoji, left, dur, delay in BALOES
)
html(f'<div class="baloes">{baloes_html}</div>')

# ---------------- Topo ----------------
desde, ate = dias_desde_e_ate_aniversario()
em_festa = desde <= DIAS_DE_PARABENS_ATRASADO

'''if desde == 0:
    texto_pilula = "Hoje é o seu dia! 🧁"
elif em_festa:
    plural = "dia" if desde == 1 else "dias"
    texto_pilula = f"Atrasei {desde} {plural}, mas o carinho chegou inteirinho"
elif ate == 1:
    texto_pilula = "Falta 1 dia para o seu aniversário"
else:
    texto_pilula = f"Faltam {ate} dias para o seu aniversário"'''

texto_pilula = "Atrasei 1 dia, mas o carinho chegou inteirinho"

html(
    f"""
    <div class="titulo">Feliz aniversário,<br>{NOME_NO_SITE}!</div>
    <div class="subtitulo">um cantinho feito com carinho só para você</div>
    <div class="pilula">{texto_pilula}</div>
    """
)

if em_festa and not st.session_state.get("festa_iniciada"):
    st.session_state["festa_iniciada"] = True
    #st.balloons()

# ---------------- Carta ----------------
paragrafos = "".join(f"<p>{p.strip()}</p>" for p in CARTA.strip().split("\n\n"))
html('<div class="secao">Uma cartinha para você</div>')
html(f'<div class="carta">{paragrafos}<p class="assinatura">{ASSINATURA}</p></div>')

# ---------------- Planos ----------------
planos_html = "".join(
    f'<div class="plano"><span class="icone">{icone}</span>{texto}</div>'
    for icone, texto in PLANOS
)
html('<div class="secao">Nossos planos</div>')
html(f'{planos_html}<div class="frase-planos">{FRASE_PLANOS}</div>')

# ---------------- Motivos ----------------
html('<div class="secao">Por que você é especial</div>')
motivo = st.session_state.get("motivo")
if motivo:
    html(f'<div class="bilhete">{motivo}</div>')
else:
    html('<div class="bilhete vazio">Clique no botão para sortear um recadinho.</div>')
st.button("Sortear um motivo", on_click=sortear_motivo)

# ---------------- Surpresa ----------------
html('<div class="secao">Mais uma coisinha</div>')
if st.button("Abrir a surpresa"):
    st.session_state["surpresa"] = True
    st.balloons()
    st.toast(f"Parabéns, {NOME_NO_SITE}!", icon="🧁")

if st.session_state.get("surpresa"):
    html(f'<div class="final">{MENSAGEM_FINAL}</div>')

html(f'<div class="rodape">feito com carinho por {ASSINATURA}</div>')
