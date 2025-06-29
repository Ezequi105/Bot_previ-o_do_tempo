import requests
import tkinter as tk
from tkinter import messagebox

API_KEY = "2a0b0d2a9c0dc4835b4bb1f24a898770"
# Certifique-se de substituir a API_KEY pela sua chave válida do OpenWeatherMap.

def buscar_clima():
    cidade = entrada_cidade.get()
    if not cidade:
        messagebox.showwarning("Atenção", "Digite uma cidade.")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&units=metric&lang=pt_br"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        temp = dados["main"]["temp"]
        descricao = dados["weather"][0]["description"]
        umidade = dados["main"]["humidity"]

        resultado.config(text=f"🌤️ Clima em {cidade}\n"
                              f"Temperatura: {temp}°C\n"
                              f"Descrição: {descricao}\n"
                              f"Umidade: {umidade}%")
    else:
        try:
            erro = resposta.json()["message"]
            resultado.config(text=f"Erro: {erro}")
        except:
            resultado.config(text="Erro desconhecido. Verifique sua conexão e API Key.")

# Interface
janela = tk.Tk()
janela.title("Previsão do Tempo")
janela.geometry("300x250")

tk.Label(janela, text="Digite a cidade (ex: Viçosa,BR):").pack(pady=10)

entrada_cidade = tk.Entry(janela, width=30)
entrada_cidade.pack()

tk.Button(janela, text="Buscar Clima", command=buscar_clima).pack(pady=10)

resultado = tk.Label(janela, text="", justify="left")
resultado.pack(pady=10)

janela.mainloop()
