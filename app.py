from flask import Flask, render_template, request
from flask_mail import Mail, Message
import os

app = Flask(__name__)

# Configure Flask-Mail for Gmail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'serverform45@gmail.com'
app.config['MAIL_PASSWORD'] = 'gdol cwrs jxxk pjqa'
app.config['MAIL_DEFAULT_SENDER'] = 'serverform45@gmail.com'

mail = Mail(app)
# Configure Flask-Mail for Gmail

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

@app.route('/photography')
def photo_portfolio():
    return render_template('photography-portfolio.html')

@app.route('/graphic-design')
def graphic_design_portfolio():
    return render_template('graphic-design-portfolio.html')

@app.route('/contact-us')
def contact_us():
    return render_template('contact-us.html')















#routes for zencounseling.me#








@app.route('/submit_contact_form', methods=['POST'])
def submit_contact_form():
    data = request.json  # Get JSON data from the request

    # Process the form data as needed
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    # Perform any necessary validation or email sending logic here

    # Send email
    try:
        send_email(name, email, message)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

    return 'OK', 200  # Return a simple response to the client

def send_email(name, email, message):
    recipient_email = 'andersonromanodasilva2020@gmail.com'  # Replace with the recipient's email address

    subject = f"New Contact Form Submission from {name}"
    body = f"Name: {name}\nEmail: {email}\nMessage: {message}"

    msg = Message(subject, recipients=[recipient_email])
    msg.body = body

    try:
        mail.send(msg)
    except Exception as e:
        print(f"Error sending email: {e}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)
