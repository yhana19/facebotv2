import requests

async def flux(bot, event):
  if not event.args:
    return await event.sendReply(event.font(":mono[Provide an image prompt.]"))
  try:
    nigro = await event.sendReply(event.font(":mono[Uploading image, please wait.]"))
    await bot.sendRemoteFiles(
      [f"https://api.joshweb.click/api/flux?prompt={event.args}&model=4"],
      thread_id=event.thread_id,
      thread_type=event.thread_type
    )
    await bot.unsend(nigro)
  except Exception as e:
    print("\033[0;31m[ERROR] \033[0m{}".format(e))
    return await event.sendReply(event.font(":mono[An error occurred while generating the image.]"))

config = {
  "name": 'flux',
  "def": flux,
  "description": "Generate an image using Flux Realism API.",
  "usage": "{p}flux [prompt]",
  "author": 'ako SI choru',
  "usePrefix": False
}