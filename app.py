import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import os
import requests
from streamlit_lottie import st_lottie

# --- Page Config ---
st.set_page_config(page_title="LexiCore AI", layout="wide", initial_sidebar_state="collapsed")

# --- Function to Load Lottie Animation ---
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Fetching a sleek, floating AI animation
lottie_ai_brain = load_lottieurl("https://lottie.host/80e9ab72-6804-45eb-8a9d-b89fb0ab20e1/TzT6gW8wE5.json")

# --- 🚀 THE ANTI-GRAVITY & GLASSMORPHISM CSS OVERHAUL 🚀 ---
st.markdown("""
<style>
    /* 1. Animated Breathing Gradient Background */
    .stApp {
        background: linear-gradient(-45deg, #e0eafc, #cfdef3, #e2e2e2, #f5f7fa);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
    }
    
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* 2. Glassmorphism Panels with Anti-Gravity Float */
    div[data-testid="column"] {
        background: rgba(255, 255, 255, 0.4) !important;
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.6) !important;
        border-radius: 24px;
        padding: 30px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1) !important;
        animation: float 6s ease-in-out infinite;
    }
    
    /* Slightly stagger the float animation for the right column so they don't move identically */
    div[data-testid="column"]:nth-of-type(3) {
        animation-delay: -3s;
    }
    
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }
    
    /* 3. Transparent Swap Bridge */
    div[data-testid="column"]:nth-of-type(2) {
        background-color: transparent !important;
        backdrop-filter: none;
        -webkit-backdrop-filter: none;
        box-shadow: none !important;
        border: none !important;
        display: flex;
        align-items: center;
        justify-content: center;
        animation: none; /* Keep the button stationary */
    }
    
    /* 4. Deep Dark Slate Text (Overriding Streamlit's defaults) */
    .stMarkdownContainer, .stMarkdownContainer p, .stCaption, label, div[data-testid="stText"] { 
        color: #1e293b !important; 
        font-weight: 500;
    }
    
    /* 5. Typography */
    .main-title {
        text-align: center;
        font-family: 'Inter', sans-serif;
        font-weight: 900;
        font-size: 4rem;
        color: #0f172a !important;
        margin-top: -20px;
        margin-bottom: 5px;
        letter-spacing: -1px;
    }
    .gradient-text {
        background: -webkit-linear-gradient(45deg, #3a7bd5, #3a6073);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .sub-title { 
        text-align: center; 
        color: #475569 !important; 
        margin-bottom: 40px; 
        font-size: 1.2rem;
        font-weight: 500;
    }
    
    /* 6. Motion Buttons */
    div.stButton > button {
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.8) !important;
        background: rgba(255, 255, 255, 0.7) !important;
        backdrop-filter: blur(5px);
        color: #0f172a !important;
        font-weight: 700;
        padding: 10px 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05) !important;
    }
    div.stButton > button:hover {
        transform: translateY(-4px);
        box-shadow: 0 15px 25px -5px rgba(0,0,0,0.1), 0 8px 10px -6px rgba(0,0,0,0.05) !important;
        background: linear-gradient(135deg, #3a7bd5 0%, #3a6073 100%) !important;
        color: #ffffff !important;
        border-color: transparent !important;
    }
    
    /* Remove Lottie white background */
    iframe { background-color: transparent !important; }
</style>
""", unsafe_allow_html=True)

# --- Animation & Headers ---
col_anim1, col_anim2, col_anim3 = st.columns([1, 2, 1])
with col_anim2:
    if lottie_ai_brain:
        st_lottie(lottie_ai_brain, height=180, key="ai_anim", quality="high")

st.markdown('<div class="main-title">👋 Welcome to <span class="gradient-text">LexiCore AI</span></div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Advanced Bi-Directional Linguistic Translation Framework</div>', unsafe_allow_html=True)

# --- Full ISO Mapping Engine ---
LANGUAGES = {
    'English': 'en', 'Hindi': 'hi', 'Marathi': 'mr', 'Gujarati': 'gu',
    'Tamil': 'ta', 'Telugu': 'te', 'Bengali': 'bn', 'Kannada': 'kn',
    'Bhojpuri': 'bho', 'Urdu': 'ur', 'Malayalam': 'ml', 'Punjabi': 'pa',
    'Spanish': 'es', 'French': 'fr', 'German': 'de', 'Italian': 'it',
    'Japanese': 'ja', 'Korean': 'ko', 'Chinese (Simplified)': 'zh-CN', 'Russian': 'ru'
}

TTS_SUPPORTED = ['en', 'hi', 'mr', 'gu', 'ta', 'te', 'bn', 'kn', 'ur', 'ml', 'pa', 'es', 'fr', 'de', 'it', 'ja', 'ko', 'zh-CN', 'ru']

if "left_text" not in st.session_state:
    st.session_state.left_text = ""
if "right_text" not in st.session_state:
    st.session_state.right_text = ""

# --- Layout Grid: Input [4] | Center Action [1] | Output [4] ---
col1, col_mid, col2 = st.columns([4, 1, 4], gap="large")

with col1:
    st.markdown("### 📝 Source Context")
    src_lang = st.selectbox("Source Language", list(LANGUAGES.keys()), index=0, key="src_lang_select")
    
    input_text = st.text_area("Input Field", value=st.session_state.left_text, height=220, max_chars=5000, placeholder="Enter text to translate...", label_visibility="collapsed")
    st.session_state.left_text = input_text
    
    st.caption(f"**Character Metric:** {len(input_text)} / 5000 characters")
    
    if input_text and st.button("🔊 Play Input Audio", use_container_width=True):
        try:
            code = LANGUAGES[src_lang]
            tts_lang = code if code in TTS_SUPPORTED else 'en'
            tts_in = gTTS(text=input_text, lang=tts_lang)
            tts_in.save("src_audio.mp3")
            st.audio("src_audio.mp3")
        except Exception:
            st.error("Audio generation failed for the selected configuration.")

with col_mid:
    st.markdown("<br><br><br><br><br>", unsafe_allow_html=True)
    if st.button("🔁", help="Swap translation output to input workspace"):
        if st.session_state.right_text:
            st.session_state.left_text = st.session_state.right_text
            st.session_state.right_text = ""
            st.rerun()

with col2:
    st.markdown("### 🌍 Target Translation")
    tgt_lang = st.selectbox("Target Language", list(LANGUAGES.keys()), index=1, key="tgt_lang_select")
    
    translated_text = ""
    if input_text.strip():
        try:
            translated_text = GoogleTranslator(source=LANGUAGES[src_lang], target=LANGUAGES[tgt_lang]).translate(input_text)
            st.session_state.right_text = translated_text
        except Exception:
            translated_text = "Translation gateway error."
            st.session_state.right_text = ""
            
    st.text_area("Output Field", value=st.session_state.right_text, height=220, disabled=True, label_visibility="collapsed")
    st.caption(f"**Character Metric:** {len(st.session_state.right_text)} / 5000 characters")
    
    if st.session_state.right_text and st.button("🔊 Play Output Audio", use_container_width=True):
        try:
            code = LANGUAGES[tgt_lang]
            tts_lang = code if code in TTS_SUPPORTED else 'hi'
            tts_out = gTTS(text=st.session_state.right_text, lang=tts_lang)
            tts_out.save("tgt_audio.mp3")
            st.audio("tgt_audio.mp3")
        except Exception:
            st.error("Audio conversion limit hit or dialect mismatch encountered.")