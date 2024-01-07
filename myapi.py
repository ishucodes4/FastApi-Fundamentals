
from fastapi import FastAPI  
app=FastAPI()  


 
student={
    1:{
    "name":"john",
    "age":17,
    "class":"year 12"
    }
}



@app.get("/") 
def index():
    return {"name":"first data"}

#understanding pass parameter.

'''google.com/get-student ->this shall give me data of all the student but i want specific student.
therefor-> google.com/get-student/1 '''

@app.get("/get-student/{student_id}") #declaring new endpoint
def get_student(student_id:int):
    return student[student_id]
#open swagger doc-> check krke dekho get students ko.
#also we can go to http://127.0.0.1:8000/get-student/1











