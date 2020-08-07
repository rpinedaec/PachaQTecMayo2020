from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user
from flask_login import logout_user
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse
from app.models import User,Producto, Categoria, Cliente, Compra, DetalleCompra
from app.forms import RegistrationForm, AddProductoForm, AddCategoriaForm, AddCompraForm, AddDetalleCompraForm, AddClienteForm
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
    categorias = Categoria.query.all()
    return render_template('productos.html', title='Productos', productos=productos, categorias=categorias)


@app.route('/categorias', methods=['GET', 'POST'])
def getCategoria():
    categorias = Categoria.query.all()
    return render_template('categorias.html', title='Categoria', categorias=categorias)



@app.route('/categoria/add', methods=['GET', 'POST'])
def addCategoria():
    form = AddCategoriaForm()
    categorias = Categoria.query.all()
    if form.validate_on_submit():
        categoria = Categoria(nombre=form.nombre.data)
        db.session.add(categoria)
        db.session.commit()
        flash('Categoria creada!')
        return redirect(url_for('getCategoria'))
    return render_template('AddCategoria.html', title='Crear Categoria', form=form)



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

 



@app.route('/cliente', methods=['GET', 'POST'])
def getCliente():
    Clientes = Cliente.query.all()
    return render_template('clientes.html', title='Clientes', Clientes=Clientes)



@app.route('/cliente/add', methods=['GET', 'POST'])
def addCliente():
    form = AddClienteForm()
    clientes = Cliente.query.all() 
    if form.validate_on_submit():
        cliente = Cliente(nombre=form.nombre.data,ruc = form.ruc.data, 
        direccion=form.direccion.data)
        db.session.add(cliente)
        db.session.commit()
        flash('Cliente creado!')
        return redirect(url_for('getCliente'))
    return render_template('AddCliente.html', title='Crear Cliente', form=form,clientes=clientes)



@app.route('/compra', methods=['GET', 'POST'])
def getCompra():
    DetalleCompras = DetalleCompra.query.all()
    Compras = Compra.query.all()
    return render_template('compra.html', title='Compra', Compras=Compras,DetalleCompras=DetalleCompras)



@app.route('/compra/add', methods=['GET', 'POST'])
def addCompra():
    formCompra = AddCompraForm(request.form)
    formDetalleCompra =  AddDetalleCompraForm()
    clientes = Cliente.query.all() 
    Productos = Producto.query.all() 
    ComprasTodas=1
    Texto = ""
    NuevaDetalleComprasTodas = 0

    try:
        ComprasTodasT = int(formCompra.correlativo.data)
        #NuevaDetalleCompra = DetalleCompra.query.filter_by(compra_id=ComprasTodasT).first()
        NuevaCompra = Compra.query.filter_by(correlativo=ComprasTodasT).first()
        ComprasTodas = ComprasTodasT
        #try:
        #    NuevaDetalleComprasTodas = DetalleCompra.query.filter_by(compra_id=CompraFilter.id).count()
        #except:
        #    pass
    except:
        #NuevaDetalleCompra = DetalleCompra.query.filter_by(compra_id=0).first()
        #NuevaDetalleComprasTodas = 0
        ComprasTodas = Compra.query.count()
        if ComprasTodas==0:
            ComprasTodas=1
        else:
            ComprasTodas+=1
        #flash('NO!') 
     

    if formCompra.validate_on_submit():
        CorrelativoGuardado = int(formCompra.correlativo.data) 
        SubtotalDetalle = formDetalleCompra.precio.data*formDetalleCompra.cantidad.data
        subT=SubtotalDetalle
        igvC=float(subT)*float(0.18)
        totalC=float(subT)+igvC
        
        try:
            CompraFilter22 = Compra.query.filter_by(correlativo=CorrelativoGuardado).first()
            if CompraFilter22.id>0:
                pass
            else:
                Comprast=Compra(correlativo=formCompra.correlativo.data
                                ,subtotal=SubtotalDetalle
                                ,igv=igvC
                                ,total=totalC
                                ,cliente_id=formCompra.cliente_id.data
                                )
                db.session.add(Comprast) 
                db.session.commit() 
        except:
            Comprast=Compra(correlativo=formCompra.correlativo.data
                            ,subtotal=SubtotalDetalle
                            ,igv=igvC
                            ,total=totalC
                            ,cliente_id=formCompra.cliente_id.data
                            )
            db.session.add(Comprast) 
            db.session.commit() 

        #flash(CorrelativoGuardado) 
        CompraFilter = Compra.query.filter_by(correlativo=CorrelativoGuardado).first() 
        #flash(CompraFilter.id)


        NuevaDetalleComprasTodas=0
        NuevaDetalleCompra = DetalleCompra.query.filter_by(compra_id=CompraFilter.id).first() 

        DetalleComprast = DetalleCompra(cantidad=formDetalleCompra.cantidad.data
                        ,precio = formDetalleCompra.precio.data
                        ,subtotal = SubtotalDetalle
                        ,producto_id =formDetalleCompra.producto_id.data
                        ,compra_id = CompraFilter.id
                        )
        db.session.add(DetalleComprast)
        db.session.commit() 
        Texto = "Guardado Correctamente, puede agregar otro producto con precio y cantidad diferente."
         
        #try: 
            #NuevaDetalleCompra = DetalleCompra.query.filter_by(compra_id=CompraFilter.id).first()
            #cantidad = DetalleCompra.query.filter_by(compra_id=CompraFilter.id).count()
            #NuevaDetalleComprasTodas = cantidad
            #flash('aqio')
            #NuevaDetalleCompra.followers.all()
            #flash(NuevaDetalleCompra.followers.all())
            #for detalle in NuevaDetalleCompra:
                #flash('xxxxx')
                #cantidad+=1
            #NuevaDetalleComprasTodas = cantidad
            #flash(cantidad)
            #NuevaDetalleComprasTodas = 10
        #except:
            #pass
            #flash('eerorr')
            #CompraTemp = Compra.query.filter_by(correlativo=formCompra.correlativo.data).first()
            #NuevaDetalleCompra = DetalleCompra.query.filter_by(compra_id=CompraTemp.id).first()
        
    NuevaDetalleCompra = ""
    return render_template('AddCompra.html', title='Crear Compra', form=formCompra,formDetalleCompra=formDetalleCompra
    ,clientes=clientes,Productos=Productos,ComprasTodas=ComprasTodas,NuevaDetalleCompra=NuevaDetalleCompra
    ,NuevaDetalleComprasTodas=NuevaDetalleComprasTodas,Texto=Texto)

