from flask import Flask, request, send_from_directory, redirect, url_for
import os

app = Flask(__name__)

# Set the upload folder and allowed file extensions
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif',"exe"}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to check if a file has an allowed extension
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route to upload a file
@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if a file was submitted
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    # Check if the file has an allowed extension
    if file and allowed_file(file.filename):
        # Save the file to the upload folder
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'File uploaded successfully!'
    else:
        return 'Invalid file extension!'

# Route to download a file
@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    # Return the file from the upload folder
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True,host='192.168.1.105')
