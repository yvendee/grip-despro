import mysql.connector

def read_all_data():
    result = []  # List to store the fetched data
    try:
        # Database connection parameters
        host = "localhost"
        user = "root"
        password = ""
        database = "gripdespro"

        # Establishing the connection to MySQL
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        if not connection.is_connected():
            print("Connection failed")

        else:
            # Creating a cursor object using the cursor() method
            cursor = connection.cursor()

            # SQL query to select all data from the "grip_active" table
            select_query = "SELECT * FROM grip_active"

            # Execute the SQL query
            cursor.execute(select_query)

            # Fetch the first row
            row = cursor.fetchone()

            # If a row is fetched, append it to the result list
            if row:
                result.append(list(row))

    except mysql.connector.Error as error:
        print("Error reading data:", error)

    finally:
        # Closing the connection
        if connection.is_connected():
            cursor.close()
            connection.close()
    
    return result


data = read_all_data()



# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


value_to_pass = data[0][1]

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


# OUTPUT_PATH = Path(__file__).parent
# ASSETS_PATH = OUTPUT_PATH / Path(r"D:\GRIP Despro\Main Frame\build\assets\frame0")

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame0"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("900x600")
window.geometry("+10+10") ## Kayven added x,y
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 600,
    width = 900,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    450.0,
    300.0,
    image=image_image_1
)

canvas.create_text(
    55.0,
    257.0,
    anchor="nw",
    text=value_to_pass,
    fill="#000000",
    font=("Inter", 45 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [print("button_1 clicked"), window.destroy()],
    relief="flat"
)
button_1.place(
    x=108.0,
    y=441.0,
    width=148.0,
    height=36.834197998046875
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [print("button_2 clicked"), window.destroy()],
    relief="flat"
)
button_2.place(
    x=275.0,
    y=441.0,
    width=148.0,
    height=36.834197998046875
)
window.resizable(False, False)
window.mainloop()
