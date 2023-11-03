# import
import os, logging,tracemalloc
from telethon import TelegramClient, events

#----------------------------------- logging --------------------------------------------
logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)
tracemalloc.start()
#---------------------------- set info acc ----------------------------------------------
api_id = 1331656
api_hash = '868c8254ed0fbc05a5ef0dab474ffdf9'
phone_number = '+989308756586'
#------------------------------ connect client ------------------------------------------
if not os.path.exists('session'):
    os.makedirs('session')

client = TelegramClient('session/'+phone_number, api_id, api_hash)

@client.on(events.NewMessage)
async def my_event_handler(event):
    async def info(event):
        chat = await event.get_chat()
        sender = await event.get_sender()
        chat_id = event.chat_id
        sender_id = event.sender_id
        infoList = [chat,sender,chat_id,sender_id]
        return infoList
    
    x = info(event)
    print(x)
    if 'ping' in event.raw_text:
        await event.reply('Pong !!')

client.start()
if client.run_until_disconnected():
    print("Start")