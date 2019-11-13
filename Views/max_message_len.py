class Max_Message_List(object):

    def __init__(self, max_len, chat_group_name):
        self.chat_group_name = chat_group_name
        self.messages = []
        self.max_len = max_len

    def add_msg(self, new_message, username, msg_time):
        if len(self.messages) == self.max_len:
            self.messages.pop(0)
        complete_msg = {"message": new_message, "username": username, "time":msg_time}
        self.messages.append(complete_msg)

    def get_messages(self):
        return self.messages

    def get_chat_group_name(self):
        return self.chat_group_name