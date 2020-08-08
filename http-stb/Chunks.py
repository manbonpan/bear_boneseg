'''from pydub import AudioSegment
from pydub.utils import make_chunks

myaudio = AudioSegment.from_file("fir.mp3","mp3") 
chunk_length_ms = 10000 # pydub calculates in millisec
chunks = make_chunks(myaudio, chunk_length_ms) #Make chunks of one sec'''

'''
file = open('fires of war.mp3','rb+')
x=file.read()
file.close'''
file=open('dis.mp3','rb')
x=file.read()
unassigned=[]
streamer=[]
master=[]
import asyncio
import datetime
import random
import websockets
import uuid 
uid=''
async def time(websocket, path):
    print(websocket)

    await websocket.send('ehlo')
    answer=await websocket.recv()
    
    
    
    print(answer)
    if answer == 'uuid':
          global uuid
          uid=str(uuid.uuid1())
          websocket.send('handshake'+uid)
          unassigned.append(uid)
    elif answer == 'song':
        await websocket.send(x)


        
    
        
    
       

start_server = websockets.serve(time, "127.0.0.1", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
