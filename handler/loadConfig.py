import json
import asyncio

async def loadConfig(botName=None, log=None):
  data = {
    "prefix": None,
    "botName": botName,
    "owner": "Unknown",
    "admin": [
      61571117768115
    ]
  }
  print(log.add(f"\033[97m⦿━━━━━━━━━━━━━━━⦿ \033[96mLoad Config \033[97m⦿━━━━━━━━━━━━━━━⦿",True))
  try:
    config = json.load(open('config.json', 'r'))
  except FileNotFoundError:
    print(log.add("\033[0;31m[CONFIG] \033[0mConfig file not found\n",True))
    return data
  await asyncio.sleep(0.2)
  prefix = config.get('prefix', '')
  if not prefix:
    print(log.add("\033[0;36m[CONFIG] \033[0mNo prefix",True))
    prefix = ''
  elif not isinstance(prefix, str):
    print(log.add("\033[0;31m[CONFIG] \033[0mInvalid prefix data types",True))
    prefix = ''
  elif ' ' in list(prefix):
    prefix = ''
    print(log.add("\033[0;31m[CONFIG] \033[0mPrefix must not include space",True))
  else:
    print(log.add(f"\033[0;36m[CONFIG] \033[0mPrefix loaded    : \033[1;97m{prefix}",True))
  
  botName = config.get('botName', data['botName'])
  print(log.add(f"\033[0;36m[CONFIG] \033[0mBot name loaded  : \033[1;97m{botName}",True))
  owner = config.get("owner", data['owner'])
  print(log.add(f"\033[0;36m[CONFIG] \033[0mBot owner loaded : \033[1;97m{owner}",True))
  _admin = config.get("admin", data['admin'])
  admin = [str(ad) for ad in _admin if isinstance(ad, int) or isinstance(ad, str)]
  print(log.add(f"\033[0;36m[CONFIG] \033[0mBot admin loaded : \033[1;97m{len(admin)}",True))
  
  data['prefix'] = prefix
  data['botName'] = botName
  data['owner'] = owner
  data['admin'] = admin
  return data