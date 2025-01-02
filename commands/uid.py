async def uid(bot, data):
  tid = data.thread_id
  sender = data.author_id
  
  await bot.shareContact(f"UID: {sender}", sender, tid)

config = {
  "name": 'uid',
  "def": uid,
  "usePrefix": False
}