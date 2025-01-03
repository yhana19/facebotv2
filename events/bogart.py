async def bogart(bot, data):
  message = data.get('message')
  tid = data.get('thread_id')
  typ = data.get('thread_type')
  if 'bogart' in message.lower():
    await bot.sendMessage("Bogart panget", tid, typ)

config = {
  "event": 'type:message',
  "def": bogart,
  "author": 'Muhammad Greeg'
}