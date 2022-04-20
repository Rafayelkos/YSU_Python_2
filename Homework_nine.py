import cv2 as cv
import numpy as np
import copy


# Problem 1.

# img_1 = cv.imread('practical_homework\pic1.jpg')
# img_2 = cv.imread('practical_homework\pic2.jpg')
# img_3 = cv.imread('practical_homework\pic3.jpg')


# cv.imshow('Food', img_3)
# cv.imshow('Dog', img_2)
# cv.imshow('City', img_1)
# cv.waitKey(4000)

#Problem 2.
# my_video_1 = cv.VideoCapture(0)
# my_video = cv.VideoCapture('Videos/vid1.mp4')
# if (my_video_1.isOpened()== False):
#   print("Error opening video stream or file")

# while my_video.isOpened():
#     bool_var, frame = my_video.read()
#     bool_var_1, frame_1=my_video_1.read()
#     if bool_var & bool_var_1:
#         cv.imshow('Frame', frame)
#         cv.imshow('Frame_1', frame_1)
#         if  cv.waitKey(20)  & 0xFF == ord('q'): 
#             break
       
#     else:
#        break
# my_video.release()

# my_video.destroyALLWindows()

#Problem 3.
# def rescale(frame, scale_1 = 1.8, scale_2 = 1.8):
#     width = int(frame.shape[1]*scale_1)
#     height = int(frame.shape[0]*scale_2)
#     dimensions = (width, height)
#     return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# img = cv.imread('practical_homework\pic1.jpg')   

# img_rescale = rescale(img)



# cv.imshow('City_rescaled',img_rescale)
# cv.waitKey(0)

#Problem 4


   
# cap = VideoCapture('practical_homework/vid1.mp4')
# fourcc = cv.VideoWriter_fourcc(*'XVID')
# out = cv.VideoWriter('Output_video.avi',fourcc, 5, (1280,720))
  
# while True:
#     frame_loaded, frame = cap.read()
#     if frame_loaded == True:
#         frame_rescaled = cv.resize(frame, (1280,720), fx =0, fy =0, interpolation=cv.INTER_CUBIC)
#         cv.imshow('Video', frame)
#         cv.imshow('Video_rescaled', frame_rescaled)
#         out.write(frame_rescaled)
#     else:
#         break

#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break

# cap.release()
# cv.destroyAllWindows() 
 

#Problem 5.
    
# img = cv.imread('practical_homework/pic2.jpg')
# print(img.shape)
# cv.imshow('DOG', img)

# newimg = cv.circle(img, center=(317,320), radius = 80, color =(0, 0, 255), thickness = 2)
# cv.imshow('DOF_Circle', newimg)


# cv.waitKey(0)

# Problem 6
# img = cv.imread('practical_homework/pic2.jpg')
# print(img.shape)
# cv.imshow('DOG', img)

# cv.rectangle(img, (600,500),(300,30),(0,255,0),thickness=2)
# cv.imshow('rectangle_DOG', img)
# cv.waitKey(0)

# Problem 7
img = cv.imread('practical_homework/pic1.jpg')
print(img.shape)
#cv.imshow('City', img)
cv.line(img, (0,400), (1024, 0),(300, 255, 50), thickness = 5)
cv.imshow('New_City', img)
cv.waitKey(0)