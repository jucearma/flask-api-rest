
from alerts.services.job_services import Job_Services
from alerts.services.product_services import Product_Services
from flask import request, jsonify, make_response
from alerts.config import app

product_svc = Product_Services()
job_svc = Job_Services()

@app.route('/jobs', methods = ['GET'])
def get_jobs():
    return make_response(jsonify({"jobs": job_svc.find_all_jobs()}))

@app.route('/jobs', methods = ['POST'])
def create_job():
    return make_response(jsonify({"job": job_svc.create_job(request.get_json())}),200)


@app.route('/products', methods = ['GET'])
def index():
    return make_response(jsonify({"product": product_svc.find_all_products()}))


@app.route('/products/<id>', methods = ['GET'])
def get_product_by_id(id):
    return make_response(jsonify({"product": product_svc.get_product_by_id(id)}))


@app.route('/products/<id>', methods = ['PUT'])
def update_product_by_id(id):
    data = request.get_json()
    return make_response(jsonify({"product": product_svc.update_product_by_id(id,data)}))


@app.route('/products/<id>', methods = ['DELETE'])
def delete_product_by_id(id):
    return make_response(jsonify({"product": product_svc.delete_product_by_id(id)}),204)


@app.route('/products', methods = ['POST'])
def create_product():
    return make_response(jsonify({"product": product_svc.create_product(request.get_json())}),200)

if __name__ == "__main__":
    app.run(debug=True)
