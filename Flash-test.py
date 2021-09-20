from flask import Flask
app = Flask(__name__) #"__main__"


@app.route('/hello', methods = ['GET'])
def hello_world():
    return """<html>
    <body>
    <h1>Hello World</h1>
    
    <p> this is a paragraph of text.<p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 8080)


