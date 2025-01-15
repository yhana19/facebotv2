import requests
from bs4 import BeautifulSoup

def getName(uid):
  try:
    response = requests.get(f"https://facebook.com/{uid}", headers={
      "User-Agent": 'Mozilla/5.0 (Windows; U; Windows NT 5.0; de-AT; rv:1.7.11) Gecko/20050728'
    })
    html = BeautifulSoup(response.text, 'html.parser')
    name = html.find('title').get_text()
    user_name = name if 'error' not in name.lower() or 'Facebook' != name else 'Facebook User'
    return user_name
  except Exception as er:
    print("\033[31m[ERROR] \033[0m{}".format(er))

async def uid(bot, data):
  tid = data.thread_id
  if not data.reply:
    sender = data.author_id
    await bot.shareContact(f"{getName(sender)}: {sender}", sender, tid)
  else:
    sender = data.reply.author
    await bot.shareContact(f"{getName(sender)}: {sender}", sender, tid)

config = {
  "name": 'uid',
  "def": uid,
  "usePrefix": False
}