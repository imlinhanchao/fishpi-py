from fishpi import FishPi

def message(msg):
    print(msg)

fish = FishPi('')

print(fish.user('imlinhanchao'))
print(fish.account.info())
print(fish.chatroom.more())
print(fish.emoji.get())
print(fish.notice.count())
fish.chatroom.add_listener(message)
fish.chatroom.redpacket.send('摸鱼者，事竟成！')