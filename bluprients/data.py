from flask import Blueprint, render_template
from bluprients.member import member
from bluprients.fetch import fetch

data = Blueprint("data", __name__, url_prefix="/<string:id>/data")
member.register_blueprint(data)


@data.route("/")
def member_Data(id):
    M_Data = fetch()
    query = """query getListedData($id:String!)
    {getListedData(m_Id:$id){_id,total_p,design,return_p,price,color,date,,member_amount,amount,memberId{_id,username}}}"""
    m_data = M_Data.post(query, id=id)

    return render_template("Data/data.html", datas=m_data['data']['getListedData'])


@data.route("/delete")
def member_data_delete(id):
    D_data = fetch()
    query = """mutation delete_data($id:String!){deleteDataField(d_id:$id){delete}}"""
    message = D_data.post(query, id=id)
    return message


@data.route("/edit")
def member_data_edit(id):
    E_data = fetch()
    query = """mutation editData($total_p:Int!,$design:String!,$return_p:Int!,$price:Int!,$color:String!,
    $id:String!){ editDataField(input:{ id:$id, total_p:$total_p, design:$design, return_p:$return_p, price:$price, 
    color:$color}){ _id, date, month, memberId, total_p, design, price, color, amount, member_amount } } """
    e_data = E_data.post(query, id=id, total_p=12, design="", return_p=0, price=5, color="")

    return e_data
