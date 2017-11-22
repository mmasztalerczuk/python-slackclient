import asyncio

from bot import Bot


class SlackClientController(object):

    def __init__(self):
        self.loop = asyncio.get_event_loop()

    def spawn(self, token):
        return Bot(token, self.loop)

    def start(self):
        self.loop.run_forever()



# slack_token =

controller = SlackClientController()

bot = controller.spawn(slack_token)
bot.start_rtm()
bot.hears(['hello'])
bot.hears(['pawelek'])

controller.start()