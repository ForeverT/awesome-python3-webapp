#!/usr/bin/env python3
# -*-coding:utf-8 -*-

import logging;logging.basicConfig(level=logging.INFO)

import asyncio,os,json,time
from datetime import datetime
from aiohttp import web

def handle(request):
	name = request.match_info.get('name', "Anonymous")
	logging.info("handle a request..."+name)
	return web.Response(body=b'<h1>Awesome</h1>')

@asyncio.coroutine
def init(loop):
	app = web.Application(loop=loop)
	app.router.add_route('GET','/{name}',handle)
	srv = yield from loop.create_server(app.make_handler(),'127.0.0.1',9000)
	logging.info("server started at http://127.0.0.1:9000..")
	return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
try:
	loop.run_forever()
except KeyboardInterrupt:
	pass
