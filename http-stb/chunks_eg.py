import asyncio
import websockets
import uuid
import os
dirs=input('input full path  to mushiz file')
os.chdir(dirs)
connected = []
rooms=[]
roomcurrent=[]

async def server(websocket, path):
    # Register.

    connected.append([websocket])


    try:

        async for message in websocket:
            print(type(message))
            

            

            if message == 'uuid':
                ids=str(uuid.uuid1())
                loop = asyncio.get_running_loop()
                nicks=message[6:]
                result = await loop.run_in_executor(None, groot,websocket,ids)
                await websocket.send(ids)
            if 'mynick' in message:
                loop = asyncio.get_running_loop()
                nicks=message[6:]
                result = await loop.run_in_executor(None, groot,websocket,nicks)
            if 'roomdata' in message:
                loop = asyncio.get_running_loop()
                result = await loop.run_in_executor(None, fetchdentata)
                await websocket.send(result)
            if 'roomname' in message:
                ids=str(uuid.uuid1())
                oooh=message[8:]+ids
                loop = asyncio.get_running_loop()
                result = await loop.run_in_executor(None,glass,websocket,oooh,message[8:],ids)
                await websocket.send('fullroomname'+oooh)

            if 'songquery' in message:
                ids=message.index('passage')
                name=message[9:ids]
                acid=message[16+ids:]
                loop = asyncio.get_running_loop()
                result = await loop.run_in_executor(None,sonquery,name,acid)
                await websocket.send(result)

            if 'askogdj' in message:
                name=message[7:]
                loop = asyncio.get_running_loop()
                result = await loop.run_in_executor(None,requestsongtimer,name,websocket)
                print(type(result[0]),result[0])
                await result[0].send('timerupdate')
                await websocket.send(result[1])
            if 'sandupdate' in message:
                timestamp=message[9:]
                loop = asyncio.get_running_loop()
                result = await loop.run_in_executor(None,updater,timestamp,websocket)
                for ws in result:
                    await ws.send('newtime'+timestamp)


            if '------->' in message:
              loop = asyncio.get_running_loop()
              result = await loop.run_in_executor(None,echo,websocket)
              for ws in result:
                  await ws.send(message)
              
                


    finally:
        
        # Unregister.
        #connected.remove(websocket)
        pass



def fetchdentata():
    roomanswer='''
<center>roomcontent</center>
'''
    for i in rooms:
    
        for j in i:
                
                roomanswer= roomanswer + "<center>{}:::::::::::::<button id='{}'onClick='reply_click()'>join</button></center>".format(j[1],j[0])
                break
    return roomanswer


def groot(socket,obj):
    for i in connected:
        if socket in i:
            i.append(obj)


    return None
            
def glass(socket,obj,nam,rid):
    rooms.append([[obj,nam,rid,socket],[socket]])

    return None

def sonquery(name,acid):
    try:
        file=open(name+'.mp3','rb')
        f=file.read()
        file.close()
        for i in roomcurrent:
            for j in i:
                if acid in j:
                    roomcurrent.remove(i)
        roomcurrent.append([acid,name])
        return f
    except:
        return 'None'
def requestsongtimer(name,socket):
    ans=[]
    for i in rooms:
        if name in i[0]:
            i[1].append(socket)
            ans.append(i[0][3])
            break
    for i in roomcurrent:
        if name in i:
            file=open(i[1]+'.mp3','rb')
            f=file.read()
            file.close()
            ans.append(f)
            break
    return ans
         
    
   
def updater(time,socket):
    for i in rooms:
        if socket in i[1]:
            ans=i[1]
    return ans      
        
def echo(socket):
    for i in rooms:
        if socket in i[1]:
            ans = i[1]
    return i[1]

    

start_server = websockets.serve(server, "127.0.0.1", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

