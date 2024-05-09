from flask import Flask, send_from_directory, render_template

app = Flask(__name__, static_folder=".", template_folder=".")

@app.route('/')
def home():
    return render_template('index.html')  # Now directly accessible

@app.route('/<path:path>')
def static_proxy(path):
    # Return the requested file (CSS, JS, images, etc.)
    return send_from_directory('.', path)

if __name__ == '__main__':
    app.run(debug=True)
