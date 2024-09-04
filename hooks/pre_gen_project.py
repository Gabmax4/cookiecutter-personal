import os
import sys

# Obtiene el valor de la variable `project_slug` desde el contexto de Cookiecutter.
# Este valor es proporcionado por el usuario durante la generación del proyecto.
project_slug = "{{ cookiecutter.project_slug }}"

# Define códigos de color para los mensajes de error y mensajes informativos.
ERROR_COLOR = "\x1b[31m"  # Rojo para errores
MESSAGE_COLOR = "\x1b[34m"  # Azul para mensajes informativos
RESET_ALL = "\x1b[0m"  # Resetea el color al valor predeterminado

# Verifica si el nombre del proyecto (`project_slug`) comienza con la letra "x".
if project_slug.startswith("x"):
    # Si el nombre del proyecto comienza con "x", imprime un mensaje de error en rojo.
    print(f"{ERROR_COLOR}ERROR: {project_slug=} is not a valid name for this template.{RESET_ALL}")

    # Termina la ejecución del script con un código de salida 1 (indicando un error).
    sys.exit(1)

# Si el nombre del proyecto es válido, imprime un mensaje informativo en azul.
print(f"{MESSAGE_COLOR}Let's do it! You're going to create something awesome!")
print(f"Creating project at {os.getcwd()}{RESET_ALL}")