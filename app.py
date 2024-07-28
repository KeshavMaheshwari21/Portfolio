from flask import Flask,render_template,url_for,request
import sqlite3 
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/thank')
def thank():
    return render_template('thank.html')

@app.route('/user_query',methods=['GET','POST'])
def user_query():
    if request.method == "POST": 
        conn =  sqlite3.connect("userdata.db")
        name = request.form['name']
        number = int(request.form['number'])
        email = request.form['email']
        message = request.form['message']


        user_data = (name,number,email,message)
        ## database 
        insert_data_query = """
        insert into userecord values(?,?,?,?)
        """
        cur = conn.cursor()
        cur.execute(insert_data_query,user_data)
        print("You have successfully inserted your data into table : ",user_data)
        conn.commit()
        cur.close()
        conn.close()

        return  render_template("thank.html")
    
if __name__ == "__main__":
    app.run(debug=True)