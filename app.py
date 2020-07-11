from flask import Flask , render_template , url_for, flash, redirect
from forms import RegistrationForm,LoginForm
app = Flask(__name__)


app.config['SECRET_KEY'] = 'a3ab9ba58d166b8064117b6f628da7a7'

postes = [
    {
        'auther':' corey schaef',
        'title':'blog poste 1 ',
        'content':'first poste content',
        'date_posted':'April 20 , 2020'
    },
    {
        'auther':' Anather auther',
        'title':'blog poste 2 ',
        'content':'anather  poste content',
        'date_posted':'April 25 , 2020'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', postes=postes)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password' :
            flash(f'You have been loged In', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Login Unseccesseful Check usename and password ', 'danger')
    return render_template('login.html',title='Login', form = form)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=2000)