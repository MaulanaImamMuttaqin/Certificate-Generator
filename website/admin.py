from flask import Blueprint, render_template

admin = Blueprint('admin', __name__)


@admin.route('/Home', methods=['GET', 'POST'])
def home():
    return render_template("Admin/index.html")
