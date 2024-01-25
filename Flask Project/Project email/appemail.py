from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

def send_email(email, to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, "jwsdlajoypwkchrn")
        
        subject = "Subject: Your Subject\n"
        message = f"{subject}\n{content}"

        server.sendmail(email, to, message)
        server.quit()
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

@app.route('/', methods=['GET', 'POST'])
def index():
    message_sent = False

    if request.method == 'POST':
        email = request.form['email']
        to = request.form['to']
        content = request.form['content']

        message_sent = send_email(email, to, content)

    return render_template('index.html', message_sent=message_sent)

if __name__ == '__main__':
    app.run(debug=True)
