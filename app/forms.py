from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import TextAreaField
from wtforms.validators import DataRequired

class UploadForm(FlaskForm):
    photo = FileField('Upload Photo', validators = [FileRequired(), FileAllowed(['jpg', 'png'])])
    description = TextAreaField('Description', validators=[DataRequired()])
    