from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user
from flask_login import logout_user
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse
from app.models import User,Producto, Categoria
from app.forms import RegistrationForm, AddProductoForm, DeleteProductoForm, UpdateProductoForm, AddCategoriaForm, DeleteCategoriaForm, UpdateCategoriaForm, AddFacturaForm, AddPedidoForm
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

@app.route('/producto/delete', methods=['GET', 'POST'])
def deleteProducto():
    form = DeleteProductoForm()
    if form.validate_on_submit():
        db.session.query(Producto).filter(Producto.nombre==form.nombre.data).delete()
        db.session.commit()
        flash('Producto eliminada!')
        return redirect(url_for('getProductos'))
    return render_template('DeleteProducto.html', title='Eliminar Producto', form=form)

@app.route('/producto/update', methods=['GET','POST'])
def updateProducto():
    form = UpdateProductoForm()
    categorias = Categoria.query.all()
    if form.validate_on_submit():
        db.session.query(Producto).filter(Producto.nombre==form.nombre.data).update({Producto.nombre:form.nuevoNombre.data, 
                                                                                     Producto.stock:form.nuevoStock.data,
                                                                                     Producto.precio:form.nuevoPrecio.data,
                                                                                     Producto.categoria_id:form.nuevaCategoria_id.data})
        db.session.commit()
        flash('Producto actualizada!')
        return redirect(url_for('getProductos'))
    return render_template('UpdateProducto.html', title='Actualizar Producto', form=form, categorias=categorias)

@app.route('/categoria', methods=['GET', 'POST'])
def getCategoria():
    categorias = Categoria.query.all()
    return render_template('categoria.html', title='Categoria', Categoria=categorias)

@app.route('/categoria/add', methods=['GET', 'POST'])
def addCategoria():
    form = AddCategoriaForm()
    if form.validate_on_submit():
        categoria = Categoria(nombre=form.nombre.data)
        
        db.session.add(categoria)
        db.session.commit()
        flash('Categoria creada!')
        return redirect(url_for('getCategoria'))
    return render_template('AddCategoria.html', title='Crear Categoria', form=form)

@app.route('/categoria/delete', methods=['GET', 'POST'])
def deleteCategoria():
    form = DeleteCategoriaForm()
    if form.validate_on_submit():
        db.session.query(Categoria).filter(Categoria.nombre==form.nombre.data).delete()
        db.session.commit()
        flash('Categoria eliminada!')
        return redirect(url_for('getCategoria'))
    return render_template('DeleteCategoria.html', title='Eliminar Categoria', form=form)


@app.route('/categoria/update', methods=['GET','POST'])
def updateCategoria():
    form = UpdateCategoriaForm()
    if form.validate_on_submit():
        db.session.query(Categoria).filter(Categoria.nombre==form.nombre.data).update({Categoria.nombre:form.nuevoNombre.data})
        db.session.commit()
        flash('Categoria actualizada!')
        return redirect(url_for('getCategoria'))
    return render_template('UpdateCategoria.html', title='Actualizar Categoria', form=form)

@app.route('/factura', methods=['GET','POST'])
def addFactura():
    form = AddFacturaForm()
    if form.validate_on_submit():
        factura = FacturaCab(fecha=form.fecha.data,tipoPago = form.tipoPago.data, total= 0.00)
        db.session.add(factura)
        db.session.commit()
        return redirect(url_for('addPedido'))
    return render_template('AddFactura.html', title='Crear Factura', form=form)

@app.route('/factura/producto', methods=['GET','POST'])
def addPedido():
    form = AddPedidoForm()
    productos = Producto.query.all()
    facturaCab = FacturaCab.query.all()
    facturaDet = facturaDet.query.all()
    if form.validate_on_submit():
        producto = db.session.query(FacturaDet).filter(FacturaDet.producto_id==form.producto_id.data)
        precio = producto.precio
        Total = precio * form.cantidad.data
        factura = FacturaDet(producto_id=form.producto_id.data,cantidad = form.cantidad.data, total= Total, facturaCab_id=max(facturaCab.id))
        db.session.add(factura)
        db.session.commit()
        return redirect(url_for('addPedido'))
    elif form.validate_on_submit1():
        sum=0
        factura = max(facturaCab.id)
        for x in facturaDet:
            y = db.session.query(FacturaDet).filter(FacturaDet.facturaCab_id==factura)
        return y
        for obj in y:
            total = sum+=obj
        return total

        db.session.query(FacturaCab).filter(FacturaCab.id==factura).update({FacturaCab.total:total})
        db.session.commit()

    return render_template('AddPedido.html', title='Crear Factura', form=form)

