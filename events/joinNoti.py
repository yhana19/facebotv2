import urllib.parse

async def bagong_tao(bot, event):
  data = event.get('msg')
  tid = event['thread_id']
  typ = event['thread_type']
  for fbuser in data.get('addedParticipants'):
    if fbuser['userFbId'] == bot.uid:
      await bot.shareContact(event.font(":mono[Thank you for adding me.]"), sender, tid)
  else:
    fbuser = data.get('addedParticipants')[0]
    
    threadX = await bot.fetchThreadInfo(tid)
    thread = threadX[tid]
    
    name = fbuser['fullName']
    groupName = thread.name if thread.name else "Group Chat"
    member = len(thread.participants)
    groupPhoto = urllib.parse.quote(thread.photo) if thread.photo else "https://i.ibb.co/G5mJZxs/rin.jpg"
    uid = fbuser['userFbId']
    background = urllib.parse.quote("https://i.ibb.co/4YBNyvP/images-76.jpg")
    
    photo = "https://api.joshweb.click/canvas/welcome?name={}&groupname={}&groupicon={}&member={}&uid={}&background={}".format(
      name, groupName,
      groupPhoto, member,
      uid, background
    )
    print(photo)
    await bot.sendRemoteFiles(photo, f"Welcome {name}", thread_id=tid, thread_type=typ)

config = {
  "event": "type:addedParticipants",
  "def": bagong_tao,
  "author": "Muhammad Greeg"
}