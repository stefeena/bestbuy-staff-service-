from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for staff data
staff_data = {}
staff_id_counter = 1

@app.route('/staff', methods=['POST'])
def create_staff():
    global staff_id_counter
    data = request.json
    staff_id = staff_id_counter
    staff_data[staff_id] = {
        "id": staff_id,
        "name": data.get("name"),
        "position": data.get("position"),
        "department": data.get("department"),
        "email": data.get("email"),
        "phone": data.get("phone"),
    }
    staff_id_counter += 1
    return jsonify({"message": "Staff created successfully", "staff": staff_data[staff_id]}), 201

@app.route('/staff/<int:id>', methods=['GET'])
def get_staff(id):
    staff = staff_data.get(id)
    if not staff:
        return jsonify({"error": "Staff not found"}), 404
    return jsonify(staff), 200

@app.route('/staff/<int:id>', methods=['PUT'])
def update_staff(id):
    staff = staff_data.get(id)
    if not staff:
        return jsonify({"error": "Staff not found"}), 404
    data = request.json
    staff.update({
        "name": data.get("name", staff["name"]),
        "position": data.get("position", staff["position"]),
        "department": data.get("department", staff["department"]),
        "email": data.get("email", staff["email"]),
        "phone": data.get("phone", staff["phone"]),
    })
    return jsonify({"message": "Staff updated successfully", "staff": staff}), 200

@app.route('/staff/<int:id>', methods=['DELETE'])
def delete_staff(id):
    if id not in staff_data:
        return jsonify({"error": "Staff not found"}), 404
    del staff_data[id]
    return jsonify({"message": "Staff deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
