from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from __init__ import create_app, db
from models import Card
import paramiko

main = Blueprint('main', __name__)

host = "192.168.1.133"
port = 22
user = "pi"
secret = "raspberry"
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


def put_file():
    client.connect(hostname=host, username=user, password=secret, port=port)
    sftp = client.open_sftp()
    sftp.put("C:/Users/dusti/Desktop/FlaskPrikol/FlaskDBandSite/db.sqlite", "./Desktop/db.sqlite")
    sftp.close()


@main.route('/admin/door', methods=['POST'])
def doorswitcheradmin():
    if request.form['btn']:
        print('1')
    return redirect(url_for('main.admin'))


@main.route('/admin')
@login_required
def admin():
    #
    allcards = Card.query.order_by(Card.id).all()
    tmp = 0
    return render_template('admin.html', allcards=allcards, tmp=tmp)


@main.route('/guard/door', methods=['POST'])
def doorswitcherguard():
    if request.form['btn']:
        print('1')
    return redirect(url_for('main.guard'))


@main.route('/guard')
@login_required
def guard():
    allcards = Card.query.order_by(Card.id).all()
    tmp = 0
    return render_template('guard.html', allcards=allcards, tmp=tmp)


@main.route("/admin/<int:id>/del")
@login_required
def delete(id):
    card = Card.query.get(id)
    try:
        db.session.delete(card)
        db.session.commit()
        return redirect(url_for('main.admin')), put_file()
    except Exception as e:
        pass


@main.route("/admin/<int:id>/edit", methods=['POST', 'GET'])
@login_required
def editfunc(id):
    if request.method == "POST":
        new_name = request.form['nameinput']
        new_card = request.form['cardinput']
        old_card = Card.query.get(id)
        editCard = Card(id=id, name=new_name, card=new_card)
        try:
            print(new_name, new_card)
            db.session.delete(old_card)
            db.session.add(editCard)
            db.session.commit()
            return redirect(url_for('main.admin')), put_file()
        except Exception as e:
            print(e)
    else:
        return redirect(url_for('main.admin'))


@main.route("/admin/card_create", methods=['POST', 'GET'])
@login_required
def cardcreate():
    if request.method == "POST":
        card = request.form['card_add']
        name = request.form['name_add']
        try:
            new_card = Card(card=card, name=name)
            db.session.add(new_card)
            db.session.commit()
            return redirect(url_for('main.admin')), put_file()
        except Exception as e:
            print(e)


app = create_app()
if __name__ == '__main__':
    db.create_all(app=create_app())
    app.run(debug=True)
