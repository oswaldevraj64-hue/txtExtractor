#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8438866543:AAHJn5RPshkfrbyc9YoTPb37gxj3LduvugA")
    API_ID = int(os.environ.get("API_ID", "30560523"))
    API_HASH = os.environ.get("API_HASH", "17ab58948bc24d85d961a39e058478a2")
