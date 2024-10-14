import os
import streamlit as st
from functions import load_history, save_history
from functions import get_commands
from functions import get_next_room_number, get_rooms
import qrcode
import socket



@st.dialog("Sala criada!")
def modal_sucesso(numero_sala):
    st.write("Para iniciar a narração selecione a sala "+str(numero_sala))
    if st.button("Ok"):
        st.rerun()


tab_config, tab_match, tab_qr_code = st.tabs(["Configurações da Sala", "Narração","Qr code"])

room = None
esporte = None
room_number = 0

with tab_config:
    
    last_rooms = get_rooms()
    last_rooms.append("Nova")
    room = st.selectbox(
        "Escolha uma sala",
        last_rooms,
        index=None,
        placeholder="Selecione uma sala...",
    )    

    if room != None and room == "Nova":
        room_name = st.text_input("Nome da sala: ")
        team_A_name = st.text_input("Nome do time A:")
        team_B_name = st.text_input("Nome do time B:")        
        room_number = get_next_room_number()
        room = "sala_"+str(room_number)
        esporte = st.selectbox(
            "Escolha uma esporte",
            ("Futebol","Futebol de Salão"),
            index=None,
            placeholder="Selecione uma esporte...",
        )

        if st.button("Criar sala"):
            if not os.path.isfile("historicos/"+room+".json"):
                data = {}
                data["nome_sala"] = room_name
                data["time_A"] = team_A_name
                data["time_B"] = team_B_name
                data["historico"] = []
                save_history(room,data)
            modal_sucesso(room_number)
            


with tab_match:
    col1, col2 = st.columns(2, gap="medium")

    if room != None and room != "Nova" and os.path.isfile("historicos/"+room+".json"):
        esporte = "Futebol"
        list_commands = get_commands(esporte)
        cont_commands = 0

        historico = load_history(room)        

        if 'clicked' not in st.session_state:
            st.session_state.clicked = False

        with col1:
            st.header("Time A: "+historico["time_A"])
            for id in list_commands["A"].keys():                
                result = st.button(list_commands["A"][id]["label"], key=cont_commands, on_click=None, type="secondary", disabled=False, use_container_width=True)
                if result:
                    historico["historico"].append((list_commands["A"][id]["texto"],list_commands["A"][id]["audio"]))
                    save_history(room, historico)
                cont_commands += 1

        with col2:
            st.header("Time B: "+historico["time_B"])
            for id in list_commands["A"].keys():                
                result = st.button(list_commands["B"][id]["label"], key=cont_commands, on_click=None, type="secondary", disabled=False, use_container_width=True)
                if result:
                    historico["historico"].append((list_commands["B"][id]["texto"],list_commands["B"][id]["audio"]))
                    save_history(room, historico)
                cont_commands += 1

        #st.expander("historico", expanded=True)
        #with st.expander("Histórico de comandos..."):
        #    st.write(historico)

with tab_qr_code:
    end = st.text_input("Endereço do app de narração","http://192.168.0.102:8502")
    qr_code_room = qrcode.make(end)
    qr_code_room.save("qr_codes/qr_code.png")
    st.image("qr_codes/qr_code.png", caption=f"Aponte a câmera de seu celular e no app selecione a sala que deseja acompanhar")


