from flask import Flask, request, redirect, url_for, render_template
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'pdf','mp3','aac','mp4','jpeg','jpg','png','exe','msi','docx','xlsx','mkv','txt','json','zip','rar'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def upload_form():
    message = {'status':"success", "message":""}
    return render_template('index.html', message=message)

@app.route('/', methods=['POST'])
def upload_file():
    message = {"status":"success","message":""}
    uploaded_file = []
    if 'files' not in request.files:
        return redirect(request.url, message=message)
    files = request.files.getlist('files')
    for file in files:
        if file.filename == '':
            return redirect(request.url, message=message)
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            uploaded_file.append(filename)
            message = {"status":"success","message":"Files uploaded successfully"}
        else:
            message = {"status":"error","message":"File extension not supported add the file extension in ALLOWED_EXTENSIONS"}
    return (render_template("index.html", message=message))


if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True, host='0.0.0.0')
