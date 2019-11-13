document.addEventListener('DOMContentLoaded', () => {

    // Connect to websocket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    // When connected, configure buttons
    socket.on('connect', () => {

        // Each button should emit a "submit vote" event
        document.querySelector('#submit-msg').onclick = () => {
                var message = document.querySelector("#message-content").value;
                var current_chat = document.getElementById("current_chat").innerHTML;
                //alert(current_chat);
                socket.emit('new message', {'message': message, 'current_chat': current_chat});
        };
    });

    // When a new vote is announced, add to the unordered list
    socket.on('added message', data => {
        const username=document.getElementById("username");

        var current_chat_name = data.current_chat_name;

        var msg_holder = document.createElement("p");
        //alert(data.username);
        msg_holder.innerHTML = data.message;

        var time_holder = document.createElement("span");
        time_holder.innerHTML=data.time;
        time_holder.setAttribute("class", "time-right");

        var name_holder = document.createElement("span");
        name_holder.innerHTML=data.username;
        name_holder.setAttribute("class", "name-left");

        var new_msg = document.createElement("div");
        new_msg.setAttribute("class", "container");

        new_msg.appendChild(msg_holder);
        new_msg.appendChild(name_holder);
        new_msg.appendChild(time_holder);

        document.getElementById("message-content").value=null;
        //document.querySelector('.chat-flex-container').firstChild.remove();
        document.querySelector('.chat-flex-container').appendChild(new_msg);
    });
});
