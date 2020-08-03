from flask import Flask,render_template,request,make_response
import sqlite3 as sql
import pdfkit
app=Flask(__name__)
name=""
address=""
mobile=""
email=""
objective=""
skills=""
exp1pos=""
exp1duration=""
exp1desc=""
exp2pos=""
exp2duration=""
exp2desc=""
exp3pos=""
exp3duration=""
exp3desc=""
ed1deg=""
ed1duration=""
ed1desc=""
ed2deg=""
ed2duration=""
ed2desc=""
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/viewtemplates")
def viewtemplates():
    return render_template("viewtemplates.html")

@app.route("/resume",methods=['POST','GET'])
def resume():
        global name,address,mobile,email,objective,skills,exp1pos
        global exp1duration,exp1desc,exp2pos,exp2duration,exp2desc,exp3pos
        global exp3duration,exp3desc,ed1deg,ed1duration,ed1desc,ed2deg
        global ed2duration,ed2desc
        choosentemplate=""
        html = ""
        skilllist = skills.split(";")
        if(exp1desc==""):
                exp1desclist=""
        else:
                exp1desclist = exp1desc.split(";")
        if(exp2desc==""):
                exp2desclist=""
        else:
                exp2desclist = exp2desc.split(";")
        if(exp3desc==""):
                exp3desclist=""
        else:
                exp3desclist = exp3desc.split(";")
        if(ed1desc==""):
                ed1desclist=""
        else:
                ed1desclist = ed1desc.split(";")
        if(ed2desc==""):
                ed2desclist=""
        else:
                ed2desclist = ed2desc.split(";")
        if request.method == 'POST':
                choosentemplate = request.form['template']
                if(choosentemplate=='minimal'):
                        html = 'minimal.html'
                if(choosentemplate=='simplenoline'):
                        html = 'simple - no line.html'
                if(choosentemplate=='simpleblue'):
                        html = 'simple - no lines -  blue.html'
                if(choosentemplate=='simplered'):
                        html = 'simple - no lines - red.html'
                if(choosentemplate=='simpleline'):
                        html = 'simple - with lines.html'
        rendered = render_template(html,name=name.upper(),address=address,mobile=mobile,email=email,objective=objective,exp1pos=exp1pos,exp1duration=exp1duration,exp2pos=exp2pos,exp2desc=exp2desclist,exp2duration=exp2duration,exp3duration=exp3duration,exp3pos=exp3pos,exp3desc=exp3desclist,ed1deg=ed1deg,ed1duration=ed1duration,ed1desc=ed1desclist,ed2deg=ed2deg,ed2duration=ed2duration,ed2desc=ed2desclist,skills=skilllist,exp1desc=exp1desclist)
        pdf = pdfkit.from_string(rendered,False)
        response = make_response(pdf)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'inline; filename=Resume.pdf'
        return response



@app.route("/form")
def form():
        return render_template("form.html")

@app.route("/entereddata",methods=['POST','GET'])
def entereddata():
        msg=''
        if request.method == 'POST':
                try:
                        global name,address,mobile,email,objective,skills,exp1pos
                        global exp1duration,exp1desc,exp2pos,exp2duration,exp2desc,exp3pos
                        global exp3duration,exp3desc,ed1deg,ed1duration,ed1desc,ed2deg
                        global ed2duration,ed2desc
                        name = request.form['name']
                        address = request.form['address']
                        mobile = request.form['mobile']
                        email = request.form['email']
                        objective = request.form['objective']
                        skills = request.form['skills']
                        exp1pos = request.form['exp1pos']
                        exp1duration = request.form['exp1duration']
                        exp1desc = request.form['exp1desc']

                        exp2pos = request.form['exp2pos']
                        exp2duration = request.form['exp2duration']
                        exp2desc = request.form['exp2desc']

                        exp3pos = request.form['exp3pos']
                        exp3duration = request.form['exp3duration']
                        exp3desc = request.form['exp3desc']

                        ed1deg = request.form['ed1deg']
                        ed1duration = request.form['ed1duration']
                        ed1desc = request.form['ed1desc']

                        ed2deg = request.form['ed2deg']
                        ed2duration = request.form['ed2duration']
                        ed2desc = request.form['ed2desc']
                        with sql.connect("resumedb.db") as con:
                                cur=con.cursor()
                                cur.execute('INSERT INTO resumes(name,address,mobile,email,objective,skills,exp1pos,exp1duration,exp1desc,exp2pos,exp2duration,exp2desc,exp3pos,exp3duration,exp3desc,ed1deg,ed1duration,ed1desc,ed2deg,ed2duration,ed2desc) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
                                        ,(name,address,mobile,email,objective,skills,exp1pos,exp1duration,exp1desc,exp2pos,exp2duration,exp2desc,exp3pos,exp3duration,exp3desc,ed1deg,ed1duration,ed1desc,ed2deg,ed2duration,ed2desc))
                                con.commit()
                                msg="Records added to database successfully!"
                except:
                        con.rollback()
                        msg="Error"
                finally:
                        return render_template("entereddata.html",msg=msg)
                        con.close()

@app.route("/about")
def about():
        return render_template("about.html")

@app.route("/minimal")
def minimal():
        return render_template("tminimal.html")

@app.route("/simplenoline")
def simplenoline():
        return render_template("tsimple - no line.html")

@app.route("/simplenolineblue")
def simplenolineblue():
        return render_template("tsimple - no lines -  blue.html")

@app.route("/simplenolinered")
def simplenolinered():
        return render_template("tsimple - no lines - red.html")

@app.route("/simpleline")
def simpleline():
        return render_template("tsimple - with lines.html")

if(__name__=='__main__'):
        app.run(debug=True)
