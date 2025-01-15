import os
import importlib

commands = {}

def loadCommands(_prefix):
  global commands
  if commands:
    return commands
  files = list(filter(lambda file: file.endswith('.py') and file!='__init__.py',os.listdir('./commands')))
  print("\033[97m⦿━━━━━━━━━━━━━━━⦿ \033[96mLoad Commands\033[97m ⦿━━━━━━━━━━━━━━━⦿")
  for file in files:
    filepath = f"commands.{os.path.splitext(file)[0]}"
    module = importlib.import_module(filepath)
    config = getattr(module, 'config', None)
    if config:
      name = config.get('name')
      function = config.get('def')
      if not name:
        print(f"\033[91m[COMMAND]\033[0m({file}) NOT LOADED - \033[0;31mMissing command name")
      elif not function:
        print(f"\033[91m[COMMAND]\033[0m({file}) NOT LOADED - \033[0;31mMissing command function")
      else:
        usePrefix = config.get('usePrefix', True)
        if not name.isalnum():
          print(f"\033[91m[COMMAND]\033[0m({file}) NOT LOADED - \033[0;31mInvalid command name")
        elif name.lower() in commands:
          print(f"\033[91m[COMMAND]\033[0m({file}) NOT LOADED - \033[0;31mCommand name already exist")
        elif usePrefix not in [True, False]:
          print(f"\033[91m[COMMAND]\033[0m({file}) NOT LOADED - \033[0;31mInvalid usePrefix value")
        else:
          admin_only = config.get('admin_only', False)
          if not admin_only in [True,False]:
            admin_only = False
            print(f"\033[0m   - Invalid 'admin_only' key in config, It will automatically set to False")
          config['admin_only'] = admin_only if admin_only in [True, False] else False
          
          config["usage"] = config.get("usage", "").replace('{p}', _prefix)
          config["description"] = config.get("description", 'No description.').replace('{p}', _prefix)
          commands[name.lower()] = config
          print(f"\033[96m[COMMAND] \033[0mLOADED \033[0;93m{name} \033[0m- \033[35m({file})\033[0m")
  print()
  return commands