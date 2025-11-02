cd ~/Desktop/flipper_Simulation

# Create app.py
cat > app.py << 'EOF'
from flask import Flask

app = Flask(__name__, static_folder='.')

@app.route('/')
def home():
    return open('index.html').read()

@app.route('/amazon')
def amazon():
    return open('amazon.html').read()

if __name__ == '__main__':
    import os
    port = int(os.getenv('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=True)
EOF

# Create requirements.txt
cat > requirements.txt << 'EOF'
flask==2.3.3
EOF