from fishpi import FishPi

def message(msg):
    print(msg)

fish = FishPi('')

print(fish.user('imlinhanchao'))
print(fish.chatroom.more())
fish.chatroom.add_listener(message)
fish.chatroom.redpacket.send('摸鱼者，事竟成！')