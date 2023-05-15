from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Default text
text = "Hello, Flask!"

@app.route('/')
def home():
    return render_template('index.html', text=text)

@app.route('/update', methods=['POST'])
def update_text():
    global text
    new_text = request.form.get('new_text')
    text = new_text
    return 'Text updated successfully!'

@app.route('/api/update', methods=['POST'])
def api_update_text():
    global text
    new_text = request.json.get('new_text')
    if new_text:
        text = new_text
        return jsonify({'message': 'Text updated successfully'})
    else:
        return jsonify({'error': 'Invalid request'})

if __name__ == '__main__':
    app.run(debug=True)