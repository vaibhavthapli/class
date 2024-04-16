from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/test")
def test():
    get_name = request.args.get("name")
    moblie_number = request.args.get("mobile")
    mail_id = request.args.get("mail")
    return "Hello World {} {} {}".format(get_name, moblie_number, mail_id)

if __name__ == "__main__":
    app.run()