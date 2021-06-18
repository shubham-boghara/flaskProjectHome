from flask import Blueprint, render_template
from bluprients.fetch import fetch

home = Blueprint("home", __name__)


@home.route("/")
def homes():
    fetch_data = fetch()
    query = """query{
  getAllData{
    _id,
    date,
    design,
    color,
    total_p,
    month,
    return_p,
    price,
    memberId {
      _id,
      username
    },
    amount,
    member_amount
    
  }
}"""
    data = fetch_data.post(query)

    return render_template("Home/home.html", datas=data['data']['getAllData'])


@home.route("/login")
def login_s():
    return "Login"


@home.route("/signup")
def signup_s():
    return "signup"
