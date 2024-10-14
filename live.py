import time
import streamlit as st
from functions import load_history, get_rooms

last_rooms = get_rooms()

if 'room' not in st.session_state:
    ind = None
else:
    ind = st.session_state.sala


room = st.selectbox(
    "Escolha uma sala",
    last_rooms,
    index=ind,
    placeholder="Selecione uma sala...",
)


if room != None:

    st.session_state["sala"] = last_rooms.index(room)+1

    historico = load_history(room)
    
    st.write(f"""
             ## {historico["nome_sala"]}
             """)
    st.write(f"""
             ### Time A ({historico["time_A"]}) x Time B: ({historico["time_B"]})
             """)

    eventos = historico["historico"][::-1]
    i = len(eventos)
    for t, a in eventos:
        st.write(f"Evento {i}: {t}")
        play = i == len(eventos)
        st.audio("audios/"+a, format="audio/mpeg", autoplay=play)
        i = i - 1

    time.sleep(6)
    st.rerun()