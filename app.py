from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index2.html')  # Render a template

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 5000  # Change to the port you prefer
    port = int(port)

    app.run(port=port, host='0.0.0.0')
