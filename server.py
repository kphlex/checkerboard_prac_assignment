from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', rows = 8, cols = 8, color_primary= 'black', color_secondary="blue")

@app.route('/<int:x>')
def rows(x):
    return render_template('index.html', rows = x, cols = 8, color_primary= 'black', color_secondary="blue")

@app.route('/<int:x>/<int:y>')
def rows_cols(x,y):
    return render_template('index.html', rows = x, cols = y, color_primary= 'black', color_secondary="blue")

@app.route('/<int:x>/<int:y>/<string:primary>')
def rows_cols_primary(x,y,primary):
    return render_template('index.html', rows = x , cols = y , color_primary= primary, color_secondary="blue")

@app.route('/<int:x>/<int:y>/<string:primary>/<string:secondary>')
def rows_cols_both(x,y,primary,secondary):
    return render_template('index.html', rows = x , cols = y , color_primary= primary, color_secondary= secondary)



if __name__ == '__main__':
    app.run(debug=True)