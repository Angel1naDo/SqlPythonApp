from connection import get_connection
def delete_car(car_id):
    connection = get_connection()
    cursor = connection.cursor()
    sql = "DELETE FROM cars WHERE id = %s"
    cursor.execute(sql, (car_id,))
    connection.commit()

    if cursor.rowcount > 0:
        print("Deleted")
    else:
        print("Not Found")

    cursor.close()
    connection.close()

    try:
        car_id + int(input("Insert ID: "))
        delete_car(car_id)

    except ValueError:
        print("Not valid ID")
