from util import (
  text_formatter
)
import os

class MessageData:
  def __init__(self, **data):
    self.bot = data.get('client')
    
    self.cmd = data.get('cmd')
    self.args = data.get('args')
    
    self.mid = data.get('mid')
    self.author_id = data.get('author_id')
    self.message = data.get('message')
    self.message_object = data.get('message_object')
    self.thread_id = data.get('thread_id')
    self.thread_type = data.get('thread_type')
    self.reply = None
    
    self.font = text_formatter
    
    if self.message_object.replied_to:
      self.reply = self.message_object.replied_to
  async def sendReply(self, message, mentions=None):
    return await self.bot.sendMessage(message, self.thread_id, self.thread_type, mentions=mentions)

async def handleMessage(bot,mid,author_id,message,message_object,thread_id,thread_type,**kwargs):
  _split = message.split(' ',1)
  cmd, args = _split if len(_split) != 1 else [_split[0],'']
  cnp = cmd if bot.prefix == "" or not cmd.startswith(bot.prefix) else cmd[1:];cnp = cnp.lower()
  if cnp in bot.commands:
    function = bot.commands[cnp]
    message_data = MessageData(
      cmd = cnp,
      args = args,
      mid = mid,
      client = bot,
      author_id = author_id,
      message = message,
      message_object = message_object,
      thread_id = thread_id,
      thread_type = thread_type
    )
    is_need_prefix = function.get('usePrefix', True)
    if bot.prefix == '' or (not is_need_prefix and cmd.startswith(bot.prefix)) or (is_need_prefix and cmd.startswith(bot.prefix)) or (not is_need_prefix and not cmd.startswith(bot.prefix)):
      return await function['def'](bot, message_data)
    else:
      return await bot.sendMessage(text_formatter(":mono[This command does not need to use prefix]"), thread_id, thread_type)