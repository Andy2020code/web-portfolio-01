from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Add a route to serve your CSS file
@app.route('/css/<filename>')
def serve_css(filename):
    return app.send_static_file('css/' + filename)

# Add a route to serve your image files
@app.route('/IMG/<filename>')
def serve_images(filename):
    return app.send_static_file('IMG/' + filename)

# Add a route to serve your JavaScript files
@app.route('/js/<filename>')
def serve_js(filename):
    return app.send_static_file('js/' + filename)

# Add routes for specific HTML pages
@app.route('/index')
def serve_index():
    return render_template('index.html')

@app.route('/services')
def serve_our_services():
    return render_template('services.html')

@app.route('/web-app')
def serve_therapists():
    return render_template('web-app.html')

@app.route('/zc')
def zc_rating():
    return render_template('zc.html')

@app.route('/osc')
def osc_rating():
    return render_template('osc.html')

@app.route('/past-work-01')
def past_works():
    return render_template('past-web-dev-work.html')

@app.route('/past-work-index')
def past_works_index():
    return render_template('past-work-index.html')

@app.route('/web-resume')
def web_resume():
    return render_template('resume.html')

@app.route('/asset-library')
def asset_update():
    return render_template('asset-library-01.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)