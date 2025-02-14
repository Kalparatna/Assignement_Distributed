import sqlite3
import threading

DB_CONFIG = {
    'users': 'users.db',
    'products': 'products.db',
    'orders': 'orders.db'
}

def create_tables():
    queries = {
        'users': """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY, 
                name TEXT NOT NULL, 
                email TEXT UNIQUE NOT NULL
            )
        """,
        'products': """
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY, 
                name TEXT UNIQUE NOT NULL, 
                price REAL NOT NULL
            )
        """,
        'orders': """
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY, 
                user_id INTEGER, 
                product_id INTEGER, 
                quantity INTEGER NOT NULL
            )
        """
    }
    for db, query in queries.items():
        conn = sqlite3.connect(DB_CONFIG[db])
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        conn.close()

def insert_data(db_name, query, data):
    conn = sqlite3.connect(DB_CONFIG[db_name])
    cur = conn.cursor()
    for record in data:
        try:
            cur.execute(query, record)
            conn.commit()
            print(f"Inserted {record} into {db_name}")
        except Exception as e:
            print(f"Failed to insert {record} into {db_name}: {e}")
    conn.close()

def validate_and_insert():
    users_data = [
        (1, 'Alice', 'alice@example.com'),
        (2, 'Bob', 'bob@example.com'),
        (3, 'Charlie', 'charlie@example.com'),
        (4, 'David', 'david@example.com'),
        (5, 'Eve', 'eve@example.com'),
        (6, 'Frank', 'frank@example.com'),
        (7, 'Grace', 'grace@example.com'),
        (8, 'Alice', 'alice@example.com'),  
        (9, 'Henry', 'henry@example.com'),
        (10, None, 'jane@example.com')      
    ]

    products_data = [
        (1, 'Laptop', 1000.00),
        (2, 'Smartphone', 700.00),
        (3, 'Headphones', 150.00),
        (4, 'Monitor', 300.00),
        (5, 'Keyboard', 50.00),
        (6, 'Mouse', 30.00),
        (7, 'Laptop', 1000.00), 
        (8, 'Smartwatch', 250.00),
        (9, 'Gaming Chair', 500.00),
        (10, 'Earbuds', -50.00)  
    ]

    orders_data = [
        (1, 1, 1, 2),
        (2, 2, 2, 1),
        (3, 3, 3, 5),
        (4, 4, 4, 1),
        (5, 5, 5, 3),
        (6, 6, 6, 4),
        (7, 7, 7, 2),
        (8, 8, 8, 0),       
        (9, 9, 1, -1),      
        (10, 10, 11, 2)     
    ]

    valid_users = []
    emails = set()
    for u in users_data:
        if u[1] is not None and u[2] not in emails:
            valid_users.append(u)
            emails.add(u[2])
        else:
            print(f"Failed user insertion: {u}")

    valid_products = []
    product_names = set()
    for p in products_data:
        if p[2] > 0 and p[1] not in product_names:
            valid_products.append(p)
            product_names.add(p[1])
        else:
            print(f"Failed product insertion: {p}")

    valid_orders = []
    product_ids = {p[0] for p in valid_products}
    for o in orders_data:
        if o[3] > 0 and o[2] in product_ids:
            valid_orders.append(o)
        else:
            print(f"Failed order insertion: {o}")

    threads = []
    queries = {
        'users': 'INSERT INTO users (id, name, email) VALUES (?, ?, ?)',
        'products': 'INSERT INTO products (id, name, price) VALUES (?, ?, ?)',
        'orders': 'INSERT INTO orders (id, user_id, product_id, quantity) VALUES (?, ?, ?, ?)'
    }

    for db_name, query, data in zip(['users', 'products', 'orders'], 
                                    [queries['users'], queries['products'], queries['orders']],
                                    [valid_users, valid_products, valid_orders]):
        thread = threading.Thread(target=insert_data, args=(db_name, query, data))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def fetch_results():
    for db_name in DB_CONFIG:
        conn = sqlite3.connect(DB_CONFIG[db_name])
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM {db_name.split(".")[0]}')
        rows = cur.fetchall()
        print(f"\n{db_name} data:")
        for row in rows:
            print(row)
        conn.close()

if __name__ == "__main__":
    create_tables()
    validate_and_insert()
    fetch_results()
