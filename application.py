import os

from flask import Flask, render_template, request, session, url_for, redirect
from flask_socketio import SocketIO, emit
from flask_session import Session

# Time
import time

from Views.max_message_len import Max_Message_List


app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

existing_chat_groups = {}

@app.route("/")
def index():
    if 'username' not in session:
        return redirect(url_for("user_chat"))
    return render_template("index.html")

@app.route("/user_login", methods=["POST"])
def user_login():
    if 'username' in session:
        session.pop('username', None)
    username = request.form.get('username')
    session["username"] = username
    return render_template("create_chat.html", username=session['username'], 
                            all_chats=list(existing_chat_groups.keys()))

@app.route("/create_chat", methods=["POST", "GET"])
def create_chat():
    if 'username' not in session:
        return render_template('index.html')
    #chat_messages = Max_Message_List(99)
    chat_group_name = request.form.get("chat_group_name")
    print(chat_group_name)
    existing_chat_groups[chat_group_name] = Max_Message_List(99, chat_group_name)
    return redirect(url_for('user_chat', current_chat=chat_group_name))

@app.route("/create_chat_group", methods=["GET"])
def create_chat_group():
    return render_template("create_chat.html", username=session['username'], 
                            all_chats=list(existing_chat_groups.keys()))

@app.route("/user_chat/<string:current_chat>")
def user_chat(current_chat):
    if 'username' not in session:
        return url_for(user_login)
    chat_data = existing_chat_groups[current_chat]
    username = session['username']
    messages = chat_data.get_messages()
    return render_template("chat_room.html", username=username, messages=messages, 
                    current_chat=current_chat, all_chats=list(existing_chat_groups.keys()))

@socketio.on("new message")
def all_messages(data):
    new_message = data['message']
    current_chat_name = data['current_chat']
    chat = existing_chat_groups[current_chat_name]

    print(new_message)

    username = session['username']
    # Time
    msg_time = time.ctime(time.time())

    chat.add_msg(new_message, username, msg_time)

    msg_data = {"message": new_message, "username": username, "time": msg_time, 
                "current_chat_name": current_chat_name}
    emit("added message", msg_data, broadcast=True)

if __name__ == "__main__":
    socketio.run(app)
