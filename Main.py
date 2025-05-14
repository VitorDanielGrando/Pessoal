from flask import flask, render_template,request 
import os

# Defina as pastas onde estão os arquivos HTML
# (Neste caso, a raiz do projeto)

template_dir = os.path.abspath(os.path.dirname(__file__))
app = flask(__name__, template_folder=template_dir)

# Direcionamento para base de index HTML
@app.route("/")
def home ():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host= "0.0.0.0", port=3000)