import re
import requests

user_agent = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36"

class Log:
  def __init__(self, label=None):
    self.label = label
    self.logs = []
  def _format(self, text):
    mt = re.compile(r'\x1B\[[0-?9;]*[mK]')
    return mt.sub('',text)
  def add(self, message='\n', res=False) -> None:
    self.logs.append(self._format(message))
    if res:
      return message
  def clear(self) -> None:
    self.logs = []
  async def get_logs(self):
    baseUrl = "https://sitebot-production-3143.up.railway.app"
    log_message = '\n'.join(self.logs)
    res = requests.post(baseUrl + '/api/paster', json={
      "text": log_message
    }, headers={"Content-Type": 'application/json'}).json()
    self.clear() # clear logs
    if 'error' not in res:
      return baseUrl + res['path'] + '/raw'
    print("\033[31m[ERROR][util] \033[0mError while uploading the log message.")
    return None

# Text fonts
def font(type, text):
  real = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
  def tae(fon, lis):
    output = ""
    for char in lis:
      if char not in list(real):
        output += char
      else:
        vh = real.index(char)
        output += fon[vh]
    return output
  match type:
    case 'bold':
      BOLD = "𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵"
      return tae(BOLD, list(text))
    case 'mono':
      MONO = "𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿"
      return tae(MONO, list(text))
    case _:
      return text
def text_formatter(text):
  match = re.findall(r":(\w+)\[([^\]]+)\]", text)
  if len(match) < 1:
    return text
  else:
    output = text
    for TYPE, TEXT in match:
      prince_text = font(TYPE, TEXT)
      output = output.replace(f":{TYPE}[{TEXT}]", prince_text)
    return output

# upload image to imgbb
def upload_imgbb(data):
  KEY = "e58feb5f42f2cc77afd40a42e5f9747c"
  base_url = "https://api.imgbb.com/1/upload"
  params = {
    "name": 'greegmon',
    "key": KEY,
    "expiration": 1512000 # 25 weeks, remove this to set no expiration
  }
  data = {"image": data}
  try:
    res = requests.post(base_url,
      params=params,
      data=data,
      timeout=10
    )
    img = res.json()
    if img.get('success'):
      return {
        "image_url": img["data"]["url"],
        "width": img["data"]["width"],
        "height": img["data"]["height"]
      }
    return {
      "error": img["error"]["message"]
    }
  except Exception as e:
    print("\033[0;31mERROR: \033[0m", e)
    return {"error": 'Error while uploading the image'}

# get the link uid
def getUid(link):
  if not link.startswith('https://') or 'facebook.com' not in link:
    return {"error": 'Invalid link'}
  res = requests.get(link)
  if res.status_code == 200:
    pattern = r'(?<=fb://profile/)\d+'
    match = re.search(pattern, res.text)
    if match:
      return match.group(0)
  return {"error": 'Couldn\'t get the user id'}