
import sqlite3


sql_create_database = """
create table if not exists visits (
	teleg_id text primary key,
	teleg_name text not null,
	visit_data text not null);
delete from visits;
insert into visits (teleg_id, teleg_name, visit_data)
values
	('11111', 'qqqqq', date('now', '-2 day')),
	('222', 'wwwww', date('now', '-1 day')),
	('3333', 'eeee', date('now'));
create table if not exists anek (txt text);
delete from anek;
insert into anek (txt)
values
	('\U0001F4A5 Если у 5 человек рядом с вами такие же сапоги - это не мода. Это армия.'),
	('\U0001F608 Себя не обманешь, но попытки продолжаются.'),
	('\U0001F6BD Недавно прочитал слово унитаз наоборот, теперь боюсь на него сесть.'),
	('\U00002668 Купила успокоительный чай, а меня бесит его запах и вкус.'),
	('\U0001F3E6 Успешная международная корпорация ищет менеджера со своей клиентской базой.'),
	('\U0001F494 Ненавижу тебя настолько, что печатаю тебе это только средним пальцем.'),
	('\U0001F4F1 Отсутствие айфона - высшая форма аскетизма.'),
	('\U0001F4F1 Розыгрыш бесплатного айфона оказался розыгрышем.'),
	('\U0001F620 Не надо все понимать. Люди, которые все понимают, целыми днями злятся.'),
	('\U0001F9A5 Мы просыпаемся вместе. Я и моя лень.'),
	('\U0001F482 Плох тот генерал, который не перестал быть солдафоном.'),
	('\U0001F37A Если ты пьяный, то это еще не повод не выпить.'),
	('\U0001F6CB Если не можешь усидеть на двух стульях, приляг на диванчик.'),
	('\U0001F6CC Смирись с неизбежным. Тебе не выспаться.'),
	('\U0001F525 От зависти не умирают, от зависти убивают.'),
	('\U0001F442 Ван Гог не обращал внимания на критику, точнее слушал ее вполуха.'),
	('\U0001F92F Голова легкой должна быть. Чем меньше знаний, тем крепче убеждения.'),
	('- Изя, ты оказался не тем, чем я думала...\n- Сара, а чем ты таки думала?\n\U0001F970'),
	('\U0001F64A Все, что не делается, я и не делаю.'),
	('\U0001F9D0 Самый лучший понедельник - это тот, который выходной.'),
	('\U0001F354 Полезное от приятного отличается отвратительным вкусом.');
"""

sql = {
		# рандомный анекдот
		'anek': "select txt from anek order by random() limit 1;",
		# 10 последних визитеров
		'visits':	"select * from visits order by visit_data desc limit 10;",
  		'upd_vis':	"insert into visits (teleg_id, teleg_name, visit_data) \
						values ('{0}', '{1}', '{2}')\
						on conflict (teleg_id)\
						do update set visit_data='{2}';",
  		}


def exec_sql(key_sql, **kvargs):
	sb_con = sqlite3.connect("SergeichBot.db")
	sb_cur = sb_con.cursor()

	while True:
		try:
			query = sql[key_sql]
			if 'upd_vis' in key_sql:
				query = sql[key_sql].format(kvargs['teleg_id'], kvargs['teleg_name'], kvargs['visit_data'])
			else:
				query = sql[key_sql]
			print(query)
			sb_cur.execute(query)
			break
		except sqlite3.DatabaseError as err:
			if 'no such table:' in str(err):
				# создаем все таблицы базы данных
				try:
					sb_cur.executescript(sql_create_database)
				except sqlite3.DatabaseError as err:
					print("Ошибка", err)
			else:
				print("Ошибка", err)
	sb_con.commit()

	res = [s for s in sb_cur]

	sb_cur.close()
	sb_con.close()

	return res

if __name__  == "__main__":
#	print(exec_sql('anek'))
#	print(exec_sql('visits'))
	print(exec_sql('upd_vis', teleg_id = '5555555', teleg_name = '2', visit_data = "3"))
	print(exec_sql('visits'))
