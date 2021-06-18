from flask import Blueprint, render_template, request, url_for, redirect
from bluprients.fetch import fetch

home = Blueprint("home", __name__)


@home.route("/")
def homes():
    # ------------get Data ---------#
    fetch_data = fetch()
    query = """query{ getAllData{_id,date,design,color,total_p,month,return_p,price,memberId {_id,username},amount,
    member_amount}} """
    data = fetch_data.post(query)
    # ------------get Members ---------#
    fetch_members = fetch()
    m_query = """query{getMember{_id,username,date}}"""
    m_data = fetch_members.post(m_query)

    return render_template("Home/home.html", datas=data['data']['getAllData'], members=m_data['data']['getMember'])


@home.route("/<string:id>/update", methods=['GET', 'POST'])
def update_data(id):
    if request.method == "GET":
        fetch_data = fetch()
        query = """query getData($id:String!){getData(at:$id){_id,total_p,return_p,price,color,date,design,
        memberId{_id,username}}} """
        data = fetch_data.post(query, id=id)
        return render_template("Home/editData.html", data=data['data']['getData'])
    if request.method == "POST":
        total_p = int(request.form['total_p'])
        design = request.form['design']
        return_p = int(request.form['return_p'])
        price = int(request.form['price'])
        color = request.form['color']
        u_data = fetch()
        query = """mutation editData($total_p:Int!,$design:String!,$return_p:Int!,$price:Int!,$color:String!,
        $id:String!){ editDataField(input:{ id:$id, total_p:$total_p, design:$design, return_p:$return_p, price:$price, 
        color:$color}){ _id, date, month, memberId, total_p, design, price, color, amount, member_amount } } """
        e_data = u_data.post(query, id=id, total_p=total_p, design=design, return_p=return_p, price=price, color=color)
        return redirect(url_for("home.homes"))


@home.route("/addData", methods=["POST"])
def add_data():
    if request.method == "POST":
        memberId = request.form['memberId']
        total_p = int(request.form['total_p'])
        design = request.form['design']
        return_p = int(request.form['return_p'])
        price = int(request.form['price'])
        color = request.form['color']
        query = """mutation add($memberId:String!,$total_p:Int!,$design:String!,$return_p:Int!,$price:Int!,
        $color:String!){createDataField(input:{ memberId:$memberId,total_p:$total_p,design:$design,return_p:$return_p,
        price:$price, color:$color }) { _id, memberId, total_p, design, return_p, price, color, month, amount } } """
        add = fetch()
        r = add.post(query, memberId=memberId, total_p=total_p, design=design, return_p=return_p,
                     price=price, color=color)
        return redirect(url_for("home.homes"))


@home.route("/login")
def login_s():
    return "Login"


@home.route("/signup")
def signup_s():
    return "signup"
