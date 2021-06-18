from flask import Blueprint, render_template, request, redirect, url_for
from bluprients.fetch import fetch

member = Blueprint("member", __name__, url_prefix="/members")


@member.route("/")
def members_s():
    fetch_members = fetch()
    query = """query{getMember{_id,username,date}}"""
    data = fetch_members.post(query)
    return render_template("Member/member.html", memberData=data['data']['getMember'])


@member.route('/<string:m_id>')
def member_id(m_id):
    fetch_member = fetch()
    query = """query getMemberData($id:String!){getMemberData(at:$id){_id,username,phonNumber,address },}"""
    data = fetch_member.post(query, id=m_id)

    return data


@member.route('/Add', methods=['GET', 'POST'])
def member_add():
    if request.method == 'GET':
        return "hello"
    if request.method == 'POST':
        username = request.form['username']
        address = request.form['address']
        phonNumber = request.form['phonNumber']
        add_member = fetch()
        m_query = """mutation createMember($username:String!,$address:String!,$phonNumber:String!){createMember(input:{
      username:$username,address:$address,phonNumber:$phonNumber}){_id,date,month,username,address,phonNumber}} """
        data = add_member.mutation(m_query, username=username, address=address, phonNumber=phonNumber)
        return redirect(url_for('member.members_s'))
