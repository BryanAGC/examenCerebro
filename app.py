from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def show_notebook():
    # Aquí puedes renderizar la plantilla HTML con la imagen generada
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
