from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json():
    """JSON faylını oxuyub list qaytarır"""
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def read_csv():
    """CSV faylını oxuyub list (dictionary kimi) qaytarır"""
    products = []
    try:
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # CSV-dən oxunan id string olur, onu int-ə çevirmək olar
                # amma biz aşağıda müqayisə edərkən hər ikisini string edəcəyik.
                row['id'] = int(row['id']) 
                row['price'] = float(row['price'])
                products.append(row)
        return products
    except FileNotFoundError:
        return []

@app.route('/products')
def products():
    # 1. URL-dən parametrləri götürürük
    source = request.args.get('source') # ?source=...
    product_id = request.args.get('id') # ?id=... (bu optionaldır)

    # 2. Source yoxlaması (Wrong source)
    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    else:
        # Əgər source json və ya csv deyilsə
        return render_template('product_display.html', error="Wrong source")

    # 3. ID filterləməsi (Product not found)
    if product_id:
        # ID-yə görə axtarış edirik.
        # Diqqət: product['id'] int ola bilər, product_id isə URL-dən gəldiyi üçün stringdir.
        # Ona görə də müqayisə üçün hər ikisini string-ə çeviririk (str).
        filtered_data = [p for p in data if str(p['id']) == str(product_id)]
        if not filtered_data:
            return render_template('product_display.html', error="Product not found")
        # Tapılan məhsulu data dəyişəninə mənimsədirik
        data = filtered_data

    # 4. Nəticəni ekrana göndəririk
    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
