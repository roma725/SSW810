from flask import Flask, render_template

app= Flask(__name__)

@app.route('/student_courses')
def students_courses():
    query='''select s.cwid, s.name, s.major, count(g.Course) as complete
             from students s join grades g on s.cwid=g.Student_CWID
             group by s.cwid, s.name, s.major'''
    db=sqlite3.connect(DB_FILE)
    results = db.execute(query)

    data=[{'cwid':cwid, 'name':name,'major':major, 'complete':complete}
          for cwid, name, major, complete in results]

    db.close()

    return render_template('student_table.html',
                           title='Stevens Repository',
                           table_title='Number of completed courses by student',
                           students=data)

    