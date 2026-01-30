from flask import Blueprint , jsonify, request
# create a blueprint/mini app for user related routes
miniflask=Blueprint("user",__name__)


@miniflask.route("/get_user", methods=['GET'])
def get_user():
    return "This is the get_user endpoint."

@miniflask.route("/create_user", methods=['POST'])
def create_user():  
    return jsonify({"message": "User created successfully."}), 201

@miniflask.route("/delete_user/<int:user_id>", methods=['DELETE'])
def delete_user(user_id):
    return jsonify({"message": f"User with id {user_id} deleted."}), 200

@miniflask.route("/update_user/<int:user_id>", methods=['PUT'])
def update_user(user_id):
    user_data = request.get_json()



