from flask import Flask, render_template

app = Flask(__name__)

### Renders a specific template after we define the route ###
@app.route('/')
def home():
    return render_template('home.html')

### Renders dashboard template ###
## NOTE: always add trailing slash to ensure only a single possible route can be used. FOR EXAMPLE: '/dashboard/' ##
@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')

