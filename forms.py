#Here is where we create forms for the html template using WTF
from flask_wtf import FlaskForm #FlaskForm is used to create fm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired,Email

class SimpleWTFForm(FlaskForm):
  #form input for username
  username = StringField("Name",validators=[DataRequired()])
  #form input for email
  email = StringField("Email",validators=[DataRequired(),Email()])
  #form input for submit button
  submit = SubmitField("Submit")