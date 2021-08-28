from flask import Blueprint, render_template

client = Blueprint('client', __name__)


@client.route('/', methods=["POST", "GET"])
def main():
    return render_template("Client/client.html")
