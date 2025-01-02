async def test(bot, data):
  url = "https://picsum.photos/200"
  tid = data.thread_id
  typ = data.thread_type
  await bot.sendRemoteFiles(url, "Hello, World", tid, typ)

config = {
  "name": 'test',
  "def": test,
  "usePrefix": False
}