from flask import Flask,request,jsonify
from flask_cors import CORS
import mysql.connector

app=Flask(__name__)
CORS(app)

conn=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Javedrix@8',
    database='api_db'
)
print(conn)
cursor=conn.cursor()

@app.route("/users",methods=["GET"])
def get_users():
    cursor.execute("select *from users")
    users=cursor.fetchall()
    return jsonify(users)

@app.route("/add",methods=["POST"])
def add_user():
    data=request.json
    name=data["name"]
    email=data["email"]
    age=data["age"]
    cursor.execute("insert into users(name,email,age) values(%s,%s,%s)",(name,email,age))
    conn.commit()
    return jsonify({"message": "User added successfully"}), 201

@app.route("/users/<int:id>",methods=["GET"])
def get_specific_user(id):
    cursor.execute("select *from users where id=%s",(id,))
    user=cursor.fetchone()
    if user:
        return jsonify(user)
    return jsonify({"message": "User not found"}), 404

@app.route("/users/<int:id>",methods=["PUT"])
def update_user(id):
    data=request.json
    name=data["name"]
    email=data["email"]
    age=data["age"]
    cursor.execute("update users set name=%s, email=%s, age=%s where id=%s",(name,email,age,id))
    conn.commit()
    return jsonify({"message":"user updated succesfully"})
    
@app.route("/users/<int:id>",methods=["DELETE"])
def delete_user(id):
    cursor.execute("delete from users where id=%s",(id,))
    conn.commit()
    return jsonify({"message":"user deleted successfully"})

if __name__=="__main__":
    app.run()