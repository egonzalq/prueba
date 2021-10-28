from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,SelectField
from wtforms.validators import DataRequired

class formVuelos(FlaskForm):

    vuelo = StringField("Vuelo", validators=[DataRequired(message="no dejar vacio")], render_kw={"placeholder":"Vuelo","class":"from_control"})
   
    
    consultar=SubmitField("Consultar",render_kw={"onmousecover":"Consularrvuelo()","class":"from_boton"})
    