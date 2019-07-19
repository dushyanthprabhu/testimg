import face_recognition
from PIL import Image, ImageDraw
import cv2
import os
import numpy
known_face_encodings = []
kfe=[]
def faceencoding():

    for path,subdir,fname in os.walk(directory):
        print(path,subdir,fname)
        for f in fname:
            #name=os.path.basename(path)
            print(f)
            img_path=os.path.join(path,f)
            img = face_recognition.load_image_file(img_path)
            face_encoding = face_recognition.face_encodings(img)[0]
            known_face_encodings.append(face_encoding)
        return  known_face_encodings
    '''image_of_bill = face_recognition.load_image_file('./img/new/1.jpeg')
    bill_face_encoding = face_recognition.face_encodings(image_of_bill)[0]

    image_of_steve = face_recognition.load_image_file('./img/new/2.jpeg')
    steve_face_encoding = face_recognition.face_encodings(image_of_steve)[0]

    image_of_elon = face_recognition.load_image_file('./img/new/5.jpeg')
    elon_face_encoding = face_recognition.face_encodings(image_of_elon)[0]

    #  Create arrays of encodings and names
    known_face_encodings = [
      bill_face_encoding,
      steve_face_encoding,
      elon_face_encoding
    ]'''


known_face_names = [
  "M",
  "v",
  "R"
]
directory="C:/Users/asus/Desktop/face_recognition_examples-master/img/new"
cam=cv2.VideoCapture(0)
while True:
    rect,test_image=cam.read()
    cv2.imshow('HI',test_image)
    image= Image.fromarray(test_image)
    # Find faces in test image
    #image = face_recognition.load_image_file("C:/Users/asus/AppData/Local/Programs/Python/Python36/data/Reona/4.jpeg")
    image = face_recognition.load_image_file(test_image,mode='RGB')
    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)

    # Convert to PIL format
    pil_image = Image.fromarray(image)

    # Create a ImageDraw instance
    draw = ImageDraw.Draw(pil_image)

    kfe=faceencoding()
    '''for path,subdir,fname in os.walk(directory):
        for f in fname:
            #name=os.path.basename(path)
            img_path=os.path.join(path,f)
            img = face_recognition.load_image_file(img_path)
            #pil_image = Image.fromarray(img)
            #pil_image.show()'''
    print(kfe)
    for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(kfe, face_encoding)

        name = "Unknown Person"
        print(matches)
        # If match
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
                  
        # Draw box
        draw.rectangle(((left, top), (right, bottom)), outline=(255,255,0))

        # Draw label
        text_width, text_height = draw.textsize(name)
        draw.rectangle(((left,bottom - text_height - 10), (right, bottom)), fill=(255,255,0), outline=(255,255,0))
        draw.text((left + 6, bottom - text_height - 5), name, fill=(0,0,0))

    del draw

    pil_image.show()
    break
        # Save image
        #pil_image.save('identify.jpg')
cam.release()
