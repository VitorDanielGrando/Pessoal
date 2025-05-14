from flask import flask, render_template,request 
import os

# Defina as pastas onde estão os arquivos HTML
# (Neste caso, a raiz do projeto)

template_dir = os.path.abspath(os.path.dirname(__file__))
app = flask(__name__, template_folder=template_dir)
