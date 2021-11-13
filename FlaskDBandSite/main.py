from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user
from __init__ import create_app, db
from models import Card


main = Blueprint('main', __name__)


@main.route('/admin') 
@login_required
def admin():
    allcards = Card.query.order_by(Card.id).all()
    return render_template('admin.html', allcards=allcards)


app = create_app()
if __name__ == '__main__':
    db.create_all(app=create_app())
    app.run(debug=True)