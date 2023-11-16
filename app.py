from flask import Flask, render_template, request
import pandas as pd


app = Flask(__name__)
port= 5000
debug = False

@app.route('/')
def index():
    return render_template('index.html')

#EJEMPLO
@app.route('/')
def index():
    return "<h1>Corriendo servidor Flask</h1>"


@app.route('/media', methods=['GET', 'POST'])
def calcular_promedio():
    if request.method == 'POST':
        if 'excel_file' in request.files:
            excel_file = request.files['excel_file']
            if excel_file.filename != '':
                try:
                    df = pd.read_excel(excel_file)
                    promedio = df.mean()  # Calcula el promedio de todas las columnas
                    html_result = promedio.to_frame().to_html()

                    return render_template('media.html', promedio=html_result)
                except Exception as e:
                    return f"Error al procesar el archivo: {e}"

    return render_template('media.html')

@app.route('/moda', methods=['GET', 'POST'])
def calcular_moda():
    if request.method == 'POST':
        if 'excel_file' in request.files:
            excel_file = request.files['excel_file']
            if excel_file.filename != '':
                try:
                    df = pd.read_excel(excel_file)
                    moda = df.mode()  # Calcula la moda de todas las columnas
                    html_result = moda.to_html()

                    return render_template('moda.html', moda=html_result)
                except Exception as e:
                    return f"Error al procesar el archivo: {e}"

    return render_template('moda.html')

@app.route('/mediana', methods=['GET', 'POST'])
def calcular_mediana():
    if request.method == 'POST':
        if 'excel_file' in request.files:
            excel_file = request.files['excel_file']
            if excel_file.filename != '':
                try:
                    df = pd.read_excel(excel_file)
                    mediana = df.median()  # Calcula la mediana de todas las columnas
                    html_result = mediana.to_frame().to_html()

                    return render_template('mediana.html', mediana=html_result)
                except Exception as e:
                    return f"Error al procesar el archivo: {e}"

    return render_template('mediana.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'up' not in request.files:
        return "No file part"

    file = request.files['up']

    if file.filename == '':
        return "No selected file"

    if file:
        df = pd.read_excel(file)
        # Puedes realizar operaciones con 'df' aquí antes de pasar los datos a la plantilla HTML
        return render_template('display.html', tables=[df.to_html(classes='data')], titles=df.columns.values)

@app.route('/ven')
def venn():
    return render_template('ven.html')

if __name__=='__main__':  
    app.run(debug=True)    
#, port=5000
