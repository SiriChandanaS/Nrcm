from flask import *
import pymysql
app=Flask(__name__)
mydb=pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="nrcm"
)
is_login=False
cursor=mydb.cursor()

@app.route("/",methods=["GET","POST"])

def login():
    error=""
    if request.method=="POST":
        roll=request.form["Username"]#NAME IN HTML CODE
        cursor.execute("SELECT * FROM users WHERE username=%s",(roll))#USERNAME IN SQL TABLE
        data=cursor.fetchone()
        
        if data==None:
            error="Invalid User"
        else:
            global is_login
            is_login=True
            
            return redirect("index1")
    
    return render_template("nrcm.html",data=error)
@app.route("/index1")
def dashboard():
    print(is_login)
    if is_login:
        return render_template("nrcm1.html")
    else:
        return redirect("/")

if __name__=="__main__":
    app.run(debug=True)