# Developer Portalで取得できるAPIKEYを設定する
CONSUMER_KEY = 'コンシューマーキーを設定'
CONSUMER_SECRET = 'コンシューマーシークレットキーを設定'
ACCESS_TOKEN = 'アクセストークンを設定'
ACCESS_TOKEN_SECRET = 'アクセストークンシークレットを設定'

# twitterモジュールをインポート
from twitter import *
twitter = Twitter(auth=OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

# タイムラインを取得
timelines = twitter.statuses.home_timeline()

# 取得したタイムラインを表示
for timeline in timelines:
    tweet = '({id})[{username}]:{text}'.format(
        id = timeline['id'], username=timeline['user']['name'], text=timeline['text'])
    print(tweet)