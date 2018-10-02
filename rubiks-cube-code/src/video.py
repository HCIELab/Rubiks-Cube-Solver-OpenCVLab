#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## Import the relevant files
from sys import exit as Die
try:
    import sys
    import cv2
    import numpy as np
    from colordetection import ColorDetector
except ImportError as err:
    Die(err)

'''
Testing variable
set to false to start task 2 & 3
'''
cameratesting = True 

'''
Initialize the camera here
'''
cam_port         = None # your code here task 1.1
cam              = None # your code here task 1.1



"""
    We are going to want to draw some stickers. In the solution
    we have 3 sets of stickers. Each set has 9 stickers to represent
    each sticker on any given face of the rubik's cube.

    The 'stickers' set of stickers are physical markers used to help the
    user see where to place the cube for color scanning.

    The 'current_stickers' set show which colors are currently being detected 
    for each position on the face.

    The 'preview_stickers' set shows the most recently recorded face.
    You can rescan a face if the preview does not match the actual colors
    on the face of the rubik's cube.

    These are the coordinates of each sticker for each set. Feel free to play
    with these values if you don't like the sticker placement.

    *note shorten split
"""
detector_stickers = [[200, 120], [300, 120], [400, 120],
                   [200, 220], [300, 220], [400, 220],
                   [200, 320], [300, 320], [400, 320]]

current_stickers = [[20, 20], [54, 20], [88, 20],
                   [20, 54], [54, 54], [88, 54],
                   [20, 88], [54, 88], [88, 88]]

recorded_stickers = [[20, 130], [54, 130], [88, 130],
                   [20, 164], [54, 164], [88, 164],
                   [20, 198], [54, 198], [88, 198]]


def draw_detector_stickers(frame):
    """Draws the 9 stickers in the frame."""
    pass
    # your code here task 2.1

def draw_current_stickers(frame, state):
    """Draws the 9 current stickers in the frame."""
    pass
    # your code here task 2.2

def draw_recorded_stickers(frame, state):
    """Draws the 9 preview stickers in the frame."""
    pass
    # your code here task 2.3

def color_to_notation(color):
    """
    Helper function for converting colors to notation
    used by solver.
    """
    notation = {
        'green'  : 'F',
        'white'  : 'U',
        'blue'   : 'B',
        'red'    : 'R',
        'orange' : 'L',
        'yellow' : 'D'
    }
    return notation[color]

def empty_callaback(x):
    '''
    Empty function for callback when slider positions change. Need input x, this is the value 
    the slider has changed to. You don't need to do anything in this function.
    '''
    pass

def scan():
    """
    Open up the webcam and scans the 9 regions in the center
    and show a preview.

    After hitting the space bar to confirm, the block below the
    current stickers shows the current state that you have.
    This is show every user can see what the computer took as input.

    :returns: dictionary
    """

    sides   = {}                            # collection of scanned sides
    preview = ['white','white','white',     # default starting preview sticker colors
               'white','white','white',
               'white','white','white']
    state   = [0,0,0,                       # current sticker colors
               0,0,0,
               0,0,0]

    defaultcal = {                          # default color calibration
                'white':[[161,67,255],[0,0,102]],
                'green':[[102,255,184],[63,85,39]],
                'red':[[172,214,220],[13,156,86]],
                'orange':[[172,255,255],[7,136,148]],
                'yellow':[[43,172,235],[23,20,52]],
                'blue':[[118,255,194],[89,178,51]]
                }

    colorcal  = {}                          # color calibration dictionary
    color = ['white', 'green', 'red', 'orange', 'yellow', 'blue']  # list of valid colors            
    
    # create trackbars here
    cv2.createTrackbar('H Upper',"default",defaultcal[color[len(colorcal)]][0][0],179, empty_callaback)
    cv2.createTrackbar('H Lower',"default",defaultcal[color[len(colorcal)]][0][1],179, empty_callaback)

    colorcal = defaultcal

    while cameratesting:
        '''
        Here we want to make sure things are working and learn about how to use some openCV functions
        Your code here
        '''
        #task 1.2 preview a camera window
        #task 1.3 draw a rectangle
        #task 1.4 make a slider
        #task 1.5 add text
        #task 1.6 make a mask based on hsv
        #task 1.7 display the masked image


    while not cameratesting:
        _, frame = None # your code here
        hsv = None      # your code here
        key = None      # your code here

        # init certain stickers.
        draw_detector_stickers(frame)
        draw_recorded_stickers(frame, preview)

        for index,(x,y) in enumerate(detector_stickers):
            roi          = hsv[y:y+32, x:x+32]              # extracts hsv values within sticker
            avg_hsv      = ColorDetector.median_hsv(roi)    # filters the hsv values into one hsv
            color_name   = ColorDetector.get_color_name(avg_hsv,colorcal) # extracts the color based on hsv
            state[index] = color_name                       # stores the color 

            # update when space bar is pressed.
            if key == 32:
                preview = list(state)
                draw_recorded_stickers(frame, state)         # draw the saved colors on the preview
                face = color_to_notation(state[4])          # convert the color to notation of the middle sticker and label this as the face
                notation = [color_to_notation(color) for color in state] # convert all colors to notation
                sides[face] = notation                      # update the face in the sides dictionary

        # show the new stickers
        draw_current_stickers(frame, state)                 # draw live sampling of face colors

        # append amount of scanned sides
        text = 'scanned sides: {}/6'.format(len(sides))
        cv2.putText(frame, text, (20, 460), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (255,255,255), 1, cv2.LINE_AA)
        
        # indicate the scanning instruction
        textInstruction = 'scan and rotate the cube with white on the top and green on the front (towards camera)'
        textInstruction2 = 'the color of center brick is used as the side identifier (since the center brick does not move)'
        textInstruction3 = 'you can scan as many times as you want'
        textInstruction4 = 'the program will overwrite the old scan when same side is detected'
        cv2.putText(frame, textInstruction, (20, 600), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (255,255,255), 1, cv2.LINE_AA)
        cv2.putText(frame, textInstruction2, (20, 620), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (255,255,255), 1, cv2.LINE_AA)
        cv2.putText(frame, textInstruction3, (20, 640), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (255,255,255), 1, cv2.LINE_AA)
        cv2.putText(frame, textInstruction4, (20, 660), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (255,255,255), 1, cv2.LINE_AA)

        # quit on escape.
        if key == 27:
            break

        # show result
        cv2.imshow("default", frame)

        if key == 99: 
            colorcal = {}   
            while len(colorcal) < 6:
                _, frame = cam.read()
                
                
                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                key = cv2.waitKey(10) & 0xff

                # hue upper lower
                hu = cv2.getTrackbarPos('H Upper','default')
                su = cv2.getTrackbarPos('H Lower','default')
                # saturation upper lower
                su = None # yourcode here
                sl = None # yourcode here
                # value upper lower
                vu = None # yourcode here
                vl = None # yourcode here

                if color[len(colorcal)] == 'red' or color[len(colorcal)] == 'orange':
                    lower_hsv = np.array([0,sl,vl])
                    upper_hsv = np.array([hl,su,vu])
                    mask1 = cv2.inRange(hsv, lower_hsv, upper_hsv)
                    lower_hsv = np.array([hu,sl,vl])
                    upper_hsv = np.array([179,su,vu])
                    mask2 = cv2.inRange(hsv, lower_hsv, upper_hsv)
                    mask = cv2.bitwise_or(mask1, mask2)
                    res = cv2.bitwise_and(frame,frame, mask= mask)
                    lower_hsv = np.array([hl,sl,vl])
                    upper_hsv = np.array([hu,su,vu])
                else:
                    lower_hsv = np.array([hl,sl,vl])
                    upper_hsv = np.array([hu,su,vu])
                    
                    # Task 3
                    mask = None # your code here
                    res = None # your code here
                
                if key == 32:
                    defaultcal[color[len(colorcal)]] = [upper_hsv,lower_hsv]
                    colorcal[color[len(colorcal)]] = [upper_hsv,lower_hsv]

                    if(len(colorcal) < 6):
                        cv2.setTrackbarPos('H Upper','default',defaultcal[color[len(colorcal)]][0][0])
                        cv2.setTrackbarPos('S Upper','default',defaultcal[color[len(colorcal)]][0][1])
                        cv2.setTrackbarPos('V Upper','default',defaultcal[color[len(colorcal)]][0][2])
                        cv2.setTrackbarPos('H Lower','default',defaultcal[color[len(colorcal)]][1][0])
                        cv2.setTrackbarPos('S Lower','default',defaultcal[color[len(colorcal)]][1][1])
                        cv2.setTrackbarPos('V Lower','default',defaultcal[color[len(colorcal)]][1][2])

                if(len(colorcal) < 6):
                    text = 'calibrating {}'.format(color[len(colorcal)])
                cv2.putText(res, text, (20, 460), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (255,255,255), 1, cv2.LINE_AA)

                cv2.imshow("default", res)
                # quit on escape key.
                if key == 27:
                    break

    cam.release()
    cv2.destroyAllWindows()
    return sides if len(sides) == 6 else False


