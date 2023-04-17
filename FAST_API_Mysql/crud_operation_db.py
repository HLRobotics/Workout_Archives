import mysql.connector
from pydantic import BaseModel
from typing import Optional

class Contents(BaseModel):
    name: Optional[str]
    address: Optional[str]
    company: Optional[str]
    salary: Optional[str]

class Database:

    def connection(self):
        self.mydb=mysql.connector.connect(host="localhost",user="root",password="",database="api_ops")
        self.cursor=self.mydb.cursor()

    def insert_data(self,contents:Contents):
        query="INSERT INTO `users`(`name`, `address`, `company`, `salary`) VALUES (%s,%s,%s,%s)"
        val=[contents.name,contents.address,contents.company,contents.salary]
        value=self.cursor.execute(query,val)
        self.mydb.commit()
        return value
    
    def update_data(self,contents:Contents):
        query="UPDATE `users` SET `name`=%s WHERE `company`=%s"
        val=[contents.name,contents.company]
        result=self.cursor.execute(query,val)
        self.mydb.commit()
        return result
    
    def delete_data(self,content:Contents):
        query="DELETE FROM `users` WHERE `company` = %s"
        val=[content.company]
        result=self.cursor.execute(query,val)
        self.mydb.commit()
        return result
    
    def get_values(self,content:Contents):
        query="SELECT * FROM users WHERE company =%s"
        val=[content.company]
        self.cursor.execute(query,val)
        result=self.cursor.fetchall()
        return result    

    def get_all_values(self):
        query="SELECT * FROM users"
        self.cursor.execute(query)
        result=self.cursor.fetchall()
        return result    


db=Database()
async def get_database() -> Database:return db