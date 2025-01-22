import random 
import asyncio
from colorama import Fore
from fbchat_muqit import (
  Client,
  Message,
  ThreadType,
  State
)

data = {}
y = input("Prefix: ")
class Bot(Client):
  async def onMessage(self,mid,author_id,message,message_object,thread_id,thread_type,**kwargs):
   async def send():
      await self.sendMessage(reply, thread_id, thread_type)
   cmd = {f"{y}bal", f"{y}roll"}
   if author_id not in data:
      data[author_id] = {"bal": 1000}
   else:
      bal = data[author_id]['bal']
   bal = data[author_id]['bal']
   
   x = message.split()
   if x[0].lower() not in cmd:
       reply = "+"
   else:
      
      
      if len(x) == 2 and x[0].lower() == f"{y}roll" and x[1].isdigit() and int(x[1]) <= 0:
          reply = "Enter a positive bet."
          await send()
      
      elif len(x) == 1 and x[0].lower() == f"{y}roll":
          reply = f"Invalid usage. usage is {y}roll <bet>."
          await send()
          
      elif len(x) == 2 and x[0].lower() == f"{y}roll" and x[1].isdigit() and int(x[1]) > 0 and int(x[1]) > bal:
          reply = "Not enough balance for bet."
          await send()
      
      elif len(x) == 2 and x[0].lower() == f"{y}roll" and not x[1].isdigit():
          reply = "Enter a valid bet."
          await send()
      
      
      elif len(x) == 2 and x[0].lower() == f"{y}roll" and x[1].isdigit() and int(x[1]) > 0 and int(x[1]) <= bal:
         chose = ['win', 'lose']
         result = random.choice(chose)
         if result == win:
            data[author_id]['bal'] += int(x[1])
            reply = f"""
🎲 𝚃𝚑𝚎 𝚍𝚒𝚌𝚎 𝚕𝚊𝚗𝚍𝚎𝚍 𝚘𝚗【1】
━━━━━━━━━━━━━
🎉 𝘾𝙤𝙣𝙜𝙧𝙖𝙩𝙪𝙡𝙖𝙩𝙞𝙤𝙣𝙨! 𝙔𝙤𝙪 𝙬𝙤𝙣
${x[1]} 💵"""
            await send()
         if result == lose:
            data[author_id]['bal'] -= int(x[1])
            reply = f"""
🎲 𝚃𝚑𝚎 𝚍𝚒𝚌𝚎 𝚕𝚊𝚗𝚍𝚎𝚍 𝚘𝚗【2】
━━━━━━━━━━━━━
💸 𝙎𝙤𝙧𝙧𝙮! 𝙔𝙤𝚞 𝚕𝚘𝚜𝚝 ${x[1]}"""
            await send()
      elif len(x) == 1 and x[0].lower() == f"{y}bal":
        reply = f"""
━━━━Balance━━━━ 
${bal:,} 💰"""
        await send()
