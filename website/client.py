from flask import Blueprint, render_template, request, jsonify, send_file
import json
import os

client = Blueprint('client', __name__)


@client.route('/', methods=["POST", "GET"])
def main():
    return render_template("Client/index.html")


@client.route('/verify', methods=["POST"])
def verify():
    data = json.loads(request.data)
    name = data["name"].lower()
    print(name)
    if verify_list(name):
        res = {"txt": "Anda terverifikasi silahkan download ",
               "filename": name.title().replace(" ", "_") + ".pdf",
               "verify": True
               }
    else:
        res = {"txt": "Nama anda tidak terdeteksi dalam daftar kami, silahkan periksa kembali nama anda",
               "verify": False
               }
    return jsonify({"response": res})


@client.route('/download', methods=['POST'])
def download_file():
    data = json.loads(request.data)
    filename = data["filename"]
    file = os.path.join(os.getcwd() + f"\\website\\files\\temp\{filename}")
    return send_file(file, as_attachment=True)


def verify_list(name):

    file = open("website/files/name.txt", "r")
    name_list = [(line.strip()).lower() for line in file]
    if name in name_list:
        return True
    else:
        return False
