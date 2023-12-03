import openai
import os
from flask import Flask, render_template, request, session
from flask_bootstrap import Bootstrap
from dotenv import load_dotenv
from datetime import datetime

app = Flask(__name__)

load_dotenv()

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def get_page():

    if request.method == 'POST':
        user_input = request.form['user_input']
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        session['conversation'].append({"user": user_input, "time": current_time})

        openai.api_key = os.environ.get("API_TOKEN")
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ])
        assistant_response = response["choices"][0]["message"]["content"]
        session['conversation'].append({"assistant": assistant_response, "time": current_time})
        session.modified = True
        return render_template("index.html", conversation=session['conversation'])
    # Clear conversation on each new page load
    session['conversation'] = []
    # Render empty conversation for a new session
    return render_template("index.html", conversation=[])


if __name__ == "__main__":
    app.run(debug=True)

