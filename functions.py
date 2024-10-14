import json
import glob
import os

def get_commands(esporte):

    if esporte == "Futebol" or esporte == "Futebol de salão":
        commands={}
        commands["A"] = {}
        commands["A"][1] = {"label": "Posse de bola", "audio": "file1A.mp3", "texto": "Posse de bola para o time A"}
        commands["A"][2] = {"label": "Lateral", "audio": "file2A.mp3", "texto": "Lateral para o time A"}
        commands["A"][3] = {"label": "Falta", "audio": "file3A.mp3", "texto": "Falta para o time A"}
        commands["A"][4] = {"label": "Gol", "audio": "file4A.mp3", "texto": "Gol do time A"}
        commands["A"][5] = {"label": "Saida de bola", "audio": "file5A.mp3", "texto": "Saída de bola para a time A"}
        commands["A"][6] = {"label": "Escanteio", "audio": "file6A.mp3", "texto": "Escanteio para o time A"}
        commands["A"][7] = {"label": "Pênalti", "audio": "file7A.mp3", "texto": "Pênalti para o time A"}
        commands["A"][8] = {"label": "Fim de jogo", "audio": "file8.mp3", "texto": "Fim de jogo"}
        commands["A"][9] = {"label": "Cartão amarelo", "audio": "file9A.mp3", "texto": "Cartão amarelo para o time A"}
        commands["A"][10] = {"label": "Cartão vermelho", "audio": "file10A.mp3", "texto": "Cartão vermelho para o time A"}
        
        commands["B"] = {}
        commands["B"][1] = {"label": "Posse de bola", "audio": "file1B.mp3", "texto": "Posse de bola para o time B"}
        commands["B"][2] = {"label": "Lateral", "audio": "file2B.mp3", "texto": "Lateral para o time B"}
        commands["B"][3] = {"label": "Falta", "audio": "file3B.mp3", "texto": "Falta para o time B"}
        commands["B"][4] = {"label": "Gol", "audio": "file4B.mp3", "texto": "Gol do time B"}
        commands["B"][5] = {"label": "Saida de bola", "audio": "file5B.mp3", "texto": "Saída de bola para a time B"}
        commands["B"][6] = {"label": "Escanteio", "audio": "file6B.mp3", "texto": "Escanteio para o time B"}
        commands["B"][7] = {"label": "Pênalti", "audio": "file7B.mp3", "texto": "Pênalti para o time B"}
        commands["B"][8] = {"label": "Fim de jogo", "audio": "file8.mp3", "texto": "Fim de jogo"}
        commands["B"][9] = {"label": "Cartão amarelo", "audio": "file9B.mp3", "texto": "Cartão amarelo para o time B"}
        commands["B"][10] = {"label": "Cartão vermelho", "audio": "file10B.mp3", "texto": "Cartão vermelho para o time B"}

        return commands
    return None

def save_history(room, historico):
    with open("historicos/"+room+".json", 'w') as file: 
        return json.dump(historico, file)
    
def load_history(room):
    with open("historicos/"+room+".json", 'r') as file: 
        return json.load(file)
    

def get_next_room_number():
    files = glob.glob("historicos/*.json")
    return len(files) +1
        
def get_rooms():
    files = glob.glob("historicos/*.json")
    files = sorted(files, reverse=True)
    files = [os.path.basename(f).split(".")[0] for f in files]
    return files
