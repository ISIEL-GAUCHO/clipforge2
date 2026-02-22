import streamlit as st
from moviepy.editor import VideoFileClip
import tempfile
import os

st.set_page_config(page_title="ClipForge AI", layout="wide")

# ====== CSS MODERNO EMBUTIDO ======
st.markdown("""
<style>
body {
    background-color: #0f0f0f;
}
[data-testid="stAppViewContainer"] {
    background: linear-gradient(rgba(15,15,15,0.95), rgba(15,15,15,0.95)),
                url("https://www.transparenttextures.com/patterns/asfalt-dark.png");
}
h1 {
    color: #00d4ff;
}
.stButton>button {
    background-color: #00d4ff;
    color: black;
    border-radius: 10px;
    font-weight: bold;
}
.stButton>button:hover {
    box-shadow: 0 0 15px #00d4ff;
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)

# ====== SIDEBAR ======
st.sidebar.title("CLIPFORGE AI")
st.sidebar.markdown("Gerador Inteligente de Cortes")
menu = st.sidebar.radio("Menu", ["Dashboard", "Upload de Vídeo"])

# ====== DASHBOARD ======
if menu == "Dashboard":
    st.title("Painel Principal")
    st.markdown("Bem-vindo ao sistema de geração automática de clipes com IA.")
    st.metric("Clipes Gerados Hoje", "3")
    st.metric("Vídeos Processados", "1")

# ====== UPLOAD ======
if menu == "Upload de Vídeo":
    st.title("Gerar Cortes Inteligentes")

    uploaded_file = st.file_uploader("Envie seu vídeo", type=["mp4", "mov", "avi"])

    if uploaded_file:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_file.read())

        st.video(tfile.name)

        if st.button("Gerar Cortes com IA"):

            video = VideoFileClip(tfile.name)
            duration = video.duration

            st.success("Processando vídeo...")

            # Simulação de 3 cortes automáticos
            cortes = [
                (0, min(10, duration)),
                (10, min(20, duration)),
                (20, min(30, duration))
            ]

            for i, (inicio, fim) in enumerate(cortes):
                clip = video.subclip(inicio, fim)
                output_path = f"clip_{i}.mp4"
                clip.write_videofile(output_path, codec="libx264", audio_codec="aac")

                st.subheader(f"Clip {i+1}")
                st.video(output_path)
                with open(output_path, "rb") as file:
                    st.download_button(
                        label="Baixar Clip",
                        data=file,
                        file_name=output_path,
                        mime="video/mp4"
                    )

            st.success("Cortes gerados com sucesso!")