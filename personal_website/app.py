from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/projects')
def projects():
    github_username = 'AustinPaulley'  # Replace with your actual GitHub username
    url = f'https://api.github.com/users/{github_username}/repos'
    response = requests.get(url)
    projects = response.json() if response.status_code == 200 else []
    return render_template('projects.html', projects=projects)

@app.route('/writeups')
def writeups():
    return render_template('writeups.html')

if __name__ == '__main__':
    app.run(debug=True)