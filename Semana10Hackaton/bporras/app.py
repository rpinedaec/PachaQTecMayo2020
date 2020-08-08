from flask import Flask, render_template, request, redirect, url_for, flash 
from flask_sqlalchemy import SQLAlchemy
#config
app = Flask(__name__)
app.secret_key = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/Hackathon_10'
db = SQLAlchemy(app)


#models
class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(64), index=True)
    producto = db.relationship('Producto', backref='product', lazy='dynamic')

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), index=True)
    stock = db.Column(db.Integer)
    precio = db.Column(db.Numeric(10,2))
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'))

#routes
@app.route('/')
def Index():
    producto = Producto.query.all()
    categoria = Categoria.query.all()
    db.session.commit()
    return render_template("index.html", productos = producto, categorias = categoria )

@app.route('/addProducto', methods=['POST'])
def add_producto():
    if request.method == 'POST':
        Nombre = request.form['name']
        Stock = request.form['stock']
        Precio = request.form['price']
        Categoria = request.form['category']
        producto = Producto(nombre = Nombre, stock = Stock, precio = Precio, categoria_id = Categoria) 
        db.session.add(producto)
        db.session.commit()
        flash('Product added sucessfully')
        return redirect(url_for('Index'))

@app.route('/addCategoria', methods=['POST'])
def add_categoria():
    if request.method == 'POST':
        Nombre = request.form['name']
        categoria = Categoria(nombre = Nombre)
        db.session.add(categoria)
        db.session.commit()
        flash('Category added sucessfully')
        return redirect(url_for('Index'))

@app.route('/editProducto/<id>')
def get_producto(id):
    producto = Producto.query.get(id)
    db.session.commit()
    return render_template("edit-product.html", product = producto )

@app.route('/editCategoria/<id>')
def get_categoria(id):
    categoria = Categoria.query.get(id)
    db.session.commit()
    return render_template("edit-category.html", category = categoria )

@app.route('/updateProducto/<id>', methods=['POST'])
def update_producto(id):
    if request.method == 'POST':
        producto = Producto.query.get(id)
        producto.nombre = request.form['name']
        producto.stock = request.form['stock']
        producto.precio = request.form['price']
        producto.categoria = request.form['category'] 
        db.session.add(producto)
        db.session.commit()
        flash('Contact updated sucessfully')
        return redirect(url_for('Index'))

@app.route('/updateCategoria/<id>', methods=['POST'])
def update_categoria(id):
    if request.method == 'POST':
        categoria = Categoria.query.get(id)
        categoria.nombre = request.form['name']
        db.session.add(categoria)
        db.session.commit()
        flash('Category updated sucessfully')
        return redirect(url_for('Index'))

@app.route('/deleteProducto/<string:id>')
def delete_producto(id):
    producto = Producto.query.get(id)
    db.session.delete(producto)
    db.session.commit()
    flash('Contact removed sucessfully')
    return redirect(url_for('Index'))

@app.route('/deleteCategoria/<string:id>')
def delete_categoria(id):
    categoria = Categoria.query.get(id)
    db.session.delete(categoria)
    db.session.commit()
    flash('Category removed sucessfully')
    return redirect(url_for('Index'))

#Config

if __name__ == '__main__':
    app.run(port = 3000, debug = True)

