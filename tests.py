from fishpi import FishPi

def message(msg):
    print(msg)

fish = FishPi('')

print(fish.user('imlinhanchao'))
print(fish.chatroom.more())
fish.chatroom.add_listener(message)