from os import name
import face_recognition
import os
from PIL import Image, ImageDraw
from face_recognition.api import face_encodings, face_locations
import tkinter as tk
from tkinter.filedialog import askopenfilename


known_face_encodings = []
known_face_names = []

for person in os.listdir(r"C:\Users\qcraddock\Desktop\Projects\Pi\tpi-marauders-map-pi\FacesRecog\known_faces"):
    loaded_image = face_recognition.load_image_file(rf"C:\Users\qcraddock\Desktop\Projects\Pi\tpi-marauders-map-pi\FacesRecog\known_faces\{person}")
    imageEncode = face_recognition.face_encodings(loaded_image)[0]

    known_face_encodings.append(imageEncode)
    known_face_names.append(person)

fn = askopenfilename()
print("user chose", fn)

Unkown_Image = face_recognition.load_image_file(rf"{fn}")

face_locations = face_recognition.face_locations(Unkown_Image)
face_encodings = face_recognition.face_encodings(Unkown_Image, face_locations)

pil_image = Image.fromarray(Unkown_Image)

draw= ImageDraw.Draw(pil_image)

for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

    name = 'Unknown Person'

    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]
    
    draw.rectangle(((left, top), (right, top)), outline=(0,0,0))

    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10), (right,bottom)), fill=(0,0,0), outline=(0,0,0))

    draw.text((left + 6, bottom - text_height-5), name, fill =(255,255,255))

del draw

pil_image.show()

