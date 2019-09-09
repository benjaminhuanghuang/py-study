import asyncio 
import aiohttp 
import time

maxTime = 0.9

async def health_check(services_adresses):
    output = {}
    # Opening session
    async with aiohttp.ClientSession() as session:
        for address in services_adresses:
            start = time.time()
            async with session.get(address) as resp:
                end = time.time()
                delay = end - start
                if (resp.status == 200) and (delay < maxTime):
                    output[address] = True
                else:
                    output[address] = False

    return output


# Testing the function
checkAddresses = ['http://python.org', 'http://goole.com']

result = asyncio.run(health_check(checkAddresses))

print(result)

