# import cv2
# import numpy as np

# from PIL import Image
# import os

# recognizer = cv2.face.LBPHFaceRecognizer()
# path="datasets"

# def getimageID(path):
#     imagepath=[os.path.join(path,f) for f in os.listdir(path)]

#     faces=[]
#     ids=[]
#     for imagepaths in imagepath:
#         faceImage=Image.open(imagepaths).convert("L")    
#         faceNP=np.array(faceImage )
#         ID=(os.path.split(imagepaths)[-1].split(".")[1])
#         faces.append(faceNP)
#         ids.append(ID)
#         cv2.imshow("Training",faceNP)
#         cv2.waitKey(1)

#     return ids, faces

# IDs, facedata = getimageID(path)
# recognizer.train(facedata, np.array(IDs))
# recognizer.write("Trainer.yml")
# cv2.destroyAllWindows()
# print("training is completed--------->")
import cv2
import numpy as np
from PIL import Image
import os

recognizer = cv2.face.LBPHFaceRecognizer_create()

path="datasets"

def getImageID(path):
    imagePath = [os.path.join(path, f) for f in os.listdir(path)]
    faces=[]
    ids=[]
    for imagePaths in imagePath:
        faceImage = Image.open(imagePaths).convert('L')
        faceNP = np.array(faceImage)
        Id= (os.path.split(imagePaths)[-1].split(".")[1])
        Id=int(Id)
        faces.append(faceNP)
        ids.append(Id)
        cv2.imshow("Training",faceNP)
        cv2.waitKey(1)
    return ids, faces

IDs, facedata = getImageID(path)
recognizer.train(facedata, np.array(IDs))
recognizer.write("Trainer.yml")
cv2.destroyAllWindows()
print("Training Completed............")