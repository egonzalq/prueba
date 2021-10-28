from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,SelectField
from wtforms.validators import DataRequired

class formVuelos(FlaskForm):

    vuelo = StringField("Vuelo", validators=[DataRequired(message="no dejar vacio")], render_kw={"placeholder":"Vuelo","class":"from_control"})
    aerolinea = StringField("Aerolinea", validators=[DataRequired(message="no dejar vacio")], render_kw={"placeholder":"Aerolinea","class":"from_control"})
    ciudad = StringField("Ciudad", validators=[DataRequired(message="no dejar vacio")], render_kw={"placeholder":"Ciudad","class":"from_control"})
    hora = StringField("Hora", validators=[DataRequired(message="no dejar vacio")], render_kw={"placeholder":"hora","class":"from_control"})
    estado = SelectField("Estado", choices=[("Aterrizo"),("Demorado"),("Adelantado"),("A Tiempo")])

    enviar=SubmitField("Guardar",render_kw={"onmousecover":"Guardarvuelo()","class":"from_boton"})
    consultar=SubmitField("Consultar",render_kw={"onmousecover":"Consultarvuelo()","class":"from_boton"})
    listar=SubmitField("Listar",render_kw={"onmousecover":"Listarvuelo()","class":"from_boton"})
    actualizar=SubmitField("Actualizar",render_kw={"onmousecover":"Actualizarvuelo()","class":"from_boton"})
    borrar=SubmitField("Borrar",render_kw={"onmousecover":"Borrarvuelo()","class":"from_boton"})



