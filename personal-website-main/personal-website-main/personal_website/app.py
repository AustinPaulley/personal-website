from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

@app.route('/')
def home():
    github_username = 'AustinPaulley'
    # Define specific repos to fetch
    repo_urls = [
        f'https://api.github.com/repos/{github_username}/personal-website',
        f'https://api.github.com/repos/{github_username}/Linkedin-Scraper-and-Ai-Phishing-Email-Generator'
    ]
    projects = []
    for url in repo_urls:
        response = requests.get(url)
        if response.status_code == 200:
            projects.append(response.json())
        else:
            projects.append({'name': 'Error', 'description': f'Failed to load repo: {url}', 'html_url': url})
    return render_template('home.html', projects=projects)

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/projects')
def projects():
    github_username = 'AustinPaulley'
    url = f'https://api.github.com/users/{github_username}/repos'
    response = requests.get(url)
    projects = response.json() if response.status_code == 200 else []
    return render_template('projects.html', projects=projects)

@app.route('/writeups')
def writeups():
    return render_template('writeups.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)