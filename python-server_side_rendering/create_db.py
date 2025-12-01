import sqlite3

def create_database():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    # Cədvəli yaradırıq
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    # Məlumatları əlavə edirik (əgər boşdursa)
    cursor.execute('INSERT OR IGNORE INTO Products (id, name, category, price) VALUES (1, "Laptop", "Electronics", 799.99)')
    cursor.execute('INSERT OR IGNORE INTO Products (id, name, category, price) VALUES (2, "Coffee Mug", "Home Goods", 15.99)')

    conn.commit()
    conn.close()
    print("products.db faylı yaradıldı və məlumatlar əlavə olundu!")

if __name__ == '__main__':
    create_database()
