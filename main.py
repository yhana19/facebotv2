import asyncio

from fbchat_muqit import Client, Message, ThreadType, State
from handler.loadCommands import loadCommands
from handler.messageHandler import handleMessage

class Greeg(Client):
  def BOT(self):
    self.prefix = '/'
    self.commands = loadCommands()
  
  async def onListening(self):
    print("\033[96m[BOT] \033[0mListening...")
    
  async def __messaging(self, mid, author_id, message, message_object, thread_id, thread_type, **kwargs):
    if author_id != self.uid: #'61571117768115':
      await handleMessage(self,mid,author_id,message,message_object,thread_id,thread_type,**kwargs)
  async def onReply(self, mid, author_id, message, message_object, thread_id,  thread_type, **kwargs):
    await self.__messaging(mid, author_id, message, message_object, thread_id,  thread_type, **kwargs)
  async def onMessage(self,mid,author_id,message,message_object,thread_id,thread_type,**kwargs):
    await self.__messaging(mid, author_id, message, message_object, thread_id,  thread_type, **kwargs)
  
  
async def main():
  cookies_path = "fbstate.json"
  bot = await Greeg.startSession(cookies_path)
  bot.BOT()
  if await bot.isLoggedIn():
    fetch_bot = await bot.fetchUserInfo(bot.uid)
    bot_info = fetch_bot[bot.uid]
    print(f"\033[32m[BOT] \033[0m{bot_info.name} is now logged in")
  try:
    await bot.listen()
  except Exception as e:
    print(e)

if __name__ == '__main__':
  asyncio.run(main())