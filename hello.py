#!/usr/bin/env python3
# shebang -> Sistema unix, comentario especial

"""Hello World Multi Linhas

Dependendo da linguagem configurada do ambiente o programa exibe a mensagem 
correspondente.

USAGE:
Tenha a variável LANG devidamente configurada, exemplo:

    export LANG=pt_BR

RUN:

    python3 hello.py
    ou
    ./hello.py

"""
# METADADOS, variáveis de distribuíções com (Dunder). 
__version__= "0.1.2"
__author__= "Bruno Rocha"
__license__= "unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Bom dia, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour Monde!"
}
# Ordem de complexidade O(N)
print(msg[current_language])