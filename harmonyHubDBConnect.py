import mariadb
from PIL import Image
import os
from io import BytesIO

user = "root"
password = "vLCXoX2qkN>qw8KP,kS}E>}qUcon9V!3"
host = "127.0.0.1"
port = 3307
database = "harm"

directory = 'images'
if not os.path.exists(directory):
    os.makedirs(directory)

try:
    conn = mariadb.connect(
        user="root",
        password="vLCXoX2qkN>qw8KP,kS}E>}qUcon9V!3",
        host="127.0.0.1",
        port=3307,
        database="harm"
    )
except mariadb.Error as e:
    print(f"Error connecting to the database: {e}")

cur = conn.cursor()

def insert_image(image_data, image_type, image_size, image_ctgy, image_name):
    try:
        cur.execute("INSERT INTO image (image_type, image, image_size, image_ctgy, image_name) VALUES (?, ?, ?, ?, ?)",
                    (image_type, mariadb.Binary(image_data), image_size, image_ctgy, image_name))
        conn.commit()
        print("Image inserted successfully!")
    except mariadb.Error as e:
        print(f"Error inserting image into the database: {e}")

def read_image_from_database(image_name):
    try:
        cur.execute("SELECT image, image_name FROM image WHERE image_name=?", (image_name,))
        image_data, image_name = cur.fetchone()
        image = Image.open(BytesIO(image_data))
        return image, image_name
    except mariadb.Error as e:
        print(f"Error reading image from the database: {e}")

def save_image(image, image_name):
    filename = os.path.join(directory, f"{image_name}.jpg")
    image.save(filename)  # Збереження зображення у вигляді файлу
    print(f"Image saved as {filename}")

# Шлях до зображення
image_path = "images/default_photo.jpg"
image_type = "jpg"
image_size = "5"
image_ctgy = "photo"
image_name = "defoult_photo"

#with open(image_path, 'rb') as f:
 #   image_data = f.read()

#insert_image(image_data, image_type, image_size, image_ctgy, image_name)
image, image_name = read_image_from_database(image_name)
save_image(image, image_name)

