import os
import subprocess

# Define códigos de color para los mensajes informativos.
MESSAGE_COLOR = "\x1b[34m"  # Azul para mensajes informativos
RESET_ALL = "\x1b[0m"  # Resetea el color al valor predeterminado

# Imprime un mensaje informativo indicando que casi se ha terminado.
print(f"{MESSAGE_COLOR}Almost done!")
print(f"Initializing a git repository...{RESET_ALL}")

# Inicializa un nuevo repositorio Git en el directorio actual.
subprocess.call(['git', 'init'])

# Añade todos los archivos en el directorio actual al índice de Git.
subprocess.call(['git', 'add', '*'])

# Realiza un commit inicial con el mensaje "Initial commit".
subprocess.call(['git', 'commit', '-m', 'Initial commit'])

# Imprime un mensaje final indicando que el proceso ha terminado y animando al usuario a crear y divertirse.
print(f"{MESSAGE_COLOR}The beginning of your destiny is defined now! Create and have fun!{RESET_ALL}")