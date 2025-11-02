cd ~/Desktop/flipper_Simulation

# ─────────────────────────────────────
# 1. app.py  (Flask + gunicorn ready)
# ─────────────────────────────────────
cat > app.py << 'EOF'
from flask import Flask, send_from_directory, jsonify
import os

app = Flask(__name__, static_folder='.')

# Serve static files (HTML, CSS, JS, images) from the root folder
@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/amazon')
def amazon():
    return send_from_directory('.', 'amazon.html')

# Simple health-check endpoint – eBay likes to see this
@app.route('/health')
def health():
    return jsonify(status="ok", app="Flipper LIVE")

# Fallback for any other static file (optional but nice)
@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    # Render (and most PaaS) inject PORT env var
    port = int(os.getenv('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=True)
EOF

# ─────────────────────────────────────
# 2. requirements.txt  (add gunicorn)
# ─────────────────────────────────────
cat > requirements.txt << 'EOF'
flask==2.3.3
gunicorn==23.0.0
EOF

# ─────────────────────────────────────
# 3. (Optional) .gitignore – keep Render clean
# ─────────────────────────────────────
cat > .gitignore << 'EOF'
__pycache__/
*.pyc
.env
venv/
*.log
EOF

# ─────────────────────────────────────
# 4. Commit & push (if you use Git)
# ─────────────────────────────────────
git add app.py requirements.txt .gitignore
git commit -m "Fix Render deploy: add gunicorn + health endpoint"
git push origin main
EOF
