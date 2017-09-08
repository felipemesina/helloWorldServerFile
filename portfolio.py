from flask import Flask, render_template
app = Flask(__name__)


@app.route('/home')
def home():
    return render_template('home.html')
# app.run(debug=True)

@app.route('/projects')
def projects():
    return render_template('projects.html')
# app.run(debug=True)

@app.route('/about')
def aboutMe():
    return render_template('about.html')




app.run(debug=True) # app.run runs the Flask server, creates a loop, and must always be
                    # at the bottom of the file.
