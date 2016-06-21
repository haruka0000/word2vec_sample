import sqlite3

def get_wiki():
  conn = sqlite3.connect("wikipedia.db")
  c = conn.cursor()
  wiki_data = list(c.execute('''SELECT * FROM wiki;''')
  conn.commit()
  return wiki_data

if __name__ == "__main__":
  word = input(">>")
  all_word = []
  
  # 書き込みモードで出力
  f = open( "text.txt", "w" )
  # すべてのtextから
  for r in get_wiki(): 
    f.write(r)  # textの書き出
  f.close
