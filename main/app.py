from flask import render_template, request, jsonify, redirect, url_for, flash, session, Blueprint
from sqlalchemy import or_
from main.db_models import Bank, Branch
from main import get_session
from main.utils import get_int

mainapp = Blueprint('mainapp', __name__, template_folder='templates')

@mainapp.route("/api/branches/autocomplete", methods=["GET"])
def hello():
    session = get_session()
    query = request.args.get('q')
    limit = get_int(request.args.get('limit'), 100)
    offset = get_int(request.args.get('offset'), 0)
    print(limit, offset, query)
    if not query:
        return jsonify({"success": False, "message": "No query specified"})

    res = session.query(Branch).filter(Branch.branch.ilike(f"%{query}%")).order_by(Branch.ifsc)
    # print(res)
    if limit and limit > 0:
        res = res.limit(limit)
    if offset and offset > 0:
        res = res.offset(offset)
    data = [row.serialize(ignore=['bank']) for row in res.all()]
    session.close()
    return jsonify({ "branches": data })

@mainapp.route("/api/branches", methods=["GET"])
def branches():
    query = request.args.get('q')
    limit = get_int(request.args.get('limit'), 100)
    offset = get_int(request.args.get('offset'), 0)
    session = get_session()

    if not query:
        return jsonify({"success": False, "message": "No query specified"})

    res = session.query(Branch).filter(
        or_(
            Branch.branch.ilike(f"%{query}%"),
            Branch.ifsc.ilike(f"%{query}%"),
            Branch.district.ilike(f"%{query}%"),
            Branch.city.ilike(f"%{query}%"),
            Branch.address.ilike(f"%{query}%"),
            Branch.state.ilike(f"%{query}%"),
            )).order_by(Branch.ifsc)
            
    if limit and limit > 0:
            res = res.limit(limit)
    if offset and offset > 0:
        res = res.offset(offset)
    data = [row.serialize(ignore=['bank']) for row in res.all()]
    session.close()
    return jsonify({ "branches": data })