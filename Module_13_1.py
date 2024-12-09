import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for _  in range(5):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял шар №{_ + 1}')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    competitor_1 = asyncio.create_task(start_strongman('Арнольд', 5))
    competitor_2 = asyncio.create_task(start_strongman('Илья Муромец', 7))
    competitor_3 = asyncio.create_task(start_strongman('Сильвестр', 3))
    await competitor_1
    await competitor_2
    await competitor_3

asyncio.run(start_tournament())