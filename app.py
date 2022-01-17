from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('hello.html', list_of_names=['Pan', 'Jamie', 'Jared'])

if __name__ == '__main__':
    app.run(debug=True)
