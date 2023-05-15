from smtplib import SMTP
from email.mime.text import MIMEText

from flask import Flask, request, render_template
import os
import json

app = Flask(__name__)
staticFolder = os.path.join('static')
app.config['UPLOAD_FOLDER'] = staticFolder

def send_email(name, num, sel):
    sender = "bryilyant16@gmail.com"
    password = "diepokkcztoogswm"
    server = SMTP("smtp.gmail.com", 587)
    server.starttls()

    message = f"Имя: {name}\nТелефон: +7 {num}\n Его выбор: {sel}" 

    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg["Subject"] = "Новый клиент!"
        server.sendmail(sender, sender, msg.as_string())

        return "success"
    except Exception as _ex:
        print(_ex)
        return "error"

@app.route('/', methods=['GET'])
def main():
    if request.method == 'GET':
        return render_template('index.html')

@app.route('/postemail', methods=['POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        num = request.form.get('phone-number')
        sel = request.form.get('input-yacht')

        if send_email(name, num, sel) == "success":
            response = {"message": "Успешно!"}
        else:
            response = {"message": "Данные не отправлены"}

        json.dumps(response)
        return response

if __name__ == "__main__":
    app.run(debug=True)