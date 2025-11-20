from flask import render_template, redirect, flash
from flask_login import login_required, current_user
from . import bp
from app.models import User, Classes, Course



@bp.route("/")
@bp.route("/home")
@login_required
def home():
    # Get user's classes from database
    user_classes = Classes.query.filter_by(user=current_user.id).first()
    
    if user_classes:
        return render_template('home.html', 
                             classes=user_classes.classes, 
                             assignments=[])
    else:
        return render_template('home.html', classes=[], assignments=[])