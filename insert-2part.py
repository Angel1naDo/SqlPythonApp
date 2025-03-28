from connection import get_connection

def insert_car(model, year, color):
    connection = get_connection()
    cursor = connection.cursor()
    sql = "INSERT INTO cars (model, year, color) VALUES (%s, %s, %s)"
    values = (model, year, color)
    cursor.execute(sql, values)
    connection.commit()
    print("Car added.")
    cursor.close()
    connection.close()

model = input("Car model: ")
year = int(input("Manufacture year: "))
color = input("Color of your car: ")

insert_car(model, year, color)