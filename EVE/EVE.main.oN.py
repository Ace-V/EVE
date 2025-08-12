'''
Important: **Use headphones**. This script uses the system default audio
input and output, which often won't include echo cancellation. So to prevent
the model from interrupting itself it is important that you use headphones.

Before running this script, ensure the `GOOGLE_API_KEY` environment
variable is set to the api-key you obtained from Google AI Studio.
'''

from EVE.EVE_Online import EVE
import asyncio

async def main():
    eve = EVE()
    async with asyncio.TaskGroup() as tg:
        tg.create_task(eve.stt())
        input_message = tg.create_task(eve.input_message())
        tg.create_task(eve.send_prompt())
        tg.create_task(eve.tts())
        tg.create_task(eve.play_audio())

        await input_message

if __name__ == "__main__":
    asyncio.run(main())