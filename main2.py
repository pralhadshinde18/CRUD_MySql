import pymysql
from fastapi import FastAPI
from pydantic import BaseModel

app =  FastAPI()
myconn=pymysql.connect(host='localhost',user='root',password='',database='Fastapi_db')
mycur = myconn.cursor()

class Student(BaseModel):
    name: str
    rollno: int

@app.post("/student")
def create(student :Student):
    mycur = myconn.cursor()
    query = "insert into students (name,rollno) values(%s,%s)"
    values = (student.name,student.rollno)
    mycur.execute(query,values)
    myconn.commit()
    return {"message" : "students created sucessfully"}

@app.get("/students")
def read_all_students():
    query = "SELECT * FROM students"
    mycur.execute(query)
    result = mycur.fetchall()
    return {"students": result}

@app.put("/student/{rollno}")
def update_student(rollno: int, student: Student):
    query = "UPDATE students SET name = %s WHERE rollno = %s"
    values = (student.name, rollno)
    mycur.execute(query, values)

@app.delete("/student/{rollno}")
def delete(rollno: int):
    mycur = myconn.cursor()
    query = "DELETE FROM students WHERE rollno=%s"
    values = (rollno,)
    mycur.execute(query, values)
    myconn.commit()
    return {"message": "Student record deleted successfully"}



myconn.close()















































































