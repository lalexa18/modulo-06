# app.py
from flask import Flask, render_template, request, redirect, url_for
import database

app = Flask(__name__)
database.init_db()

@app.route('/')
def index():
    recipes = database.get_recipes()
    return render_template("index.html", recipes=recipes)

@app.route('/recipe/<int:recipe_id>')
def view_recipe(recipe_id):
    recipe = database.get_recipe(recipe_id)
    if recipe:
        return render_template("recipe.html", recipe=recipe)
    return "Recipe not found", 404

@app.route('/add', methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        name = request.form['name']
        ingredients = request.form['ingredients']
        steps = request.form['steps']
        database.add_recipe(name, ingredients, steps)
        return redirect(url_for('index'))
    return render_template("form.html", action="Add")

@app.route('/edit/<int:recipe_id>', methods=["GET", "POST"])
def edit_recipe(recipe_id):
    recipe = database.get_recipe(recipe_id)
    if request.method == "POST":
        name = request.form['name']
        ingredients = request.form['ingredients']
        steps = request.form['steps']
        database.update_recipe(recipe_id, name, ingredients, steps)
        return redirect(url_for('index'))
    return render_template("form.html", action="Edit", recipe=recipe)

@app.route('/delete/<int:recipe_id>')
def delete_recipe(recipe_id):
    database.delete_recipe(recipe_id)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)