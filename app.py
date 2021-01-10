
from Chatbot import chatbot
from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'templates'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    userOutput = str(chatbot.get_response(userText))

    f = open('data_collector/data_Collector_All.txt', 'a')
    execute_ = userText + '\n' + userOutput + '\n'
    f.write(execute_)
    f.close()
    f = open('data_collector/data_Collector_Input.txt', 'a')
    f.write(userText+'\n')
    f.close()
    f = open('data_collector/data_Collector_Output.txt', 'a')
    f.write(userOutput+'\n')
    f.close()
    return userOutput

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='5000')