import functools

from elections.us_states import postal_abbreviations
from elections.controller.ocd_id_controller import OCDIDController
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('address_form', __name__, url_prefix='/')


@bp.route('/', methods=('GET', 'POST'))
@bp.route('/search', methods=('POST',))
def search():
    """Take in an address."""
    if request.method == 'POST':
        form_data = request.form
        ocd_o = OCDIDController(address=form_data)
        ocd_ids = ocd_o.prepare()
        elections = ocd_o.get_elections(data=ocd_ids)
        return render_template('election_results.html', elections=elections)
    
    return render_template('address_form.html', states=postal_abbreviations)
