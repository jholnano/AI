# AI

Desenvolvendo novas funcionalidades para interagir com a API OpenAI,

foram utilizadar bibliotecas adicionais neste projeto para obtermos uma interface grafica mais agradavel e moderna
utilizei as seguinte bibliotecas neste projeto basico.

1 Biblioteca Tkinter / CustomTKinter: para criar um template 
2 Biblioteca SpeechRecognition / PyAudio: para reconhecimento de voz esta api do Google pretorna a respostas em texto do foi falado no MIC
3 Biblioteca gTTS / Playsound: gtts é uma API que repoduz a voz Google e salva um arquivo MP3, já a Playsounde utilizamos para produzir o audio 
4 Biblioteca OpenAI, esta API desponibiliza a iteração com o site GPT, com isso obtivemos resposta em texto,

Tratamento de Erros
No próximos passos irei tratar os varios IF's criado para tratar os boões de verificação checkbox para ciar as regras se a caixa esta selecionada ou não 
a iteração com o programa é muito simples, 
temos a opção de "Pergunta" e de "Resposta", cada uma contem 2 checkbox para ativar os botões de pesquisa ou de fala, e os outros dois botões do Resposta, habilita a se esta pergunta será respondido em Texto ou em Audio, 
criei um tratamento para os boões de pesquisa não habilitarem caso não esteja com as opções não tem respota, porem realizei um que não tem tanta utilizadade porem criei mesmo assim para ter o risco de uma resposta sem termos chamado 

![Captura de Tela 2023-02-18 às 15 58 13](https://user-images.githubusercontent.com/50936327/220205040-14eccdcc-594f-4f91-89f3-0a7d1c9c7c6c.png)
