async def uid(bot, **event):
  tid = event.get('thread_id')
  sender = event.get('author_id')
  
  await bot.shareContact(f"UID: {sender}", sender, tid)

config = {
  "name": 'uid',
  "def": uid,
  "usePrefix": False
}