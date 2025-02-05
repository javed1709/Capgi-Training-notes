from flask import Flask,request,jsonify
from flask_cors import CORS
import mysql.connector
app=Flask(__name__)
CORS(app)

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Javedrix@8",
    database="school_db"
)

cursor=conn.cursor()


def create_table():
    cursor.execute('''create table if not exists students(
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            age INT,
            gender VARCHAR(10),
            department VARCHAR(255),
            email VARCHAR(255),
            phone VARCHAR(20)
                   )'''
                )
    conn.commit()

@app.route("/students", methods=["GET"])
def get_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    return jsonify(students)

@app.route("/students", methods=["POST"])
def add_student():
    data = request.json
    name = data["name"]
    age = data["age"]
    gender = data["gender"]
    department = data["department"]
    email = data["email"]
    phone = data["phone"]
    cursor.execute("INSERT INTO students (name, age, gender, department, email, phone) VALUES (%s, %s, %s, %s, %s, %s)", (name, age, gender, department, email, phone))
    conn.commit()
    return jsonify({"message": "Student added successfully"}), 201

@app.route("/students/<int:id>", methods=["GET"])
def get_specific_student(id):
    cursor.execute("SELECT * FROM students WHERE id = %s", (id,))
    student = cursor.fetchone()
    if student:
        return jsonify(student)
    return jsonify({"message": "Student not found"}), 404

@app.route("/students/<int:id>", methods=["PUT"])
def update_student(id):
    data = request.json
    name = data.get("name")
    age = data.get("age")
    gender = data.get("gender")
    department = data.get("department")
    email = data.get("email")
    phone = data.get("phone")
    cursor.execute("UPDATE students SET name = %s, age = %s, gender = %s, department = %s, email = %s, phone = %s WHERE id = %s", (name, age, gender, department, email, phone, id))
    conn.commit()
    return jsonify({"message": "Student updated successfully"}), 200

@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    cursor.execute("DELETE FROM students WHERE id = %s", (id,))
    conn.commit()
    return jsonify({"message": "Student deleted successfully"}), 200

@app.route("/students/gender/<string:gender>",methods=["GET"])
def get_students_by_gender(gender):
    cursor.execute("select *from students where gender=%s",(gender,))
    students=cursor.fetchall()
    return jsonify(students)

@app.route("/students/dept/<string:dept>",methods=["GET"])
def get_students_by_dept(dept):
    cursor.execute("select *from students where department=%s",(dept,))
    students=cursor.fetchall()
    return jsonify(students)

@app.route("/students/count",methods=["GET"])                                                       
def get_students_count():
    cursor.execute("select count(*) from students")
    cnt=cursor.fetchone()
    return jsonify({"Students count":cnt})

create_table()
if __name__=="__main__":
    app.run()