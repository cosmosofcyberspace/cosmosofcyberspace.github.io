from flask import Flask, request, render_template_string

app = Flask(__name__)

app.secret_key = 'secret'

@app.route('/', methods=['GET', 'POST'])
def home():
    name = ''
    if request.method == 'POST':
        name = request.form.get('name', '')
    
    template = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>SSTI Lab - Welcome</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css">
    </head>
    <body>
        <div class="container mt-5">
            <h1 class="mb-4">Template Injection Lab</h1>
            <div class="card">
                <div class="card-header bg-primary text-white">
                    <h3>Welcome Message Generator</h3>
                </div>
                <div class="card-body">
                    <form method="POST">
                        <div class="mb-3">
                            <label for="name" class="form-label">Enter your name:</label>
                            <input type="text" class="form-control" id="name" name="name" placeholder="Your name">
                        </div>
                        <button type="submit" class="btn btn-primary">Generate Welcome</button>
                    </form>
                    ''' + ('''
                    <div class="mt-4 p-3 bg-light border rounded">
                        <h4>Generated Welcome:</h4>
                        <p>Hello ''' + name + '''!</p>
                    </div>
                    ''' if name else '') + '''
                </div>
            </div>
            
            <div class="mt-4">
                <div class="alert alert-info">
                    <h4>Lab Instructions:</h4>
                    <p>This web application has a Server-Side Template Injection vulnerability. Try to exploit it!</p>
                    <p>Hint: Jinja2 templates can execute Python code with specific syntax.</p>
                </div>
            </div>
            
            <div class="mt-3">
                <a href="/secure" class="btn btn-success">Secure Version</a>
            </div>
        </div>
    </body>
    </html>
    '''
    
    return render_template_string(template)

@app.route('/secure', methods=['GET', 'POST'])
def secure():
    name = ''
    if request.method == 'POST':
        name = request.form.get('name', '')
    
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>SSTI Lab - Secure Version</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css">
    </head>
    <body>
        <div class="container mt-5">
            <h1 class="mb-4">Template Injection Lab (Secure Version)</h1>
            <div class="card">
                <div class="card-header bg-success text-white">
                    <h3>Welcome Message Generator - Secure</h3>
                </div>
                <div class="card-body">
                    <form method="POST">
                        <div class="mb-3">
                            <label for="name" class="form-label">Enter your name:</label>
                            <input type="text" class="form-control" id="name" name="name" placeholder="Your name">
                        </div>
                        <button type="submit" class="btn btn-success">Generate Welcome</button>
                    </form>
                    
                    {% if name %}
                    <div class="mt-4 p-3 bg-light border rounded">
                        <h4>Generated Welcome:</h4>
                        <p>Hello {{ name }}!</p>
                    </div>
                    {% endif %}
                </div>
            </div>
            
            <div class="mt-4">
                <div class="alert alert-success">
                    <h4>Secure Implementation:</h4>
                    <p>This page uses proper template variable interpolation, which is safe from injection attacks.</p>
                </div>
            </div>
            
            <div class="mt-3">
                <a href="/" class="btn btn-primary">Back to Vulnerable Version</a>
            </div>
        </div>
    </body>
    </html>
    ''', name=name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 
