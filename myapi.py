#import fastapi  #installing fastapi and running in my command by using python myapi.py
from fastapi import FastAPI  #importing fastapi like an object.FastAPI is an object here
app=FastAPI()  #creating instance of the object here.


 #creating end point of the API(communication channel)-> Basically URL
#example->amazon.com/create-user ->create user is endpoint.beacuse it tells what resource now you want to interact with

'''there are different types of endpoints:
GET-get an information
POST-create new object in the database
PUT-update something in particular object
DELETE-erase
'''

@app.get("/") #get->for getting information and /->because we are talking about homepage.
def index():
    return {"name":"first data"}

#now for running itna part->command->inside directory->uvicorn myapi:app --reload ->paste the URL
#http://127.0.0.1:8000/docs ->opens swagger documentation->test api(no postman needed)->try out->execute






