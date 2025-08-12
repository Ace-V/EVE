from EVE.EVE_Local import EVE
import asyncio

async def main():
    eve = EVE()
    async with asyncio.TaskGroup() as tg:
        tg.create_task(eve.stt())
        input_message = tg.create_task(eve.input_message())
        tg.create_task(eve.send_prompt())
        tg.create_task(eve.tts())

        await input_message

if __name__ == "__main__":
    asyncio.run(main())