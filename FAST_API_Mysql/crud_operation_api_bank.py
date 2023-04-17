from fastapi import FastAPI,Depends
from crud_operation_db import Database,get_database
from crud_operation_db import Contents
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()
app.add_middleware(CORSMiddleware,allow_origins=['*'])

@app.post("/insert_item/")
def insert_to_db(item:Contents,DB:Database=Depends(get_database)):
    try:
        DB.connection()
        print("DB connection successful")
    except Exception as e:
        print(e)
    finally:
        print(item)
        user_input=DB.insert_data(item)       
        return{'inserted successfully'}
    
@app.put("/update_item/")
def update_to_db(item:Contents,DB:Database=Depends(get_database)):
    try:
        DB.connection()
        print("DB connection successful")
    except Exception as e:
        print(e)
    finally:
        update=DB.update_data(item)
        return{'updated data succesfully'}
    
@app.delete("/delete_item/")
def delete_from_db(item:Contents,DB:Database=Depends(get_database)):
    try:
        DB.connection()
        print("DB connection successful")
    except Exception as e:
        print(e)
    finally:
        DB.delete_data(item)
        return{'Deleted Successfully'}
        
@app.get("/selected/")
def select_from_db(item:Contents,DB:Database=Depends(get_database)):
    try:
        DB.connection()
        print("DB connection successful")
    except Exception as e:
        print(e)
    finally:   
        user=DB.get_values(item)
        print (user)
        return{"Success":user}

@app.get("/select_all/")
def select_all_from_db(DB:Database=Depends(get_database)):
    try:
        DB.connection()
        print("DB connection successful")
    except Exception as e:
        print(e)
    finally: 
        user=DB.get_all_values()  
        return{'Users':user}   


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000,)