#!/usr/bin/env python
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image as im
import cairo 
import math
import rospy
from nav_msgs.msg import *
from std_msgs.msg import *

# pass in numpy array into a function to convert to occupancy grid
def main(array_np):
    # create numpy array from scratch for now --> but array will actually be the output of a neural net
    array = np.zeros((200, 200, 4), dtype = np.uint8)
    surface = cairo.ImageSurface.create_for_data(
        array, cairo.FORMAT_ARGB32, 200, 200)

    cr = cairo.Context(surface)

    # fill with solid white
    cr.set_source_rgb(1.0,1.0, 1.0)
    cr.paint()

    # draw black circle
    cr.arc(100, 100, 25, 0, 2 *math.pi)
    cr.set_line_width(3)
    cr.set_source_rgb(0.0, 0.0, .00)
    cr.fill()

    # array will be black circle on white background

    print(array.shape)

    # reshape array into familiar resolution
    array = np.reshape(array, (800, 200))

    # show shape of array
    print(array.shape)
    print(array)

    # creating image from array
    data = im.fromarray(array)
    # saving image as png file
    data.save('image.png')

    # converted simple numpy array into an image --> now convert image into occupancy grid
    image_gray = cv.imread('image.png', cv.IMREAD_GRAYSCALE)
    # size = 0
    # image_bw = np.zeros(size, dtype=np.uint8)
    # cv.threshold(image_gray, image_bw, 127, 255, cv.THRESH_BINARY)
    cv.imwrite("output.pgm", image_gray)
    # write result to text file for debugging purposes
    # 255 is white pixels
    # 0 is black pixels
    file = cv.FileStorage("output.yaml", cv.FILE_STORAGE_WRITE)
    file.write('img', image_gray)
    file.release()

    # possibly converted into occupancy grid --> not sure because image thresholding function does not work 
    # output.pgm contains the occupancy grid


    # trying to publish occupancy grid that was just created
   
    # pub = rospy.Publisher('/costmap_topic', OccupancyGrid, queue_size = 10)
    # rospy.init_node('occupancygrid', anonymous = True)
    # grid_img = cv.imread('output.pgm', 0)

    # for i in range(len(grid_img)):
    #     grid_img[i] = (grid_img[i] / 255) * 100

    # grid.data = grid_img

    # r = rospy.Rate(10)
    # while not rospy.is_shutdown():
    #     pub.publish(grid)
    #     r.sleep()
 

    


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass