class Chatroom:
    def __init__(self,name):
        self.name=name
        self.messages=[]
        self.users=[]

    def enter_room(self,name):
        if name not in self.users:
            self.users.append(name)
            self.messages.append(f"{name}进入了聊天室")

    def leave_room(self,name):
        if name in self.users:
            self.users.remove(name)
            self.messages.append(f"{name}离开了聊天室")

    def send_message(self,user,message):
        if user in self.users:
            self.messages.append(f"{user}:{message}")

    def show_message(self):
        for message in self.messages:
            print(message)

chatroom=Chatroom("聊天室")
chatroom.enter_room("Vichen")
chatroom.send_message("Vichen","Hello!")
chatroom.leave_room("Vichen")
chatroom.show_message()