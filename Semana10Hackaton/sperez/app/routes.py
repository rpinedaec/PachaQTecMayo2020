from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user
from flask_login import logout_user
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse
from app.models import User, Producto, Categoria, TipoDocumento, Cliente, DetalleFactura, Factura
from app.forms import RegistrationForm, AddProductoForm, AddCategoriaForm, AddTipoDocumentoForm, AddClienteForm, AddFacturaForm, AddDetalleFacturaForm, DetalleForm
from app import db

@app.route('/')
@app.route('/index')
@login_required
def index():
    posts = ['Categorias', 'Productos', 'Clientes', 'Facturas']
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
            flash('Usuario o contraseña incorrecta')
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
        flash('Felicidades, Se registro correctamente al usuario!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/Productos', methods=['GET', 'POST'])
def getProductos():
    productos = db.session.query(Producto,Categoria).join(Categoria, Producto.categoria_id==Categoria.id).all()
    categorias = Categoria.query.all()
    return render_template('productos.html', title='Productos', productos=productos)

@app.route('/Producto/add', methods=['GET', 'POST'])
def addProducto():
    form = AddProductoForm()
    categorias = Categoria.query.all()
    if form.validate_on_submit():
        producto = Producto(nombre=form.nombre.data,stock = form.stock.data, 
        precio=form.precio.data,categoria_id=form.categoria.data)        
        db.session.add(producto)
        db.session.commit()
        flash('Producto agregado!')
        return redirect(url_for('getProductos'))
    return render_template('AddProducto.html', title='Crear Producto', form=form, categorias = categorias)

@app.route('/Categorias', methods=['GET', 'POST'])
def getCategorias():
    categorias = Categoria.query.all()
    return render_template('categorias.html', title='Categorias', categorias = categorias)

@app.route('/Categoria/add', methods=['GET', 'POST'])
def addCategoria():
    form = AddCategoriaForm()    
    if form.validate_on_submit():
        categoria = Categoria(nombre=form.nombre.data)        
        db.session.add(categoria)
        db.session.commit()
        flash('Categoria agregado!')
        return redirect(url_for('getCategorias'))
    return render_template('AddCategoria.html', title='Crear Categoria', form=form)

@app.route('/TipoDocumento', methods=['GET', 'POST'])
def getTipoDocumento():
    tipodocumento = TipoDocumento.query.all()
    return render_template('tipodocumento.html', title='Tipo de Documento', tipodocumento = tipodocumento)

@app.route('/TipoDocumento/add', methods=['GET', 'POST'])
def addTipoDocumento():
    form = AddTipoDocumentoForm()    
    if form.validate_on_submit():
        tipodocumento = TipoDocumento(descripcion=form.descripcion.data)        
        db.session.add(tipodocumento)
        db.session.commit()
        flash('Tipo de Documento agregado!')
        return redirect(url_for('getTipoDocumento'))
    return render_template('AddTipoDocumento.html', title='Crear Tipo de Documento', form=form)

@app.route('/Clientes', methods=['GET', 'POST'])
def getClientes():    
    clientes = db.session.query(Cliente, TipoDocumento).join(TipoDocumento, Cliente.documento==TipoDocumento.id).all()
    return render_template('clientes.html', title='Clientes', clientes = clientes)

@app.route('/Cliente/add', methods=['GET', 'POST'])
def addCliente():
    form = AddClienteForm()
    if form.validate_on_submit():
        cliente = Cliente(nombre=form.nombre.data, apellido_pat=form.apellido_pat.data, 
                        apellido_mat=form.apellido_mat.data, documento=form.documento.data, 
                        numero_documento = form.numero_documento.data)        
        db.session.add(cliente)
        db.session.commit()
        flash('Cliente agregado!')
        return redirect(url_for('getClientes'))
    return render_template('AddCliente.html', title='Crear Cliente', form=form)

@app.route('/Facturas', methods=['GET', 'POST'])
def getFacturas():
    form2 = DetalleForm() 
    facturas = db.session.query(Factura, DetalleFactura, Producto, Cliente).join(DetalleFactura, Factura.id==DetalleFactura.factura).join(Producto, DetalleFactura.producto==Producto.id).join(Cliente, Factura.cliente==Cliente.id).distinct(DetalleFactura.factura).all()
    print(form2.errors)
    if form2.validate_on_submit():
        factura = db.session.query(DetalleFactura, Factura, Producto, Cliente).filter_by(factura=request.form['factura']).join(Factura, Factura.id==DetalleFactura.factura).join(Producto, Producto.id==DetalleFactura.producto).join(Cliente, Cliente.id==Factura.cliente).all()
        cliente = db.session.query(DetalleFactura, Factura, Producto, Cliente).filter_by(factura=request.form['factura']).join(Factura, Factura.id==DetalleFactura.factura).join(Producto, Producto.id==DetalleFactura.producto).join(Cliente, Cliente.id==Factura.cliente).distinct(Cliente.nombre).all()
        print(form2.errors , '*', factura)
        return render_template('Factura.html', tittle='Factura', factura=factura, cliente=cliente)
    return render_template('facturas.html', title='Facturas', facturas = facturas, form2=form2)

@app.route('/Factura/add', methods=['GET', 'POST'])
def addFactura():
    form = AddFacturaForm()
    form1 = AddDetalleFacturaForm()
    form2 = DetalleForm()
    print(form.errors, '', form2, '', form2.errors)
    if form.validate_on_submit():
        factura = Factura(cliente=form.cliente.data)
        db.session.add(factura)
        db.session.commit()
        flash('Factura Creada!')
        fac = Factura.query.filter_by(cliente=form.cliente.data).order_by(Factura.id.desc()).first()
        cliente = Cliente.query.filter_by(id=form.cliente.data).first()
        return render_template('AddDetalle.html', title='Detalle Factura', form1=form1, fac=fac, cliente=cliente, form2=form2)
        #return redirect(url_for('addDetalle', cliente=cliente))
    if form1.validate_on_submit():
        detalle = DetalleFactura(factura=request.form['factura'], producto=form1.producto.data, cantidad=form1.cantidad.data)
        db.session.add(detalle)
        db.session.commit()
        flash('Producto Añadido!')
        fac = Factura.query.filter_by(id=request.form['factura']).first()
        cliente = Cliente.query.filter_by(id=request.form['cli']).first()
        print("submit")
        return render_template('AddDetalle.html', title='Detalle Factura', form1=form1, fac=fac, cliente=cliente, form2=form2)
    if form2.validate_on_submit():
        factura = db.session.query(DetalleFactura, Factura, Producto, Cliente).filter_by(factura=request.form['factura']).join(Factura, Factura.id==DetalleFactura.factura).join(Producto, Producto.id==DetalleFactura.producto).join(Cliente, Cliente.id==Factura.cliente).all()
        cliente = db.session.query(DetalleFactura, Factura, Producto, Cliente).filter_by(factura=request.form['factura']).join(Factura, Factura.id==DetalleFactura.factura).join(Producto, Producto.id==DetalleFactura.producto).join(Cliente, Cliente.id==Factura.cliente).distinct(Cliente.nombre).all()
        print("submit2")
        flash('Factura Realizada!')
        return render_template('Factura.html', tittle='Factura', factura=factura, cliente=cliente)
    print(form.errors, '', form2, '*', form2.errors)
    return render_template('AddFactura.html', title='Crear Factura', form=form)