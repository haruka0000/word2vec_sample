import tweepy
import json
import datetime
import N

# OAuth2.0用のキーを取得する
with open("secret.json") as f:
  secretjson = json.load(f)

# 各種キーをセット
CONSUMER_KEY = secretjson["consumer_key"]
CONSUMER_SECRET = secretjson["consumer_secret"]
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
ACCESS_TOKEN = secretjson["access_token"]
ACCESS_SECRET = secretjson["access_token_secret"]
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

#APIインスタンスを作成
api = tweepy.API(auth)

# Twitter APIをPythonから操作するための準備完了
print('Done!')

def Search(word):
  search_result = api.search(q=word, count=200, until="2016-06-13")
  last_at = list(search_result)[-1].created_at
  result = {"results":search_result, "last_at":last_at}
  return result

def Write(word):
  date = datetime.date.today()
  print(date)
  # 追記モードで出力
  f = open( "test.txt", "a" )
  txt = word + ' -rt -【自動】-【定期】-http -https -【 -/'

  search = Search(txt)
  for result in search["results"]:	
    try:
      f.write(result.text)
    except:
      print('ERROR')
  date = str(search["last_at"])[0:10]
  f.close()

if __name__ == "__main__":
  f = open('test.txt')
  text = f.read()
  f.close()
  name = list(set(N.collect(text)))
  for n in name:
    Write(n)

  #Write('井上麻里奈')
