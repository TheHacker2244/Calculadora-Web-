from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculadora():
    resultado = ""
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operacion = request.form['operacion']
            
            if operacion == 'suma':
                resultado = f"{num1} + {num2} = {num1 + num2}"
            elif operacion == 'resta':
                resultado = f"{num1} - {num2} = {num1 - num2}"
            elif operacion == 'multiplicacion':
                resultado = f"{num1} x {num2} = {num1 * num2}"
            elif operacion == 'division':
                if num2 == 0:
                    resultado = "Error: División por cero"
                else:
                    resultado = f"{num1} ÷ {num2} = {num1 / num2}"
            else:
                resultado = "Operación no válida"
                
        except ValueError:
            resultado = "Error: Entrada no válida"
    
    return render_template('calculadora.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)