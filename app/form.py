from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, DataRequired, Length
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    linkedin_url = StringField('Your linkedin profile URL', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    invitation_key = StringField('If you have an invitation key, put it here:')
    keywords_perso = TextAreaField('Type 2 keywords (titles / skills / experience/ ect..) you are interested in, separated by "," :',
                                   validators=[Length(min=0, max=120)],render_kw={"placeholder": "Exemple: Computers, engineer"})
    where_searh = SelectField(u'In which city (region) you want to find your new job ?',
                              choices=[('Sydney', 'Sydney (NSW)'), ('Melbourne', 'Melbourne (VIC)'), ('Perth', 'Perth (WA)'),
                                       ('Adelaide', 'Adelaide (SA)'), ("Brisbane", "Brisbane (QLD)")])
    submit = SubmitField('Create your account')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

    # def validate_lkn(self, linkedin_url):
    #     if 'https://www.linkedin.com/' not in linkedin_url:
    #         raise ValidationError('Please use your linkedin url profile ')


class EditProfileForm(FlaskForm):
    reload_emu = BooleanField('Reload my linkedin profile')
    where_searh = SelectField(u'In which city (region) you want to find your new job ?',
                              choices=[('Sydney', 'Sydney (NSW)'), ('Melbourne', 'Melbourne (VIC)'), ('Perth', 'Perth (WA)'),
                                       ('Adelaide', 'Adelaide (SA)'), ("Brisbane", "Brisbane (QLD)")])
    keywords_perso = TextAreaField("Keywords to use (job title, skills, ect..), separated by ',':",
                                   validators=[Length(min=3, max=140)])
    search_level = SelectField(u'How much jobs do you want to analyse ?',
                          choices=[(1, 'Quick - 1 coin / ~ 100 jobs'),
                                   (2, 'Average - 2 coin / ~ 200 jobs'),
                                   (5, 'Long - 5 coin / ~ 600 jobs'), (15, 'Ultra - 15 coin / ~ 2000 jobs'),(100, 'All - 100 coin / ~ all the pages')], coerce=int)
    submit = SubmitField('Create an AI order')


class contactus(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    subject = SelectField(u'What is the category of your message ?',
                          choices=[('general', 'General question - Idea - Suggestion'),('bug', 'Bug - Technical issues'),
                                   ('business', 'Business inquirie - something that looks professional'),
                                   ('greet', "'Thank you ! I find a job' message")])
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Message:', validators=[Length(min=20, max=400)])
    submit = SubmitField('Send a ticket')
class admin_action(FlaskForm):
    submit = SubmitField('test')
