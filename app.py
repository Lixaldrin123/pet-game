import streamlit as st
import time

# Page configuration
st.set_page_config(page_title="Boba's Virtual Pet 🐾", page_icon="🐶", layout="centered")

# Initialize Session State for Pet Stats
if "hunger" not in st.session_state:
    st.session_state.hunger = 70
if "happiness" not in st.session_state:
    st.session_state.happiness = 80
if "energy" not in st.session_state:
    st.session_state.energy = 90
if "cleanliness" not in st.session_state:
    st.session_state.cleanliness = 85
if "is_sleeping" not in st.session_state:
    st.session_state.is_sleeping = False
if "message" not in st.session_state:
    st.session_state.message = "Boba is happy to see you! 💕"

# Custom CSS for cute styling
st.markdown("""
    <style>
    .stButton>button {
        border-radius: 20px;
        font-weight: bold;
        width: 100%;
        height: 50px;
    }
    .pet-card {
        background-color: #fff0f5;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

st.title("🐾 Boba's Virtual Pet Care 🐾")
st.write("Take care of your cute puppy Boba right here in your browser!")

# Choose Pet Visual based on state
if st.session_state.is_sleeping:
    pet_display = "😴💤 (Boba is fast asleep... Zzz)"
else:
    pet_display = "🐶✨ (Boba is happy and wagging his tail!)"

# Display Pet Avatar Area
st.markdown(f"""
    <div class="pet-card">
        <h1>{pet_display}</h1>
        <p style="font-size: 18px; color: #555;">{st.session_state.message}</p>
    </div>
""", unsafe_allow_html=True)

st.write("")

# Display Stats using Columns and Progress Bars
col1, col2 = st.columns(2)

with col1:
    st.write("🍎 **Hunger**")
    st.progress(st.session_state.hunger / 100)
    st.write(f"{st.session_state.hunger}%")
    
    st.write("😊 **Happiness**")
    st.progress(st.session_state.happiness / 100)
    st.write(f"{st.session_state.happiness}%")

with col2:
    st.write("⚡ **Energy**")
    st.progress(st.session_state.energy / 100)
    st.write(f"{st.session_state.energy}%")
    
    st.write("🧼 **Cleanliness**")
    st.progress(st.session_state.cleanliness / 100)
    st.write(f"{st.session_state.cleanliness}%")

st.divider()

# Action Buttons
st.subheader("Actions")
b1, b2, b3, b4 = st.columns(4)

with b1:
    if st.button("🍎 Feed"):
        if st.session_state.is_sleeping:
            st.session_state.message = "Shh! Boba is sleeping... 🤫"
        else:
            st.session_state.hunger = min(100, st.session_state.hunger + 20)
            st.session_state.message = "Yum! Boba enjoyed a tasty snack! 🍎"
            st.rerun()

with b2:
    if st.button("🎾 Play"):
        if st.session_state.is_sleeping:
            st.session_state.message = "Wake Boba up first before playing!"
        elif st.session_state.energy < 20:
            st.session_state.message = "Boba is too tired to play... 💤"
        else:
            st.session_state.happiness = min(100, st.session_state.happiness + 20)
            st.session_state.energy = max(0, st.session_state.energy - 15)
            st.session_state.cleanliness = max(0, st.session_state.cleanliness - 10)
            st.session_state.message = "Yay! Boba had so much fun playing fetch! 🎾"
            st.rerun()

with b3:
    if st.button("🧼 Bath"):
        if st.session_state.is_sleeping:
            st.session_state.message = "Don't wash Boba while he's sleeping!"
        else:
            st.session_state.cleanliness = 100
            st.session_state.message = "Squeaky clean! Boba smells wonderful! 🧼✨"
            st.rerun()

with b4:
    if st.button("😴 Sleep"):
        st.session_state.is_sleeping = not st.session_state.is_sleeping
        if st.session_state.is_sleeping:
            st.session_state.message = "Goodnight Boba! Rest well... 🌙"
            st.session_state.energy = min(100, st.session_state.energy + 30)
        else:
            st.session_state.message = "Good morning! Boba woke up refreshed! ☀️"
        st.rerun()