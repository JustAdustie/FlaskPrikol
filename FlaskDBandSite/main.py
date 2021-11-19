from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from __init__ import create_app, db
from models import Card


main = Blueprint('main', __name__)


@main.route('/admin') 
@login_required
def admin():
    allcards = Card.query.order_by(Card.id).all()
    tmp = 0
    return render_template('admin.html', allcards=allcards, tmp=tmp)

@main.route('/guard')
@login_required
def guard():
    return render_template('guard.html')

@main.route("/admin/<int:id>/del")
def delete(id):
    card = Card.query.get(id)

    try:
        db.session.delete(card)
        db.session.commit()
        return redirect(url_for('main.admin'))
    except Exception as e:
        pass


app = create_app()
if __name__ == '__main__':
    db.create_all(app=create_app())
    app.run(debug=True)