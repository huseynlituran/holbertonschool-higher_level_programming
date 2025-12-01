from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# --- JSON Oxuma Funksiyası ---
def read_json():
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# --- CSV Oxuma Funksiyası ---
def read_csv():
    products = []
    try:
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
        return products
    except FileNotFoundError:
        return []

# --- SQL (SQLite) Oxuma Funksiyası (YENİ) ---
def read_sql():
    products = []
    try:
        # Bazaya qoşuluruq
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()

        # Bütün məlumatları seçirik
        cursor.execute('SELECT * FROM Products')
        rows = cursor.fetchall()

        # Gələn məlumatlar tuple formasındadır (1, 'Laptop', ...).
        # Onları dictionary-ə (lüğətə) çevirməliyik ki, template başa düşsün.
        for row in rows:
            product = {
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            }
            products.append(product)

        conn.close()
        return products
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []

# --- Əsas Route ---
@app.route('/products')
def products():
    # Parametrləri alırıq
    source = request.args.get('source')
    product_id = request.args.get('id')

    # Hansı mənbədən oxuyacağımızı seçirik
    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    elif source == 'sql': # Yeni SQL şərti
        data = read_sql()
    else:
        return render_template('product_display.html', error="Wrong source")

    # ID filterləməsi (Bütün mənbələr üçün eynidir)
    if product_id:
        filtered_data = [p for p in data if str(p['id']) == str(product_id)]
        if not filtered_data:
            return render_template('product_display.html', error="Product not found")

        data = filtered_data

    # Nəticəni şablona göndəririk
    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
