import telegram
import asyncio

#텔레그램 토큰
chat_token = "1340164445:AAFGSPa4aKzvJbeDV9Gp6S5DVIm3x03x4j0"
#텔레그램 id
bot_id = '846598578'


async def main(): #실행시킬 함수명 임의지정
    token = "텔레그램 봇 API"
    bot = telegram.Bot( chat_token)
    await bot.send_message(bot_id,'보낼메세지')

asyncio.run(main()) #봇 실행하는 코드