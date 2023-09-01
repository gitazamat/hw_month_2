import sqlite3

conn = sqlite3.connect('company.db')
cursor = conn.cursor()

cursor.execute("SELECT id, title FROM cities")
cities = cursor.fetchall()

print(
    "Вы можете отобразить список сотрудников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")
for city in cities:
    print(f"{city[0]}. {city[1]}")

selected_city_id = int(input("Введите id города: "))

if selected_city_id == 0:
    conn.close()
else:
    cursor.execute("""
        SELECT e.first_name, e.last_name, c.title AS city, c.area, co.title AS country
        FROM employees e
        JOIN cities c ON e.city_id = c.id
        JOIN countries co ON c.country_id = co.id
        WHERE c.id = ?
    """, (selected_city_id,))

    employees = cursor.fetchall()

    print(f"Сотрудники, проживающие в выбранном городе:")
    for employee in employees:
        print(
            f"Имя: {employee[0]}, Фамилия: {employee[1]}, Город: {employee[2]}, Площадь города: {employee[3]}, Страна: {employee[4]}")

    conn.close()
