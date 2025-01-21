# required packages
# pip install flask flask-cors pymongo dataset

from flask import Flask, make_response, jsonify, request
from flask_cors import CORS
import dataset

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
db = dataset.connect('sqlite:///transport.db')

# Create tables
users_table = db['users']
routes_table = db['routes']
timetables_table = db['timetables']
route_data_table = db['route_data']

# Mock data structure for the application
mock_data = {
    "student": {
        "timetable": {
            "student_info": {
                "name": "John Smith",
                "id": "STU001",
                "classes": [
                    {"name": "Mathematics", "day": "Monday", "timing": "09:00"},
                    {"name": "Physics", "day": "Monday", "timing": "11:00"},
                    {"name": "Chemistry", "day": "Wednesday", "timing": "14:00"},
                    {"name": "Biology", "day": "Thursday", "timing": "10:00"},
                    {"name": "English", "day": "Friday", "timing": "13:00"}
                ]
            },
            "time_slots": ["09:00", "10:00", "11:00", "13:00", "14:00"],
            "days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        }
    },
    
    "driver": {
        "route_data": {
            "stops": [
                "IUGC Main Campus",
                "Maskan Chowrangi",
                "Safari Park",
                "Gulshan Chowrangi",
                "Hassan Square",
                "NIPA",
                "Liaquatabad No. 10",
                "Teen Hatti",
                "PIB Colony",
                "Jail Chowrangi"
            ],
            "timings": {
                "morning": [
                    "7:00 AM",  # IUGC
                    "7:15 AM",  # Maskan
                    "7:25 AM",  # Safari Park
                    "7:35 AM",  # Gulshan Chowrangi
                    "7:45 AM",  # Hassan Square
                    "7:55 AM",  # NIPA
                    "8:10 AM",  # Liaquatabad
                    "8:20 AM",  # Teen Hatti
                    "8:30 AM",  # PIB
                    "8:45 AM"   # Jail Chowrangi
                ],
                "evening": [
                    "4:00 PM",  # IUGC
                    "4:15 PM",  # Maskan
                    "4:25 PM",  # Safari Park
                    "4:35 PM",  # Gulshan Chowrangi
                    "4:45 PM",  # Hassan Square
                    "4:55 PM",  # NIPA
                    "5:10 PM",  # Liaquatabad
                    "5:20 PM",  # Teen Hatti
                    "5:30 PM",  # PIB
                    "5:45 PM"   # Jail Chowrangi
                ]
            }
        }
    },
    
    "admin": {
        "users": [
            {
                "_id": "ADM001",
                "username": "Admin User",
                "email": "admin@iugc.edu",
                "phone": "111-111-1111",
                "role": "admin",
                "password": "admin123"
            },
            {
                "_id": "STU001",
                "username": "John Smith",
                "email": "john@example.com",
                "phone": "123-456-7890",
                "role": "student",
                "classes": ["Mathematics", "Physics", "Chemistry", "Biology", "English"],
                "fee_status": "paid",
                "password": "student123",
                "assigned_route": "Route A"
            },
            {
                "_id": "STU002",
                "username": "Sarah Wilson",
                "email": "sarah@example.com",
                "phone": "098-765-4321",
                "role": "student",
                "classes": ["Computer Science", "Data Structures", "Database", "Web Development", "Programming"],
                "fee_status": "unpaid",
                "password": "student123",
                "assigned_route": "Route B"
            },
            {
                "_id": "STU003",
                "username": "Michael Brown",
                "email": "michael@example.com",
                "phone": "111-222-3333",
                "role": "student",
                "classes": ["Economics", "Business", "Marketing", "Finance", "Accounting"],
                "fee_status": "paid",
                "password": "student123",
                "assigned_route": "Route C"
            },
            {
                "_id": "DRV001",
                "username": "David Driver",
                "email": "david@example.com",
                "phone": "444-555-6666",
                "role": "driver",
                "available_seats": 30,
                "total_seats": 50,
                "route": "Route A",
                "password": "driver123",
                "license_no": "DL-2024-001",
                "experience": "5 years"
            },
            {
                "_id": "DRV002",
                "username": "James Wilson",
                "email": "james@example.com",
                "phone": "777-888-9999",
                "role": "driver",
                "available_seats": 25,
                "total_seats": 40,
                "route": "Route B",
                "password": "driver123",
                "license_no": "DL-2024-002",
                "experience": "3 years"
            },
            {
                "_id": "DRV003",
                "username": "Robert Johnson",
                "email": "robert@example.com",
                "phone": "222-333-4444",
                "role": "driver",
                "available_seats": 35,
                "total_seats": 45,
                "route": "Route C",
                "password": "driver123",
                "license_no": "DL-2024-003",
                "experience": "7 years"
            }
        ],
        "routes": [
            {
                "id": "R001",
                "name": "Route A",
                "stops": [
                    "IUGC Main Campus",
                    "Maskan Chowrangi",
                    "Safari Park",
                    "Gulshan Chowrangi"
                ],
                "driver": "David Driver",
                "timings": {
                    "morning": "7:00 AM - 8:30 AM",
                    "evening": "4:00 PM - 5:30 PM"
                },
                "total_students": 25,
                "distance": "15 km"
            },
            {
                "id": "R002",
                "name": "Route B",
                "stops": [
                    "IUGC Main Campus",
                    "NIPA",
                    "Liaquatabad",
                    "Teen Hatti"
                ],
                "driver": "James Wilson",
                "timings": {
                    "morning": "7:30 AM - 9:00 AM",
                    "evening": "4:30 PM - 6:00 PM"
                },
                "total_students": 20,
                "distance": "12 km"
            },
            {
                "id": "R003",
                "name": "Route C",
                "stops": [
                    "IUGC Main Campus",
                    "Nazimabad",
                    "North Nazimabad",
                    "Buffer Zone"
                ],
                "driver": "Robert Johnson",
                "timings": {
                    "morning": "7:15 AM - 8:45 AM",
                    "evening": "4:15 PM - 5:45 PM"
                },
                "total_students": 22,
                "distance": "18 km"
            }
        ]
    }
}

# Helper functions
def fetch_user(user_id):
    return users_table.find_one(user_id=user_id)

def fetch_all_users():
    return list(users_table.all())

def fetch_route(route_id):
    return routes_table.find_one(route_id=route_id)

def fetch_all_routes():
    return list(routes_table.all())

@app.route('/api/mockupload', methods=['GET'])
def upload_mock_data():
    """Upload all mock data to the database"""
    try:
        # Clear existing data
        users_table.delete()
        routes_table.delete()
        timetables_table.delete()
        route_data_table.delete()

        # Insert users with passwords
        for user in mock_data["admin"]["users"]:
            users_table.insert({
                "user_id": user["_id"],
                "username": user["username"],
                "email": user["email"],
                "phone": user["phone"],
                "role": user["role"],
                "password": user.get("password", "password123"),  # Default password
                "classes": str(user.get("classes", [])),
                "fee_status": user.get("fee_status", ""),
                "available_seats": user.get("available_seats", 0),
                "total_seats": user.get("total_seats", 0),
                "route": user.get("route", ""),
                "assigned_route": user.get("assigned_route", "")
            })

        # Insert routes
        for route in mock_data["admin"]["routes"]:
            routes_table.insert({
                "route_id": route["id"],
                "name": route["name"],
                "stops": str(route["stops"]),  # Convert list to string
                "driver": route["driver"],
                "morning_time": route["timings"]["morning"],
                "evening_time": route["timings"]["evening"],
                "total_students": route["total_students"],
                "distance": route["distance"]
            })

        # Insert student timetables
        for user in mock_data["admin"]["users"]:
            if user["role"] == "student":
                timetables_table.insert({
                    "student_id": user["_id"],
                    "name": user["username"],
                    "classes": str([
                        {"name": class_name, "day": "Monday", "timing": "09:00"}
                        for class_name in user["classes"]
                    ]),
                    "time_slots": str(["09:00", "10:00", "11:00", "13:00", "14:00"]),
                    "days": str(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
                })

        # Insert driver route data
        route_data_table.insert({
            "stops": str(mock_data["driver"]["route_data"]["stops"]),
            "morning_timings": str(mock_data["driver"]["route_data"]["timings"]["morning"]),
            "evening_timings": str(mock_data["driver"]["route_data"]["timings"]["evening"])
        })

        return make_response(jsonify({"message": "Mock data uploaded successfully"}), 200)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)

@app.route('/api/login', methods=['POST'])
def login():
    """Handle login requests"""
    content = request.json
    if not content or 'email' not in content or 'password' not in content:
        return make_response(jsonify({
            "error": "Email and password are required"
        }), 400)

    user = users_table.find_one(email=content['email'])
    
    if user:
        # For testing purposes, we'll use a simple password check
        # In production, you should use check_password_hash()
        if content['password'] == user.get('password', ''):
            return make_response(jsonify({
                "user_id": user["user_id"],
                "role": user["role"],
                "username": user["username"]
            }), 200)
        else:
            return make_response(jsonify({
                "error": "Invalid password"
            }), 401)
    
    return make_response(jsonify({
        "error": "User not found"
    }), 404)

@app.route('/api/users', methods=['GET'])
def get_users():
    """Get all users or filtered by role"""
    role = request.args.get('role')
    if role:
        users = list(users_table.find(role=role))
    else:
        users = fetch_all_users()
    return make_response(jsonify(users), 200)

@app.route('/api/users/<user_id>', methods=['GET', 'PUT', 'DELETE'])
def manage_user(user_id):
    """Manage individual user operations"""
    if request.method == "GET":
        user = fetch_user(user_id)
        if user:
            return make_response(jsonify(user), 200)
        return make_response(jsonify({"error": "User not found"}), 404)
    
    elif request.method == "PUT":
        content = request.json
        users_table.update(content, ['user_id'])
        return make_response(jsonify(fetch_user(user_id)), 200)
    
    elif request.method == "DELETE":
        users_table.delete(user_id=user_id)
        return make_response(jsonify({}), 204)

@app.route('/api/routes', methods=['GET', 'POST'])
def manage_routes():
    """Get all routes or create new route"""
    if request.method == "GET":
        routes = fetch_all_routes()
        return make_response(jsonify(routes), 200)
    
    elif request.method == "POST":
        content = request.json
        routes_table.insert(content)
        return make_response(jsonify(content), 201)

@app.route('/api/routes/<route_id>', methods=['GET', 'PUT', 'DELETE'])
def manage_route(route_id):
    """Manage individual route operations"""
    if request.method == "GET":
        route = fetch_route(route_id)
        if route:
            return make_response(jsonify(route), 200)
        return make_response(jsonify({"error": "Route not found"}), 404)
    
    elif request.method == "PUT":
        content = request.json
        routes_table.update(content, ['route_id'])
        return make_response(jsonify(fetch_route(route_id)), 200)
    
    elif request.method == "DELETE":
        routes_table.delete(route_id=route_id)
        return make_response(jsonify({}), 204)

@app.route('/api/student/<student_id>/timetable', methods=['GET'])
def get_student_timetable(student_id):
    """Get student timetable"""
    try:
        student = users_table.find_one(user_id=student_id)
        timetable = timetables_table.find_one(student_id=student_id)
        
        if student and timetable:
            # Create a list of classes with proper timing distribution
            classes = eval(timetable["classes"])  # Convert string back to list
            time_slots = eval(timetable["time_slots"])
            days = eval(timetable["days"])
            
            # Distribute classes across different times and days
            distributed_classes = []
            for i, class_info in enumerate(classes):
                distributed_classes.append({
                    "name": class_info["name"],
                    "day": days[i % len(days)],
                    "timing": time_slots[i % len(time_slots)]
                })
            
            return make_response(jsonify({
                "student_id": student_id,
                "name": student["username"],
                "classes": str(distributed_classes),
                "time_slots": timetable["time_slots"],
                "days": timetable["days"],
                "assigned_route": student.get("assigned_route", ""),
                "fee_status": student.get("fee_status", "")
            }), 200)
        return make_response(jsonify({"error": "Timetable not found"}), 404)
    except Exception as e:
        return make_response(jsonify({
            "error": "Failed to fetch timetable",
            "details": str(e)
        }), 500)

@app.route('/api/driver/<driver_id>/route', methods=['GET'])
def get_driver_route(driver_id):
    """Get driver route data"""
    driver = users_table.find_one(user_id=driver_id, role="driver")
    if driver:
        route = routes_table.find_one(name=driver["route"])
        route_data = route_data_table.find_one()  # Assuming one route data for now
        return make_response(jsonify({
            "route": route,
            "route_data": route_data
        }), 200)
    return make_response(jsonify({"error": "Driver not found"}), 404)

@app.route('/api/db/all', methods=['GET'])
def get_all_db_data():
    """Get all data from all tables in the database"""
    try:
        all_data = {
            "users": list(users_table.all()),
            "routes": list(routes_table.all()),
            "timetables": list(timetables_table.all()),
            "route_data": list(route_data_table.all())
        }
        
        # Add table counts
        table_counts = {
            "total_users": len(all_data["users"]),
            "total_routes": len(all_data["routes"]),
            "total_timetables": len(all_data["timetables"]),
            "total_route_data": len(all_data["route_data"]),
        }
        
        # Add role-based user counts
        user_counts = {
            "students": len([u for u in all_data["users"] if u["role"] == "student"]),
            "drivers": len([u for u in all_data["users"] if u["role"] == "driver"])
        }
        
        response_data = {
            "table_counts": table_counts,
            "user_counts": user_counts,
            "data": all_data
        }
        
        return make_response(jsonify(response_data), 200)
    except Exception as e:
        return make_response(jsonify({
            "error": "Failed to fetch database data",
            "details": str(e)
        }), 500)

if __name__ == '__main__':
    app.run(debug=True)


# http://localhost:5000/api/mockupload
# http://localhost:5000/api/db/all