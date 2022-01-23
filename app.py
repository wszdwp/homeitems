from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='templates')

@app.route("/", methods=['GET'])
def index():
    request_method = request.method
    return render_template('index.html', list_of_names=['Category', 'Location', 'Item'], request_method=request_method)

@app.route('/category')
def category():
    return render_template('category.html',  page_name='category', list_of_names=['furnitures', 'tools', 'clothes'])

@app.route('/location')
def location():
    return render_template('location.html', page_name='location', list_of_names=['furnitures', 'tools', 'clothes'])

@app.route('/item', methods=['GET', 'POST'])
def item():
    request_method = request.method
    if request_method == 'POST':
        print('----------')
        print(request.form)
        print('----------')
        return redirect(url_for('item'))
    else:
        return render_template('item.html', page_name='item')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
