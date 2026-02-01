#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8277242043:AAHWcp5qC3IXXb8mZMweeX4jMP5ktx83mEg")
    API_ID = int(os.environ.get("API_ID", "30560523"))
    API_HASH = os.environ.get("API_HASH", "17ab58948bc24d85d961a39e058478a2")
    AUTH_USERS = os.environ.get("AUTH_USERS", "8342427239")
