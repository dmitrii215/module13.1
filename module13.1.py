import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнование')
    for i in range(5):
        nbol = i+1
        await asyncio.sleep(nbol//power)
        print(f'Силач {name} поднял {nbol} шар')
    print(f'Силач {name} закончил соревнования')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Pasha', 3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task1
    await task2
    await task3

asyncio.run(start_tournament())