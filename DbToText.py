import sqlite3

def get_wiki():
  conn = sqlite3.connect("wikipedia.db")
  c = conn.cursor()
  wiki_data = list(c.execute('''SELECT * FROM wiki;''' ))[0]
  conn.commit()
  return wiki_data

if __name__ == '__main__':
	print(type(get_wiki()))
	
