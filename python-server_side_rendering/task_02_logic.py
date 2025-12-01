from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# --- YENİ HİSSƏ: /items routu ---
@app.route('/items')
def items():
    items_list = []
    try:
        # JSON faylını oxuyuruq
        with open('items.json', 'r') as f:
            data = json.load(f)
            # 'items' açarını götürürük, yoxdursa boş list qaytarırıq
            items_list = data.get('items', [])
    except FileNotFoundError:
        # Fayl tapılmazsa xəta verməsin, sadəcə boş siyahı olsun
        items_list = []

    # Şablona 'items' dəyişənini göndəririk
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
