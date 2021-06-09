import sqlite3
import json
from os.path import isfile
import collections
from dummies import data_categories

def create_db():
	conn = sqlite3.connect('data.db')
	cursor = conn.cursor()
	
	# drop table categories
	cursor.execute("DROP TABLE IF EXISTS categories")

	# create table categories
	cursor.execute('''CREATE TABLE IF NOT EXISTS categories
		(id integer primary key NOT NULL,
		parent_id integer NULL,
		name varchar(45) NOT NULL)''')

	# insert dummies data
	cursor.executemany('INSERT INTO categories(id, parent_id, name) VALUES (?,?,?)', data_categories)

	conn.commit()
	conn.close()

def create_json():
	DB = './data.db'
	if (isfile(DB)):
		conn = sqlite3.connect(DB)
		cursor = conn.cursor()
		cursor.execute('SELECT id, parent_id, name from categories')
		
		categories = cursor.fetchall()
		roots = [root for root in categories if root[1] == '']
		items = [
			{
				'category': root[2],
				'subcategories': [
					category[2]
					for category in categories
					if category[1] == root[0]
				]
			}
			for root in roots
		]
		
		with open('categories.json', 'w') as file:
			json.dump(items, file)

		conn.commit()
		conn.close()

def main():
	create_db()
	create_json()


if __name__ == '__main__':
	main()