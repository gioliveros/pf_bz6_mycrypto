from flask_wtf import Flaskform
from wtforms import DateField, StringField, FloatField
from wtforms.validators import DataRequired, Lenght
from datetime import date

class MovementForm(Flaskform)
    fecha = DateField('Fecha', validators=[DataRequired(), validate_startDate])
    hora = TimeField('Hora', format='%H:%M', validators=[DataRequired()])
    moneda_from = StringField ("Moneda_from", validators=[DataRequired, Lenght(max=4, message="la cryptomoneda no debe tener más de 4 caracteres")])
    cantidad_from = FloatField ('Cantidad_from', validators=[DataRequired()])
    moneda_to = StringField ("Moneda_from", validators=[DataRequired, Lenght(max=4, message="la cryptomoneda no debe tener más de 4 caracteres")])
    cantidad_to = FloatField ('Cantidad_from', validators=[DataRequired()])

    submit = SubmitField('Aceptar')
    

