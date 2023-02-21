import os
import gtts
import openai
import tkinter
import pyaudio
import customtkinter
from PIL import Image
import tkinter.messagebox
from tkinter import PhotoImage
import speech_recognition as sr
from playsound import playsound

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
openai.api_key = "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"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("AI.py")
        self.geometry(f"{1248}x{720}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=100, height=50, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=6, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(6, weight=1)

        # Logo Apresentação
        self.img = PhotoImage(file='/Users/jholwashego/Dropbox/Jupyter/TKinter/ai_ok/logo.png')
        self.label_img = customtkinter.CTkLabel(self.sidebar_frame, text=None, image=self.img)
        self.label_img.grid(row=0, column=0, padx=0, pady=(20, 10), sticky="nsew")

        # Label pergunta
        self.logo_label = customtkinter.CTkLabel(master=self.sidebar_frame, text="- Selecione para Perguntar -",
                                                 font=customtkinter.CTkFont(size=12, weight="bold"))
        self.logo_label.grid(row=1, column=0, padx=(0, 0), pady=(20, 0), sticky="nsew")
        # Botão Checkbox 1
        self.checkbox_1 = customtkinter.CTkCheckBox(master=self.sidebar_frame, text='Digite o Texto____',
                                                    command=self.status_checkbox)
        self.checkbox_1.grid(row=2, column=0, pady=(20, 0), padx=(0, 10), sticky="n")
        self.checkbox_2 = customtkinter.CTkCheckBox(master=self.sidebar_frame, text='Falar Algo para AI_',
                                                    command=self.status_checkbox)
        self.checkbox_2.grid(row=3, column=0, pady=(20, 0), padx=(0, 10), sticky="n")

        # Label resposta
        self.logo_label = customtkinter.CTkLabel(master=self.sidebar_frame, text="- Selecione a Resposta -",
                                                 font=customtkinter.CTkFont(size=12, weight="bold"))
        self.logo_label.grid(row=4, column=0, padx=(0, 0), pady=(50, 0), sticky="nsew")
        # Botão Checkbox 2
        self.checkbox_3 = customtkinter.CTkCheckBox(master=self.sidebar_frame, text='Resposta em Texto',
                                                    command=self.status_checkbox)
        self.checkbox_3.grid(row=5, column=0, pady=(20, 0), padx=(0, 10), sticky="n")
        self.checkbox_4 = customtkinter.CTkCheckBox(master=self.sidebar_frame, text='Resposta em Audio',
                                                    command=self.status_checkbox)
        self.checkbox_4.grid(row=6, column=0, pady=(20, 0), padx=(0, 10), sticky="n")

        # THEME
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=8, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                                       values=["Light", "Dark", "System"],
                                                                       command=self.tema)
        self.appearance_mode_optionemenu.grid(row=9, column=0, padx=20, pady=(10, 10))

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=360, scrollbar_button_color='blue')
        self.textbox.grid(row=0, column=1, columnspan=4, padx=(20, 20), pady=(25, 0), sticky="nsew")

        # Label nome prog
        self.logo_label = customtkinter.CTkLabel(master=self, text="--  Inteligência Artificial  --",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=2, column=1, columnspan=4, padx=(25, 25), pady=(50, 100), sticky="nsew")

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Escreva a pergunta")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
        # Botão pergunta 1
        self.main_button_1 = customtkinter.CTkButton(master=self, text='Enviar', fg_color="transparent", border_width=2,
                                                     text_color=("gray10", "#DCE4EE"), command=self.texto)
        self.main_button_1.grid(row=3, column=3, padx=(20, 0), pady=(20, 20), sticky="nsew")
        # Botão pergunta 2
        self.main_button_2 = customtkinter.CTkButton(master=self, text='Falar', fg_color="transparent", border_width=2,
                                                     text_color=("gray10", "#DCE4EE"), command=self.fala)
        self.main_button_2.grid(row=3, column=4, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # definir parametros iniciais
        self.E = '\n' + ('_' * 132) + '\n'
        self.appearance_mode_optionemenu.set("Dark")
        self.main_button_1.configure(state="disabled", text="Texto Desativado")
        self.main_button_2.configure(state="disabled", text="Fala Desativada ")
        self.textbox.insert('0.0',
                            self.E + '\nPara ativar o modo de perguntas e respostar selecione as opções ao lado Texto '
                                     'ou Fala \nEscreva sua pergunta e clique no botão --> "Enviar" <-- ou Clique em '
                                     '--> "Falar" <-- e faça sua pergunta... ' + self.E)

    # Temas do console
    def tema(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    # Pergunta e respostas
    def texto(self):
        # Pergunta em Texto
        self.textbox.insert('0.0', '\nPergunta: \n' + str(self.entry.get()) + '\n')
        self.textbox.insert('0.0', self.E)

        # Consult AI Recebendo Entry
        completion = openai.Completion.create(engine="text-davinci-003", prompt=self.entry.get(), max_tokens=1024, n=1, stop=None, temperature=0.5, )
        response = completion.choices[0].text

        # Chamando Respostas # Essas regras é porque se não os botões texto e fala chamão as funções
        if self.checkbox_1.get() == 1 and self.checkbox_2.get() == 0:
            # Resposta somente em Texto
            if self.checkbox_3.get() == 1:
                self.textbox.insert('0.0', '\nResposta:' + response + '\n')
                self.textbox.insert('0.0', self.E)
            if self.checkbox_3.get() == 0:
                self.textbox.insert('0.0', '\n--> Resposta em Texto Desativada <-- \n')
                self.textbox.insert('0.0', self.E)
            # Resposta somente em Audio 1
            if self.checkbox_4.get() == 1:
                frase = gtts.gTTS(response, lang='pt-br')
                frase.save('resposta.mp3')
                playsound('resposta.mp3')
                self.textbox.insert('0.0', '\nResposta em Audio... \n')
                self.textbox.insert('0.0', self.E)
            if self.checkbox_4.get() == 0:
                self.textbox.insert('0.0', '\n--> Resposta em Audio Desativada <-- \n')
                self.textbox.insert('0.0', self.E)

        # Respostas em Texto e Audio
        elif self.checkbox_1.get() == 1 and self.checkbox_2.get() == 1:
            # Resposta em Texto
            if self.checkbox_3.get() == 1:
                self.textbox.insert('0.0', '\nResposta:' + response + '\n')
                self.textbox.insert('0.0', self.E)
            # Resposta em Audio
            if self.checkbox_4.get() == 1:
                frase = gtts.gTTS(response, lang='pt-br')
                frase.save('resposta.mp3')
                playsound('resposta.mp3')
                self.textbox.insert('0.0', '\nResposta em Texto e Audio... \n')
                self.textbox.insert('0.0', self.E)

    def fala(self):
        # Pergunta em Voz
        self.r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = self.r.listen(source)
            try:
                self.textbox.insert('0.0', "\nVocê disse: " + self.r.recognize_google(audio, language='pt-BR'))
                self.frase = self.r.recognize_google(audio, language='pt-BR')
                self.textbox.insert('0.0', self.E)
            except sr.UnknownValueError:
                # Resposta em Texto
                if self.checkbox_3.get() == 1:
                    self.textbox.insert('0.0', "\nNão entendi o que você disse")
                    self.textbox.insert('0.0', self.E)
                # Resposta em Audio
                if self.checkbox_4.get() == 1:
                    response = "\nNão entendi o que você disse"
                    retorno = gtts.gTTS(response, lang='pt-br')
                    retorno.save('resposta.mp3')
                    playsound('resposta.mp3')
            except sr.RequestError as e:
                # Resposta em Texto
                if self.checkbox_3.get() == 1:
                    self.textbox.insert('0.0', '\nNão foi possível realizar a requisição; {0} \n'.format(e))
                    self.textbox.insert('0.0', self.E)
                # Resposta em Audio
                if self.checkbox_4.get() == 1:
                    response = "\nNão foi possível realizar a requisição. "
                    retorno = gtts.gTTS(response, lang='pt-br')
                    retorno.save('resposta.mp3')
                    playsound('resposta.mp3')

            completion = openai.Completion.create(engine="text-davinci-003", prompt=self.frase, max_tokens=1024, n=1,
                                                  stop=None, temperature=0.5, )
            response = completion.choices[0].text

        if self.checkbox_1.get() == 0 and self.checkbox_2.get() == 1:
            # Resposta somente em Texto
            if self.checkbox_3.get() == 1:
                self.textbox.insert('0.0', '\nResposta:' + response + '\n')
                self.textbox.insert('0.0', self.E)
            if self.checkbox_3.get() == 0:
                self.textbox.insert('0.0', '\n--> Resposta em Texto Desativada <-- \n')
                self.textbox.insert('0.0', self.E)
            # Resposta somente em Audio 1
            if self.checkbox_4.get() == 1:
                frase = gtts.gTTS(response, lang='pt-br')
                frase.save('resposta.mp3')
                playsound('resposta.mp3')
                self.textbox.insert('0.0', '\nResposta em Audio... \n')
                self.textbox.insert('0.0', self.E)
            if self.checkbox_4.get() == 0:
                self.textbox.insert('0.0', '\n--> Resposta em Audio Desativada <-- \n')
                self.textbox.insert('0.0', self.E)

        # Respostas em Texto e Audio
        elif self.checkbox_1.get() == 1 and self.checkbox_2.get() == 1:
            # Resposta em Texto
            if self.checkbox_3.get() == 1:
                self.textbox.insert('0.0', '\nResposta:' + response + '\n')
                self.textbox.insert('0.0', self.E)
            # Resposta em Audio
            if self.checkbox_4.get() == 1:
                frase = gtts.gTTS(response, lang='pt-br')
                frase.save('resposta.mp3')
                playsound('resposta.mp3')
                self.textbox.insert('0.0', '\nResposta em Texto e Audio Ativado... \n')
                self.textbox.insert('0.0', self.E)

    # Ativar botoes
    def att(self):
        self.main_button_1.configure(state="enable", text="Enviar", text_color=("gray10", "#DCE4EE"), )

    def atf(self):
        self.main_button_2.configure(state="enable", text="Falar", text_color=("gray10", "#DCE4EE"), )

    # Desativar botoes
    def dtt(self):
        self.main_button_1.configure(state="disabled", text="Texto Desativado", border_width=2,
                                     text_color=("gray10", "#DCE4EE"), )

    def dtf(self):
        self.main_button_2.configure(state="disabled", text="Fala Desativada", border_width=2,
                                     text_color=("gray10", "#DCE4EE"), )

    # Regras do Checkbox
    def status_checkbox(self):
        # Plugs Checkbox desativado gelral
        if self.checkbox_1.get() == 0 and self.checkbox_3.get() == 0 and self.checkbox_4.get() == 0: self.dtt()
        if self.checkbox_2.get() == 0 and self.checkbox_3.get() == 0 and self.checkbox_4.get() == 0: self.dtf()
        # Plugs Checkbox ativado gelral
        if self.checkbox_1.get() == 1 and self.checkbox_3.get() == 1 and self.checkbox_4.get() == 1: self.att()
        if self.checkbox_2.get() == 1 and self.checkbox_3.get() == 1 and self.checkbox_4.get() == 1: self.atf()
        # Plugs Checkbox Text
        if self.checkbox_1.get() == 1 and self.checkbox_3.get() == 0 and self.checkbox_4.get() == 0: self.dtt()
        if self.checkbox_1.get() == 1 and self.checkbox_3.get() == 1 and self.checkbox_4.get() == 0: self.att()
        if self.checkbox_1.get() == 1 and self.checkbox_3.get() == 0 and self.checkbox_4.get() == 1: self.att()
        # Plugs Checkbox fala
        if self.checkbox_2.get() == 1 and self.checkbox_3.get() == 0 and self.checkbox_4.get() == 0: self.dtf()
        if self.checkbox_2.get() == 1 and self.checkbox_3.get() == 1 and self.checkbox_4.get() == 0: self.atf()
        if self.checkbox_2.get() == 1 and self.checkbox_3.get() == 0 and self.checkbox_4.get() == 1: self.atf()
        # Plugs Checkbox de tex e fala desativado e resposta ativadas
        if self.checkbox_1.get() == 0 and self.checkbox_3.get() == 1 and self.checkbox_4.get() == 1: self.dtt()
        if self.checkbox_1.get() == 0 and self.checkbox_3.get() == 0 and self.checkbox_4.get() == 1: self.dtt()
        if self.checkbox_2.get() == 0 and self.checkbox_3.get() == 1 and self.checkbox_4.get() == 1: self.dtf()
        if self.checkbox_2.get() == 0 and self.checkbox_3.get() == 0 and self.checkbox_4.get() == 1: self.dtf()
        # Plugs Checkbox de tex e fala inverter desativador e resposta ativadas
        if self.checkbox_1.get() == 1 and self.checkbox_2.get() == 0 and self.checkbox_3.get() == 1 and self.checkbox_4.get() == 1: self.dtf()
        if self.checkbox_1.get() == 1 and self.checkbox_2.get() == 0 and self.checkbox_3.get() == 0 and self.checkbox_4.get() == 1: self.dtf()
        if self.checkbox_1.get() == 1 and self.checkbox_2.get() == 0 and self.checkbox_3.get() == 1 and self.checkbox_4.get() == 0: self.dtf()
        if self.checkbox_1.get() == 0 and self.checkbox_2.get() == 0 and self.checkbox_3.get() == 0 and self.checkbox_4.get() == 1: self.dtf()
        if self.checkbox_1.get() == 0 and self.checkbox_2.get() == 0 and self.checkbox_3.get() == 1 and self.checkbox_4.get() == 0: self.dtf()
        if self.checkbox_1.get() == 0 and self.checkbox_2.get() == 1 and self.checkbox_3.get() == 1 and self.checkbox_4.get() == 1: self.dtt()
        if self.checkbox_1.get() == 0 and self.checkbox_2.get() == 1 and self.checkbox_3.get() == 0 and self.checkbox_4.get() == 1: self.dtt()
        if self.checkbox_1.get() == 0 and self.checkbox_2.get() == 1 and self.checkbox_3.get() == 1 and self.checkbox_4.get() == 0: self.dtt()
        if self.checkbox_1.get() == 0 and self.checkbox_2.get() == 0 and self.checkbox_3.get() == 0 and self.checkbox_4.get() == 1: self.dtt()
        if self.checkbox_1.get() == 0 and self.checkbox_2.get() == 0 and self.checkbox_3.get() == 1 and self.checkbox_4.get() == 0: self.dtt()

if __name__ == "__main__":
    app = App()
    app.mainloop()