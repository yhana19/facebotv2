import requests

async def function(bot, event):
  if event.args: return await event.sendReply(event.font(":mono[This command dont need an argument]"))
  loading = await bot.sendMessage(event.font(":mono[Fetching random shoti, please wait...]"), event.thread_id, event.thread_type)
  try:
    url = "https://sitebot-production-3143.up.railway.app/api/shoti"
    res = requests.get(url)
    data = res.json()
    if res.status_code != 200:
      await bot.unsend(loading)
      return await event.sendReply(event.font(f":mono[{data['error']}]"))
    message = f":bold[user]: {data['username']}\n"
    message += f":mono[{data['description']}]"
    video = data['videoSource']
    await bot.sendRemoteFiles(
      video,
      event.font(message),
      thread_id = event.thread_id,
      thread_type = event.thread_type
    )
    await bot.unsend(loading)
  except Exception as e:
    print(f"\033[91m[ERROR] \033[0m{e}")
    await event.sendReply(event.font(f":mono[{e}]"))


# config = {
#   "name": 'shoti',
#   "def": function,
#   "author": "Muhammad Greeg",
#   "usage": '{p}shoti',
#   "description": 'Fetch a random shoti video',
#   "usePrefix": False
# }
