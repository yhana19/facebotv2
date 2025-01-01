from dataclasses import dataclass

class Astro:
  def __init__(self, bot):
    self.bot = bot
    self.prefix = self.bot.prefix
    self.commands = self.bot.commands
  async def sendMessage(self, message):
    pass
async def handleMessage(bot,mid,author_id,message,message_object,thread_id,thread_type,**kwargs):
  _split = message.split(' ',1)
  cmd, args = _split if len(_split) != 1 else [_split[0],'']
  cnp = cmd if not cmd.startswith(bot.prefix) else cmd[1:];cnp = cnp.lower()
  
  if cnp in bot.commands:
    function = bot.commands[cnp]
    is_need_prefix = function.get('usePrefix', True)
    if (is_need_prefix == True and cmd.startswith(bot.prefix)) or (not is_need_prefix and not cmd.startswith(bot.prefix)):
      return await function['def'](bot, 
        cmd = cnp,
        args = args,
        mid = mid,
        author_id = author_id,
        message = message,
        message_object = message_object,
        thread_id = thread_id,
        thread_type = thread_type,
        **kwargs
      )
    else:
      return await bot.sendMessage("Prefix error", thread_id, thread_type)