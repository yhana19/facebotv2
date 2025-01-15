import os
import importlib

events = []

# ━━━━━━━━━━━━━━━ ⦿
def loadEvents(log):
  global events
  if events:
    return events
  files = list(filter(lambda file: file.endswith('.py') and
  file!='__init__.py',os.listdir('./events')))
  print(log.add("\033[97m⦿━━━━━━━━━━━━━━━⦿ \033[96mLoad Events\033[97m ⦿━━━━━━━━━━━━━━━⦿",True))
  for file in files:
    filepath = f"events.{os.path.splitext(file)[0]}"
    module = importlib.import_module(filepath)
    config = getattr(module, 'config', None)
    if config:
      event_type = config.get('event')
      function = config.get('def')
      if not event_type:
        print(log.add(f"\033[0;93m({file}) \033[97mEVENT NOT LOADED - \033[0;31mMissing event type",True))
      elif not function:
        print(log.add(f"\033[0;93m({file}) \033[97mEVENT NOT LOADED - \033[0;31mMissing event function", True))
      else:
        if not event_type.startswith('type:'):
          print(log.add(f"\033[0;93m({file}) \033[97mEVENT NOT LOADED - \033[0;31mInvalid event type",True))
        else:
          config["event"] = config["event"].lower()
          events.append(config)
          print(log.add(f"\033[0;97mEVENT LOADED: \033[0;32m{file}\033[0m", True))
  print()
  log.add()
  return events