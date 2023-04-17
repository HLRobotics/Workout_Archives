from flask import Flask,redirect,Response,url_for,render_template,request,flash
import bot_logic
app=Flask(__name__)

@app.route("/")
def load_login_Page():
    return(render_template("login.html"))

@app.route("/login_page" ,methods=['POST','GET'])
def login():  
    if request.method=='POST':  
        error="Invalid Credentials"
        employee_id=request.form['employee_id']
        password=request.form['password']
        if(employee_id=="1304" and password=="test"):
          return render_template("bot.html", id=employee_id)
        else:
            return error
        
@app.route("/bot_reply",methods=['POST','GET'])
def bot():
    if request.method=='POST':  
        question=request.form['query']
        answer=bot_logic.ask_bot(question)      
        return render_template("bot.html", reply=answer)

if __name__=="__main__":
    app.run(debug=True)