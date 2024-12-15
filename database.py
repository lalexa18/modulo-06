import sqlite3

def connect_db():
    return sqlite3.connect("recipes.db")

def init_db():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS recipes (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            ingredients TEXT NOT NULL,
            steps TEXT NOT NULL
        )
        """)
        conn.commit()

def add_recipe(name, ingredients, steps):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO recipes (name, ingredients, steps) VALUES (?, ?, ?)", (name, ingredients, steps))
        conn.commit()

def get_recipes():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM recipes")
        return cursor.fetchall()

def get_recipe(recipe_id):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM recipes WHERE id = ?", (recipe_id,))
        return cursor.fetchone()

def update_recipe(recipe_id, name, ingredients, steps):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE recipes SET name = ?, ingredients = ?, steps = ? WHERE id = ?", (name, ingredients, steps, recipe_id))
        conn.commit()

def delete_recipe(recipe_id):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM recipes WHERE id = ?", (recipe_id,))
        conn.commit()