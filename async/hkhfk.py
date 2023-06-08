from __future__ import annotations
import aiohttp
import asyncio


async def async_request():
    link = 'https://api.thecatapi.com/v1/images/search?limit=10'
    async with aiohttp.ClientSession() as session:
        async with session.get(link) as response:
            answer: list[dict[str, str | int]] = await response.json()
            tasks = []

            for i in range(10):
                img_url = answer[i]["url"]
                tasks.append(downloud_cat(session, img_url, i))
            await asyncio.gather(*tasks)

async def downloud_cat(session: aiohttp.ClientSession, img_url: str, i: int):
    async with session.get(img_url) as response:
        img = await response.read()

        format = img_url[-3:]

        with open(f"cat{i+1}.{format}", "wb") as file:
            file.write(img)


def main():
    asyncio.run(async_request())
main()