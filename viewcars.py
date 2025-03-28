from connection import get_connection

def view_cars():
    connection = get_connection()
    cursor = connection.cursor()
    sql = "SELECT * FROM cars"
    cursor.execute(sql)
    cars = cursor.fetchall()

    if cars:
        print("List of Cars")
        for car in cars:
            print(f"Id: {car[0]},model: {car[1]}, year: {car[2]}, color {car[3]}")
    else:
        print("There is no cars.")
    cursor.close()
    connection.close()

view_cars()