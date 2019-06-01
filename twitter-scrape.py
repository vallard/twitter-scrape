#!/usr/bin/env python3

import twitter
import os

api = twitter.Api(consumer_key=os.environ['TWITTER_KEY'],
  consumer_secret=os.environ['TWITTER_SECRET'],
  access_token_key=os.environ['TWITTER_TOKEN'],
  access_token_secret=os.environ['TWITTER_TOKEN_SECRET'])

print(api.VerifyCredentials())
