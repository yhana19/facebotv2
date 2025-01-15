import asyncio
import json
from fbchat_muqit import (
  Client,
  Message,
  ThreadType,
  State,
  FBchatException
)
from handler.loadConfig import loadConfig
from handler.loadEvents import loadEvents
from handler.loadCommands import loadCommands
from handler.messageHandler import handleMessage
from handler.eventHandler import handleEvent
from util import Log

log = Log('FacebotV2')

config = json.load(open('config.json', 'r'))

class Greeg(Client):
  def BOT(self, data):
    self.commands = loadCommands(data['prefix'], log) # dict
    self.events = loadEvents(log) # list
    self.log = Log
    # Bot info
    self.prefix = data['prefix']
    self.botName = data['botName']
    self.owner = data['owner']
    self.admin = data['admin']
    # exception
    self.FBchatException = FBchatException
    # thread type
    self.thread_user = ThreadType.USER
  def error(self, message):
    print(f"\033[0;91m[ERROR] \033[0m{message}")
  async def onListening(self):
    log.add("[BOT] Listening...")
    link = await log.get_logs()
    message = "Bot is now online.\n\n"
    message += f"Name: {self.botName}\n"
    message += f"Owner: {self.owner}\n"
    message += f"Admins: {len(self.admin)}\n"
    message += f"Prefix: {self.prefix if self.prefix != '' else 'I dont have prefix'}\n"
    message += f"Commands: {len(self.commands)}\n"
    message += f"Events: {len(self.events)}\n\n"
    message += f"LOG: {link}"
    await self.sendMessage(message, self.admin[0])
    print("\033[32m[BOT] \033[0mListening...")
    print()
  async def __botEvent(self, event, **data):
    asyncio.create_task(handleEvent(self, event.lower(), **data))
  async def __messaging(self, mid, author_id, message, message_object, thread_id, thread_type, **kwargs):
    if author_id != self.uid:
      await self.__botEvent('type:message', mid=mid,author_id=author_id,message=message,message_object=message_object,thread_id=thread_id,thread_type=thread_type,**kwargs)
      asyncio.create_task(handleMessage(self,mid,author_id,message,message_object,thread_id,thread_type,**kwargs))
  
  """MESSAGE EVENTS"""
  async def onReply(self, mid, author_id, message, message_object, thread_id,thread_type, **kwargs):
    await self.__messaging(mid, author_id, message, message_object, thread_id,  thread_type, **kwargs)
  async def onMessage(self,mid,author_id,message,message_object,thread_id,thread_type,**kwargs):
    await self.__messaging(mid, author_id, message, message_object, thread_id,  thread_type, **kwargs)
  
  """OTHER EVENTS"""
  async def onPeopleAdded(self, **data):
    await self.__botEvent("type:addedParticipants",thread_type=ThreadType.GROUP, **data)
  
  
async def main():
  cookies_path = "fbstate.json"
  bot = await Greeg.startSession(cookies_path)
  if await bot.isLoggedIn():
    fetch_bot = await bot.fetchUserInfo(bot.uid)
    bot_info = fetch_bot[bot.uid]
    kol = await loadConfig(bot_info.name, log)
    bot.BOT(kol)
    print(log.add(f"\033[97m⦿━━━━━━━━━━━━━━━⦿ \033[96mFACEBOT \033[97m⦿━━━━━━━━━━━━━━━⦿",True))
    print(log.add(f"\033[32m[BOT] \033[0m{bot_info.name} is now logged in",True))
  try:
    await bot.listen()
  except FBchatException as g:
    print(g)
    print("=====>>>")
  except Exception as e:
    print(log.add("\033[0;91m[BOT] \033[0mAn error occured while trying to login, please check your bot account or get a new fbstate",True))

if __name__ == '__main__':
  asyncio.run(main())