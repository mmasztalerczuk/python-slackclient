from _ssl import SSLError

import json
import websocket
import websockets

from slackclient import SlackClient
import asyncio

from slackclient.slackrequest import SlackRequest


class Bot:

    def __init__(self, token, loop):
        self.token = token
        self.loop = loop
        self.keywords = []

    def start_rtm(self, callBack=None):
        self.client = SlackClient(self.token)

        api_requester = SlackRequest(proxies=None)
        connect_method = "rtm.connect"
        reply = api_requester.do(self.token, connect_method, timeout=None)

        login_data = reply.json()

        async def dispatcher():
            async with websockets.connect(login_data['url']) as websocket:
                while True:
                    print("elo")
                    data = []

                    data = await websocket.recv()
                    data = json.loads(data)

                    if 'text' in data:
                        for keyword in self.keywords:
                            if keyword in data['text']:
                                print("<{} {}".format(keyword, data))

                #asyncio.ensure_future(dispatcher(), loop=self.loop)

        asyncio.ensure_future(dispatcher(), loop=self.loop)

    def hears(self, keywords, callback):
        self.keywords.append(keywords, callback)
