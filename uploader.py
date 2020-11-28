from flask import Flask, render_template, request, redirect, url_for
import os
import recognition

app = Flask(__name__)

app.config['IMAGE_UPLOADS'] = '/home/saurabh/Code/WebAPI/static/image/'

@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/about', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        if request.files:
            image = request.files['file']
            image.save(os.path.join(app.config['IMAGE_UPLOADS'], image.filename))
            print('Image saved!')
            return redirect(request.url)
    return render_template("load.html")

@app.route('/engine', methods=['GET','POST'])
def out():
    return recognition.extract_values()

if __name__ == '__main__':
    app.run(debug=True)