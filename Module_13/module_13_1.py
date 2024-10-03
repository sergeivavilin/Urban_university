import asyncio
from random import randint


AMOUNT = 5

async def start_strongman(name, power):
    print(f"Силач {name} начал соревнование")
    for i in range(1, AMOUNT+1):
        await asyncio.sleep(i / power)
        print(f"Силач {name} поднял {i} шар")
    print(f"Силач {name} закончил соревнования.")

async def start_tournament():
    power_lifters = ["Добрыня", "Илья", "Алёша"]
    tasks = []
    for name in power_lifters:
        tasks.append(asyncio.create_task(start_strongman(name, randint(1, 10))))

    for task in tasks:
        await task

    print("Соревнование завершено")


if __name__ == '__main__':
    asyncio.run(start_tournament())
