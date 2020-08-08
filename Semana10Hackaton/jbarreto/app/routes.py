from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user
from flask_login import logout_user
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse
from app.models import User, Producto, Categoria, Cab_comprobante, Cliente, Det_comprobante
from app.forms import RegistrationForm, AddProductoForm, AddComprobanteForm, AddClienteForm
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
    productos = Producto.query.all()
    return render_template('productos.html', title='Productos', productos=productos)

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

@app.route('/comprobantes', methods=['GET', 'POST'])
def getComprobantes():
    cabComprobantes = Cab_comprobante.query.all()
    return render_template('comprobantes.html', title='Comprobantes', cabComprobantes=cabComprobantes)

@app.route('/comprobante/add', methods=['GET', 'POST'])
def addComprobante():
    form = AddComprobanteForm()
    clientes = Cliente.query.all()
    productos = Producto.query.all()
    if form.validate_on_submit():
        comprobante = Cab_comprobante(fecha=form.fecha.data,tipo_comprobante_id=form.tipo_comprobante_id.data, 
         nro_comprobante=form.nro_comprobante.data,igv=form.igv.data,total=form.total.data,cliente_id=form.cliente_id.data)
        db.session.add(comprobante)
        db.session.commit()

        det_comprobante = Det_comprobante(item=form.item.data,cantidad=form.cantidad.data,precio=form.precio.data,
        subtotal=form.subtotal.data,cab_comprobante_id=comprobante.id,producto_id=form.producto_id.data)
        db.session.add(det_comprobante)
        db.session.commit()

        flash('Comprobante creado!')
        return redirect(url_for('getComprobantes'))
    return render_template('AddComprobante.html', title='Crear Comprobante', form=form, clientes = clientes, productos = productos)

@app.route('/clientes', methods=['GET', 'POST'])
def getClientes():
    clientes = Cliente.query.all()
    return render_template('clientes.html', title='Clientes', clientes=clientes)

@app.route('/cliente/add', methods=['GET', 'POST'])
def addCliente():
    form = AddClienteForm()
    if form.validate_on_submit():
        cliente = Cliente(dni=form.dni.data,nombre=form.nombre.data,apellidos=form.apellidos.data)
        
        db.session.add(cliente)
        db.session.commit()
        flash('Cliente creado!')
        return redirect(url_for('getClientes'))
    return render_template('AddCliente.html', title='Crear Cliente', form=form)