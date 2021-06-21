# Developer Portalで取得できるAPIKEYを設定する
CONSUMER_KEY = 'コンシューマーキーを設定'
CONSUMER_SECRET = 'コンシューマーシークレットキーを設定'
ACCESS_TOKEN = 'アクセストークンを設定'
ACCESS_TOKEN_SECRET = 'アクセストークンシークレットを設定'

# twitterモジュールをインポート
from twitter import *
twitter = Twitter(auth=OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

# 特定のワードのタイムラインを取得
response = twitter.search.tweets(q="好きな文字列")
timelines = response['statuses']

# 取得したタイムラインを表示
for timeline in timelines:
    print(timeline['text'])
    print("-----------------------")