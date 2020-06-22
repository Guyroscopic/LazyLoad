from flask import Flask, render_template, request
import copy
from dictionaries import *
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('indexpage.html')
@app.route('/attendance')
def attendance():
    return render_template("class_choose.html")
@app.route("/attendance/section_a")
def attendance_section_a():
    return render_template("course_choose.html")


                                  # physics section A##############
@app.route("/attendance/section_a/physics")
def attendance_physics_a():
    return render_template("attendance_physics_a.html",names_a=names_a)
@app.route('/attendance/section_a/physics/saved_physics', methods=['post'])
def saved_physics_a():
    x=request.form['attendance']
    f=open("attendance_physics_a.txt","a")
    f.write("{}\n".format(x))
    return "SAVED SUCCESSFULLY"
@app.route("/attendance/section_a/physics/saved_physics/display")
def display_attendance_physics_a():
    f = open("attendance_physics_a.txt", "r")
    attendance_physics_a = {}
    n = 0
    lines = f.readlines()
    for i in lines:
        attendance_physics_a[names_a[n]] = i
        n = n + 1
    f.close()
    g = open("attendance_physics_a_display.txt", "w")
    for i,j in attendance_physics_a.items():
        g.write("{}:{}".format(i,j))
    g.close()
    g=open("attendance_physics_a_display.txt","r")
    text=g.readlines()
    g.close()
    return render_template("display.html",text=text)


                                          #chemistry section A##############
@app.route("/attendance/section_a/chemistry")
def attendance_chemistry_a():
    return render_template("attendance_chemistry_a.html",names_a=names_a)
@app.route('/attendance/section_a/chemistry/saved_chemistry', methods=['post'])
def saved_chemistry_a():
    x=request.form['attendance']
    f=open("attendance_chemistry_a.txt","a")
    f.write("{}\n".format(x))
    return "SAVED SUCCESSFULLY"
@app.route("/attendance/section_a/chemistry/saved_chemistry/display")
def display_attendance_chemistry_a():
    f = open("attendance_chemistry_a.txt", "r")
    attendance_chemistry_a = {}
    n = 0
    lines = f.readlines()
    for i in lines:
        attendance_chemistry_a[names_a[n]] = i
        n = n + 1
    f.close()
    g = open("attendance_chemistry_a_display.txt", "w")
    for i,j in attendance_chemistry_a.items():
        g.write("{}:{}".format(i,j))
    g.close()
    g=open("attendance_chemistry_a_display.txt","r")
    text=g.readlines()
    g.close()
    return render_template("display.html",text=text)





#@app.route('/testA', methods=['POST'])
#def test_choose():
 #   return render_template('radiobox.html')


#@app.route('/test/test2')
#def names():
#    return render_template('names.html',student_list=student_list)

#@app.route('/test/test1')
#def test_marks():
 # test1=request.form['testtype']
  #return "you are about to enter the results of {}".format(test1)


@app.route('/test')
def test_choose():
    return render_template("test_choose.html")



@app.route('/test/marks_spring')
def marks_spring():
    return render_template("marks_spring.html",names_a=names_a)
@app.route('/test/marks_fall')
def marks_fall():
    return render_template("marks_fall.html",names_a=names_a)
@app.route('/test/marks_final')
def marks_final():
    return render_template("marks_final.html",names_a=names_a)



@app.route('/test/marks_spring/saved_spring', methods=['post'])
def saved_spring():
    x=request.form['marks']
    f=open("marks_spring.txt","a")
    f.write("{}\n".format(x))
    return "SAVED SUCCESSFULLY"
@app.route('/test/marks_fall/saved_fall', methods=['post'])
def saved_fall():
    x=request.form['marks_fall']
    f=open("marks_fall.txt","a")
    f.write("{}\n".format(x))
    return "SAVED SUCCESSFULLY"
@app.route('/test/marks_final/saved_final', methods=['post'])
def saved_final():
    x=request.form['marks_final']
    f=open("marks_final.txt","a")
    f.write("{}\n".format(x))
    return "SAVED SUCCESSFULLY"



@app.route("/test/marks_final/saved_final/display")
def display_final():
    f = open("marks_final.txt", "r")
    marks_final_a = {}
    n = 0
    lines = f.readlines()
    for i in lines:
        marks_final_a[names_a[n]] = i
        n = n + 1
    f.close()
    g = open("marks_final_display.txt", "w")
    for i,j in marks_final_a.items():
        g.write("{}:{}".format(i,j))
    g.close()
    g=open("marks_final_display.txt","r")
    text=g.readlines()
    g.close()
    return render_template("display.html",text=text)
@app.route("/test/marks_fall/saved_fall/display")
def display_fall():
    f = open("marks_fall.txt", "r")
    marks_fall_a = {}
    n = 0
    lines = f.readlines()
    for i in lines:
        marks_fall_a[names_a[n]] = i
        n = n + 1
    f.close()
    g = open("marks_fall_display.txt", "w")
    for i,j in marks_fall_a.items():
        g.write("{}:{}".format(i,j))
    g.close()
    g=open("marks_fall_display.txt","r")
    text=g.readlines()
    g.close()
    return render_template("display.html",text=text)
@app.route("/test/marks_spring/saved_spring/display")
def display_spring():
    f = open("marks_spring.txt", "r")
    marks_spring_a = {}
    n = 0
    lines = f.readlines()
    for i in lines:
        marks_spring_a[names_a[n]] = i
        n = n + 1
    f.close()
    g = open("marks_spring_display.txt", "w")
    for i,j in marks_spring_a.items():
        g.write("{}:{}".format(i,j))
    g.close()
    g=open("marks_spring_display.txt","r")
    text=g.readlines()
    g.close()
    return render_template("display.html",text=text)



if __name__=='__main__':
    app.run(debug=True)