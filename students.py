app= Flask(__name__)

@app.route('/choose_student')
    query= '''select cwid, name from students group by cwid, name'''
    db=sqlite3.connect(DB_FILE)
    results= db.execute(query)

    students=[{'cwid':cwid, 'name':name} for cwid, name in results]
    db.close()
    return render_template('students.html', students=students)