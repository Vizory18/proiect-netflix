import streamlit as st
from PIL import Image
import time

# Setări pagină
st.set_page_config(page_title="AI Fashion Finder", page_icon="👗")

# Design stil Netflix
st.markdown("""
    <style>
    .main { background-color: #111; color: white; }
    .stButton>button { background-color: #E50914; color: white; border: none; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎬 Netflix AI Fashion Finder")
st.write("Încarcă o captură de ecran și lasă AI-ul să găsească hainele!")

# Componenta de upload
uploaded_file = st.file_uploader("Alege o imagine...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Cadru procesat', use_container_width=True)
    
    if st.button('🔍 SCAN OUTFIT'):
        with st.spinner('AI-ul analizează piesele vestimentare...'):
            time.sleep(2) # Simulare AI
            
            st.subheader("Potriviri găsite:")
            
            col1, col2 = st.columns(2)
            with col1:
                st.info("*Produs 1*")
                st.write("👗 Rochie Florală")
                st.write("🏷️ Brand: Zara")
                st.write("💰 Preț: 249 RON")
            
            with col2:
                st.info("*Produs 2*")
                st.write("🕶️ Ochelari Soare")
                st.write("🏷️ Brand: Ray-Ban")
                st.write("💰 Preț: 600 RON")
