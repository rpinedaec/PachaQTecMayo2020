from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import IntegerField, DecimalField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User





class LoginForm(FlaskForm):
    username = StringField('Nombre de Usuario', validators=[DataRequired()])
    password = PasswordField('Contreseña', validators=[DataRequired()])
    remember_me = BooleanField('recuerdame')
    submit = SubmitField('Ingresar')

class RegistrationForm(FlaskForm):
    username = StringField('Nombre', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repita el Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrar')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Usuario regstrado usa otro nombre.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Mail registrado usa otro email.')


class AddProductoForm(FlaskForm):
    nombre = StringField('Nombre de Producto', validators=[DataRequired()])
    stock = IntegerField('Stock Inicial', validators=[DataRequired()])
    precio = DecimalField('Precio Inicial',places=2, validators=[DataRequired()])
    categoria_id =IntegerField('Categoria', validators=[DataRequired()])
    submit = SubmitField('Guardar')


class AddCategoriaForm(FlaskForm):
    nombre = StringField('Nombre de Categoria', validators=[DataRequired()]) 
    submit = SubmitField('Guardar')


class AddClienteForm(FlaskForm):
    nombre = StringField('Nombre del Cliente', validators=[DataRequired()]) 
    ruc = IntegerField('Ruc', validators=[DataRequired()])
    direccion = StringField('Dirección', validators=[DataRequired()]) 
    submit = SubmitField('Guardar')




class AddCompraForm(FlaskForm):
    #correlativo = StringField('Correlativo', validators=[DataRequired()]) 
    correlativo = StringField('Correlativo') 
    #subtotal = DecimalField('SubTotal',places=2, validators=[DataRequired()]) 
    subtotal = DecimalField('SubTotal',places=2) 
    igv = DecimalField('Igv',places=2) 
    total = DecimalField('Total',places=2)
    #igv = DecimalField('Igv',places=2, validators=[DataRequired()]) 
    #total = DecimalField('Total',places=2, validators=[DataRequired()])
    cliente_id =IntegerField('Cliente', validators=[DataRequired()])
    submit = SubmitField('Guardar')


class AddDetalleCompraForm(FlaskForm):
    cantidad = DecimalField('Cantidad',places=2, validators=[DataRequired()]) 
    precio = DecimalField('Precio',places=2, validators=[DataRequired()]) 
    #subtotal = DecimalField('SubTotal',places=2, validators=[DataRequired()])
    subtotal = DecimalField('SubTotal',places=2)
    compra_id =IntegerField('Compra', validators=[DataRequired()])
    producto_id =IntegerField('Producto', validators=[DataRequired()])

