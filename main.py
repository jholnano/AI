# Projeto futuro Realizar Auto_Instaledor
import os

# realizar verificação do sistema em que será utilizado o instalar manual

# abrindo o buscador
os.system('open -a "Google Chrome"')

# instalar dependencias
os.system("sh packeges.sh")

# Atualizando pip
os.system("pip install --upgrade pip")