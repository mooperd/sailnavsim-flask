"""Logged-in page routes."""
from flask import Blueprint, redirect, render_template, url_for, request
from flask_login import current_user, login_required, logout_user
from .forms import NewRaceForm, TestForm
from .models import User, BoatRace, Boat, db

# Blueprint Configuration
pages_bp = Blueprint(
    'pages_bp', __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/pages'
)


@pages_bp.route('/', methods=['GET'])
@login_required
def dashboard():
    """Logged-in User Dashboard."""
    users = db.session.query(User).all()
    races = db.session.query(BoatRace).all()
    boats = db.session.query(User).all()
    for user in users:
        print(user)
    return render_template(
        'dashboard.jinja2',
        title='Flask-Login Tutorial.',
        template='dashboard-template',
        current_user=current_user,
        body="You are now logged in!",
        users=users,
        races=races,
        boats=boats
    )


@pages_bp.route('/races', methods=['GET'])
@login_required
def races():
    """New Race Form"""
    form = NewRaceForm()
    return render_template(
        'races.jinja2',
        title='New Race Form',
        template='dashboard-template',
        current_user=current_user,
        body="You are now logged in!",
        races=db.session.query(BoatRace).all(),
        form=form
    )


@pages_bp.route('/race/<race_id>', methods=['GET'])
@login_required
def race(race_id):
    """New Race Form"""
    return render_template(
        'race.jinja2',
        title='The race page',
        template='dashboard-template',
        current_user=current_user,
        body="You are now logged in!",
        race=db.session.query(BoatRace).filter(BoatRace.id == race_id).one()
    )


@pages_bp.route('/test_page', methods=['GET'])
@login_required
def test():
    """This is a test page"""
    form = TestForm()
    return render_template(
        'test.jinja2',
        title='Test Page',
        template='dashboard-template',
        current_user=current_user,
        body="You are now testing!",
        form=form
    )
    

@pages_bp.route('/boat', methods=['GET'])
@login_required
def boat():
    """Logged-in User Dashboard."""
    return render_template(
        'boat.jinja2',
        title='Boat Page Title',
        template='dashboard-template',
        current_user=current_user,
        message="You are now logged in!"
    )


@pages_bp.route("/logout")
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for('auth_bp.login'))
