from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user
from flask_login import logout_user
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse
from app.models import User, Producto, Categoria, Factura
from app.forms import RegistrationForm, AddProductoForm, DeleteProductoForm, addFacturaForm, DeleteFacturaForm, addCategoriaForm, DeleteCategoriaForm
from app import db

@app.route('/')
@app.route('/index')
@login_required
def index():
    user = {'username': 'Lorena'}
    posts = [
        {
            'author': {'username': 'a'},
            'body': 'Hi!'
        },
        {
            'author': {'username': 'b'},
            'body': 'Hey!'
        }
    ]
    return render_template('index.html', title='Inicio', posts=posts)

# @app.route('/back')
# def GoBack():
#     <input type="button" value="Go back!" onclick="history.back()">

@app.route('/users')
def getUsers():
    usuarios =[
        {
            "nombre":"Lorena"
        },{
            "nombre":"Andrea"
        }
    ]
    return render_template('users.html', title='Usuarios', usuarios=usuarios)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/productos')
def Productos():
    return render_template('productspage.html', title='Products')

@app.route('/showproductos', methods=['GET', 'POST'])
def getProductos():
    prodcutos = Producto.query.all()
    return render_template('productos.html', title='Productos', productos=prodcutos)

@app.route('/producto/add', methods=['GET', 'POST'])
def addProducto():
    form = AddProductoForm()
    categorias = Categoria.query.all()
    if form.validate_on_submit():
        producto = Producto(nombre=form.nombre.data,stock = form.stock.data, 
        precio=form.precio.data,categoria_id=form.categoria_id.data)
        
        db.session.add(producto)
        db.session.commit()
        flash('Product created!')
        return redirect(url_for('index'))
    return render_template('addProducto.html', title='Crear Producto', form=form, categorias = categorias)

@app.route('/producto/add', methods=['GET', 'POST'])
def DeleteProducto():
    form = DeleteProductoForm()
    categorias = Categoria.query.all()
    if form.validate_on_submit():
        producto = Producto(nombre=form.nombre.data,stock = form.stock.data, 
        precio=form.precio.data,categoria_id=form.categoria_id.data)
        
        db.session.delete(producto)
        db.session.commit()
        flash('Product deleted!')
        return redirect(url_for('index'))
    return render_template('DeleteProducto.html', title='Delete Product', form=form, categorias = categorias)

@app.route('/cajero/factura', methods=['GET', 'POST'])
def addFactura():
    form = addFactura()
    categorias = Categoria.query.all()
    if form.validate_on_submit():
        factura = factura(date=form.date.data, products = form.products.data, 
         total=form.total.data)
        
        db.session.add(factura)
        db.session.commit()
        flash('Recipt created!')
        return redirect(url_for('factura'))
    return render_template('productspage.html', title='Products', form=form, categorias = categorias)

@app.route('/facturas/show', methods=['GET', 'POST'])
def showfacturas():
    facturas = Factura.query.all()
    return render_template('showfacturas.html', title='Facturas', facturas=facturas)

@app.route('/facturas/add', methods=['GET', 'POST'])
def DeleteFactura():
    form = DeleteFacturaForm()
    categorias = Categoria.query.all()
    if form.validate_on_submit():
        factura = Factura(date=form.date.data,products = form.products.data, 
         total=form.total.data)
        
        db.session.delete(factura)
        db.session.commit()
        flash('Product deleted!')
        return redirect(url_for('DeleteProducto'))
    return render_template('DeleteProducto.html', title='Delete Product', form=form, categorias = categorias)

@app.route('/cajero')
def Cajero():
    return render_template('cajero.html', title='Cajero')

@app.route('/administrador')
def Administrador():
    return render_template('administrador.html', title='Administrator')

@app.route('/categories/show', methods=['GET', 'POST'])
def getCategorias():
    categoria = Categoria.query.all()
    return render_template('categoria.html', title='Categorias', categoria=categoria)

@app.route('/producto/add', methods=['GET', 'POST'])
def addCategoria():
    form = AddProductoForm()
    if form.validate_on_submit():
        categoria = Categoria(nombre=form.nombre.data)
        
        db.session.add(categoria)
        db.session.commit()
        flash('Category created!')
        return redirect(url_for('categoria'))
    return render_template('addCategoria.html', title='Crear Categoria', form=form, categoria = categoria)

@app.route('/producto/add', methods=['GET', 'POST'])
def DeleteCategoria():
    form = DeleteCategoriaForm()
    if form.validate_on_submit():
        categoria = Categoria(nombre=form.nombre.data)
        
        db.session.delete(categoria)
        db.session.commit()
        flash('Category deleted!')
        return redirect(url_for('categoria'))
    return render_template('DeleteCategoria.html', title='Delete Category', form=form, categoria = categoria)