from flask import Flask , render_template , url_for

app = Flask(__name__)


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



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=2000)