from flask import Flask, render_template, url_for,request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Auth(db.Model):
    login = db.Column(db.String(), primary_key=True, nullable=False)
    password = db.Column(db.String(), primary_key=True, nullable=False)

    def __repr__(self):
        return '<Auth %r>' % self.login

    def __repr__(self):
        return '<Auth %r>' % self.password


class CardAuth(db.Model):
    id = db.Column(db.String(), primary_key=True, nullable=False)

    def __repr__(self):
        return '<CardAuth %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        login = request.form['login']
        password = request.form['password']
        auth = Auth(login=login, password=password)

        try:
            db.session.add(auth)
            db.session.commit()
            return redirect('/')
        except:
            return "Logging error."
    else:
        return render_template("index.html")


@app.route('/guard')
def guard():
    return render_template("guard.html")


@app.route('/admin')
def admin():
    all_auth = Auth.query.order_by(Auth.login).all()
    return render_template("admin.html", allauth=all_auth)


#@app.route('/admin/<string:login><string:password>/delete')
#def authdelete(login, password):

if __name__ == "__main__":
    app.run(debug=True)