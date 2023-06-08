import asyncio
import aiohttp
import os

for file in os.listdir('cats'):
    os.remove('cats/'+ file)

async def download_cat(session: aiohttp.ClientSession, img_url: str, i: int):
    response = await session.get(img_url)
    img_butes = await response.read()

    format = img_url[-3:]
    
    file = open(f'cat{i+1}.{format}')
    file.write(img_butes)
    file.close()

async def request():
    link ='https://api.thecatapi.com/v1/images/search?limit=10'
    session = aiohttp.ClientSession()
    response = await session.get(link)
    
    answer:list[dict[str: str | int]] = await response.json()
    
    task = []
    for i in range(10):
        img_url = answer[i]["url"]
        task.append(download_cat(session, img_url, i))

    await asyncio.gather(*task)

    await session.close()

def main():
    asyncio.run(request())

main()