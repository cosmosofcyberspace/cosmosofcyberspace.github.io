from flask import Flask

app = Flask(__name__)

@app.route('/flag.txt')
def flag():
    with open('flag.txt', 'r') as f:
        flag_content = f.read()
    return flag_content

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001) 
