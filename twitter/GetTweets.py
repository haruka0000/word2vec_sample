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

def search(word):
  txt = word + '-RT -【自動】-【定期】-http -https -【 -/'
  search_result = api.search(q=txt, count=200)
  last_at = list(search_result)[0].created_at
  print(last_at)
  result = {"results":search_result, "last_at":last_at}
  print(api.rate_limit_status()['resources']['search']['/search/tweets'])
  return result

if __name__ == "__main__":
  word = "広島"
  all_word = []
  
  # 追記モードで出力
  f = open( "text.txt", "a" )
  
  # すべてのtextから名詞を抽出
  for r in search(word)["results"]: 
    #print(r.text)
    all_word = all_word + N.collect(r.text)
    f.write(r.text)  # textの書き出し

  top10_word = []
  for t in N.count(all_word):
    #print(t[0])
    top10_word.append(t[0])

  # 数の多い上位50個に関するtextを再度集める
  for aw in top10_word:
    print(aw)
    for r2 in search(aw)["results"]:
      f.write(r2.text)

  f.close()
