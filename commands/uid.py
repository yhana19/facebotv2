async def uid(bot, data):
  tid = data.thread_id
  if not data.reply:
    sender = data.author_id
    await bot.shareContact(f"{sender}", sender, tid)
  else:
    sender = data.reply.author
    await bot.shareContact(f"{sender}", sender, tid)

config = {
  "name": 'uid',
  "def": uid,
  "usePrefix": False
}