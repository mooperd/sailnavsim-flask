"""Logged-in page routes."""
from flask import Blueprint, flash, redirect, render_template, url_for, request
from flask_login import current_user, login_required, logout_user
from .forms import NewRaceForm, TestForm
from .models import User, BoatRace, db

# Blueprint Configuration
routes_bp = Blueprint(
    'routes_bp', __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/api'
)


def create_race(new_race_dict, current_user):
    existing_race = BoatRace.query.filter_by(name=new_race_dict["name"]).first()
    if existing_race is None:
        print("Form Validated")
        race = BoatRace()
        race.name = new_race_dict["name"]
        race.latitude = new_race_dict["latitude"]
        race.longitude = new_race_dict["longitude"]
        race.sw_corner = new_race_dict["sw_corner"]
        race.ne_corner = new_race_dict["ne_corner"]
        race.boat_type = new_race_dict["boat_type"]
        race.start_time = new_race_dict["start_time"]
        race.private = int(new_race_dict["private"])
        race.user = current_user
        db.session.add(race)
        db.session.commit()
        return
    else:
        return f"Race name {new_race_dict['name']} already taken"


@routes_bp.route('/race', methods=['GET', 'POST'])
@login_required
def race():
    """
    Race Endpoint
    """
    # TODO: Add json
    if request.method == 'POST':
        # If the request is form data.
        if request.headers['Content-Type'] == 'application/x-www-form-urlencoded':
            print("Content-Type OK")
            form = NewRaceForm()
            if form.validate_on_submit():
                race_output = create_race(form.data, current_user)
                if race_output is None:
                    # TODO: Return race page not the dashboard
                    return redirect(url_for('pages_bp.races'))
                else:
                    flash(race_output)
                    # TODO: This return feels super boilerplate!
                    return render_template(
                        'races.jinja2',
                        title='New Race Form',
                        template='signup-page',
                        current_user=current_user,
                        body="You are now logged in!",
                        races=db.session.query(BoatRace).all(),
                        form=form
                    )
                    
            

@routes_bp.route('/test', methods=['GET', 'POST'])
@login_required
def test():
    """
    TEST
    """
    form = TestForm()
    if form.validate_on_submit():
        return redirect(url_for('pages_bp.dashboard'))
    return render_template(
        'test.jinja2',
        title='Create an Account.',
        form=form,
        template='test-page',
        body="Sign up for a user account."
    )


@routes_bp.route("/logout")
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for('auth_bp.login'))
