from asyncio import sleep, run, gather

async def count_down(n: int, sleep_time = 1):
    for i in range(n, 0, -1):
        print(i)
        await sleep(sleep_time)
        
async def count_up(n: int, sleep_time = 1):
    for i in range(1, n):
        print(i)
        await sleep(sleep_time)


async def main():
    await gather(count_down(7, 0.5), count_up(5, 2))

    
run(main())