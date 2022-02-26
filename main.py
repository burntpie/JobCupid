from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/qn1")
def qn1():
    options = ['Accountancy', 'Arts', 'Business', 'Computer Science', 
                'Communication Studies', 'Engineering','History', 'Mathematics', 
                'Pyschology', 'Science', 'Sociology', 'Select']
    return render_template("question1.html", options=options, npage="qn2")

@app.route("/qn2")
def qn2():
    options = ['Australia', 'China', 'Canada', 'Indonesia', 'Malaysia',
                'Singapore', 'Thailand', "United Kingdom", 'USA', 'Select']
    return render_template("question2.html", options=options, npage="qn3", bpage="qn1")

@app.route("/qn3")
def qn3():
    options = ['Full Time', 'Part Time', 'Summer Internship',
               'Credit-Bearing Internship', 'Select']
    return render_template("question3.html", options=options, npage="qn4", bpage="qn2")

@app.route("/qn4")
def qn4():
    options = ['< $1000', '$1000 to $2000', '$2000 to $3000',
               '$3000 to $4000', '$4000 to $5000', '> $5000', 'Select']
    return render_template("question4.html", options=options, npage="qn5", bpage="qn3")

@app.route("/qn5")
def qn5():
    options = ['Banking & Finance', 'Consulting and Management','Engineering and Manufacturing',
                'IT', 'Marketing',
               'Chemical Manufacturing', 'Medical', 'Select']
    return render_template("question5.html", options=options, npage="qn6", bpage="qn4")

@app.route("/qn6")
def qn6():
    options = ['Team-player', 'Independent-worker',
               'Fast-learner', 'Leader', 'Select']
    return render_template("question6.html", options=options, npage="qn7", bpage="qn5")

@app.route("/qn7")
def qn7():
    return render_template("question7.html", npage="jobmatchsuccess", bpage="qn6")

@app.route("/job1")
def job1():
    return render_template("job1.html", page="job2", joblink="https://careers.shopee.sg/students")

@app.route("/job2")
def job2():
    return render_template("job2.html", page='job3', fpage="job1", joblink="https://capps.com.sg/career")

@app.route("/job3")
def job3():
    return render_template("job3.html", page="job4", fpage="job2", joblink="https://www.anotech-energy.com/jobs/")

@app.route("/job4")
def job4():
    return render_template("job4.html", page="job5", fpage="job3", joblink="https://jobs.institutedata.com/")

@app.route("/job5")
def job5():
    return render_template("job4.html", page="home", fpage="job4", joblink="https://jobs.institutedata.com/")

@app.route("/jobmatchsuccess")
def jobmatchsuccess():
    return render_template("jobmatchsuccess.html")


"""
& C:/Users/ngliw/AppData/Local/Programs/Python/Python38-32/python.exe "c:/Users/ngliw/OneDrive - Nanyang Technological University/intuition hackathon/xiaolongbaoz/main.py"
"""


if __name__ == "__main__":
    app.run(debug= True)