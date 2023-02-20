import tkinter
import tkinter.messagebox
import customtkinter
from tkinter import PhotoImage

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("AI example.py")
        self.geometry(f"{1248}x{720}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=100, height=50, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=6, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(6, weight=1)

        # Nome Apresentação
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="   Selecione as opções   ",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=0, pady=(20, 10))

        # Botão
        self.checkbox_1 = customtkinter.CTkCheckBox(master=self.sidebar_frame, text='Digite o Texto____',
                                                    command=self.status_checkbox_escreva_text)
        self.checkbox_1.grid(row=1, column=0, pady=(20, 0), padx=(0, 10), sticky="n")
        self.checkbox_2 = customtkinter.CTkCheckBox(master=self.sidebar_frame, text='Falar Algo para AI_',
                                                    command=self.status_checkbox_fale_a_pergunta)
        self.checkbox_2.grid(row=2, column=0, pady=(20, 0), padx=(0, 10), sticky="n")

        self.checkbox_3 = customtkinter.CTkCheckBox(master=self.sidebar_frame, text='Resposta em Texto',
                                                    command=self.status_checkbox_escrever_a_resposta)
        self.checkbox_3.grid(row=3, column=0, pady=(20, 0), padx=(0, 10), sticky="n")
        self.checkbox_4 = customtkinter.CTkCheckBox(master=self.sidebar_frame, text='Resposta em Audio',
                                                    command=self.status_checkbox_falar_a_resposta)
        self.checkbox_4.grid(row=4, column=0, pady=(20, 0), padx=(0, 10), sticky="n")

        # THEME
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                                       values=["Light", "Dark", "System"],
                                                                       command=self.tema)
        self.appearance_mode_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 10))

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=300, scrollbar_button_color='blue')
        self.textbox.grid(row=0, column=1, columnspan=4, padx=(20, 20), pady=(20, 0), sticky="nsew")

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Escreva a pergunta")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(master=self, text='Enviar', fg_color="transparent", border_width=2,
                                                     text_color=("gray10", "#DCE4EE"), command=self.escreva_a_pergunta)
        self.main_button_1.grid(row=3, column=3, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_2 = customtkinter.CTkButton(master=self, text='Falar', fg_color="transparent", border_width=2,
                                                     text_color=("gray10", "#DCE4EE"), command=self.fale_a_pergunta)
        self.main_button_2.grid(row=3, column=4, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # definir parametros iniciais
        self.appearance_mode_optionemenu.set("Dark")
        self.main_button_1.configure(state="disabled", text="Texto Desativado")
        self.main_button_2.configure(state="disabled", text="Fala Desativada ")
        self.textbox.insert('0.0', '\n Para acionar o modo Texto ou Fala selecione as opções ao lado \n')

    def tema(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def status_checkbox_escreva_text(self):
        if self.checkbox_1.get() == 1:
            self.info_1 = '\nModo Texto Ativado \n'
            self.textbox.insert('0.0', self.info_1)
            self.main_button_1.configure(state="enable", text="Enviar")
        if self.checkbox_1.get() == 0:
            self.textbox.insert('0.0', '\nModo Texto Desativado \n')
            self.main_button_1.configure(state="disabled", text="Texto Desativada")

    def status_checkbox_fale_a_pergunta(self):
        if self.checkbox_2.get() == 1:
            self.info_1 = '\nModo Fala Ativado \n'
            self.textbox.insert('0.0', self.info_1)
            self.main_button_2.configure(state="enable", text="Falar")
        if self.checkbox_2.get() == 0:
            self.textbox.insert('0.0', '\nModo Fala Desativado \n')
            self.main_button_2.configure(state="disabled", text="Fala Desativada")

    def escreva_a_pergunta(self):
        if self.textbox.insert == None:
            self.textbox.insert('0.0', '\n Escreva sua pergunta e clique em Enviar \n')
        else:
            self.textbox.insert('0.0', '\n' + str(self.entry.get()) + '\n')

    def fale_a_pergunta(self):
        self.textbox.insert('0.0', '\n' + str(self.entry.get()) + '\n')

    def status_checkbox_escrever_a_resposta(self):
        if self.checkbox_3.get() == 1:
            self.textbox.insert('0.0', '\n Resposta em Texto Ativado \n')
        if self.checkbox_3.get() == 0:
            self.textbox.insert('0.0', '\n Resposta em Texto Desativado \n')

    def status_checkbox_falar_a_resposta(self):
        if self.checkbox_4.get() == 1:
            self.textbox.insert('0.0', '\n Resposta em Fala Ativado \n')
        if self.checkbox_4.get() == 0:
            self.textbox.insert('0.0', '\n Resposta em Fala Desativado \n')

    def resposta_em_texto(self):
        self.textbox.insert('0.0', '\n Teste BT3 ok \n')

    def resposta_em_audio(self):
        self.textbox.insert('0.0', '\n Teste BT4 ok \n')


if __name__ == "__main__":
    app = App()
    app.mainloop()