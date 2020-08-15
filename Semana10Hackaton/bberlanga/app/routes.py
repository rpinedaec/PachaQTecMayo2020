from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user
from flask_login import logout_user
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse
from app.models import User,Producto, Categoria
from app.forms import RegistrationForm, AddProductoForm
from app import db

@app.route('/')
@app.route('/index')
@login_required
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Inicio', posts=posts)
@app.route('/users')
def getUsers():
    usuarios =[
        {
            "nombre":"Roberto"
        },{
            "nombre":"David"
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

@app.route('/productos', methods=['GET', 'POST'])
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
        flash('Producto creado!')
        return redirect(url_for('getProductos'))
    return render_template('AddProducto.html', title='Crear Producto', form=form, categorias = categorias)