#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on April 17, 2022, at 21:15
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'untitled'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='D:\\padhai\\2.Courses\\UGP\\Experiments\\original - Copy (2)\\foragingnew_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "intro"
introClock = core.Clock()
introtext = visual.TextStim(win=win, name='introtext',
    text='Hey there! This is the basic foraging task. \nRules:\n1. Click on the circle at the bottom center to start the game\n2.  Click of the patch adjacent to the circle to collect the reward\n3. Click the space bar to move forward to the next patch. \nYour goal is to maximise your reward in the given time\nGoodluck!',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
mouse_5 = event.Mouse(win=win)
x, y = [None, None]
mouse_5.mouseClock = core.Clock()

# Initialize components for Routine "bound_3"
bound_3Clock = core.Clock()

# Initialize components for Routine "random_seed"
random_seedClock = core.Clock()

# Initialize components for Routine "rewardframe1_3"
rewardframe1_3Clock = core.Clock()
tree1_18 = visual.ImageStim(
    win=win,
    name='tree1_18', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
tree2_18 = visual.ImageStim(
    win=win,
    name='tree2_18', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
tree3_18 = visual.ImageStim(
    win=win,
    name='tree3_18', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
tree4_18 = visual.ImageStim(
    win=win,
    name='tree4_18', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
circle1 = visual.ImageStim(
    win=win,
    name='circle1', 
    image='images/hollow.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
forward_11 = visual.ImageStim(
    win=win,
    name='forward_11', 
    image='images/arrow.png', mask=None,
    ori=0, pos=(0.5, -0.2), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
squaree_3 = visual.ImageStim(
    win=win,
    name='squaree_3', 
    image='images/square.png', mask=None,
    ori=0, pos=(0.5, -0.2), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
mouse_3 = event.Mouse(win=win)
x, y = [None, None]
mouse_3.mouseClock = core.Clock()

# Initialize components for Routine "rewardframe1_2"
rewardframe1_2Clock = core.Clock()
tree1_12 = visual.ImageStim(
    win=win,
    name='tree1_12', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
tree2_12 = visual.ImageStim(
    win=win,
    name='tree2_12', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
tree3_12 = visual.ImageStim(
    win=win,
    name='tree3_12', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
tree4_12 = visual.ImageStim(
    win=win,
    name='tree4_12', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
circle2 = visual.ImageStim(
    win=win,
    name='circle2', 
    image='images/hollow.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
wait_3 = visual.TextStim(win=win, name='wait_3',
    text='',
    font='Arial',
    pos=(-0.6, -0.08), height=0.02, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
forward_2 = visual.ImageStim(
    win=win,
    name='forward_2', 
    image='images/arrow.png', mask=None,
    ori=0, pos=(0.5, -0.2), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
squaree_2 = visual.ImageStim(
    win=win,
    name='squaree_2', 
    image='images/square.png', mask=None,
    ori=0, pos=(0.5, -0.2), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
gcircle = visual.ImageStim(
    win=win,
    name='gcircle', 
    image='images/gcircle.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)

# Initialize components for Routine "rewardframe1"
rewardframe1Clock = core.Clock()
tree1_4 = visual.ImageStim(
    win=win,
    name='tree1_4', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
tree2_4 = visual.ImageStim(
    win=win,
    name='tree2_4', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
tree3_4 = visual.ImageStim(
    win=win,
    name='tree3_4', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
tree4_4 = visual.ImageStim(
    win=win,
    name='tree4_4', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
circle3 = visual.ImageStim(
    win=win,
    name='circle3', 
    image='images/hollow.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
reward_2 = visual.TextStim(win=win, name='reward_2',
    text=None,
    font='Arial',
    pos=(-0.6, -0.08), height=0.05, wrapWidth=None, ori=0, 
    color='green', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
resp = event.Mouse(win=win)
x, y = [None, None]
resp.mouseClock = core.Clock()
forward = visual.ImageStim(
    win=win,
    name='forward', 
    image='images/arrow.png', mask=None,
    ori=0, pos=(0.5, -0.2), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
key_resp = keyboard.Keyboard()
sol = event.Mouse(win=win)
x, y = [None, None]
sol.mouseClock = core.Clock()
gcircle_2 = visual.ImageStim(
    win=win,
    name='gcircle_2', 
    image='images/gcircle.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.12, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
skipsq = visual.ImageStim(
    win=win,
    name='skipsq', 
    image='images/square.png', mask=None,
    ori=0, pos=(0.5, -0.2), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)

# Initialize components for Routine "rewardframe1_4"
rewardframe1_4Clock = core.Clock()
tree1_19 = visual.ImageStim(
    win=win,
    name='tree1_19', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
tree2_19 = visual.ImageStim(
    win=win,
    name='tree2_19', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
tree3_19 = visual.ImageStim(
    win=win,
    name='tree3_19', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
tree4_19 = visual.ImageStim(
    win=win,
    name='tree4_19', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
circle4 = visual.ImageStim(
    win=win,
    name='circle4', 
    image='images/hollow.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
wait_8 = visual.TextStim(win=win, name='wait_8',
    text='',
    font='Arial',
    pos=(0, -0.08), height=0.02, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
forward_12 = visual.ImageStim(
    win=win,
    name='forward_12', 
    image='images/arrow.png', mask=None,
    ori=0, pos=(0.5, -0.2), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
squaree_4 = visual.ImageStim(
    win=win,
    name='squaree_4', 
    image='images/square.png', mask=None,
    ori=0, pos=(0.5, -0.2), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
gcircle_3 = visual.ImageStim(
    win=win,
    name='gcircle_3', 
    image='images/gcircle.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
reward_7 = visual.TextStim(win=win, name='reward_7',
    text='',
    font='Arial',
    pos=(-0.6, -0.08), height=0.05, wrapWidth=None, ori=0, 
    color='green', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);
gcircle_4 = visual.ImageStim(
    win=win,
    name='gcircle_4', 
    image='images/gcircle.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.12, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-12.0)

# Initialize components for Routine "movetrees"
movetreesClock = core.Clock()
tree1_6 = visual.ImageStim(
    win=win,
    name='tree1_6', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
tree2_6 = visual.ImageStim(
    win=win,
    name='tree2_6', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
tree3_6 = visual.ImageStim(
    win=win,
    name='tree3_6', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
tree4_6 = visual.ImageStim(
    win=win,
    name='tree4_6', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
circle5 = visual.ImageStim(
    win=win,
    name='circle5', 
    image='images/hollow.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)

# Initialize components for Routine "random_seed_1"
random_seed_1Clock = core.Clock()

# Initialize components for Routine "rewardframe2_3"
rewardframe2_3Clock = core.Clock()
tree1_20 = visual.ImageStim(
    win=win,
    name='tree1_20', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
tree2_20 = visual.ImageStim(
    win=win,
    name='tree2_20', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
tree3_20 = visual.ImageStim(
    win=win,
    name='tree3_20', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
tree4_20 = visual.ImageStim(
    win=win,
    name='tree4_20', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
circle = visual.ImageStim(
    win=win,
    name='circle', 
    image='images/hollow.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
forward_13 = visual.ImageStim(
    win=win,
    name='forward_13', 
    image='images/arrow.png', mask=None,
    ori=0, pos=(-0.5, -0.2), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
square1 = visual.ImageStim(
    win=win,
    name='square1', 
    image='images/square.png', mask=None,
    ori=0.0, pos=(-0.5, -0.2), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
mouse_4 = event.Mouse(win=win)
x, y = [None, None]
mouse_4.mouseClock = core.Clock()

# Initialize components for Routine "rewardframe2_2"
rewardframe2_2Clock = core.Clock()
tree1_13 = visual.ImageStim(
    win=win,
    name='tree1_13', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
tree2_13 = visual.ImageStim(
    win=win,
    name='tree2_13', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
tree3_13 = visual.ImageStim(
    win=win,
    name='tree3_13', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
tree4_13 = visual.ImageStim(
    win=win,
    name='tree4_13', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
circle6 = visual.ImageStim(
    win=win,
    name='circle6', 
    image='images/hollow.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
wait = visual.TextStim(win=win, name='wait',
    text='',
    font='Arial',
    pos=(0.6, -0.08), height=0.02, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
forward_3 = visual.ImageStim(
    win=win,
    name='forward_3', 
    image='images/arrow.png', mask=None,
    ori=0, pos=(-0.5, -0.2), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)

# Initialize components for Routine "rewardframe2"
rewardframe2Clock = core.Clock()
tree1_5 = visual.ImageStim(
    win=win,
    name='tree1_5', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
tree2_5 = visual.ImageStim(
    win=win,
    name='tree2_5', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
tree3_5 = visual.ImageStim(
    win=win,
    name='tree3_5', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
tree4_5 = visual.ImageStim(
    win=win,
    name='tree4_5', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
circle_5 = visual.ImageStim(
    win=win,
    name='circle_5', 
    image='images/hollow.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
reward_3 = visual.TextStim(win=win, name='reward_3',
    text='',
    font='Arial',
    pos=(0.6, -0.08), height=0.05, wrapWidth=None, ori=0, 
    color='green', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
mouse_6 = event.Mouse(win=win)
x, y = [None, None]
mouse_6.mouseClock = core.Clock()
forward_7 = visual.ImageStim(
    win=win,
    name='forward_7', 
    image='images/arrow.png', mask=None,
    ori=0, pos=(-0.5, -0.2), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
sol_2 = event.Mouse(win=win)
x, y = [None, None]
sol_2.mouseClock = core.Clock()
gcircle_5 = visual.ImageStim(
    win=win,
    name='gcircle_5', 
    image='images/gcircle.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.12, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
skipsq_2 = visual.ImageStim(
    win=win,
    name='skipsq_2', 
    image='images/square.png', mask=None,
    ori=0, pos=(-0.5, -0.2), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)

# Initialize components for Routine "rewardframe2_4"
rewardframe2_4Clock = core.Clock()
tree1_21 = visual.ImageStim(
    win=win,
    name='tree1_21', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
tree2_21 = visual.ImageStim(
    win=win,
    name='tree2_21', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
tree3_21 = visual.ImageStim(
    win=win,
    name='tree3_21', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
tree4_21 = visual.ImageStim(
    win=win,
    name='tree4_21', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
wait1 = visual.TextStim(win=win, name='wait1',
    text='wait',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
forward_15 = visual.ImageStim(
    win=win,
    name='forward_15', 
    image='images/arrow.png', mask=None,
    ori=0, pos=(-0.5, -0.2), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
square5 = visual.ImageStim(
    win=win,
    name='square5', 
    image='images/square.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
gcircle1 = visual.ImageStim(
    win=win,
    name='gcircle1', 
    image='images/gcircle.png', mask=None,
    ori=0.0, pos=(0, -0.2), size=(0.12, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
reward_9 = visual.TextStim(win=win, name='reward_9',
    text='',
    font='Arial',
    pos=(0.6, -0.08), height=0.05, wrapWidth=None, ori=0, 
    color='green', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
circle_6 = visual.ImageStim(
    win=win,
    name='circle_6', 
    image='images/hollow.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)

# Initialize components for Routine "movetrees2"
movetrees2Clock = core.Clock()
tree1_22 = visual.ImageStim(
    win=win,
    name='tree1_22', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
tree2_22 = visual.ImageStim(
    win=win,
    name='tree2_22', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
tree3_22 = visual.ImageStim(
    win=win,
    name='tree3_22', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
tree4_22 = visual.ImageStim(
    win=win,
    name='tree4_22', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
circle5_2 = visual.ImageStim(
    win=win,
    name='circle5_2', 
    image='images/hollow.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)

# Initialize components for Routine "end"
endClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='The end~',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "random_seed"
random_seedClock = core.Clock()

# Initialize components for Routine "rewardframe1_3"
rewardframe1_3Clock = core.Clock()
tree1_18 = visual.ImageStim(
    win=win,
    name='tree1_18', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
tree2_18 = visual.ImageStim(
    win=win,
    name='tree2_18', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
tree3_18 = visual.ImageStim(
    win=win,
    name='tree3_18', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
tree4_18 = visual.ImageStim(
    win=win,
    name='tree4_18', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
circle1 = visual.ImageStim(
    win=win,
    name='circle1', 
    image='images/hollow.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
forward_11 = visual.ImageStim(
    win=win,
    name='forward_11', 
    image='images/arrow.png', mask=None,
    ori=0, pos=(0.5, -0.2), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
squaree_3 = visual.ImageStim(
    win=win,
    name='squaree_3', 
    image='images/square.png', mask=None,
    ori=0, pos=(0.5, -0.2), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
mouse_3 = event.Mouse(win=win)
x, y = [None, None]
mouse_3.mouseClock = core.Clock()

# Initialize components for Routine "rewardframe1_2"
rewardframe1_2Clock = core.Clock()
tree1_12 = visual.ImageStim(
    win=win,
    name='tree1_12', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
tree2_12 = visual.ImageStim(
    win=win,
    name='tree2_12', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
tree3_12 = visual.ImageStim(
    win=win,
    name='tree3_12', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
tree4_12 = visual.ImageStim(
    win=win,
    name='tree4_12', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
circle2 = visual.ImageStim(
    win=win,
    name='circle2', 
    image='images/hollow.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
wait_3 = visual.TextStim(win=win, name='wait_3',
    text='',
    font='Arial',
    pos=(-0.6, -0.08), height=0.02, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
forward_2 = visual.ImageStim(
    win=win,
    name='forward_2', 
    image='images/arrow.png', mask=None,
    ori=0, pos=(0.5, -0.2), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
squaree_2 = visual.ImageStim(
    win=win,
    name='squaree_2', 
    image='images/square.png', mask=None,
    ori=0, pos=(0.5, -0.2), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
gcircle = visual.ImageStim(
    win=win,
    name='gcircle', 
    image='images/gcircle.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)

# Initialize components for Routine "rewardframe1"
rewardframe1Clock = core.Clock()
tree1_4 = visual.ImageStim(
    win=win,
    name='tree1_4', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
tree2_4 = visual.ImageStim(
    win=win,
    name='tree2_4', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
tree3_4 = visual.ImageStim(
    win=win,
    name='tree3_4', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
tree4_4 = visual.ImageStim(
    win=win,
    name='tree4_4', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
circle3 = visual.ImageStim(
    win=win,
    name='circle3', 
    image='images/hollow.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
reward_2 = visual.TextStim(win=win, name='reward_2',
    text=None,
    font='Arial',
    pos=(-0.6, -0.08), height=0.05, wrapWidth=None, ori=0, 
    color='green', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
resp = event.Mouse(win=win)
x, y = [None, None]
resp.mouseClock = core.Clock()
forward = visual.ImageStim(
    win=win,
    name='forward', 
    image='images/arrow.png', mask=None,
    ori=0, pos=(0.5, -0.2), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
key_resp = keyboard.Keyboard()
sol = event.Mouse(win=win)
x, y = [None, None]
sol.mouseClock = core.Clock()
gcircle_2 = visual.ImageStim(
    win=win,
    name='gcircle_2', 
    image='images/gcircle.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.12, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
skipsq = visual.ImageStim(
    win=win,
    name='skipsq', 
    image='images/square.png', mask=None,
    ori=0, pos=(0.5, -0.2), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)

# Initialize components for Routine "rewardframe1_4"
rewardframe1_4Clock = core.Clock()
tree1_19 = visual.ImageStim(
    win=win,
    name='tree1_19', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
tree2_19 = visual.ImageStim(
    win=win,
    name='tree2_19', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
tree3_19 = visual.ImageStim(
    win=win,
    name='tree3_19', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
tree4_19 = visual.ImageStim(
    win=win,
    name='tree4_19', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
circle4 = visual.ImageStim(
    win=win,
    name='circle4', 
    image='images/hollow.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
wait_8 = visual.TextStim(win=win, name='wait_8',
    text='',
    font='Arial',
    pos=(0, -0.08), height=0.02, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
forward_12 = visual.ImageStim(
    win=win,
    name='forward_12', 
    image='images/arrow.png', mask=None,
    ori=0, pos=(0.5, -0.2), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
squaree_4 = visual.ImageStim(
    win=win,
    name='squaree_4', 
    image='images/square.png', mask=None,
    ori=0, pos=(0.5, -0.2), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
gcircle_3 = visual.ImageStim(
    win=win,
    name='gcircle_3', 
    image='images/gcircle.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
reward_7 = visual.TextStim(win=win, name='reward_7',
    text='',
    font='Arial',
    pos=(-0.6, -0.08), height=0.05, wrapWidth=None, ori=0, 
    color='green', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);
gcircle_4 = visual.ImageStim(
    win=win,
    name='gcircle_4', 
    image='images/gcircle.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.12, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-12.0)

# Initialize components for Routine "movetrees3"
movetrees3Clock = core.Clock()
tree1_23 = visual.ImageStim(
    win=win,
    name='tree1_23', 
    image='images/tree.png', mask=None,
    ori=0.0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
tree2_23 = visual.ImageStim(
    win=win,
    name='tree2_23', 
    image='images/tree.png', mask=None,
    ori=0.0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
tree3_23 = visual.ImageStim(
    win=win,
    name='tree3_23', 
    image='images/tree.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
tree4_23 = visual.ImageStim(
    win=win,
    name='tree4_23', 
    image='images/tree.png', mask=None,
    ori=0.0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
circle_7 = visual.ImageStim(
    win=win,
    name='circle_7', 
    image='images/hollow.png', mask=None,
    ori=0.0, pos=(0, -0.2), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# Initialize components for Routine "random_seed"
random_seedClock = core.Clock()

# Initialize components for Routine "rewardframe2_3"
rewardframe2_3Clock = core.Clock()
tree1_20 = visual.ImageStim(
    win=win,
    name='tree1_20', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
tree2_20 = visual.ImageStim(
    win=win,
    name='tree2_20', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
tree3_20 = visual.ImageStim(
    win=win,
    name='tree3_20', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
tree4_20 = visual.ImageStim(
    win=win,
    name='tree4_20', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
circle = visual.ImageStim(
    win=win,
    name='circle', 
    image='images/hollow.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
forward_13 = visual.ImageStim(
    win=win,
    name='forward_13', 
    image='images/arrow.png', mask=None,
    ori=0, pos=(-0.5, -0.2), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
square1 = visual.ImageStim(
    win=win,
    name='square1', 
    image='images/square.png', mask=None,
    ori=0.0, pos=(-0.5, -0.2), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
mouse_4 = event.Mouse(win=win)
x, y = [None, None]
mouse_4.mouseClock = core.Clock()

# Initialize components for Routine "rewardframe2_2"
rewardframe2_2Clock = core.Clock()
tree1_13 = visual.ImageStim(
    win=win,
    name='tree1_13', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
tree2_13 = visual.ImageStim(
    win=win,
    name='tree2_13', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
tree3_13 = visual.ImageStim(
    win=win,
    name='tree3_13', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
tree4_13 = visual.ImageStim(
    win=win,
    name='tree4_13', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
circle6 = visual.ImageStim(
    win=win,
    name='circle6', 
    image='images/hollow.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
wait = visual.TextStim(win=win, name='wait',
    text='',
    font='Arial',
    pos=(0.6, -0.08), height=0.02, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
forward_3 = visual.ImageStim(
    win=win,
    name='forward_3', 
    image='images/arrow.png', mask=None,
    ori=0, pos=(-0.5, -0.2), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)

# Initialize components for Routine "rewardframe2"
rewardframe2Clock = core.Clock()
tree1_5 = visual.ImageStim(
    win=win,
    name='tree1_5', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
tree2_5 = visual.ImageStim(
    win=win,
    name='tree2_5', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
tree3_5 = visual.ImageStim(
    win=win,
    name='tree3_5', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
tree4_5 = visual.ImageStim(
    win=win,
    name='tree4_5', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
circle_5 = visual.ImageStim(
    win=win,
    name='circle_5', 
    image='images/hollow.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
reward_3 = visual.TextStim(win=win, name='reward_3',
    text='',
    font='Arial',
    pos=(0.6, -0.08), height=0.05, wrapWidth=None, ori=0, 
    color='green', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
mouse_6 = event.Mouse(win=win)
x, y = [None, None]
mouse_6.mouseClock = core.Clock()
forward_7 = visual.ImageStim(
    win=win,
    name='forward_7', 
    image='images/arrow.png', mask=None,
    ori=0, pos=(-0.5, -0.2), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
sol_2 = event.Mouse(win=win)
x, y = [None, None]
sol_2.mouseClock = core.Clock()
gcircle_5 = visual.ImageStim(
    win=win,
    name='gcircle_5', 
    image='images/gcircle.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.12, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
skipsq_2 = visual.ImageStim(
    win=win,
    name='skipsq_2', 
    image='images/square.png', mask=None,
    ori=0, pos=(-0.5, -0.2), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)

# Initialize components for Routine "rewardframe2_4"
rewardframe2_4Clock = core.Clock()
tree1_21 = visual.ImageStim(
    win=win,
    name='tree1_21', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
tree2_21 = visual.ImageStim(
    win=win,
    name='tree2_21', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
tree3_21 = visual.ImageStim(
    win=win,
    name='tree3_21', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
tree4_21 = visual.ImageStim(
    win=win,
    name='tree4_21', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
wait1 = visual.TextStim(win=win, name='wait1',
    text='wait',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
forward_15 = visual.ImageStim(
    win=win,
    name='forward_15', 
    image='images/arrow.png', mask=None,
    ori=0, pos=(-0.5, -0.2), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
square5 = visual.ImageStim(
    win=win,
    name='square5', 
    image='images/square.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
gcircle1 = visual.ImageStim(
    win=win,
    name='gcircle1', 
    image='images/gcircle.png', mask=None,
    ori=0.0, pos=(0, -0.2), size=(0.12, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
reward_9 = visual.TextStim(win=win, name='reward_9',
    text='',
    font='Arial',
    pos=(0.6, -0.08), height=0.05, wrapWidth=None, ori=0, 
    color='green', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
circle_6 = visual.ImageStim(
    win=win,
    name='circle_6', 
    image='images/hollow.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)

# Initialize components for Routine "movetrees_3"
movetrees_3Clock = core.Clock()
tree1_9 = visual.ImageStim(
    win=win,
    name='tree1_9', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
tree2_9 = visual.ImageStim(
    win=win,
    name='tree2_9', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
tree3_9 = visual.ImageStim(
    win=win,
    name='tree3_9', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
tree4_9 = visual.ImageStim(
    win=win,
    name='tree4_9', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
square_9 = visual.ImageStim(
    win=win,
    name='square_9', 
    image='images/hollow.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)

# Initialize components for Routine "end"
endClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='The end~',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "random_seed"
random_seedClock = core.Clock()

# Initialize components for Routine "rewardframe1_3"
rewardframe1_3Clock = core.Clock()
tree1_18 = visual.ImageStim(
    win=win,
    name='tree1_18', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
tree2_18 = visual.ImageStim(
    win=win,
    name='tree2_18', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
tree3_18 = visual.ImageStim(
    win=win,
    name='tree3_18', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
tree4_18 = visual.ImageStim(
    win=win,
    name='tree4_18', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
circle1 = visual.ImageStim(
    win=win,
    name='circle1', 
    image='images/hollow.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
forward_11 = visual.ImageStim(
    win=win,
    name='forward_11', 
    image='images/arrow.png', mask=None,
    ori=0, pos=(0.5, -0.2), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
squaree_3 = visual.ImageStim(
    win=win,
    name='squaree_3', 
    image='images/square.png', mask=None,
    ori=0, pos=(0.5, -0.2), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
mouse_3 = event.Mouse(win=win)
x, y = [None, None]
mouse_3.mouseClock = core.Clock()

# Initialize components for Routine "rewardframe1_2"
rewardframe1_2Clock = core.Clock()
tree1_12 = visual.ImageStim(
    win=win,
    name='tree1_12', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
tree2_12 = visual.ImageStim(
    win=win,
    name='tree2_12', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
tree3_12 = visual.ImageStim(
    win=win,
    name='tree3_12', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
tree4_12 = visual.ImageStim(
    win=win,
    name='tree4_12', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
circle2 = visual.ImageStim(
    win=win,
    name='circle2', 
    image='images/hollow.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
wait_3 = visual.TextStim(win=win, name='wait_3',
    text='',
    font='Arial',
    pos=(-0.6, -0.08), height=0.02, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
forward_2 = visual.ImageStim(
    win=win,
    name='forward_2', 
    image='images/arrow.png', mask=None,
    ori=0, pos=(0.5, -0.2), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
squaree_2 = visual.ImageStim(
    win=win,
    name='squaree_2', 
    image='images/square.png', mask=None,
    ori=0, pos=(0.5, -0.2), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
gcircle = visual.ImageStim(
    win=win,
    name='gcircle', 
    image='images/gcircle.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)

# Initialize components for Routine "rewardframe1"
rewardframe1Clock = core.Clock()
tree1_4 = visual.ImageStim(
    win=win,
    name='tree1_4', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
tree2_4 = visual.ImageStim(
    win=win,
    name='tree2_4', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
tree3_4 = visual.ImageStim(
    win=win,
    name='tree3_4', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
tree4_4 = visual.ImageStim(
    win=win,
    name='tree4_4', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
circle3 = visual.ImageStim(
    win=win,
    name='circle3', 
    image='images/hollow.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
reward_2 = visual.TextStim(win=win, name='reward_2',
    text=None,
    font='Arial',
    pos=(-0.6, -0.08), height=0.05, wrapWidth=None, ori=0, 
    color='green', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
resp = event.Mouse(win=win)
x, y = [None, None]
resp.mouseClock = core.Clock()
forward = visual.ImageStim(
    win=win,
    name='forward', 
    image='images/arrow.png', mask=None,
    ori=0, pos=(0.5, -0.2), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
key_resp = keyboard.Keyboard()
sol = event.Mouse(win=win)
x, y = [None, None]
sol.mouseClock = core.Clock()
gcircle_2 = visual.ImageStim(
    win=win,
    name='gcircle_2', 
    image='images/gcircle.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.12, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
skipsq = visual.ImageStim(
    win=win,
    name='skipsq', 
    image='images/square.png', mask=None,
    ori=0, pos=(0.5, -0.2), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)

# Initialize components for Routine "rewardframe1_4"
rewardframe1_4Clock = core.Clock()
tree1_19 = visual.ImageStim(
    win=win,
    name='tree1_19', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
tree2_19 = visual.ImageStim(
    win=win,
    name='tree2_19', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
tree3_19 = visual.ImageStim(
    win=win,
    name='tree3_19', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
tree4_19 = visual.ImageStim(
    win=win,
    name='tree4_19', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
circle4 = visual.ImageStim(
    win=win,
    name='circle4', 
    image='images/hollow.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
wait_8 = visual.TextStim(win=win, name='wait_8',
    text='',
    font='Arial',
    pos=(0, -0.08), height=0.02, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
forward_12 = visual.ImageStim(
    win=win,
    name='forward_12', 
    image='images/arrow.png', mask=None,
    ori=0, pos=(0.5, -0.2), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
squaree_4 = visual.ImageStim(
    win=win,
    name='squaree_4', 
    image='images/square.png', mask=None,
    ori=0, pos=(0.5, -0.2), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
gcircle_3 = visual.ImageStim(
    win=win,
    name='gcircle_3', 
    image='images/gcircle.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
reward_7 = visual.TextStim(win=win, name='reward_7',
    text='',
    font='Arial',
    pos=(-0.6, -0.08), height=0.05, wrapWidth=None, ori=0, 
    color='green', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);
gcircle_4 = visual.ImageStim(
    win=win,
    name='gcircle_4', 
    image='images/gcircle.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.12, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-12.0)

# Initialize components for Routine "movetrees5"
movetrees5Clock = core.Clock()
tree1_24 = visual.ImageStim(
    win=win,
    name='tree1_24', 
    image='images/tree.png', mask=None,
    ori=0.0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "movetrees"
movetreesClock = core.Clock()
tree1_6 = visual.ImageStim(
    win=win,
    name='tree1_6', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
tree2_6 = visual.ImageStim(
    win=win,
    name='tree2_6', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
tree3_6 = visual.ImageStim(
    win=win,
    name='tree3_6', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
tree4_6 = visual.ImageStim(
    win=win,
    name='tree4_6', 
    image='images/tree.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
circle5 = visual.ImageStim(
    win=win,
    name='circle5', 
    image='images/hollow.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)

# Initialize components for Routine "end"
endClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='The end~',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "intro"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_5
gotValidClick = False  # until a click is received
# keep track of which components have finished
introComponents = [introtext, mouse_5]
for thisComponent in introComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "intro"-------
while continueRoutine:
    # get current time
    t = introClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *introtext* updates
    if introtext.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        introtext.frameNStart = frameN  # exact frame index
        introtext.tStart = t  # local t and not account for scr refresh
        introtext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(introtext, 'tStartRefresh')  # time at next scr refresh
        introtext.setAutoDraw(True)
    # *mouse_5* updates
    if mouse_5.status == NOT_STARTED and t >= 0-frameTolerance:
        # keep track of start time/frame for later
        mouse_5.frameNStart = frameN  # exact frame index
        mouse_5.tStart = t  # local t and not account for scr refresh
        mouse_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_5, 'tStartRefresh')  # time at next scr refresh
        mouse_5.status = STARTED
        mouse_5.mouseClock.reset()
        prevButtonState = mouse_5.getPressed()  # if button is down already this ISN'T a new click
    if mouse_5.status == STARTED:  # only update if started and not finished!
        buttons = mouse_5.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # abort routine on response
                continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "intro"-------
for thisComponent in introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('introtext.started', introtext.tStartRefresh)
thisExp.addData('introtext.stopped', introtext.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse_5.getPos()
buttons = mouse_5.getPressed()
thisExp.addData('mouse_5.x', x)
thisExp.addData('mouse_5.y', y)
thisExp.addData('mouse_5.leftButton', buttons[0])
thisExp.addData('mouse_5.midButton', buttons[1])
thisExp.addData('mouse_5.rightButton', buttons[2])
thisExp.addData('mouse_5.started', mouse_5.tStart)
thisExp.addData('mouse_5.stopped', mouse_5.tStop)
thisExp.nextEntry()
# the Routine "intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
time = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='time')
thisExp.addLoop(time)  # add the loop to the experiment
thisTime = time.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTime.rgb)
if thisTime != None:
    for paramName in thisTime:
        exec('{} = thisTime[paramName]'.format(paramName))

for thisTime in time:
    currentLoop = time
    # abbreviate parameter names if possible (e.g. rgb = thisTime.rgb)
    if thisTime != None:
        for paramName in thisTime:
            exec('{} = thisTime[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "bound_3"-------
    continueRoutine = True
    # update component parameters for each repeat
    if time.thisN == 0: # only on the first trial
        startTime = globalClock.getTime()
    # keep track of which components have finished
    bound_3Components = []
    for thisComponent in bound_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    bound_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "bound_3"-------
    while continueRoutine:
        # get current time
        t = bound_3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=bound_3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if globalClock.getTime() - startTime >= 5:
            time.finished = True
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in bound_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "bound_3"-------
    for thisComponent in bound_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "bound_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "random_seed"-------
    continueRoutine = True
    # update component parameters for each repeat
    from random import randint
    random_seed= randint(1,5)
    a1i=0
    a2i=0
    a3i=0
    a4i=0
    a5i=0
    a1=[7.5,7.1,6.2,5.9,5.1,4.8,4,3.1,2.6,2.1,1.3,0.7,0]
    a2=[7.3,6.9,6.2,5.8,5.1,4.6,4,3.2,2.4,1.3,0]
    a3=[7.6,7.1,6.8,6.3,5.9,5.4,4.6,3.9,3.2,2.4,1.7,1.1,0]
    a4=[7.1,6.6,6.1,5.8,5.3,4.8,4,3.6,3.1,2.7,2.1,1.3,0]
    a5=[7.4,6.8,6.1,5.8,5.1,4.6,4.1,3.6,2.8,2.1,1.4,0]
    display=14
    # keep track of which components have finished
    random_seedComponents = []
    for thisComponent in random_seedComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    random_seedClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "random_seed"-------
    while continueRoutine:
        # get current time
        t = random_seedClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=random_seedClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in random_seedComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "random_seed"-------
    for thisComponent in random_seedComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "random_seed" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_5 = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_5')
    thisExp.addLoop(trials_5)  # add the loop to the experiment
    thisTrial_5 = trials_5.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
    if thisTrial_5 != None:
        for paramName in thisTrial_5:
            exec('{} = thisTrial_5[paramName]'.format(paramName))
    
    for thisTrial_5 in trials_5:
        currentLoop = trials_5
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
        if thisTrial_5 != None:
            for paramName in thisTrial_5:
                exec('{} = thisTrial_5[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "rewardframe1_3"-------
        continueRoutine = True
        # update component parameters for each repeat
        tree1_18.setPos((-0.5, -0.2))
        tree2_18.setPos((0.5, 0.2))
        tree3_18.setPos((-0.5, 0.6))
        tree4_18.setPos((0.5, -0.6))
        # setup some python lists for storing info about the mouse_3
        mouse_3.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        rewardframe1_3Components = [tree1_18, tree2_18, tree3_18, tree4_18, circle1, forward_11, squaree_3, mouse_3]
        for thisComponent in rewardframe1_3Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        rewardframe1_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "rewardframe1_3"-------
        while continueRoutine:
            # get current time
            t = rewardframe1_3Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=rewardframe1_3Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *tree1_18* updates
            if tree1_18.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree1_18.frameNStart = frameN  # exact frame index
                tree1_18.tStart = t  # local t and not account for scr refresh
                tree1_18.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree1_18, 'tStartRefresh')  # time at next scr refresh
                tree1_18.setAutoDraw(True)
            
            # *tree2_18* updates
            if tree2_18.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree2_18.frameNStart = frameN  # exact frame index
                tree2_18.tStart = t  # local t and not account for scr refresh
                tree2_18.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree2_18, 'tStartRefresh')  # time at next scr refresh
                tree2_18.setAutoDraw(True)
            if tree2_18.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree2_18.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree2_18.tStop = t  # not accounting for scr refresh
                    tree2_18.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree2_18, 'tStopRefresh')  # time at next scr refresh
                    tree2_18.setAutoDraw(False)
            
            # *tree3_18* updates
            if tree3_18.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree3_18.frameNStart = frameN  # exact frame index
                tree3_18.tStart = t  # local t and not account for scr refresh
                tree3_18.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree3_18, 'tStartRefresh')  # time at next scr refresh
                tree3_18.setAutoDraw(True)
            if tree3_18.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree3_18.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree3_18.tStop = t  # not accounting for scr refresh
                    tree3_18.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree3_18, 'tStopRefresh')  # time at next scr refresh
                    tree3_18.setAutoDraw(False)
            
            # *tree4_18* updates
            if tree4_18.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree4_18.frameNStart = frameN  # exact frame index
                tree4_18.tStart = t  # local t and not account for scr refresh
                tree4_18.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree4_18, 'tStartRefresh')  # time at next scr refresh
                tree4_18.setAutoDraw(True)
            if tree4_18.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree4_18.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree4_18.tStop = t  # not accounting for scr refresh
                    tree4_18.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree4_18, 'tStopRefresh')  # time at next scr refresh
                    tree4_18.setAutoDraw(False)
            
            # *circle1* updates
            if circle1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                circle1.frameNStart = frameN  # exact frame index
                circle1.tStart = t  # local t and not account for scr refresh
                circle1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle1, 'tStartRefresh')  # time at next scr refresh
                circle1.setAutoDraw(True)
            
            # *forward_11* updates
            if forward_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                forward_11.frameNStart = frameN  # exact frame index
                forward_11.tStart = t  # local t and not account for scr refresh
                forward_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(forward_11, 'tStartRefresh')  # time at next scr refresh
                forward_11.setAutoDraw(True)
            
            # *squaree_3* updates
            if squaree_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                squaree_3.frameNStart = frameN  # exact frame index
                squaree_3.tStart = t  # local t and not account for scr refresh
                squaree_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(squaree_3, 'tStartRefresh')  # time at next scr refresh
                squaree_3.setAutoDraw(True)
            if squaree_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > squaree_3.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    squaree_3.tStop = t  # not accounting for scr refresh
                    squaree_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(squaree_3, 'tStopRefresh')  # time at next scr refresh
                    squaree_3.setAutoDraw(False)
            # *mouse_3* updates
            if mouse_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_3.frameNStart = frameN  # exact frame index
                mouse_3.tStart = t  # local t and not account for scr refresh
                mouse_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_3, 'tStartRefresh')  # time at next scr refresh
                mouse_3.status = STARTED
                mouse_3.mouseClock.reset()
                prevButtonState = mouse_3.getPressed()  # if button is down already this ISN'T a new click
            if mouse_3.status == STARTED:  # only update if started and not finished!
                buttons = mouse_3.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter(circle1)
                            clickableList = circle1
                        except:
                            clickableList = [circle1]
                        for obj in clickableList:
                            if obj.contains(mouse_3):
                                gotValidClick = True
                                mouse_3.clicked_name.append(obj.name)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rewardframe1_3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "rewardframe1_3"-------
        for thisComponent in rewardframe1_3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_5.addData('tree1_18.started', tree1_18.tStartRefresh)
        trials_5.addData('tree1_18.stopped', tree1_18.tStopRefresh)
        trials_5.addData('tree2_18.started', tree2_18.tStartRefresh)
        trials_5.addData('tree2_18.stopped', tree2_18.tStopRefresh)
        trials_5.addData('tree3_18.started', tree3_18.tStartRefresh)
        trials_5.addData('tree3_18.stopped', tree3_18.tStopRefresh)
        trials_5.addData('tree4_18.started', tree4_18.tStartRefresh)
        trials_5.addData('tree4_18.stopped', tree4_18.tStopRefresh)
        trials_5.addData('circle1.started', circle1.tStartRefresh)
        trials_5.addData('circle1.stopped', circle1.tStopRefresh)
        trials_5.addData('forward_11.started', forward_11.tStartRefresh)
        trials_5.addData('forward_11.stopped', forward_11.tStopRefresh)
        trials_5.addData('squaree_3.started', squaree_3.tStartRefresh)
        trials_5.addData('squaree_3.stopped', squaree_3.tStopRefresh)
        # store data for trials_5 (TrialHandler)
        x, y = mouse_3.getPos()
        buttons = mouse_3.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            try:
                iter(circle1)
                clickableList = circle1
            except:
                clickableList = [circle1]
            for obj in clickableList:
                if obj.contains(mouse_3):
                    gotValidClick = True
                    mouse_3.clicked_name.append(obj.name)
        trials_5.addData('mouse_3.x', x)
        trials_5.addData('mouse_3.y', y)
        trials_5.addData('mouse_3.leftButton', buttons[0])
        trials_5.addData('mouse_3.midButton', buttons[1])
        trials_5.addData('mouse_3.rightButton', buttons[2])
        if len(mouse_3.clicked_name):
            trials_5.addData('mouse_3.clicked_name', mouse_3.clicked_name[0])
        trials_5.addData('mouse_3.started', mouse_3.tStart)
        trials_5.addData('mouse_3.stopped', mouse_3.tStop)
        # the Routine "rewardframe1_3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "rewardframe1_2"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        tree1_12.setPos((-0.5, -0.2))
        tree2_12.setPos((0.5, 0.2))
        tree3_12.setPos((-0.5, 0.6))
        tree4_12.setPos((0.5, -0.6))
        wait_3.setText('wait')
        # keep track of which components have finished
        rewardframe1_2Components = [tree1_12, tree2_12, tree3_12, tree4_12, circle2, wait_3, forward_2, squaree_2, gcircle]
        for thisComponent in rewardframe1_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        rewardframe1_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "rewardframe1_2"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = rewardframe1_2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=rewardframe1_2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *tree1_12* updates
            if tree1_12.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree1_12.frameNStart = frameN  # exact frame index
                tree1_12.tStart = t  # local t and not account for scr refresh
                tree1_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree1_12, 'tStartRefresh')  # time at next scr refresh
                tree1_12.setAutoDraw(True)
            if tree1_12.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree1_12.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    tree1_12.tStop = t  # not accounting for scr refresh
                    tree1_12.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree1_12, 'tStopRefresh')  # time at next scr refresh
                    tree1_12.setAutoDraw(False)
            
            # *tree2_12* updates
            if tree2_12.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree2_12.frameNStart = frameN  # exact frame index
                tree2_12.tStart = t  # local t and not account for scr refresh
                tree2_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree2_12, 'tStartRefresh')  # time at next scr refresh
                tree2_12.setAutoDraw(True)
            if tree2_12.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree2_12.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree2_12.tStop = t  # not accounting for scr refresh
                    tree2_12.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree2_12, 'tStopRefresh')  # time at next scr refresh
                    tree2_12.setAutoDraw(False)
            
            # *tree3_12* updates
            if tree3_12.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree3_12.frameNStart = frameN  # exact frame index
                tree3_12.tStart = t  # local t and not account for scr refresh
                tree3_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree3_12, 'tStartRefresh')  # time at next scr refresh
                tree3_12.setAutoDraw(True)
            if tree3_12.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree3_12.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree3_12.tStop = t  # not accounting for scr refresh
                    tree3_12.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree3_12, 'tStopRefresh')  # time at next scr refresh
                    tree3_12.setAutoDraw(False)
            
            # *tree4_12* updates
            if tree4_12.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree4_12.frameNStart = frameN  # exact frame index
                tree4_12.tStart = t  # local t and not account for scr refresh
                tree4_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree4_12, 'tStartRefresh')  # time at next scr refresh
                tree4_12.setAutoDraw(True)
            if tree4_12.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree4_12.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree4_12.tStop = t  # not accounting for scr refresh
                    tree4_12.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree4_12, 'tStopRefresh')  # time at next scr refresh
                    tree4_12.setAutoDraw(False)
            
            # *circle2* updates
            if circle2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                circle2.frameNStart = frameN  # exact frame index
                circle2.tStart = t  # local t and not account for scr refresh
                circle2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle2, 'tStartRefresh')  # time at next scr refresh
                circle2.setAutoDraw(True)
            if circle2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > circle2.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    circle2.tStop = t  # not accounting for scr refresh
                    circle2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(circle2, 'tStopRefresh')  # time at next scr refresh
                    circle2.setAutoDraw(False)
            
            # *wait_3* updates
            if wait_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wait_3.frameNStart = frameN  # exact frame index
                wait_3.tStart = t  # local t and not account for scr refresh
                wait_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wait_3, 'tStartRefresh')  # time at next scr refresh
                wait_3.setAutoDraw(True)
            if wait_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > wait_3.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    wait_3.tStop = t  # not accounting for scr refresh
                    wait_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(wait_3, 'tStopRefresh')  # time at next scr refresh
                    wait_3.setAutoDraw(False)
            
            # *forward_2* updates
            if forward_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                forward_2.frameNStart = frameN  # exact frame index
                forward_2.tStart = t  # local t and not account for scr refresh
                forward_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(forward_2, 'tStartRefresh')  # time at next scr refresh
                forward_2.setAutoDraw(True)
            if forward_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > forward_2.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    forward_2.tStop = t  # not accounting for scr refresh
                    forward_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(forward_2, 'tStopRefresh')  # time at next scr refresh
                    forward_2.setAutoDraw(False)
            
            # *squaree_2* updates
            if squaree_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                squaree_2.frameNStart = frameN  # exact frame index
                squaree_2.tStart = t  # local t and not account for scr refresh
                squaree_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(squaree_2, 'tStartRefresh')  # time at next scr refresh
                squaree_2.setAutoDraw(True)
            if squaree_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > squaree_2.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    squaree_2.tStop = t  # not accounting for scr refresh
                    squaree_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(squaree_2, 'tStopRefresh')  # time at next scr refresh
                    squaree_2.setAutoDraw(False)
            
            # *gcircle* updates
            if gcircle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                gcircle.frameNStart = frameN  # exact frame index
                gcircle.tStart = t  # local t and not account for scr refresh
                gcircle.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(gcircle, 'tStartRefresh')  # time at next scr refresh
                gcircle.setAutoDraw(True)
            if gcircle.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > gcircle.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    gcircle.tStop = t  # not accounting for scr refresh
                    gcircle.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(gcircle, 'tStopRefresh')  # time at next scr refresh
                    gcircle.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rewardframe1_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "rewardframe1_2"-------
        for thisComponent in rewardframe1_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_5.addData('tree1_12.started', tree1_12.tStartRefresh)
        trials_5.addData('tree1_12.stopped', tree1_12.tStopRefresh)
        trials_5.addData('tree2_12.started', tree2_12.tStartRefresh)
        trials_5.addData('tree2_12.stopped', tree2_12.tStopRefresh)
        trials_5.addData('tree3_12.started', tree3_12.tStartRefresh)
        trials_5.addData('tree3_12.stopped', tree3_12.tStopRefresh)
        trials_5.addData('tree4_12.started', tree4_12.tStartRefresh)
        trials_5.addData('tree4_12.stopped', tree4_12.tStopRefresh)
        trials_5.addData('circle2.started', circle2.tStartRefresh)
        trials_5.addData('circle2.stopped', circle2.tStopRefresh)
        trials_5.addData('wait_3.started', wait_3.tStartRefresh)
        trials_5.addData('wait_3.stopped', wait_3.tStopRefresh)
        trials_5.addData('forward_2.started', forward_2.tStartRefresh)
        trials_5.addData('forward_2.stopped', forward_2.tStopRefresh)
        trials_5.addData('squaree_2.started', squaree_2.tStartRefresh)
        trials_5.addData('squaree_2.stopped', squaree_2.tStopRefresh)
        trials_5.addData('gcircle.started', gcircle.tStartRefresh)
        trials_5.addData('gcircle.stopped', gcircle.tStopRefresh)
        
        # ------Prepare to start Routine "rewardframe1"-------
        continueRoutine = True
        # update component parameters for each repeat
        tree1_4.setPos((-0.5, -0.2))
        tree2_4.setPos((0.5, 0.2))
        tree3_4.setPos((-0.5, 0.6))
        tree4_4.setPos((0.5, -0.6))
        reward_2.setText('')
        # setup some python lists for storing info about the resp
        resp.x = []
        resp.y = []
        resp.leftButton = []
        resp.midButton = []
        resp.rightButton = []
        resp.time = []
        resp.clicked_name = []
        gotValidClick = False  # until a click is received
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # setup some python lists for storing info about the sol
        sol.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        rewardframe1Components = [tree1_4, tree2_4, tree3_4, tree4_4, circle3, reward_2, resp, forward, key_resp, sol, gcircle_2, skipsq]
        for thisComponent in rewardframe1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        rewardframe1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "rewardframe1"-------
        while continueRoutine:
            # get current time
            t = rewardframe1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=rewardframe1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *tree1_4* updates
            if tree1_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree1_4.frameNStart = frameN  # exact frame index
                tree1_4.tStart = t  # local t and not account for scr refresh
                tree1_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree1_4, 'tStartRefresh')  # time at next scr refresh
                tree1_4.setAutoDraw(True)
            
            # *tree2_4* updates
            if tree2_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree2_4.frameNStart = frameN  # exact frame index
                tree2_4.tStart = t  # local t and not account for scr refresh
                tree2_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree2_4, 'tStartRefresh')  # time at next scr refresh
                tree2_4.setAutoDraw(True)
            if tree2_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree2_4.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree2_4.tStop = t  # not accounting for scr refresh
                    tree2_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree2_4, 'tStopRefresh')  # time at next scr refresh
                    tree2_4.setAutoDraw(False)
            
            # *tree3_4* updates
            if tree3_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree3_4.frameNStart = frameN  # exact frame index
                tree3_4.tStart = t  # local t and not account for scr refresh
                tree3_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree3_4, 'tStartRefresh')  # time at next scr refresh
                tree3_4.setAutoDraw(True)
            if tree3_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree3_4.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree3_4.tStop = t  # not accounting for scr refresh
                    tree3_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree3_4, 'tStopRefresh')  # time at next scr refresh
                    tree3_4.setAutoDraw(False)
            
            # *tree4_4* updates
            if tree4_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree4_4.frameNStart = frameN  # exact frame index
                tree4_4.tStart = t  # local t and not account for scr refresh
                tree4_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree4_4, 'tStartRefresh')  # time at next scr refresh
                tree4_4.setAutoDraw(True)
            if tree4_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree4_4.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree4_4.tStop = t  # not accounting for scr refresh
                    tree4_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree4_4, 'tStopRefresh')  # time at next scr refresh
                    tree4_4.setAutoDraw(False)
            
            # *circle3* updates
            if circle3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                circle3.frameNStart = frameN  # exact frame index
                circle3.tStart = t  # local t and not account for scr refresh
                circle3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle3, 'tStartRefresh')  # time at next scr refresh
                circle3.setAutoDraw(True)
            
            # *reward_2* updates
            if reward_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                reward_2.frameNStart = frameN  # exact frame index
                reward_2.tStart = t  # local t and not account for scr refresh
                reward_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(reward_2, 'tStartRefresh')  # time at next scr refresh
                reward_2.setAutoDraw(True)
            if reward_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > reward_2.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    reward_2.tStop = t  # not accounting for scr refresh
                    reward_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(reward_2, 'tStopRefresh')  # time at next scr refresh
                    reward_2.setAutoDraw(False)
            # *resp* updates
            if resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                resp.frameNStart = frameN  # exact frame index
                resp.tStart = t  # local t and not account for scr refresh
                resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
                resp.status = STARTED
                resp.mouseClock.reset()
                prevButtonState = resp.getPressed()  # if button is down already this ISN'T a new click
            if resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > resp.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    resp.tStop = t  # not accounting for scr refresh
                    resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(resp, 'tStopRefresh')  # time at next scr refresh
                    resp.status = FINISHED
            if resp.status == STARTED:  # only update if started and not finished!
                buttons = resp.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter(tree1_4)
                            clickableList = tree1_4
                        except:
                            clickableList = [tree1_4]
                        for obj in clickableList:
                            if obj.contains(resp):
                                gotValidClick = True
                                resp.clicked_name.append(obj.name)
                        x, y = resp.getPos()
                        resp.x.append(x)
                        resp.y.append(y)
                        buttons = resp.getPressed()
                        resp.leftButton.append(buttons[0])
                        resp.midButton.append(buttons[1])
                        resp.rightButton.append(buttons[2])
                        resp.time.append(resp.mouseClock.getTime())
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # *forward* updates
            if forward.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                forward.frameNStart = frameN  # exact frame index
                forward.tStart = t  # local t and not account for scr refresh
                forward.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(forward, 'tStartRefresh')  # time at next scr refresh
                forward.setAutoDraw(True)
            
            # *key_resp* updates
            waitOnFlip = False
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp.tStop = t  # not accounting for scr refresh
                    key_resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                    key_resp.status = FINISHED
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            # *sol* updates
            if sol.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sol.frameNStart = frameN  # exact frame index
                sol.tStart = t  # local t and not account for scr refresh
                sol.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sol, 'tStartRefresh')  # time at next scr refresh
                sol.status = STARTED
                sol.mouseClock.reset()
                prevButtonState = sol.getPressed()  # if button is down already this ISN'T a new click
            if sol.status == STARTED:  # only update if started and not finished!
                buttons = sol.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter(skipsq, tree1_4)
                            clickableList = skipsq, tree1_4
                        except:
                            clickableList = [skipsq, tree1_4]
                        for obj in clickableList:
                            if obj.contains(sol):
                                gotValidClick = True
                                sol.clicked_name.append(obj.name)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # *gcircle_2* updates
            if gcircle_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                gcircle_2.frameNStart = frameN  # exact frame index
                gcircle_2.tStart = t  # local t and not account for scr refresh
                gcircle_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(gcircle_2, 'tStartRefresh')  # time at next scr refresh
                gcircle_2.setAutoDraw(True)
            
            # *skipsq* updates
            if skipsq.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                skipsq.frameNStart = frameN  # exact frame index
                skipsq.tStart = t  # local t and not account for scr refresh
                skipsq.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(skipsq, 'tStartRefresh')  # time at next scr refresh
                skipsq.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rewardframe1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "rewardframe1"-------
        for thisComponent in rewardframe1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_5.addData('tree1_4.started', tree1_4.tStartRefresh)
        trials_5.addData('tree1_4.stopped', tree1_4.tStopRefresh)
        trials_5.addData('tree2_4.started', tree2_4.tStartRefresh)
        trials_5.addData('tree2_4.stopped', tree2_4.tStopRefresh)
        trials_5.addData('tree3_4.started', tree3_4.tStartRefresh)
        trials_5.addData('tree3_4.stopped', tree3_4.tStopRefresh)
        trials_5.addData('tree4_4.started', tree4_4.tStartRefresh)
        trials_5.addData('tree4_4.stopped', tree4_4.tStopRefresh)
        trials_5.addData('circle3.started', circle3.tStartRefresh)
        trials_5.addData('circle3.stopped', circle3.tStopRefresh)
        trials_5.addData('reward_2.started', reward_2.tStartRefresh)
        trials_5.addData('reward_2.stopped', reward_2.tStopRefresh)
        # store data for trials_5 (TrialHandler)
        if len(resp.x): trials_5.addData('resp.x', resp.x[0])
        if len(resp.y): trials_5.addData('resp.y', resp.y[0])
        if len(resp.leftButton): trials_5.addData('resp.leftButton', resp.leftButton[0])
        if len(resp.midButton): trials_5.addData('resp.midButton', resp.midButton[0])
        if len(resp.rightButton): trials_5.addData('resp.rightButton', resp.rightButton[0])
        if len(resp.time): trials_5.addData('resp.time', resp.time[0])
        if len(resp.clicked_name): trials_5.addData('resp.clicked_name', resp.clicked_name[0])
        trials_5.addData('resp.started', resp.tStart)
        trials_5.addData('resp.stopped', resp.tStop)
        trials_5.addData('forward.started', forward.tStartRefresh)
        trials_5.addData('forward.stopped', forward.tStopRefresh)
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        trials_5.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            trials_5.addData('key_resp.rt', key_resp.rt)
        trials_5.addData('key_resp.started', key_resp.tStartRefresh)
        trials_5.addData('key_resp.stopped', key_resp.tStopRefresh)
        # store data for trials_5 (TrialHandler)
        x, y = sol.getPos()
        buttons = sol.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            try:
                iter(skipsq, tree1_4)
                clickableList = skipsq, tree1_4
            except:
                clickableList = [skipsq, tree1_4]
            for obj in clickableList:
                if obj.contains(sol):
                    gotValidClick = True
                    sol.clicked_name.append(obj.name)
        trials_5.addData('sol.x', x)
        trials_5.addData('sol.y', y)
        trials_5.addData('sol.leftButton', buttons[0])
        trials_5.addData('sol.midButton', buttons[1])
        trials_5.addData('sol.rightButton', buttons[2])
        if len(sol.clicked_name):
            trials_5.addData('sol.clicked_name', sol.clicked_name[0])
        trials_5.addData('sol.started', sol.tStart)
        trials_5.addData('sol.stopped', sol.tStop)
        trials_5.addData('gcircle_2.started', gcircle_2.tStartRefresh)
        trials_5.addData('gcircle_2.stopped', gcircle_2.tStopRefresh)
        trials_5.addData('skipsq.started', skipsq.tStartRefresh)
        trials_5.addData('skipsq.stopped', skipsq.tStopRefresh)
        # the Routine "rewardframe1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "rewardframe1_4"-------
        continueRoutine = True
        routineTimer.add(1.000100)
        # update component parameters for each repeat
        display=17
        if random_seed==1:
            if a1i>5:
                display=0
            else:
                display=a1[a1i];
            a1i=a1i+1;
        elif random_seed==2:
            if a2i>5:
                display=0
            else:
                display=a2[a2i];
            a2i=a2i+1;
        elif random_seed==3:
            if a3i>5:
                display=0
            else:
                display=a3[a3i];
            a3i=a3i+1;
        elif random_seed==4:
            if a4i>5:
                display=0
            else:
                display=a4[a4i];
            a4i=a4i+1;
        else:
            if a5i>5:
                display=0
            else:
                display=a5[a5i];
            a5i=a5i+1;
        if sol.clicked_name[0] =='skipsq':
            continueRoutine = False
            reward1.finished = True
        tree1_19.setPos((-0.5, -0.2))
        tree2_19.setPos((0.5, 0.2))
        tree3_19.setPos((-0.5, 0.6))
        tree4_19.setPos((0.5, -0.6))
        wait_8.setText('wait')
        reward_7.setText(display)
        # keep track of which components have finished
        rewardframe1_4Components = [tree1_19, tree2_19, tree3_19, tree4_19, circle4, wait_8, forward_12, squaree_4, gcircle_3, reward_7, gcircle_4]
        for thisComponent in rewardframe1_4Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        rewardframe1_4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "rewardframe1_4"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = rewardframe1_4Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=rewardframe1_4Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *tree1_19* updates
            if tree1_19.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree1_19.frameNStart = frameN  # exact frame index
                tree1_19.tStart = t  # local t and not account for scr refresh
                tree1_19.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree1_19, 'tStartRefresh')  # time at next scr refresh
                tree1_19.setAutoDraw(True)
            if tree1_19.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree1_19.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    tree1_19.tStop = t  # not accounting for scr refresh
                    tree1_19.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree1_19, 'tStopRefresh')  # time at next scr refresh
                    tree1_19.setAutoDraw(False)
            
            # *tree2_19* updates
            if tree2_19.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree2_19.frameNStart = frameN  # exact frame index
                tree2_19.tStart = t  # local t and not account for scr refresh
                tree2_19.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree2_19, 'tStartRefresh')  # time at next scr refresh
                tree2_19.setAutoDraw(True)
            if tree2_19.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree2_19.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree2_19.tStop = t  # not accounting for scr refresh
                    tree2_19.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree2_19, 'tStopRefresh')  # time at next scr refresh
                    tree2_19.setAutoDraw(False)
            
            # *tree3_19* updates
            if tree3_19.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree3_19.frameNStart = frameN  # exact frame index
                tree3_19.tStart = t  # local t and not account for scr refresh
                tree3_19.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree3_19, 'tStartRefresh')  # time at next scr refresh
                tree3_19.setAutoDraw(True)
            if tree3_19.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree3_19.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree3_19.tStop = t  # not accounting for scr refresh
                    tree3_19.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree3_19, 'tStopRefresh')  # time at next scr refresh
                    tree3_19.setAutoDraw(False)
            
            # *tree4_19* updates
            if tree4_19.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree4_19.frameNStart = frameN  # exact frame index
                tree4_19.tStart = t  # local t and not account for scr refresh
                tree4_19.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree4_19, 'tStartRefresh')  # time at next scr refresh
                tree4_19.setAutoDraw(True)
            if tree4_19.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree4_19.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree4_19.tStop = t  # not accounting for scr refresh
                    tree4_19.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree4_19, 'tStopRefresh')  # time at next scr refresh
                    tree4_19.setAutoDraw(False)
            
            # *circle4* updates
            if circle4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                circle4.frameNStart = frameN  # exact frame index
                circle4.tStart = t  # local t and not account for scr refresh
                circle4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle4, 'tStartRefresh')  # time at next scr refresh
                circle4.setAutoDraw(True)
            if circle4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > circle4.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    circle4.tStop = t  # not accounting for scr refresh
                    circle4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(circle4, 'tStopRefresh')  # time at next scr refresh
                    circle4.setAutoDraw(False)
            
            # *wait_8* updates
            if wait_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wait_8.frameNStart = frameN  # exact frame index
                wait_8.tStart = t  # local t and not account for scr refresh
                wait_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wait_8, 'tStartRefresh')  # time at next scr refresh
                wait_8.setAutoDraw(True)
            if wait_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > wait_8.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    wait_8.tStop = t  # not accounting for scr refresh
                    wait_8.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(wait_8, 'tStopRefresh')  # time at next scr refresh
                    wait_8.setAutoDraw(False)
            
            # *forward_12* updates
            if forward_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                forward_12.frameNStart = frameN  # exact frame index
                forward_12.tStart = t  # local t and not account for scr refresh
                forward_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(forward_12, 'tStartRefresh')  # time at next scr refresh
                forward_12.setAutoDraw(True)
            if forward_12.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > forward_12.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    forward_12.tStop = t  # not accounting for scr refresh
                    forward_12.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(forward_12, 'tStopRefresh')  # time at next scr refresh
                    forward_12.setAutoDraw(False)
            
            # *squaree_4* updates
            if squaree_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                squaree_4.frameNStart = frameN  # exact frame index
                squaree_4.tStart = t  # local t and not account for scr refresh
                squaree_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(squaree_4, 'tStartRefresh')  # time at next scr refresh
                squaree_4.setAutoDraw(True)
            if squaree_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > squaree_4.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    squaree_4.tStop = t  # not accounting for scr refresh
                    squaree_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(squaree_4, 'tStopRefresh')  # time at next scr refresh
                    squaree_4.setAutoDraw(False)
            
            # *gcircle_3* updates
            if gcircle_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                gcircle_3.frameNStart = frameN  # exact frame index
                gcircle_3.tStart = t  # local t and not account for scr refresh
                gcircle_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(gcircle_3, 'tStartRefresh')  # time at next scr refresh
                gcircle_3.setAutoDraw(True)
            if gcircle_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > gcircle_3.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    gcircle_3.tStop = t  # not accounting for scr refresh
                    gcircle_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(gcircle_3, 'tStopRefresh')  # time at next scr refresh
                    gcircle_3.setAutoDraw(False)
            
            # *reward_7* updates
            if reward_7.status == NOT_STARTED and tThisFlip >= 0.0001-frameTolerance:
                # keep track of start time/frame for later
                reward_7.frameNStart = frameN  # exact frame index
                reward_7.tStart = t  # local t and not account for scr refresh
                reward_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(reward_7, 'tStartRefresh')  # time at next scr refresh
                reward_7.setAutoDraw(True)
            if reward_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > reward_7.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    reward_7.tStop = t  # not accounting for scr refresh
                    reward_7.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(reward_7, 'tStopRefresh')  # time at next scr refresh
                    reward_7.setAutoDraw(False)
            
            # *gcircle_4* updates
            if gcircle_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                gcircle_4.frameNStart = frameN  # exact frame index
                gcircle_4.tStart = t  # local t and not account for scr refresh
                gcircle_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(gcircle_4, 'tStartRefresh')  # time at next scr refresh
                gcircle_4.setAutoDraw(True)
            if gcircle_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > gcircle_4.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    gcircle_4.tStop = t  # not accounting for scr refresh
                    gcircle_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(gcircle_4, 'tStopRefresh')  # time at next scr refresh
                    gcircle_4.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rewardframe1_4Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "rewardframe1_4"-------
        for thisComponent in rewardframe1_4Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData("randint",display)
        print(display)
        trials_5.addData('tree1_19.started', tree1_19.tStartRefresh)
        trials_5.addData('tree1_19.stopped', tree1_19.tStopRefresh)
        trials_5.addData('tree2_19.started', tree2_19.tStartRefresh)
        trials_5.addData('tree2_19.stopped', tree2_19.tStopRefresh)
        trials_5.addData('tree3_19.started', tree3_19.tStartRefresh)
        trials_5.addData('tree3_19.stopped', tree3_19.tStopRefresh)
        trials_5.addData('tree4_19.started', tree4_19.tStartRefresh)
        trials_5.addData('tree4_19.stopped', tree4_19.tStopRefresh)
        trials_5.addData('circle4.started', circle4.tStartRefresh)
        trials_5.addData('circle4.stopped', circle4.tStopRefresh)
        trials_5.addData('wait_8.started', wait_8.tStartRefresh)
        trials_5.addData('wait_8.stopped', wait_8.tStopRefresh)
        trials_5.addData('forward_12.started', forward_12.tStartRefresh)
        trials_5.addData('forward_12.stopped', forward_12.tStopRefresh)
        trials_5.addData('squaree_4.started', squaree_4.tStartRefresh)
        trials_5.addData('squaree_4.stopped', squaree_4.tStopRefresh)
        trials_5.addData('gcircle_3.started', gcircle_3.tStartRefresh)
        trials_5.addData('gcircle_3.stopped', gcircle_3.tStopRefresh)
        trials_5.addData('reward_7.started', reward_7.tStartRefresh)
        trials_5.addData('reward_7.stopped', reward_7.tStopRefresh)
        trials_5.addData('gcircle_4.started', gcircle_4.tStartRefresh)
        trials_5.addData('gcircle_4.stopped', gcircle_4.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_5'
    
    
    # set up handler to look after randomisation of conditions etc
    pos_1 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('pos.xlsx'),
        seed=None, name='pos_1')
    thisExp.addLoop(pos_1)  # add the loop to the experiment
    thisPo_1 = pos_1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPo_1.rgb)
    if thisPo_1 != None:
        for paramName in thisPo_1:
            exec('{} = thisPo_1[paramName]'.format(paramName))
    
    for thisPo_1 in pos_1:
        currentLoop = pos_1
        # abbreviate parameter names if possible (e.g. rgb = thisPo_1.rgb)
        if thisPo_1 != None:
            for paramName in thisPo_1:
                exec('{} = thisPo_1[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "movetrees"-------
        continueRoutine = True
        routineTimer.add(0.200000)
        # update component parameters for each repeat
        tree1_6.setPos((-0.5, tree1_n))
        tree2_6.setPos((0.5, tree2_p))
        tree3_6.setPos((-0.5,0))
        tree4_6.setPos((0.5, 0))
        # keep track of which components have finished
        movetreesComponents = [tree1_6, tree2_6, tree3_6, tree4_6, circle5]
        for thisComponent in movetreesComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        movetreesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "movetrees"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = movetreesClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=movetreesClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *tree1_6* updates
            if tree1_6.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree1_6.frameNStart = frameN  # exact frame index
                tree1_6.tStart = t  # local t and not account for scr refresh
                tree1_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree1_6, 'tStartRefresh')  # time at next scr refresh
                tree1_6.setAutoDraw(True)
            if tree1_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree1_6.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    tree1_6.tStop = t  # not accounting for scr refresh
                    tree1_6.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree1_6, 'tStopRefresh')  # time at next scr refresh
                    tree1_6.setAutoDraw(False)
            
            # *tree2_6* updates
            if tree2_6.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree2_6.frameNStart = frameN  # exact frame index
                tree2_6.tStart = t  # local t and not account for scr refresh
                tree2_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree2_6, 'tStartRefresh')  # time at next scr refresh
                tree2_6.setAutoDraw(True)
            if tree2_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree2_6.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    tree2_6.tStop = t  # not accounting for scr refresh
                    tree2_6.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree2_6, 'tStopRefresh')  # time at next scr refresh
                    tree2_6.setAutoDraw(False)
            
            # *tree3_6* updates
            if tree3_6.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree3_6.frameNStart = frameN  # exact frame index
                tree3_6.tStart = t  # local t and not account for scr refresh
                tree3_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree3_6, 'tStartRefresh')  # time at next scr refresh
                tree3_6.setAutoDraw(True)
            if tree3_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree3_6.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree3_6.tStop = t  # not accounting for scr refresh
                    tree3_6.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree3_6, 'tStopRefresh')  # time at next scr refresh
                    tree3_6.setAutoDraw(False)
            
            # *tree4_6* updates
            if tree4_6.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree4_6.frameNStart = frameN  # exact frame index
                tree4_6.tStart = t  # local t and not account for scr refresh
                tree4_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree4_6, 'tStartRefresh')  # time at next scr refresh
                tree4_6.setAutoDraw(True)
            if tree4_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree4_6.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree4_6.tStop = t  # not accounting for scr refresh
                    tree4_6.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree4_6, 'tStopRefresh')  # time at next scr refresh
                    tree4_6.setAutoDraw(False)
            
            # *circle5* updates
            if circle5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                circle5.frameNStart = frameN  # exact frame index
                circle5.tStart = t  # local t and not account for scr refresh
                circle5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle5, 'tStartRefresh')  # time at next scr refresh
                circle5.setAutoDraw(True)
            if circle5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > circle5.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    circle5.tStop = t  # not accounting for scr refresh
                    circle5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(circle5, 'tStopRefresh')  # time at next scr refresh
                    circle5.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in movetreesComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "movetrees"-------
        for thisComponent in movetreesComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        pos_1.addData('tree1_6.started', tree1_6.tStartRefresh)
        pos_1.addData('tree1_6.stopped', tree1_6.tStopRefresh)
        pos_1.addData('tree2_6.started', tree2_6.tStartRefresh)
        pos_1.addData('tree2_6.stopped', tree2_6.tStopRefresh)
        pos_1.addData('tree3_6.started', tree3_6.tStartRefresh)
        pos_1.addData('tree3_6.stopped', tree3_6.tStopRefresh)
        pos_1.addData('tree4_6.started', tree4_6.tStartRefresh)
        pos_1.addData('tree4_6.stopped', tree4_6.tStopRefresh)
        pos_1.addData('circle5.started', circle5.tStartRefresh)
        pos_1.addData('circle5.stopped', circle5.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'pos_1'
    
    
    # ------Prepare to start Routine "random_seed_1"-------
    continueRoutine = True
    # update component parameters for each repeat
    from random import randint
    random_seed= randint(1,5)
    a1i=0
    a2i=0
    a3i=0
    a4i=0
    a5i=0
    a1=[7.5,7.1,6.2,5.9,5.1,4.8,4,3.1,2.6,2.1,1.3,0.7,0]
    a2=[7.3,6.9,6.2,5.8,5.1,4.6,4,3.2,2.4,1.3,0]
    a3=[7.6,7.1,6.8,6.3,5.9,5.4,4.6,3.9,3.2,2.4,1.7,1.1,0]
    a4=[7.1,6.6,6.1,5.8,5.3,4.8,4,3.6,3.1,2.7,2.1,1.3,0]
    a5=[7.4,6.8,6.1,5.8,5.1,4.6,4.1,3.6,2.8,2.1,1.4,0]
    display=14
    # keep track of which components have finished
    random_seed_1Components = []
    for thisComponent in random_seed_1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    random_seed_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "random_seed_1"-------
    while continueRoutine:
        # get current time
        t = random_seed_1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=random_seed_1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in random_seed_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "random_seed_1"-------
    for thisComponent in random_seed_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "random_seed_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "rewardframe2_3"-------
    continueRoutine = True
    # update component parameters for each repeat
    tree1_20.setPos((-0.5, -0.6))
    tree2_20.setPos((0.5, -0.2))
    tree3_20.setPos((-0.5, 0.2))
    tree4_20.setPos((0.5, 0.6))
    # setup some python lists for storing info about the mouse_4
    mouse_4.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    rewardframe2_3Components = [tree1_20, tree2_20, tree3_20, tree4_20, circle, forward_13, square1, mouse_4]
    for thisComponent in rewardframe2_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    rewardframe2_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "rewardframe2_3"-------
    while continueRoutine:
        # get current time
        t = rewardframe2_3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=rewardframe2_3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *tree1_20* updates
        if tree1_20.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            tree1_20.frameNStart = frameN  # exact frame index
            tree1_20.tStart = t  # local t and not account for scr refresh
            tree1_20.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tree1_20, 'tStartRefresh')  # time at next scr refresh
            tree1_20.setAutoDraw(True)
        if tree1_20.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > tree1_20.tStartRefresh + 0-frameTolerance:
                # keep track of stop time/frame for later
                tree1_20.tStop = t  # not accounting for scr refresh
                tree1_20.frameNStop = frameN  # exact frame index
                win.timeOnFlip(tree1_20, 'tStopRefresh')  # time at next scr refresh
                tree1_20.setAutoDraw(False)
        
        # *tree2_20* updates
        if tree2_20.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            tree2_20.frameNStart = frameN  # exact frame index
            tree2_20.tStart = t  # local t and not account for scr refresh
            tree2_20.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tree2_20, 'tStartRefresh')  # time at next scr refresh
            tree2_20.setAutoDraw(True)
        
        # *tree3_20* updates
        if tree3_20.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            tree3_20.frameNStart = frameN  # exact frame index
            tree3_20.tStart = t  # local t and not account for scr refresh
            tree3_20.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tree3_20, 'tStartRefresh')  # time at next scr refresh
            tree3_20.setAutoDraw(True)
        if tree3_20.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > tree3_20.tStartRefresh + 0-frameTolerance:
                # keep track of stop time/frame for later
                tree3_20.tStop = t  # not accounting for scr refresh
                tree3_20.frameNStop = frameN  # exact frame index
                win.timeOnFlip(tree3_20, 'tStopRefresh')  # time at next scr refresh
                tree3_20.setAutoDraw(False)
        
        # *tree4_20* updates
        if tree4_20.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            tree4_20.frameNStart = frameN  # exact frame index
            tree4_20.tStart = t  # local t and not account for scr refresh
            tree4_20.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tree4_20, 'tStartRefresh')  # time at next scr refresh
            tree4_20.setAutoDraw(True)
        if tree4_20.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > tree4_20.tStartRefresh + 0-frameTolerance:
                # keep track of stop time/frame for later
                tree4_20.tStop = t  # not accounting for scr refresh
                tree4_20.frameNStop = frameN  # exact frame index
                win.timeOnFlip(tree4_20, 'tStopRefresh')  # time at next scr refresh
                tree4_20.setAutoDraw(False)
        
        # *circle* updates
        if circle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            circle.frameNStart = frameN  # exact frame index
            circle.tStart = t  # local t and not account for scr refresh
            circle.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circle, 'tStartRefresh')  # time at next scr refresh
            circle.setAutoDraw(True)
        
        # *forward_13* updates
        if forward_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            forward_13.frameNStart = frameN  # exact frame index
            forward_13.tStart = t  # local t and not account for scr refresh
            forward_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(forward_13, 'tStartRefresh')  # time at next scr refresh
            forward_13.setAutoDraw(True)
        
        # *square1* updates
        if square1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            square1.frameNStart = frameN  # exact frame index
            square1.tStart = t  # local t and not account for scr refresh
            square1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(square1, 'tStartRefresh')  # time at next scr refresh
            square1.setAutoDraw(True)
        if square1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > square1.tStartRefresh + 0-frameTolerance:
                # keep track of stop time/frame for later
                square1.tStop = t  # not accounting for scr refresh
                square1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(square1, 'tStopRefresh')  # time at next scr refresh
                square1.setAutoDraw(False)
        # *mouse_4* updates
        if mouse_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_4.frameNStart = frameN  # exact frame index
            mouse_4.tStart = t  # local t and not account for scr refresh
            mouse_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_4, 'tStartRefresh')  # time at next scr refresh
            mouse_4.status = STARTED
            mouse_4.mouseClock.reset()
            prevButtonState = mouse_4.getPressed()  # if button is down already this ISN'T a new click
        if mouse_4.status == STARTED:  # only update if started and not finished!
            buttons = mouse_4.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(circle)
                        clickableList = circle
                    except:
                        clickableList = [circle]
                    for obj in clickableList:
                        if obj.contains(mouse_4):
                            gotValidClick = True
                            mouse_4.clicked_name.append(obj.name)
                    # abort routine on response
                    continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in rewardframe2_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rewardframe2_3"-------
    for thisComponent in rewardframe2_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    time.addData('tree1_20.started', tree1_20.tStartRefresh)
    time.addData('tree1_20.stopped', tree1_20.tStopRefresh)
    time.addData('tree2_20.started', tree2_20.tStartRefresh)
    time.addData('tree2_20.stopped', tree2_20.tStopRefresh)
    time.addData('tree3_20.started', tree3_20.tStartRefresh)
    time.addData('tree3_20.stopped', tree3_20.tStopRefresh)
    time.addData('tree4_20.started', tree4_20.tStartRefresh)
    time.addData('tree4_20.stopped', tree4_20.tStopRefresh)
    time.addData('circle.started', circle.tStartRefresh)
    time.addData('circle.stopped', circle.tStopRefresh)
    time.addData('forward_13.started', forward_13.tStartRefresh)
    time.addData('forward_13.stopped', forward_13.tStopRefresh)
    time.addData('square1.started', square1.tStartRefresh)
    time.addData('square1.stopped', square1.tStopRefresh)
    # store data for time (TrialHandler)
    x, y = mouse_4.getPos()
    buttons = mouse_4.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        try:
            iter(circle)
            clickableList = circle
        except:
            clickableList = [circle]
        for obj in clickableList:
            if obj.contains(mouse_4):
                gotValidClick = True
                mouse_4.clicked_name.append(obj.name)
    time.addData('mouse_4.x', x)
    time.addData('mouse_4.y', y)
    time.addData('mouse_4.leftButton', buttons[0])
    time.addData('mouse_4.midButton', buttons[1])
    time.addData('mouse_4.rightButton', buttons[2])
    if len(mouse_4.clicked_name):
        time.addData('mouse_4.clicked_name', mouse_4.clicked_name[0])
    time.addData('mouse_4.started', mouse_4.tStart)
    time.addData('mouse_4.stopped', mouse_4.tStop)
    # the Routine "rewardframe2_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "rewardframe2_2"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    tree1_13.setPos((-0.5, -0.6))
    tree2_13.setPos((0.5, -0.2))
    tree3_13.setPos((-0.5, 0.2))
    tree4_13.setPos((0.5, 0.6))
    wait.setText('wait')
    # keep track of which components have finished
    rewardframe2_2Components = [tree1_13, tree2_13, tree3_13, tree4_13, circle6, wait, forward_3]
    for thisComponent in rewardframe2_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    rewardframe2_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "rewardframe2_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = rewardframe2_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=rewardframe2_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *tree1_13* updates
        if tree1_13.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            tree1_13.frameNStart = frameN  # exact frame index
            tree1_13.tStart = t  # local t and not account for scr refresh
            tree1_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tree1_13, 'tStartRefresh')  # time at next scr refresh
            tree1_13.setAutoDraw(True)
        if tree1_13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > tree1_13.tStartRefresh + 0-frameTolerance:
                # keep track of stop time/frame for later
                tree1_13.tStop = t  # not accounting for scr refresh
                tree1_13.frameNStop = frameN  # exact frame index
                win.timeOnFlip(tree1_13, 'tStopRefresh')  # time at next scr refresh
                tree1_13.setAutoDraw(False)
        
        # *tree2_13* updates
        if tree2_13.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            tree2_13.frameNStart = frameN  # exact frame index
            tree2_13.tStart = t  # local t and not account for scr refresh
            tree2_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tree2_13, 'tStartRefresh')  # time at next scr refresh
            tree2_13.setAutoDraw(True)
        if tree2_13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > tree2_13.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                tree2_13.tStop = t  # not accounting for scr refresh
                tree2_13.frameNStop = frameN  # exact frame index
                win.timeOnFlip(tree2_13, 'tStopRefresh')  # time at next scr refresh
                tree2_13.setAutoDraw(False)
        
        # *tree3_13* updates
        if tree3_13.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            tree3_13.frameNStart = frameN  # exact frame index
            tree3_13.tStart = t  # local t and not account for scr refresh
            tree3_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tree3_13, 'tStartRefresh')  # time at next scr refresh
            tree3_13.setAutoDraw(True)
        if tree3_13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > tree3_13.tStartRefresh + 0-frameTolerance:
                # keep track of stop time/frame for later
                tree3_13.tStop = t  # not accounting for scr refresh
                tree3_13.frameNStop = frameN  # exact frame index
                win.timeOnFlip(tree3_13, 'tStopRefresh')  # time at next scr refresh
                tree3_13.setAutoDraw(False)
        
        # *tree4_13* updates
        if tree4_13.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            tree4_13.frameNStart = frameN  # exact frame index
            tree4_13.tStart = t  # local t and not account for scr refresh
            tree4_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tree4_13, 'tStartRefresh')  # time at next scr refresh
            tree4_13.setAutoDraw(True)
        if tree4_13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > tree4_13.tStartRefresh + 0-frameTolerance:
                # keep track of stop time/frame for later
                tree4_13.tStop = t  # not accounting for scr refresh
                tree4_13.frameNStop = frameN  # exact frame index
                win.timeOnFlip(tree4_13, 'tStopRefresh')  # time at next scr refresh
                tree4_13.setAutoDraw(False)
        
        # *circle6* updates
        if circle6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            circle6.frameNStart = frameN  # exact frame index
            circle6.tStart = t  # local t and not account for scr refresh
            circle6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circle6, 'tStartRefresh')  # time at next scr refresh
            circle6.setAutoDraw(True)
        if circle6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > circle6.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                circle6.tStop = t  # not accounting for scr refresh
                circle6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(circle6, 'tStopRefresh')  # time at next scr refresh
                circle6.setAutoDraw(False)
        
        # *wait* updates
        if wait.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            wait.frameNStart = frameN  # exact frame index
            wait.tStart = t  # local t and not account for scr refresh
            wait.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wait, 'tStartRefresh')  # time at next scr refresh
            wait.setAutoDraw(True)
        if wait.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > wait.tStartRefresh + 0-frameTolerance:
                # keep track of stop time/frame for later
                wait.tStop = t  # not accounting for scr refresh
                wait.frameNStop = frameN  # exact frame index
                win.timeOnFlip(wait, 'tStopRefresh')  # time at next scr refresh
                wait.setAutoDraw(False)
        
        # *forward_3* updates
        if forward_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            forward_3.frameNStart = frameN  # exact frame index
            forward_3.tStart = t  # local t and not account for scr refresh
            forward_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(forward_3, 'tStartRefresh')  # time at next scr refresh
            forward_3.setAutoDraw(True)
        if forward_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > forward_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                forward_3.tStop = t  # not accounting for scr refresh
                forward_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(forward_3, 'tStopRefresh')  # time at next scr refresh
                forward_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in rewardframe2_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rewardframe2_2"-------
    for thisComponent in rewardframe2_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    time.addData('tree1_13.started', tree1_13.tStartRefresh)
    time.addData('tree1_13.stopped', tree1_13.tStopRefresh)
    time.addData('tree2_13.started', tree2_13.tStartRefresh)
    time.addData('tree2_13.stopped', tree2_13.tStopRefresh)
    time.addData('tree3_13.started', tree3_13.tStartRefresh)
    time.addData('tree3_13.stopped', tree3_13.tStopRefresh)
    time.addData('tree4_13.started', tree4_13.tStartRefresh)
    time.addData('tree4_13.stopped', tree4_13.tStopRefresh)
    time.addData('circle6.started', circle6.tStartRefresh)
    time.addData('circle6.stopped', circle6.tStopRefresh)
    time.addData('wait.started', wait.tStartRefresh)
    time.addData('wait.stopped', wait.tStopRefresh)
    time.addData('forward_3.started', forward_3.tStartRefresh)
    time.addData('forward_3.stopped', forward_3.tStopRefresh)
    
    # ------Prepare to start Routine "rewardframe2"-------
    continueRoutine = True
    # update component parameters for each repeat
    tree1_5.setPos((-0.5, -0.6))
    tree2_5.setPos((0.5, -0.2))
    tree3_5.setPos((-0.5, 0.2))
    tree4_5.setPos((0.5, 0.6))
    reward_3.setText('\n')
    # setup some python lists for storing info about the mouse_6
    mouse_6.clicked_name = []
    gotValidClick = False  # until a click is received
    # setup some python lists for storing info about the sol_2
    sol_2.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    rewardframe2Components = [tree1_5, tree2_5, tree3_5, tree4_5, circle_5, reward_3, mouse_6, forward_7, sol_2, gcircle_5, skipsq_2]
    for thisComponent in rewardframe2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    rewardframe2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "rewardframe2"-------
    while continueRoutine:
        # get current time
        t = rewardframe2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=rewardframe2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *tree1_5* updates
        if tree1_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            tree1_5.frameNStart = frameN  # exact frame index
            tree1_5.tStart = t  # local t and not account for scr refresh
            tree1_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tree1_5, 'tStartRefresh')  # time at next scr refresh
            tree1_5.setAutoDraw(True)
        if tree1_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > tree1_5.tStartRefresh + 0-frameTolerance:
                # keep track of stop time/frame for later
                tree1_5.tStop = t  # not accounting for scr refresh
                tree1_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(tree1_5, 'tStopRefresh')  # time at next scr refresh
                tree1_5.setAutoDraw(False)
        
        # *tree2_5* updates
        if tree2_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            tree2_5.frameNStart = frameN  # exact frame index
            tree2_5.tStart = t  # local t and not account for scr refresh
            tree2_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tree2_5, 'tStartRefresh')  # time at next scr refresh
            tree2_5.setAutoDraw(True)
        
        # *tree3_5* updates
        if tree3_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            tree3_5.frameNStart = frameN  # exact frame index
            tree3_5.tStart = t  # local t and not account for scr refresh
            tree3_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tree3_5, 'tStartRefresh')  # time at next scr refresh
            tree3_5.setAutoDraw(True)
        if tree3_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > tree3_5.tStartRefresh + 0-frameTolerance:
                # keep track of stop time/frame for later
                tree3_5.tStop = t  # not accounting for scr refresh
                tree3_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(tree3_5, 'tStopRefresh')  # time at next scr refresh
                tree3_5.setAutoDraw(False)
        
        # *tree4_5* updates
        if tree4_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            tree4_5.frameNStart = frameN  # exact frame index
            tree4_5.tStart = t  # local t and not account for scr refresh
            tree4_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tree4_5, 'tStartRefresh')  # time at next scr refresh
            tree4_5.setAutoDraw(True)
        if tree4_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > tree4_5.tStartRefresh + 0-frameTolerance:
                # keep track of stop time/frame for later
                tree4_5.tStop = t  # not accounting for scr refresh
                tree4_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(tree4_5, 'tStopRefresh')  # time at next scr refresh
                tree4_5.setAutoDraw(False)
        
        # *circle_5* updates
        if circle_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            circle_5.frameNStart = frameN  # exact frame index
            circle_5.tStart = t  # local t and not account for scr refresh
            circle_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circle_5, 'tStartRefresh')  # time at next scr refresh
            circle_5.setAutoDraw(True)
        
        # *reward_3* updates
        if reward_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            reward_3.frameNStart = frameN  # exact frame index
            reward_3.tStart = t  # local t and not account for scr refresh
            reward_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(reward_3, 'tStartRefresh')  # time at next scr refresh
            reward_3.setAutoDraw(True)
        if reward_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > reward_3.tStartRefresh + 0-frameTolerance:
                # keep track of stop time/frame for later
                reward_3.tStop = t  # not accounting for scr refresh
                reward_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(reward_3, 'tStopRefresh')  # time at next scr refresh
                reward_3.setAutoDraw(False)
        # *mouse_6* updates
        if mouse_6.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_6.frameNStart = frameN  # exact frame index
            mouse_6.tStart = t  # local t and not account for scr refresh
            mouse_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_6, 'tStartRefresh')  # time at next scr refresh
            mouse_6.status = STARTED
            mouse_6.mouseClock.reset()
            prevButtonState = mouse_6.getPressed()  # if button is down already this ISN'T a new click
        if mouse_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse_6.tStartRefresh + 0-frameTolerance:
                # keep track of stop time/frame for later
                mouse_6.tStop = t  # not accounting for scr refresh
                mouse_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(mouse_6, 'tStopRefresh')  # time at next scr refresh
                mouse_6.status = FINISHED
        if mouse_6.status == STARTED:  # only update if started and not finished!
            buttons = mouse_6.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(tree2_5)
                        clickableList = tree2_5
                    except:
                        clickableList = [tree2_5]
                    for obj in clickableList:
                        if obj.contains(mouse_6):
                            gotValidClick = True
                            mouse_6.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # *forward_7* updates
        if forward_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            forward_7.frameNStart = frameN  # exact frame index
            forward_7.tStart = t  # local t and not account for scr refresh
            forward_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(forward_7, 'tStartRefresh')  # time at next scr refresh
            forward_7.setAutoDraw(True)
        # *sol_2* updates
        if sol_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sol_2.frameNStart = frameN  # exact frame index
            sol_2.tStart = t  # local t and not account for scr refresh
            sol_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sol_2, 'tStartRefresh')  # time at next scr refresh
            sol_2.status = STARTED
            sol_2.mouseClock.reset()
            prevButtonState = sol_2.getPressed()  # if button is down already this ISN'T a new click
        if sol_2.status == STARTED:  # only update if started and not finished!
            buttons = sol_2.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(skipsq_2, tree2_5)
                        clickableList = skipsq_2, tree2_5
                    except:
                        clickableList = [skipsq_2, tree2_5]
                    for obj in clickableList:
                        if obj.contains(sol_2):
                            gotValidClick = True
                            sol_2.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # *gcircle_5* updates
        if gcircle_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            gcircle_5.frameNStart = frameN  # exact frame index
            gcircle_5.tStart = t  # local t and not account for scr refresh
            gcircle_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(gcircle_5, 'tStartRefresh')  # time at next scr refresh
            gcircle_5.setAutoDraw(True)
        
        # *skipsq_2* updates
        if skipsq_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            skipsq_2.frameNStart = frameN  # exact frame index
            skipsq_2.tStart = t  # local t and not account for scr refresh
            skipsq_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(skipsq_2, 'tStartRefresh')  # time at next scr refresh
            skipsq_2.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in rewardframe2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rewardframe2"-------
    for thisComponent in rewardframe2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    time.addData('tree1_5.started', tree1_5.tStartRefresh)
    time.addData('tree1_5.stopped', tree1_5.tStopRefresh)
    time.addData('tree2_5.started', tree2_5.tStartRefresh)
    time.addData('tree2_5.stopped', tree2_5.tStopRefresh)
    time.addData('tree3_5.started', tree3_5.tStartRefresh)
    time.addData('tree3_5.stopped', tree3_5.tStopRefresh)
    time.addData('tree4_5.started', tree4_5.tStartRefresh)
    time.addData('tree4_5.stopped', tree4_5.tStopRefresh)
    time.addData('circle_5.started', circle_5.tStartRefresh)
    time.addData('circle_5.stopped', circle_5.tStopRefresh)
    time.addData('reward_3.started', reward_3.tStartRefresh)
    time.addData('reward_3.stopped', reward_3.tStopRefresh)
    # store data for time (TrialHandler)
    x, y = mouse_6.getPos()
    buttons = mouse_6.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        try:
            iter(tree2_5)
            clickableList = tree2_5
        except:
            clickableList = [tree2_5]
        for obj in clickableList:
            if obj.contains(mouse_6):
                gotValidClick = True
                mouse_6.clicked_name.append(obj.name)
    time.addData('mouse_6.x', x)
    time.addData('mouse_6.y', y)
    time.addData('mouse_6.leftButton', buttons[0])
    time.addData('mouse_6.midButton', buttons[1])
    time.addData('mouse_6.rightButton', buttons[2])
    if len(mouse_6.clicked_name):
        time.addData('mouse_6.clicked_name', mouse_6.clicked_name[0])
    time.addData('mouse_6.started', mouse_6.tStart)
    time.addData('mouse_6.stopped', mouse_6.tStop)
    time.addData('forward_7.started', forward_7.tStartRefresh)
    time.addData('forward_7.stopped', forward_7.tStopRefresh)
    # store data for time (TrialHandler)
    x, y = sol_2.getPos()
    buttons = sol_2.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        try:
            iter(skipsq_2, tree2_5)
            clickableList = skipsq_2, tree2_5
        except:
            clickableList = [skipsq_2, tree2_5]
        for obj in clickableList:
            if obj.contains(sol_2):
                gotValidClick = True
                sol_2.clicked_name.append(obj.name)
    time.addData('sol_2.x', x)
    time.addData('sol_2.y', y)
    time.addData('sol_2.leftButton', buttons[0])
    time.addData('sol_2.midButton', buttons[1])
    time.addData('sol_2.rightButton', buttons[2])
    if len(sol_2.clicked_name):
        time.addData('sol_2.clicked_name', sol_2.clicked_name[0])
    time.addData('sol_2.started', sol_2.tStart)
    time.addData('sol_2.stopped', sol_2.tStop)
    time.addData('gcircle_5.started', gcircle_5.tStartRefresh)
    time.addData('gcircle_5.stopped', gcircle_5.tStopRefresh)
    time.addData('skipsq_2.started', skipsq_2.tStartRefresh)
    time.addData('skipsq_2.stopped', skipsq_2.tStopRefresh)
    # the Routine "rewardframe2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "rewardframe2_4"-------
    continueRoutine = True
    routineTimer.add(1.000001)
    # update component parameters for each repeat
    display=17
    if random_seed==1:
        if a1i>5:
            display=0
        else:
            display=a1[a1i];
        a1i=a1i+1;
    elif random_seed==2:
        if a2i>5:
            display=0
        else:
            display=a2[a2i];
        a2i=a2i+1;
    elif random_seed==3:
        if a3i>5:
            display=0
        else:
            display=a3[a3i];
        a3i=a3i+1;
    elif random_seed==4:
        if a4i>5:
            display=0
        else:
            display=a4[a4i];
        a4i=a4i+1;
    else:
        if a5i>5:
            display=0
        else:
            display=a5[a5i];
        a5i=a5i+1;
    if sol_2.clicked_name[0] =='skipsq_2':
        reward2.finished = True
    tree1_21.setPos((-0.5, -0.6))
    tree2_21.setPos((0.5, -0.2))
    tree3_21.setPos((-0.5, 0.2))
    tree4_21.setPos((0.5, 0.6))
    reward_9.setText(display)
    # keep track of which components have finished
    rewardframe2_4Components = [tree1_21, tree2_21, tree3_21, tree4_21, wait1, forward_15, square5, gcircle1, reward_9, circle_6]
    for thisComponent in rewardframe2_4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    rewardframe2_4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "rewardframe2_4"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = rewardframe2_4Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=rewardframe2_4Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *tree1_21* updates
        if tree1_21.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            tree1_21.frameNStart = frameN  # exact frame index
            tree1_21.tStart = t  # local t and not account for scr refresh
            tree1_21.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tree1_21, 'tStartRefresh')  # time at next scr refresh
            tree1_21.setAutoDraw(True)
        if tree1_21.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > tree1_21.tStartRefresh + 0-frameTolerance:
                # keep track of stop time/frame for later
                tree1_21.tStop = t  # not accounting for scr refresh
                tree1_21.frameNStop = frameN  # exact frame index
                win.timeOnFlip(tree1_21, 'tStopRefresh')  # time at next scr refresh
                tree1_21.setAutoDraw(False)
        
        # *tree2_21* updates
        if tree2_21.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            tree2_21.frameNStart = frameN  # exact frame index
            tree2_21.tStart = t  # local t and not account for scr refresh
            tree2_21.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tree2_21, 'tStartRefresh')  # time at next scr refresh
            tree2_21.setAutoDraw(True)
        if tree2_21.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > tree2_21.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                tree2_21.tStop = t  # not accounting for scr refresh
                tree2_21.frameNStop = frameN  # exact frame index
                win.timeOnFlip(tree2_21, 'tStopRefresh')  # time at next scr refresh
                tree2_21.setAutoDraw(False)
        
        # *tree3_21* updates
        if tree3_21.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            tree3_21.frameNStart = frameN  # exact frame index
            tree3_21.tStart = t  # local t and not account for scr refresh
            tree3_21.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tree3_21, 'tStartRefresh')  # time at next scr refresh
            tree3_21.setAutoDraw(True)
        if tree3_21.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > tree3_21.tStartRefresh + 0-frameTolerance:
                # keep track of stop time/frame for later
                tree3_21.tStop = t  # not accounting for scr refresh
                tree3_21.frameNStop = frameN  # exact frame index
                win.timeOnFlip(tree3_21, 'tStopRefresh')  # time at next scr refresh
                tree3_21.setAutoDraw(False)
        
        # *tree4_21* updates
        if tree4_21.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            tree4_21.frameNStart = frameN  # exact frame index
            tree4_21.tStart = t  # local t and not account for scr refresh
            tree4_21.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tree4_21, 'tStartRefresh')  # time at next scr refresh
            tree4_21.setAutoDraw(True)
        if tree4_21.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > tree4_21.tStartRefresh + 0-frameTolerance:
                # keep track of stop time/frame for later
                tree4_21.tStop = t  # not accounting for scr refresh
                tree4_21.frameNStop = frameN  # exact frame index
                win.timeOnFlip(tree4_21, 'tStopRefresh')  # time at next scr refresh
                tree4_21.setAutoDraw(False)
        
        # *wait1* updates
        if wait1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            wait1.frameNStart = frameN  # exact frame index
            wait1.tStart = t  # local t and not account for scr refresh
            wait1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wait1, 'tStartRefresh')  # time at next scr refresh
            wait1.setAutoDraw(True)
        if wait1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > wait1.tStartRefresh + 0-frameTolerance:
                # keep track of stop time/frame for later
                wait1.tStop = t  # not accounting for scr refresh
                wait1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(wait1, 'tStopRefresh')  # time at next scr refresh
                wait1.setAutoDraw(False)
        
        # *forward_15* updates
        if forward_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            forward_15.frameNStart = frameN  # exact frame index
            forward_15.tStart = t  # local t and not account for scr refresh
            forward_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(forward_15, 'tStartRefresh')  # time at next scr refresh
            forward_15.setAutoDraw(True)
        if forward_15.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > forward_15.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                forward_15.tStop = t  # not accounting for scr refresh
                forward_15.frameNStop = frameN  # exact frame index
                win.timeOnFlip(forward_15, 'tStopRefresh')  # time at next scr refresh
                forward_15.setAutoDraw(False)
        
        # *square5* updates
        if square5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            square5.frameNStart = frameN  # exact frame index
            square5.tStart = t  # local t and not account for scr refresh
            square5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(square5, 'tStartRefresh')  # time at next scr refresh
            square5.setAutoDraw(True)
        if square5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > square5.tStartRefresh + 0-frameTolerance:
                # keep track of stop time/frame for later
                square5.tStop = t  # not accounting for scr refresh
                square5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(square5, 'tStopRefresh')  # time at next scr refresh
                square5.setAutoDraw(False)
        
        # *gcircle1* updates
        if gcircle1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            gcircle1.frameNStart = frameN  # exact frame index
            gcircle1.tStart = t  # local t and not account for scr refresh
            gcircle1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(gcircle1, 'tStartRefresh')  # time at next scr refresh
            gcircle1.setAutoDraw(True)
        if gcircle1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > gcircle1.tStartRefresh + 0-frameTolerance:
                # keep track of stop time/frame for later
                gcircle1.tStop = t  # not accounting for scr refresh
                gcircle1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(gcircle1, 'tStopRefresh')  # time at next scr refresh
                gcircle1.setAutoDraw(False)
        
        # *reward_9* updates
        if reward_9.status == NOT_STARTED and tThisFlip >= 0.000001-frameTolerance:
            # keep track of start time/frame for later
            reward_9.frameNStart = frameN  # exact frame index
            reward_9.tStart = t  # local t and not account for scr refresh
            reward_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(reward_9, 'tStartRefresh')  # time at next scr refresh
            reward_9.setAutoDraw(True)
        if reward_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > reward_9.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                reward_9.tStop = t  # not accounting for scr refresh
                reward_9.frameNStop = frameN  # exact frame index
                win.timeOnFlip(reward_9, 'tStopRefresh')  # time at next scr refresh
                reward_9.setAutoDraw(False)
        
        # *circle_6* updates
        if circle_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            circle_6.frameNStart = frameN  # exact frame index
            circle_6.tStart = t  # local t and not account for scr refresh
            circle_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circle_6, 'tStartRefresh')  # time at next scr refresh
            circle_6.setAutoDraw(True)
        if circle_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > circle_6.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                circle_6.tStop = t  # not accounting for scr refresh
                circle_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(circle_6, 'tStopRefresh')  # time at next scr refresh
                circle_6.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in rewardframe2_4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rewardframe2_4"-------
    for thisComponent in rewardframe2_4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData("randint",display)
    print(display)
    time.addData('tree1_21.started', tree1_21.tStartRefresh)
    time.addData('tree1_21.stopped', tree1_21.tStopRefresh)
    time.addData('tree2_21.started', tree2_21.tStartRefresh)
    time.addData('tree2_21.stopped', tree2_21.tStopRefresh)
    time.addData('tree3_21.started', tree3_21.tStartRefresh)
    time.addData('tree3_21.stopped', tree3_21.tStopRefresh)
    time.addData('tree4_21.started', tree4_21.tStartRefresh)
    time.addData('tree4_21.stopped', tree4_21.tStopRefresh)
    time.addData('wait1.started', wait1.tStartRefresh)
    time.addData('wait1.stopped', wait1.tStopRefresh)
    time.addData('forward_15.started', forward_15.tStartRefresh)
    time.addData('forward_15.stopped', forward_15.tStopRefresh)
    time.addData('square5.started', square5.tStartRefresh)
    time.addData('square5.stopped', square5.tStopRefresh)
    time.addData('gcircle1.started', gcircle1.tStartRefresh)
    time.addData('gcircle1.stopped', gcircle1.tStopRefresh)
    time.addData('reward_9.started', reward_9.tStartRefresh)
    time.addData('reward_9.stopped', reward_9.tStopRefresh)
    time.addData('circle_6.started', circle_6.tStartRefresh)
    time.addData('circle_6.stopped', circle_6.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    pos_2 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('pos.xlsx'),
        seed=None, name='pos_2')
    thisExp.addLoop(pos_2)  # add the loop to the experiment
    thisPo_2 = pos_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPo_2.rgb)
    if thisPo_2 != None:
        for paramName in thisPo_2:
            exec('{} = thisPo_2[paramName]'.format(paramName))
    
    for thisPo_2 in pos_2:
        currentLoop = pos_2
        # abbreviate parameter names if possible (e.g. rgb = thisPo_2.rgb)
        if thisPo_2 != None:
            for paramName in thisPo_2:
                exec('{} = thisPo_2[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "movetrees2"-------
        continueRoutine = True
        routineTimer.add(0.200000)
        # update component parameters for each repeat
        tree1_22.setPos((0.5, tree1_n))
        tree2_22.setPos((-0.5, tree2_p))
        tree3_22.setPos((-0.5,0))
        tree4_22.setPos((0.5, 0))
        # keep track of which components have finished
        movetrees2Components = [tree1_22, tree2_22, tree3_22, tree4_22, circle5_2]
        for thisComponent in movetrees2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        movetrees2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "movetrees2"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = movetrees2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=movetrees2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *tree1_22* updates
            if tree1_22.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree1_22.frameNStart = frameN  # exact frame index
                tree1_22.tStart = t  # local t and not account for scr refresh
                tree1_22.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree1_22, 'tStartRefresh')  # time at next scr refresh
                tree1_22.setAutoDraw(True)
            if tree1_22.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree1_22.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    tree1_22.tStop = t  # not accounting for scr refresh
                    tree1_22.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree1_22, 'tStopRefresh')  # time at next scr refresh
                    tree1_22.setAutoDraw(False)
            
            # *tree2_22* updates
            if tree2_22.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree2_22.frameNStart = frameN  # exact frame index
                tree2_22.tStart = t  # local t and not account for scr refresh
                tree2_22.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree2_22, 'tStartRefresh')  # time at next scr refresh
                tree2_22.setAutoDraw(True)
            if tree2_22.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree2_22.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    tree2_22.tStop = t  # not accounting for scr refresh
                    tree2_22.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree2_22, 'tStopRefresh')  # time at next scr refresh
                    tree2_22.setAutoDraw(False)
            
            # *tree3_22* updates
            if tree3_22.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree3_22.frameNStart = frameN  # exact frame index
                tree3_22.tStart = t  # local t and not account for scr refresh
                tree3_22.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree3_22, 'tStartRefresh')  # time at next scr refresh
                tree3_22.setAutoDraw(True)
            if tree3_22.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree3_22.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree3_22.tStop = t  # not accounting for scr refresh
                    tree3_22.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree3_22, 'tStopRefresh')  # time at next scr refresh
                    tree3_22.setAutoDraw(False)
            
            # *tree4_22* updates
            if tree4_22.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree4_22.frameNStart = frameN  # exact frame index
                tree4_22.tStart = t  # local t and not account for scr refresh
                tree4_22.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree4_22, 'tStartRefresh')  # time at next scr refresh
                tree4_22.setAutoDraw(True)
            if tree4_22.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree4_22.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree4_22.tStop = t  # not accounting for scr refresh
                    tree4_22.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree4_22, 'tStopRefresh')  # time at next scr refresh
                    tree4_22.setAutoDraw(False)
            
            # *circle5_2* updates
            if circle5_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                circle5_2.frameNStart = frameN  # exact frame index
                circle5_2.tStart = t  # local t and not account for scr refresh
                circle5_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle5_2, 'tStartRefresh')  # time at next scr refresh
                circle5_2.setAutoDraw(True)
            if circle5_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > circle5_2.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    circle5_2.tStop = t  # not accounting for scr refresh
                    circle5_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(circle5_2, 'tStopRefresh')  # time at next scr refresh
                    circle5_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in movetrees2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "movetrees2"-------
        for thisComponent in movetrees2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        pos_2.addData('tree1_22.started', tree1_22.tStartRefresh)
        pos_2.addData('tree1_22.stopped', tree1_22.tStopRefresh)
        pos_2.addData('tree2_22.started', tree2_22.tStartRefresh)
        pos_2.addData('tree2_22.stopped', tree2_22.tStopRefresh)
        pos_2.addData('tree3_22.started', tree3_22.tStartRefresh)
        pos_2.addData('tree3_22.stopped', tree3_22.tStopRefresh)
        pos_2.addData('tree4_22.started', tree4_22.tStartRefresh)
        pos_2.addData('tree4_22.stopped', tree4_22.tStopRefresh)
        pos_2.addData('circle5_2.started', circle5_2.tStartRefresh)
        pos_2.addData('circle5_2.stopped', circle5_2.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'pos_2'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'time'


# ------Prepare to start Routine "end"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [text]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)

# set up handler to look after randomisation of conditions etc
time2 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('reward.xlsx'),
    seed=None, name='time2')
thisExp.addLoop(time2)  # add the loop to the experiment
thisTime2 = time2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTime2.rgb)
if thisTime2 != None:
    for paramName in thisTime2:
        exec('{} = thisTime2[paramName]'.format(paramName))

for thisTime2 in time2:
    currentLoop = time2
    # abbreviate parameter names if possible (e.g. rgb = thisTime2.rgb)
    if thisTime2 != None:
        for paramName in thisTime2:
            exec('{} = thisTime2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "random_seed"-------
    continueRoutine = True
    # update component parameters for each repeat
    from random import randint
    random_seed= randint(1,5)
    a1i=0
    a2i=0
    a3i=0
    a4i=0
    a5i=0
    a1=[7.5,7.1,6.2,5.9,5.1,4.8,4,3.1,2.6,2.1,1.3,0.7,0]
    a2=[7.3,6.9,6.2,5.8,5.1,4.6,4,3.2,2.4,1.3,0]
    a3=[7.6,7.1,6.8,6.3,5.9,5.4,4.6,3.9,3.2,2.4,1.7,1.1,0]
    a4=[7.1,6.6,6.1,5.8,5.3,4.8,4,3.6,3.1,2.7,2.1,1.3,0]
    a5=[7.4,6.8,6.1,5.8,5.1,4.6,4.1,3.6,2.8,2.1,1.4,0]
    display=14
    # keep track of which components have finished
    random_seedComponents = []
    for thisComponent in random_seedComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    random_seedClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "random_seed"-------
    while continueRoutine:
        # get current time
        t = random_seedClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=random_seedClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in random_seedComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "random_seed"-------
    for thisComponent in random_seedComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "random_seed" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    reward3 = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='reward3')
    thisExp.addLoop(reward3)  # add the loop to the experiment
    thisReward3 = reward3.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisReward3.rgb)
    if thisReward3 != None:
        for paramName in thisReward3:
            exec('{} = thisReward3[paramName]'.format(paramName))
    
    for thisReward3 in reward3:
        currentLoop = reward3
        # abbreviate parameter names if possible (e.g. rgb = thisReward3.rgb)
        if thisReward3 != None:
            for paramName in thisReward3:
                exec('{} = thisReward3[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "rewardframe1_3"-------
        continueRoutine = True
        # update component parameters for each repeat
        tree1_18.setPos((-0.5, -0.2))
        tree2_18.setPos((0.5, 0.2))
        tree3_18.setPos((-0.5, 0.6))
        tree4_18.setPos((0.5, -0.6))
        # setup some python lists for storing info about the mouse_3
        mouse_3.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        rewardframe1_3Components = [tree1_18, tree2_18, tree3_18, tree4_18, circle1, forward_11, squaree_3, mouse_3]
        for thisComponent in rewardframe1_3Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        rewardframe1_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "rewardframe1_3"-------
        while continueRoutine:
            # get current time
            t = rewardframe1_3Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=rewardframe1_3Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *tree1_18* updates
            if tree1_18.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree1_18.frameNStart = frameN  # exact frame index
                tree1_18.tStart = t  # local t and not account for scr refresh
                tree1_18.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree1_18, 'tStartRefresh')  # time at next scr refresh
                tree1_18.setAutoDraw(True)
            
            # *tree2_18* updates
            if tree2_18.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree2_18.frameNStart = frameN  # exact frame index
                tree2_18.tStart = t  # local t and not account for scr refresh
                tree2_18.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree2_18, 'tStartRefresh')  # time at next scr refresh
                tree2_18.setAutoDraw(True)
            if tree2_18.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree2_18.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree2_18.tStop = t  # not accounting for scr refresh
                    tree2_18.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree2_18, 'tStopRefresh')  # time at next scr refresh
                    tree2_18.setAutoDraw(False)
            
            # *tree3_18* updates
            if tree3_18.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree3_18.frameNStart = frameN  # exact frame index
                tree3_18.tStart = t  # local t and not account for scr refresh
                tree3_18.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree3_18, 'tStartRefresh')  # time at next scr refresh
                tree3_18.setAutoDraw(True)
            if tree3_18.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree3_18.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree3_18.tStop = t  # not accounting for scr refresh
                    tree3_18.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree3_18, 'tStopRefresh')  # time at next scr refresh
                    tree3_18.setAutoDraw(False)
            
            # *tree4_18* updates
            if tree4_18.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree4_18.frameNStart = frameN  # exact frame index
                tree4_18.tStart = t  # local t and not account for scr refresh
                tree4_18.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree4_18, 'tStartRefresh')  # time at next scr refresh
                tree4_18.setAutoDraw(True)
            if tree4_18.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree4_18.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree4_18.tStop = t  # not accounting for scr refresh
                    tree4_18.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree4_18, 'tStopRefresh')  # time at next scr refresh
                    tree4_18.setAutoDraw(False)
            
            # *circle1* updates
            if circle1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                circle1.frameNStart = frameN  # exact frame index
                circle1.tStart = t  # local t and not account for scr refresh
                circle1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle1, 'tStartRefresh')  # time at next scr refresh
                circle1.setAutoDraw(True)
            
            # *forward_11* updates
            if forward_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                forward_11.frameNStart = frameN  # exact frame index
                forward_11.tStart = t  # local t and not account for scr refresh
                forward_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(forward_11, 'tStartRefresh')  # time at next scr refresh
                forward_11.setAutoDraw(True)
            
            # *squaree_3* updates
            if squaree_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                squaree_3.frameNStart = frameN  # exact frame index
                squaree_3.tStart = t  # local t and not account for scr refresh
                squaree_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(squaree_3, 'tStartRefresh')  # time at next scr refresh
                squaree_3.setAutoDraw(True)
            if squaree_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > squaree_3.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    squaree_3.tStop = t  # not accounting for scr refresh
                    squaree_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(squaree_3, 'tStopRefresh')  # time at next scr refresh
                    squaree_3.setAutoDraw(False)
            # *mouse_3* updates
            if mouse_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_3.frameNStart = frameN  # exact frame index
                mouse_3.tStart = t  # local t and not account for scr refresh
                mouse_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_3, 'tStartRefresh')  # time at next scr refresh
                mouse_3.status = STARTED
                mouse_3.mouseClock.reset()
                prevButtonState = mouse_3.getPressed()  # if button is down already this ISN'T a new click
            if mouse_3.status == STARTED:  # only update if started and not finished!
                buttons = mouse_3.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter(circle1)
                            clickableList = circle1
                        except:
                            clickableList = [circle1]
                        for obj in clickableList:
                            if obj.contains(mouse_3):
                                gotValidClick = True
                                mouse_3.clicked_name.append(obj.name)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rewardframe1_3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "rewardframe1_3"-------
        for thisComponent in rewardframe1_3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        reward3.addData('tree1_18.started', tree1_18.tStartRefresh)
        reward3.addData('tree1_18.stopped', tree1_18.tStopRefresh)
        reward3.addData('tree2_18.started', tree2_18.tStartRefresh)
        reward3.addData('tree2_18.stopped', tree2_18.tStopRefresh)
        reward3.addData('tree3_18.started', tree3_18.tStartRefresh)
        reward3.addData('tree3_18.stopped', tree3_18.tStopRefresh)
        reward3.addData('tree4_18.started', tree4_18.tStartRefresh)
        reward3.addData('tree4_18.stopped', tree4_18.tStopRefresh)
        reward3.addData('circle1.started', circle1.tStartRefresh)
        reward3.addData('circle1.stopped', circle1.tStopRefresh)
        reward3.addData('forward_11.started', forward_11.tStartRefresh)
        reward3.addData('forward_11.stopped', forward_11.tStopRefresh)
        reward3.addData('squaree_3.started', squaree_3.tStartRefresh)
        reward3.addData('squaree_3.stopped', squaree_3.tStopRefresh)
        # store data for reward3 (TrialHandler)
        x, y = mouse_3.getPos()
        buttons = mouse_3.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            try:
                iter(circle1)
                clickableList = circle1
            except:
                clickableList = [circle1]
            for obj in clickableList:
                if obj.contains(mouse_3):
                    gotValidClick = True
                    mouse_3.clicked_name.append(obj.name)
        reward3.addData('mouse_3.x', x)
        reward3.addData('mouse_3.y', y)
        reward3.addData('mouse_3.leftButton', buttons[0])
        reward3.addData('mouse_3.midButton', buttons[1])
        reward3.addData('mouse_3.rightButton', buttons[2])
        if len(mouse_3.clicked_name):
            reward3.addData('mouse_3.clicked_name', mouse_3.clicked_name[0])
        reward3.addData('mouse_3.started', mouse_3.tStart)
        reward3.addData('mouse_3.stopped', mouse_3.tStop)
        # the Routine "rewardframe1_3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "rewardframe1_2"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        tree1_12.setPos((-0.5, -0.2))
        tree2_12.setPos((0.5, 0.2))
        tree3_12.setPos((-0.5, 0.6))
        tree4_12.setPos((0.5, -0.6))
        wait_3.setText('wait')
        # keep track of which components have finished
        rewardframe1_2Components = [tree1_12, tree2_12, tree3_12, tree4_12, circle2, wait_3, forward_2, squaree_2, gcircle]
        for thisComponent in rewardframe1_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        rewardframe1_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "rewardframe1_2"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = rewardframe1_2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=rewardframe1_2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *tree1_12* updates
            if tree1_12.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree1_12.frameNStart = frameN  # exact frame index
                tree1_12.tStart = t  # local t and not account for scr refresh
                tree1_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree1_12, 'tStartRefresh')  # time at next scr refresh
                tree1_12.setAutoDraw(True)
            if tree1_12.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree1_12.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    tree1_12.tStop = t  # not accounting for scr refresh
                    tree1_12.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree1_12, 'tStopRefresh')  # time at next scr refresh
                    tree1_12.setAutoDraw(False)
            
            # *tree2_12* updates
            if tree2_12.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree2_12.frameNStart = frameN  # exact frame index
                tree2_12.tStart = t  # local t and not account for scr refresh
                tree2_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree2_12, 'tStartRefresh')  # time at next scr refresh
                tree2_12.setAutoDraw(True)
            if tree2_12.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree2_12.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree2_12.tStop = t  # not accounting for scr refresh
                    tree2_12.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree2_12, 'tStopRefresh')  # time at next scr refresh
                    tree2_12.setAutoDraw(False)
            
            # *tree3_12* updates
            if tree3_12.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree3_12.frameNStart = frameN  # exact frame index
                tree3_12.tStart = t  # local t and not account for scr refresh
                tree3_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree3_12, 'tStartRefresh')  # time at next scr refresh
                tree3_12.setAutoDraw(True)
            if tree3_12.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree3_12.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree3_12.tStop = t  # not accounting for scr refresh
                    tree3_12.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree3_12, 'tStopRefresh')  # time at next scr refresh
                    tree3_12.setAutoDraw(False)
            
            # *tree4_12* updates
            if tree4_12.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree4_12.frameNStart = frameN  # exact frame index
                tree4_12.tStart = t  # local t and not account for scr refresh
                tree4_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree4_12, 'tStartRefresh')  # time at next scr refresh
                tree4_12.setAutoDraw(True)
            if tree4_12.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree4_12.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree4_12.tStop = t  # not accounting for scr refresh
                    tree4_12.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree4_12, 'tStopRefresh')  # time at next scr refresh
                    tree4_12.setAutoDraw(False)
            
            # *circle2* updates
            if circle2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                circle2.frameNStart = frameN  # exact frame index
                circle2.tStart = t  # local t and not account for scr refresh
                circle2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle2, 'tStartRefresh')  # time at next scr refresh
                circle2.setAutoDraw(True)
            if circle2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > circle2.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    circle2.tStop = t  # not accounting for scr refresh
                    circle2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(circle2, 'tStopRefresh')  # time at next scr refresh
                    circle2.setAutoDraw(False)
            
            # *wait_3* updates
            if wait_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wait_3.frameNStart = frameN  # exact frame index
                wait_3.tStart = t  # local t and not account for scr refresh
                wait_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wait_3, 'tStartRefresh')  # time at next scr refresh
                wait_3.setAutoDraw(True)
            if wait_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > wait_3.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    wait_3.tStop = t  # not accounting for scr refresh
                    wait_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(wait_3, 'tStopRefresh')  # time at next scr refresh
                    wait_3.setAutoDraw(False)
            
            # *forward_2* updates
            if forward_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                forward_2.frameNStart = frameN  # exact frame index
                forward_2.tStart = t  # local t and not account for scr refresh
                forward_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(forward_2, 'tStartRefresh')  # time at next scr refresh
                forward_2.setAutoDraw(True)
            if forward_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > forward_2.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    forward_2.tStop = t  # not accounting for scr refresh
                    forward_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(forward_2, 'tStopRefresh')  # time at next scr refresh
                    forward_2.setAutoDraw(False)
            
            # *squaree_2* updates
            if squaree_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                squaree_2.frameNStart = frameN  # exact frame index
                squaree_2.tStart = t  # local t and not account for scr refresh
                squaree_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(squaree_2, 'tStartRefresh')  # time at next scr refresh
                squaree_2.setAutoDraw(True)
            if squaree_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > squaree_2.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    squaree_2.tStop = t  # not accounting for scr refresh
                    squaree_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(squaree_2, 'tStopRefresh')  # time at next scr refresh
                    squaree_2.setAutoDraw(False)
            
            # *gcircle* updates
            if gcircle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                gcircle.frameNStart = frameN  # exact frame index
                gcircle.tStart = t  # local t and not account for scr refresh
                gcircle.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(gcircle, 'tStartRefresh')  # time at next scr refresh
                gcircle.setAutoDraw(True)
            if gcircle.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > gcircle.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    gcircle.tStop = t  # not accounting for scr refresh
                    gcircle.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(gcircle, 'tStopRefresh')  # time at next scr refresh
                    gcircle.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rewardframe1_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "rewardframe1_2"-------
        for thisComponent in rewardframe1_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        reward3.addData('tree1_12.started', tree1_12.tStartRefresh)
        reward3.addData('tree1_12.stopped', tree1_12.tStopRefresh)
        reward3.addData('tree2_12.started', tree2_12.tStartRefresh)
        reward3.addData('tree2_12.stopped', tree2_12.tStopRefresh)
        reward3.addData('tree3_12.started', tree3_12.tStartRefresh)
        reward3.addData('tree3_12.stopped', tree3_12.tStopRefresh)
        reward3.addData('tree4_12.started', tree4_12.tStartRefresh)
        reward3.addData('tree4_12.stopped', tree4_12.tStopRefresh)
        reward3.addData('circle2.started', circle2.tStartRefresh)
        reward3.addData('circle2.stopped', circle2.tStopRefresh)
        reward3.addData('wait_3.started', wait_3.tStartRefresh)
        reward3.addData('wait_3.stopped', wait_3.tStopRefresh)
        reward3.addData('forward_2.started', forward_2.tStartRefresh)
        reward3.addData('forward_2.stopped', forward_2.tStopRefresh)
        reward3.addData('squaree_2.started', squaree_2.tStartRefresh)
        reward3.addData('squaree_2.stopped', squaree_2.tStopRefresh)
        reward3.addData('gcircle.started', gcircle.tStartRefresh)
        reward3.addData('gcircle.stopped', gcircle.tStopRefresh)
        
        # ------Prepare to start Routine "rewardframe1"-------
        continueRoutine = True
        # update component parameters for each repeat
        tree1_4.setPos((-0.5, -0.2))
        tree2_4.setPos((0.5, 0.2))
        tree3_4.setPos((-0.5, 0.6))
        tree4_4.setPos((0.5, -0.6))
        reward_2.setText('')
        # setup some python lists for storing info about the resp
        resp.x = []
        resp.y = []
        resp.leftButton = []
        resp.midButton = []
        resp.rightButton = []
        resp.time = []
        resp.clicked_name = []
        gotValidClick = False  # until a click is received
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # setup some python lists for storing info about the sol
        sol.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        rewardframe1Components = [tree1_4, tree2_4, tree3_4, tree4_4, circle3, reward_2, resp, forward, key_resp, sol, gcircle_2, skipsq]
        for thisComponent in rewardframe1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        rewardframe1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "rewardframe1"-------
        while continueRoutine:
            # get current time
            t = rewardframe1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=rewardframe1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *tree1_4* updates
            if tree1_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree1_4.frameNStart = frameN  # exact frame index
                tree1_4.tStart = t  # local t and not account for scr refresh
                tree1_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree1_4, 'tStartRefresh')  # time at next scr refresh
                tree1_4.setAutoDraw(True)
            
            # *tree2_4* updates
            if tree2_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree2_4.frameNStart = frameN  # exact frame index
                tree2_4.tStart = t  # local t and not account for scr refresh
                tree2_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree2_4, 'tStartRefresh')  # time at next scr refresh
                tree2_4.setAutoDraw(True)
            if tree2_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree2_4.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree2_4.tStop = t  # not accounting for scr refresh
                    tree2_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree2_4, 'tStopRefresh')  # time at next scr refresh
                    tree2_4.setAutoDraw(False)
            
            # *tree3_4* updates
            if tree3_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree3_4.frameNStart = frameN  # exact frame index
                tree3_4.tStart = t  # local t and not account for scr refresh
                tree3_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree3_4, 'tStartRefresh')  # time at next scr refresh
                tree3_4.setAutoDraw(True)
            if tree3_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree3_4.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree3_4.tStop = t  # not accounting for scr refresh
                    tree3_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree3_4, 'tStopRefresh')  # time at next scr refresh
                    tree3_4.setAutoDraw(False)
            
            # *tree4_4* updates
            if tree4_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree4_4.frameNStart = frameN  # exact frame index
                tree4_4.tStart = t  # local t and not account for scr refresh
                tree4_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree4_4, 'tStartRefresh')  # time at next scr refresh
                tree4_4.setAutoDraw(True)
            if tree4_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree4_4.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree4_4.tStop = t  # not accounting for scr refresh
                    tree4_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree4_4, 'tStopRefresh')  # time at next scr refresh
                    tree4_4.setAutoDraw(False)
            
            # *circle3* updates
            if circle3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                circle3.frameNStart = frameN  # exact frame index
                circle3.tStart = t  # local t and not account for scr refresh
                circle3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle3, 'tStartRefresh')  # time at next scr refresh
                circle3.setAutoDraw(True)
            
            # *reward_2* updates
            if reward_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                reward_2.frameNStart = frameN  # exact frame index
                reward_2.tStart = t  # local t and not account for scr refresh
                reward_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(reward_2, 'tStartRefresh')  # time at next scr refresh
                reward_2.setAutoDraw(True)
            if reward_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > reward_2.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    reward_2.tStop = t  # not accounting for scr refresh
                    reward_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(reward_2, 'tStopRefresh')  # time at next scr refresh
                    reward_2.setAutoDraw(False)
            # *resp* updates
            if resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                resp.frameNStart = frameN  # exact frame index
                resp.tStart = t  # local t and not account for scr refresh
                resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
                resp.status = STARTED
                resp.mouseClock.reset()
                prevButtonState = resp.getPressed()  # if button is down already this ISN'T a new click
            if resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > resp.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    resp.tStop = t  # not accounting for scr refresh
                    resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(resp, 'tStopRefresh')  # time at next scr refresh
                    resp.status = FINISHED
            if resp.status == STARTED:  # only update if started and not finished!
                buttons = resp.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter(tree1_4)
                            clickableList = tree1_4
                        except:
                            clickableList = [tree1_4]
                        for obj in clickableList:
                            if obj.contains(resp):
                                gotValidClick = True
                                resp.clicked_name.append(obj.name)
                        x, y = resp.getPos()
                        resp.x.append(x)
                        resp.y.append(y)
                        buttons = resp.getPressed()
                        resp.leftButton.append(buttons[0])
                        resp.midButton.append(buttons[1])
                        resp.rightButton.append(buttons[2])
                        resp.time.append(resp.mouseClock.getTime())
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # *forward* updates
            if forward.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                forward.frameNStart = frameN  # exact frame index
                forward.tStart = t  # local t and not account for scr refresh
                forward.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(forward, 'tStartRefresh')  # time at next scr refresh
                forward.setAutoDraw(True)
            
            # *key_resp* updates
            waitOnFlip = False
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp.tStop = t  # not accounting for scr refresh
                    key_resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                    key_resp.status = FINISHED
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            # *sol* updates
            if sol.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sol.frameNStart = frameN  # exact frame index
                sol.tStart = t  # local t and not account for scr refresh
                sol.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sol, 'tStartRefresh')  # time at next scr refresh
                sol.status = STARTED
                sol.mouseClock.reset()
                prevButtonState = sol.getPressed()  # if button is down already this ISN'T a new click
            if sol.status == STARTED:  # only update if started and not finished!
                buttons = sol.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter(skipsq, tree1_4)
                            clickableList = skipsq, tree1_4
                        except:
                            clickableList = [skipsq, tree1_4]
                        for obj in clickableList:
                            if obj.contains(sol):
                                gotValidClick = True
                                sol.clicked_name.append(obj.name)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # *gcircle_2* updates
            if gcircle_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                gcircle_2.frameNStart = frameN  # exact frame index
                gcircle_2.tStart = t  # local t and not account for scr refresh
                gcircle_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(gcircle_2, 'tStartRefresh')  # time at next scr refresh
                gcircle_2.setAutoDraw(True)
            
            # *skipsq* updates
            if skipsq.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                skipsq.frameNStart = frameN  # exact frame index
                skipsq.tStart = t  # local t and not account for scr refresh
                skipsq.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(skipsq, 'tStartRefresh')  # time at next scr refresh
                skipsq.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rewardframe1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "rewardframe1"-------
        for thisComponent in rewardframe1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        reward3.addData('tree1_4.started', tree1_4.tStartRefresh)
        reward3.addData('tree1_4.stopped', tree1_4.tStopRefresh)
        reward3.addData('tree2_4.started', tree2_4.tStartRefresh)
        reward3.addData('tree2_4.stopped', tree2_4.tStopRefresh)
        reward3.addData('tree3_4.started', tree3_4.tStartRefresh)
        reward3.addData('tree3_4.stopped', tree3_4.tStopRefresh)
        reward3.addData('tree4_4.started', tree4_4.tStartRefresh)
        reward3.addData('tree4_4.stopped', tree4_4.tStopRefresh)
        reward3.addData('circle3.started', circle3.tStartRefresh)
        reward3.addData('circle3.stopped', circle3.tStopRefresh)
        reward3.addData('reward_2.started', reward_2.tStartRefresh)
        reward3.addData('reward_2.stopped', reward_2.tStopRefresh)
        # store data for reward3 (TrialHandler)
        if len(resp.x): reward3.addData('resp.x', resp.x[0])
        if len(resp.y): reward3.addData('resp.y', resp.y[0])
        if len(resp.leftButton): reward3.addData('resp.leftButton', resp.leftButton[0])
        if len(resp.midButton): reward3.addData('resp.midButton', resp.midButton[0])
        if len(resp.rightButton): reward3.addData('resp.rightButton', resp.rightButton[0])
        if len(resp.time): reward3.addData('resp.time', resp.time[0])
        if len(resp.clicked_name): reward3.addData('resp.clicked_name', resp.clicked_name[0])
        reward3.addData('resp.started', resp.tStart)
        reward3.addData('resp.stopped', resp.tStop)
        reward3.addData('forward.started', forward.tStartRefresh)
        reward3.addData('forward.stopped', forward.tStopRefresh)
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        reward3.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            reward3.addData('key_resp.rt', key_resp.rt)
        reward3.addData('key_resp.started', key_resp.tStartRefresh)
        reward3.addData('key_resp.stopped', key_resp.tStopRefresh)
        # store data for reward3 (TrialHandler)
        x, y = sol.getPos()
        buttons = sol.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            try:
                iter(skipsq, tree1_4)
                clickableList = skipsq, tree1_4
            except:
                clickableList = [skipsq, tree1_4]
            for obj in clickableList:
                if obj.contains(sol):
                    gotValidClick = True
                    sol.clicked_name.append(obj.name)
        reward3.addData('sol.x', x)
        reward3.addData('sol.y', y)
        reward3.addData('sol.leftButton', buttons[0])
        reward3.addData('sol.midButton', buttons[1])
        reward3.addData('sol.rightButton', buttons[2])
        if len(sol.clicked_name):
            reward3.addData('sol.clicked_name', sol.clicked_name[0])
        reward3.addData('sol.started', sol.tStart)
        reward3.addData('sol.stopped', sol.tStop)
        reward3.addData('gcircle_2.started', gcircle_2.tStartRefresh)
        reward3.addData('gcircle_2.stopped', gcircle_2.tStopRefresh)
        reward3.addData('skipsq.started', skipsq.tStartRefresh)
        reward3.addData('skipsq.stopped', skipsq.tStopRefresh)
        # the Routine "rewardframe1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "rewardframe1_4"-------
        continueRoutine = True
        routineTimer.add(1.000100)
        # update component parameters for each repeat
        display=17
        if random_seed==1:
            if a1i>5:
                display=0
            else:
                display=a1[a1i];
            a1i=a1i+1;
        elif random_seed==2:
            if a2i>5:
                display=0
            else:
                display=a2[a2i];
            a2i=a2i+1;
        elif random_seed==3:
            if a3i>5:
                display=0
            else:
                display=a3[a3i];
            a3i=a3i+1;
        elif random_seed==4:
            if a4i>5:
                display=0
            else:
                display=a4[a4i];
            a4i=a4i+1;
        else:
            if a5i>5:
                display=0
            else:
                display=a5[a5i];
            a5i=a5i+1;
        if sol.clicked_name[0] =='skipsq':
            continueRoutine = False
            reward1.finished = True
        tree1_19.setPos((-0.5, -0.2))
        tree2_19.setPos((0.5, 0.2))
        tree3_19.setPos((-0.5, 0.6))
        tree4_19.setPos((0.5, -0.6))
        wait_8.setText('wait')
        reward_7.setText(display)
        # keep track of which components have finished
        rewardframe1_4Components = [tree1_19, tree2_19, tree3_19, tree4_19, circle4, wait_8, forward_12, squaree_4, gcircle_3, reward_7, gcircle_4]
        for thisComponent in rewardframe1_4Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        rewardframe1_4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "rewardframe1_4"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = rewardframe1_4Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=rewardframe1_4Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *tree1_19* updates
            if tree1_19.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree1_19.frameNStart = frameN  # exact frame index
                tree1_19.tStart = t  # local t and not account for scr refresh
                tree1_19.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree1_19, 'tStartRefresh')  # time at next scr refresh
                tree1_19.setAutoDraw(True)
            if tree1_19.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree1_19.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    tree1_19.tStop = t  # not accounting for scr refresh
                    tree1_19.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree1_19, 'tStopRefresh')  # time at next scr refresh
                    tree1_19.setAutoDraw(False)
            
            # *tree2_19* updates
            if tree2_19.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree2_19.frameNStart = frameN  # exact frame index
                tree2_19.tStart = t  # local t and not account for scr refresh
                tree2_19.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree2_19, 'tStartRefresh')  # time at next scr refresh
                tree2_19.setAutoDraw(True)
            if tree2_19.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree2_19.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree2_19.tStop = t  # not accounting for scr refresh
                    tree2_19.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree2_19, 'tStopRefresh')  # time at next scr refresh
                    tree2_19.setAutoDraw(False)
            
            # *tree3_19* updates
            if tree3_19.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree3_19.frameNStart = frameN  # exact frame index
                tree3_19.tStart = t  # local t and not account for scr refresh
                tree3_19.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree3_19, 'tStartRefresh')  # time at next scr refresh
                tree3_19.setAutoDraw(True)
            if tree3_19.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree3_19.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree3_19.tStop = t  # not accounting for scr refresh
                    tree3_19.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree3_19, 'tStopRefresh')  # time at next scr refresh
                    tree3_19.setAutoDraw(False)
            
            # *tree4_19* updates
            if tree4_19.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree4_19.frameNStart = frameN  # exact frame index
                tree4_19.tStart = t  # local t and not account for scr refresh
                tree4_19.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree4_19, 'tStartRefresh')  # time at next scr refresh
                tree4_19.setAutoDraw(True)
            if tree4_19.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree4_19.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree4_19.tStop = t  # not accounting for scr refresh
                    tree4_19.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree4_19, 'tStopRefresh')  # time at next scr refresh
                    tree4_19.setAutoDraw(False)
            
            # *circle4* updates
            if circle4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                circle4.frameNStart = frameN  # exact frame index
                circle4.tStart = t  # local t and not account for scr refresh
                circle4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle4, 'tStartRefresh')  # time at next scr refresh
                circle4.setAutoDraw(True)
            if circle4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > circle4.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    circle4.tStop = t  # not accounting for scr refresh
                    circle4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(circle4, 'tStopRefresh')  # time at next scr refresh
                    circle4.setAutoDraw(False)
            
            # *wait_8* updates
            if wait_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wait_8.frameNStart = frameN  # exact frame index
                wait_8.tStart = t  # local t and not account for scr refresh
                wait_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wait_8, 'tStartRefresh')  # time at next scr refresh
                wait_8.setAutoDraw(True)
            if wait_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > wait_8.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    wait_8.tStop = t  # not accounting for scr refresh
                    wait_8.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(wait_8, 'tStopRefresh')  # time at next scr refresh
                    wait_8.setAutoDraw(False)
            
            # *forward_12* updates
            if forward_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                forward_12.frameNStart = frameN  # exact frame index
                forward_12.tStart = t  # local t and not account for scr refresh
                forward_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(forward_12, 'tStartRefresh')  # time at next scr refresh
                forward_12.setAutoDraw(True)
            if forward_12.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > forward_12.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    forward_12.tStop = t  # not accounting for scr refresh
                    forward_12.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(forward_12, 'tStopRefresh')  # time at next scr refresh
                    forward_12.setAutoDraw(False)
            
            # *squaree_4* updates
            if squaree_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                squaree_4.frameNStart = frameN  # exact frame index
                squaree_4.tStart = t  # local t and not account for scr refresh
                squaree_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(squaree_4, 'tStartRefresh')  # time at next scr refresh
                squaree_4.setAutoDraw(True)
            if squaree_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > squaree_4.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    squaree_4.tStop = t  # not accounting for scr refresh
                    squaree_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(squaree_4, 'tStopRefresh')  # time at next scr refresh
                    squaree_4.setAutoDraw(False)
            
            # *gcircle_3* updates
            if gcircle_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                gcircle_3.frameNStart = frameN  # exact frame index
                gcircle_3.tStart = t  # local t and not account for scr refresh
                gcircle_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(gcircle_3, 'tStartRefresh')  # time at next scr refresh
                gcircle_3.setAutoDraw(True)
            if gcircle_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > gcircle_3.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    gcircle_3.tStop = t  # not accounting for scr refresh
                    gcircle_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(gcircle_3, 'tStopRefresh')  # time at next scr refresh
                    gcircle_3.setAutoDraw(False)
            
            # *reward_7* updates
            if reward_7.status == NOT_STARTED and tThisFlip >= 0.0001-frameTolerance:
                # keep track of start time/frame for later
                reward_7.frameNStart = frameN  # exact frame index
                reward_7.tStart = t  # local t and not account for scr refresh
                reward_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(reward_7, 'tStartRefresh')  # time at next scr refresh
                reward_7.setAutoDraw(True)
            if reward_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > reward_7.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    reward_7.tStop = t  # not accounting for scr refresh
                    reward_7.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(reward_7, 'tStopRefresh')  # time at next scr refresh
                    reward_7.setAutoDraw(False)
            
            # *gcircle_4* updates
            if gcircle_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                gcircle_4.frameNStart = frameN  # exact frame index
                gcircle_4.tStart = t  # local t and not account for scr refresh
                gcircle_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(gcircle_4, 'tStartRefresh')  # time at next scr refresh
                gcircle_4.setAutoDraw(True)
            if gcircle_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > gcircle_4.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    gcircle_4.tStop = t  # not accounting for scr refresh
                    gcircle_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(gcircle_4, 'tStopRefresh')  # time at next scr refresh
                    gcircle_4.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rewardframe1_4Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "rewardframe1_4"-------
        for thisComponent in rewardframe1_4Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData("randint",display)
        print(display)
        reward3.addData('tree1_19.started', tree1_19.tStartRefresh)
        reward3.addData('tree1_19.stopped', tree1_19.tStopRefresh)
        reward3.addData('tree2_19.started', tree2_19.tStartRefresh)
        reward3.addData('tree2_19.stopped', tree2_19.tStopRefresh)
        reward3.addData('tree3_19.started', tree3_19.tStartRefresh)
        reward3.addData('tree3_19.stopped', tree3_19.tStopRefresh)
        reward3.addData('tree4_19.started', tree4_19.tStartRefresh)
        reward3.addData('tree4_19.stopped', tree4_19.tStopRefresh)
        reward3.addData('circle4.started', circle4.tStartRefresh)
        reward3.addData('circle4.stopped', circle4.tStopRefresh)
        reward3.addData('wait_8.started', wait_8.tStartRefresh)
        reward3.addData('wait_8.stopped', wait_8.tStopRefresh)
        reward3.addData('forward_12.started', forward_12.tStartRefresh)
        reward3.addData('forward_12.stopped', forward_12.tStopRefresh)
        reward3.addData('squaree_4.started', squaree_4.tStartRefresh)
        reward3.addData('squaree_4.stopped', squaree_4.tStopRefresh)
        reward3.addData('gcircle_3.started', gcircle_3.tStartRefresh)
        reward3.addData('gcircle_3.stopped', gcircle_3.tStopRefresh)
        reward3.addData('reward_7.started', reward_7.tStartRefresh)
        reward3.addData('reward_7.stopped', reward_7.tStopRefresh)
        reward3.addData('gcircle_4.started', gcircle_4.tStartRefresh)
        reward3.addData('gcircle_4.stopped', gcircle_4.tStopRefresh)
    # completed 1.0 repeats of 'reward3'
    
    
    # set up handler to look after randomisation of conditions etc
    pos3 = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('pos.xlsx'),
        seed=None, name='pos3')
    thisExp.addLoop(pos3)  # add the loop to the experiment
    thisPos3 = pos3.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPos3.rgb)
    if thisPos3 != None:
        for paramName in thisPos3:
            exec('{} = thisPos3[paramName]'.format(paramName))
    
    for thisPos3 in pos3:
        currentLoop = pos3
        # abbreviate parameter names if possible (e.g. rgb = thisPos3.rgb)
        if thisPos3 != None:
            for paramName in thisPos3:
                exec('{} = thisPos3[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "movetrees3"-------
        continueRoutine = True
        routineTimer.add(0.100000)
        # update component parameters for each repeat
        tree1_23.setPos((-0.5, tree1_n))
        tree2_23.setPos((0.5, tree2_p))
        tree4_23.setPos((0, 0))
        # keep track of which components have finished
        movetrees3Components = [tree1_23, tree2_23, tree3_23, tree4_23, circle_7]
        for thisComponent in movetrees3Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        movetrees3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "movetrees3"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = movetrees3Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=movetrees3Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *tree1_23* updates
            if tree1_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                tree1_23.frameNStart = frameN  # exact frame index
                tree1_23.tStart = t  # local t and not account for scr refresh
                tree1_23.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree1_23, 'tStartRefresh')  # time at next scr refresh
                tree1_23.setAutoDraw(True)
            if tree1_23.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree1_23.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    tree1_23.tStop = t  # not accounting for scr refresh
                    tree1_23.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree1_23, 'tStopRefresh')  # time at next scr refresh
                    tree1_23.setAutoDraw(False)
            
            # *tree2_23* updates
            if tree2_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                tree2_23.frameNStart = frameN  # exact frame index
                tree2_23.tStart = t  # local t and not account for scr refresh
                tree2_23.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree2_23, 'tStartRefresh')  # time at next scr refresh
                tree2_23.setAutoDraw(True)
            if tree2_23.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree2_23.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    tree2_23.tStop = t  # not accounting for scr refresh
                    tree2_23.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree2_23, 'tStopRefresh')  # time at next scr refresh
                    tree2_23.setAutoDraw(False)
            
            # *tree3_23* updates
            if tree3_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                tree3_23.frameNStart = frameN  # exact frame index
                tree3_23.tStart = t  # local t and not account for scr refresh
                tree3_23.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree3_23, 'tStartRefresh')  # time at next scr refresh
                tree3_23.setAutoDraw(True)
            if tree3_23.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree3_23.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree3_23.tStop = t  # not accounting for scr refresh
                    tree3_23.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree3_23, 'tStopRefresh')  # time at next scr refresh
                    tree3_23.setAutoDraw(False)
            
            # *tree4_23* updates
            if tree4_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                tree4_23.frameNStart = frameN  # exact frame index
                tree4_23.tStart = t  # local t and not account for scr refresh
                tree4_23.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree4_23, 'tStartRefresh')  # time at next scr refresh
                tree4_23.setAutoDraw(True)
            if tree4_23.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree4_23.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree4_23.tStop = t  # not accounting for scr refresh
                    tree4_23.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree4_23, 'tStopRefresh')  # time at next scr refresh
                    tree4_23.setAutoDraw(False)
            
            # *circle_7* updates
            if circle_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                circle_7.frameNStart = frameN  # exact frame index
                circle_7.tStart = t  # local t and not account for scr refresh
                circle_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle_7, 'tStartRefresh')  # time at next scr refresh
                circle_7.setAutoDraw(True)
            if circle_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > circle_7.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    circle_7.tStop = t  # not accounting for scr refresh
                    circle_7.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(circle_7, 'tStopRefresh')  # time at next scr refresh
                    circle_7.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in movetrees3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "movetrees3"-------
        for thisComponent in movetrees3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        pos3.addData('tree1_23.started', tree1_23.tStartRefresh)
        pos3.addData('tree1_23.stopped', tree1_23.tStopRefresh)
        pos3.addData('tree2_23.started', tree2_23.tStartRefresh)
        pos3.addData('tree2_23.stopped', tree2_23.tStopRefresh)
        pos3.addData('tree3_23.started', tree3_23.tStartRefresh)
        pos3.addData('tree3_23.stopped', tree3_23.tStopRefresh)
        pos3.addData('tree4_23.started', tree4_23.tStartRefresh)
        pos3.addData('tree4_23.stopped', tree4_23.tStopRefresh)
        pos3.addData('circle_7.started', circle_7.tStartRefresh)
        pos3.addData('circle_7.stopped', circle_7.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'pos3'
    
    
    # ------Prepare to start Routine "random_seed"-------
    continueRoutine = True
    # update component parameters for each repeat
    from random import randint
    random_seed= randint(1,5)
    a1i=0
    a2i=0
    a3i=0
    a4i=0
    a5i=0
    a1=[7.5,7.1,6.2,5.9,5.1,4.8,4,3.1,2.6,2.1,1.3,0.7,0]
    a2=[7.3,6.9,6.2,5.8,5.1,4.6,4,3.2,2.4,1.3,0]
    a3=[7.6,7.1,6.8,6.3,5.9,5.4,4.6,3.9,3.2,2.4,1.7,1.1,0]
    a4=[7.1,6.6,6.1,5.8,5.3,4.8,4,3.6,3.1,2.7,2.1,1.3,0]
    a5=[7.4,6.8,6.1,5.8,5.1,4.6,4.1,3.6,2.8,2.1,1.4,0]
    display=14
    # keep track of which components have finished
    random_seedComponents = []
    for thisComponent in random_seedComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    random_seedClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "random_seed"-------
    while continueRoutine:
        # get current time
        t = random_seedClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=random_seedClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in random_seedComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "random_seed"-------
    for thisComponent in random_seedComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "random_seed" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_4 = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('pos.xlsx'),
        seed=None, name='trials_4')
    thisExp.addLoop(trials_4)  # add the loop to the experiment
    thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4:
            exec('{} = thisTrial_4[paramName]'.format(paramName))
    
    for thisTrial_4 in trials_4:
        currentLoop = trials_4
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
        if thisTrial_4 != None:
            for paramName in thisTrial_4:
                exec('{} = thisTrial_4[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "rewardframe2_3"-------
        continueRoutine = True
        # update component parameters for each repeat
        tree1_20.setPos((-0.5, -0.6))
        tree2_20.setPos((0.5, -0.2))
        tree3_20.setPos((-0.5, 0.2))
        tree4_20.setPos((0.5, 0.6))
        # setup some python lists for storing info about the mouse_4
        mouse_4.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        rewardframe2_3Components = [tree1_20, tree2_20, tree3_20, tree4_20, circle, forward_13, square1, mouse_4]
        for thisComponent in rewardframe2_3Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        rewardframe2_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "rewardframe2_3"-------
        while continueRoutine:
            # get current time
            t = rewardframe2_3Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=rewardframe2_3Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *tree1_20* updates
            if tree1_20.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree1_20.frameNStart = frameN  # exact frame index
                tree1_20.tStart = t  # local t and not account for scr refresh
                tree1_20.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree1_20, 'tStartRefresh')  # time at next scr refresh
                tree1_20.setAutoDraw(True)
            if tree1_20.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree1_20.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree1_20.tStop = t  # not accounting for scr refresh
                    tree1_20.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree1_20, 'tStopRefresh')  # time at next scr refresh
                    tree1_20.setAutoDraw(False)
            
            # *tree2_20* updates
            if tree2_20.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree2_20.frameNStart = frameN  # exact frame index
                tree2_20.tStart = t  # local t and not account for scr refresh
                tree2_20.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree2_20, 'tStartRefresh')  # time at next scr refresh
                tree2_20.setAutoDraw(True)
            
            # *tree3_20* updates
            if tree3_20.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree3_20.frameNStart = frameN  # exact frame index
                tree3_20.tStart = t  # local t and not account for scr refresh
                tree3_20.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree3_20, 'tStartRefresh')  # time at next scr refresh
                tree3_20.setAutoDraw(True)
            if tree3_20.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree3_20.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree3_20.tStop = t  # not accounting for scr refresh
                    tree3_20.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree3_20, 'tStopRefresh')  # time at next scr refresh
                    tree3_20.setAutoDraw(False)
            
            # *tree4_20* updates
            if tree4_20.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree4_20.frameNStart = frameN  # exact frame index
                tree4_20.tStart = t  # local t and not account for scr refresh
                tree4_20.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree4_20, 'tStartRefresh')  # time at next scr refresh
                tree4_20.setAutoDraw(True)
            if tree4_20.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree4_20.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree4_20.tStop = t  # not accounting for scr refresh
                    tree4_20.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree4_20, 'tStopRefresh')  # time at next scr refresh
                    tree4_20.setAutoDraw(False)
            
            # *circle* updates
            if circle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                circle.frameNStart = frameN  # exact frame index
                circle.tStart = t  # local t and not account for scr refresh
                circle.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle, 'tStartRefresh')  # time at next scr refresh
                circle.setAutoDraw(True)
            
            # *forward_13* updates
            if forward_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                forward_13.frameNStart = frameN  # exact frame index
                forward_13.tStart = t  # local t and not account for scr refresh
                forward_13.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(forward_13, 'tStartRefresh')  # time at next scr refresh
                forward_13.setAutoDraw(True)
            
            # *square1* updates
            if square1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                square1.frameNStart = frameN  # exact frame index
                square1.tStart = t  # local t and not account for scr refresh
                square1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square1, 'tStartRefresh')  # time at next scr refresh
                square1.setAutoDraw(True)
            if square1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > square1.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    square1.tStop = t  # not accounting for scr refresh
                    square1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(square1, 'tStopRefresh')  # time at next scr refresh
                    square1.setAutoDraw(False)
            # *mouse_4* updates
            if mouse_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_4.frameNStart = frameN  # exact frame index
                mouse_4.tStart = t  # local t and not account for scr refresh
                mouse_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_4, 'tStartRefresh')  # time at next scr refresh
                mouse_4.status = STARTED
                mouse_4.mouseClock.reset()
                prevButtonState = mouse_4.getPressed()  # if button is down already this ISN'T a new click
            if mouse_4.status == STARTED:  # only update if started and not finished!
                buttons = mouse_4.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter(circle)
                            clickableList = circle
                        except:
                            clickableList = [circle]
                        for obj in clickableList:
                            if obj.contains(mouse_4):
                                gotValidClick = True
                                mouse_4.clicked_name.append(obj.name)
                        # abort routine on response
                        continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rewardframe2_3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "rewardframe2_3"-------
        for thisComponent in rewardframe2_3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_4.addData('tree1_20.started', tree1_20.tStartRefresh)
        trials_4.addData('tree1_20.stopped', tree1_20.tStopRefresh)
        trials_4.addData('tree2_20.started', tree2_20.tStartRefresh)
        trials_4.addData('tree2_20.stopped', tree2_20.tStopRefresh)
        trials_4.addData('tree3_20.started', tree3_20.tStartRefresh)
        trials_4.addData('tree3_20.stopped', tree3_20.tStopRefresh)
        trials_4.addData('tree4_20.started', tree4_20.tStartRefresh)
        trials_4.addData('tree4_20.stopped', tree4_20.tStopRefresh)
        trials_4.addData('circle.started', circle.tStartRefresh)
        trials_4.addData('circle.stopped', circle.tStopRefresh)
        trials_4.addData('forward_13.started', forward_13.tStartRefresh)
        trials_4.addData('forward_13.stopped', forward_13.tStopRefresh)
        trials_4.addData('square1.started', square1.tStartRefresh)
        trials_4.addData('square1.stopped', square1.tStopRefresh)
        # store data for trials_4 (TrialHandler)
        x, y = mouse_4.getPos()
        buttons = mouse_4.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            try:
                iter(circle)
                clickableList = circle
            except:
                clickableList = [circle]
            for obj in clickableList:
                if obj.contains(mouse_4):
                    gotValidClick = True
                    mouse_4.clicked_name.append(obj.name)
        trials_4.addData('mouse_4.x', x)
        trials_4.addData('mouse_4.y', y)
        trials_4.addData('mouse_4.leftButton', buttons[0])
        trials_4.addData('mouse_4.midButton', buttons[1])
        trials_4.addData('mouse_4.rightButton', buttons[2])
        if len(mouse_4.clicked_name):
            trials_4.addData('mouse_4.clicked_name', mouse_4.clicked_name[0])
        trials_4.addData('mouse_4.started', mouse_4.tStart)
        trials_4.addData('mouse_4.stopped', mouse_4.tStop)
        # the Routine "rewardframe2_3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "rewardframe2_2"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        tree1_13.setPos((-0.5, -0.6))
        tree2_13.setPos((0.5, -0.2))
        tree3_13.setPos((-0.5, 0.2))
        tree4_13.setPos((0.5, 0.6))
        wait.setText('wait')
        # keep track of which components have finished
        rewardframe2_2Components = [tree1_13, tree2_13, tree3_13, tree4_13, circle6, wait, forward_3]
        for thisComponent in rewardframe2_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        rewardframe2_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "rewardframe2_2"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = rewardframe2_2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=rewardframe2_2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *tree1_13* updates
            if tree1_13.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree1_13.frameNStart = frameN  # exact frame index
                tree1_13.tStart = t  # local t and not account for scr refresh
                tree1_13.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree1_13, 'tStartRefresh')  # time at next scr refresh
                tree1_13.setAutoDraw(True)
            if tree1_13.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree1_13.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree1_13.tStop = t  # not accounting for scr refresh
                    tree1_13.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree1_13, 'tStopRefresh')  # time at next scr refresh
                    tree1_13.setAutoDraw(False)
            
            # *tree2_13* updates
            if tree2_13.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree2_13.frameNStart = frameN  # exact frame index
                tree2_13.tStart = t  # local t and not account for scr refresh
                tree2_13.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree2_13, 'tStartRefresh')  # time at next scr refresh
                tree2_13.setAutoDraw(True)
            if tree2_13.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree2_13.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    tree2_13.tStop = t  # not accounting for scr refresh
                    tree2_13.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree2_13, 'tStopRefresh')  # time at next scr refresh
                    tree2_13.setAutoDraw(False)
            
            # *tree3_13* updates
            if tree3_13.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree3_13.frameNStart = frameN  # exact frame index
                tree3_13.tStart = t  # local t and not account for scr refresh
                tree3_13.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree3_13, 'tStartRefresh')  # time at next scr refresh
                tree3_13.setAutoDraw(True)
            if tree3_13.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree3_13.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree3_13.tStop = t  # not accounting for scr refresh
                    tree3_13.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree3_13, 'tStopRefresh')  # time at next scr refresh
                    tree3_13.setAutoDraw(False)
            
            # *tree4_13* updates
            if tree4_13.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree4_13.frameNStart = frameN  # exact frame index
                tree4_13.tStart = t  # local t and not account for scr refresh
                tree4_13.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree4_13, 'tStartRefresh')  # time at next scr refresh
                tree4_13.setAutoDraw(True)
            if tree4_13.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree4_13.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree4_13.tStop = t  # not accounting for scr refresh
                    tree4_13.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree4_13, 'tStopRefresh')  # time at next scr refresh
                    tree4_13.setAutoDraw(False)
            
            # *circle6* updates
            if circle6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                circle6.frameNStart = frameN  # exact frame index
                circle6.tStart = t  # local t and not account for scr refresh
                circle6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle6, 'tStartRefresh')  # time at next scr refresh
                circle6.setAutoDraw(True)
            if circle6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > circle6.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    circle6.tStop = t  # not accounting for scr refresh
                    circle6.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(circle6, 'tStopRefresh')  # time at next scr refresh
                    circle6.setAutoDraw(False)
            
            # *wait* updates
            if wait.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wait.frameNStart = frameN  # exact frame index
                wait.tStart = t  # local t and not account for scr refresh
                wait.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wait, 'tStartRefresh')  # time at next scr refresh
                wait.setAutoDraw(True)
            if wait.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > wait.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    wait.tStop = t  # not accounting for scr refresh
                    wait.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(wait, 'tStopRefresh')  # time at next scr refresh
                    wait.setAutoDraw(False)
            
            # *forward_3* updates
            if forward_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                forward_3.frameNStart = frameN  # exact frame index
                forward_3.tStart = t  # local t and not account for scr refresh
                forward_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(forward_3, 'tStartRefresh')  # time at next scr refresh
                forward_3.setAutoDraw(True)
            if forward_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > forward_3.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    forward_3.tStop = t  # not accounting for scr refresh
                    forward_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(forward_3, 'tStopRefresh')  # time at next scr refresh
                    forward_3.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rewardframe2_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "rewardframe2_2"-------
        for thisComponent in rewardframe2_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_4.addData('tree1_13.started', tree1_13.tStartRefresh)
        trials_4.addData('tree1_13.stopped', tree1_13.tStopRefresh)
        trials_4.addData('tree2_13.started', tree2_13.tStartRefresh)
        trials_4.addData('tree2_13.stopped', tree2_13.tStopRefresh)
        trials_4.addData('tree3_13.started', tree3_13.tStartRefresh)
        trials_4.addData('tree3_13.stopped', tree3_13.tStopRefresh)
        trials_4.addData('tree4_13.started', tree4_13.tStartRefresh)
        trials_4.addData('tree4_13.stopped', tree4_13.tStopRefresh)
        trials_4.addData('circle6.started', circle6.tStartRefresh)
        trials_4.addData('circle6.stopped', circle6.tStopRefresh)
        trials_4.addData('wait.started', wait.tStartRefresh)
        trials_4.addData('wait.stopped', wait.tStopRefresh)
        trials_4.addData('forward_3.started', forward_3.tStartRefresh)
        trials_4.addData('forward_3.stopped', forward_3.tStopRefresh)
        
        # ------Prepare to start Routine "rewardframe2"-------
        continueRoutine = True
        # update component parameters for each repeat
        tree1_5.setPos((-0.5, -0.6))
        tree2_5.setPos((0.5, -0.2))
        tree3_5.setPos((-0.5, 0.2))
        tree4_5.setPos((0.5, 0.6))
        reward_3.setText('\n')
        # setup some python lists for storing info about the mouse_6
        mouse_6.clicked_name = []
        gotValidClick = False  # until a click is received
        # setup some python lists for storing info about the sol_2
        sol_2.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        rewardframe2Components = [tree1_5, tree2_5, tree3_5, tree4_5, circle_5, reward_3, mouse_6, forward_7, sol_2, gcircle_5, skipsq_2]
        for thisComponent in rewardframe2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        rewardframe2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "rewardframe2"-------
        while continueRoutine:
            # get current time
            t = rewardframe2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=rewardframe2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *tree1_5* updates
            if tree1_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree1_5.frameNStart = frameN  # exact frame index
                tree1_5.tStart = t  # local t and not account for scr refresh
                tree1_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree1_5, 'tStartRefresh')  # time at next scr refresh
                tree1_5.setAutoDraw(True)
            if tree1_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree1_5.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree1_5.tStop = t  # not accounting for scr refresh
                    tree1_5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree1_5, 'tStopRefresh')  # time at next scr refresh
                    tree1_5.setAutoDraw(False)
            
            # *tree2_5* updates
            if tree2_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree2_5.frameNStart = frameN  # exact frame index
                tree2_5.tStart = t  # local t and not account for scr refresh
                tree2_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree2_5, 'tStartRefresh')  # time at next scr refresh
                tree2_5.setAutoDraw(True)
            
            # *tree3_5* updates
            if tree3_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree3_5.frameNStart = frameN  # exact frame index
                tree3_5.tStart = t  # local t and not account for scr refresh
                tree3_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree3_5, 'tStartRefresh')  # time at next scr refresh
                tree3_5.setAutoDraw(True)
            if tree3_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree3_5.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree3_5.tStop = t  # not accounting for scr refresh
                    tree3_5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree3_5, 'tStopRefresh')  # time at next scr refresh
                    tree3_5.setAutoDraw(False)
            
            # *tree4_5* updates
            if tree4_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree4_5.frameNStart = frameN  # exact frame index
                tree4_5.tStart = t  # local t and not account for scr refresh
                tree4_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree4_5, 'tStartRefresh')  # time at next scr refresh
                tree4_5.setAutoDraw(True)
            if tree4_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree4_5.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree4_5.tStop = t  # not accounting for scr refresh
                    tree4_5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree4_5, 'tStopRefresh')  # time at next scr refresh
                    tree4_5.setAutoDraw(False)
            
            # *circle_5* updates
            if circle_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                circle_5.frameNStart = frameN  # exact frame index
                circle_5.tStart = t  # local t and not account for scr refresh
                circle_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle_5, 'tStartRefresh')  # time at next scr refresh
                circle_5.setAutoDraw(True)
            
            # *reward_3* updates
            if reward_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                reward_3.frameNStart = frameN  # exact frame index
                reward_3.tStart = t  # local t and not account for scr refresh
                reward_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(reward_3, 'tStartRefresh')  # time at next scr refresh
                reward_3.setAutoDraw(True)
            if reward_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > reward_3.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    reward_3.tStop = t  # not accounting for scr refresh
                    reward_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(reward_3, 'tStopRefresh')  # time at next scr refresh
                    reward_3.setAutoDraw(False)
            # *mouse_6* updates
            if mouse_6.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_6.frameNStart = frameN  # exact frame index
                mouse_6.tStart = t  # local t and not account for scr refresh
                mouse_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_6, 'tStartRefresh')  # time at next scr refresh
                mouse_6.status = STARTED
                mouse_6.mouseClock.reset()
                prevButtonState = mouse_6.getPressed()  # if button is down already this ISN'T a new click
            if mouse_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > mouse_6.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    mouse_6.tStop = t  # not accounting for scr refresh
                    mouse_6.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(mouse_6, 'tStopRefresh')  # time at next scr refresh
                    mouse_6.status = FINISHED
            if mouse_6.status == STARTED:  # only update if started and not finished!
                buttons = mouse_6.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter(tree2_5)
                            clickableList = tree2_5
                        except:
                            clickableList = [tree2_5]
                        for obj in clickableList:
                            if obj.contains(mouse_6):
                                gotValidClick = True
                                mouse_6.clicked_name.append(obj.name)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # *forward_7* updates
            if forward_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                forward_7.frameNStart = frameN  # exact frame index
                forward_7.tStart = t  # local t and not account for scr refresh
                forward_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(forward_7, 'tStartRefresh')  # time at next scr refresh
                forward_7.setAutoDraw(True)
            # *sol_2* updates
            if sol_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sol_2.frameNStart = frameN  # exact frame index
                sol_2.tStart = t  # local t and not account for scr refresh
                sol_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sol_2, 'tStartRefresh')  # time at next scr refresh
                sol_2.status = STARTED
                sol_2.mouseClock.reset()
                prevButtonState = sol_2.getPressed()  # if button is down already this ISN'T a new click
            if sol_2.status == STARTED:  # only update if started and not finished!
                buttons = sol_2.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter(skipsq_2, tree2_5)
                            clickableList = skipsq_2, tree2_5
                        except:
                            clickableList = [skipsq_2, tree2_5]
                        for obj in clickableList:
                            if obj.contains(sol_2):
                                gotValidClick = True
                                sol_2.clicked_name.append(obj.name)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # *gcircle_5* updates
            if gcircle_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                gcircle_5.frameNStart = frameN  # exact frame index
                gcircle_5.tStart = t  # local t and not account for scr refresh
                gcircle_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(gcircle_5, 'tStartRefresh')  # time at next scr refresh
                gcircle_5.setAutoDraw(True)
            
            # *skipsq_2* updates
            if skipsq_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                skipsq_2.frameNStart = frameN  # exact frame index
                skipsq_2.tStart = t  # local t and not account for scr refresh
                skipsq_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(skipsq_2, 'tStartRefresh')  # time at next scr refresh
                skipsq_2.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rewardframe2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "rewardframe2"-------
        for thisComponent in rewardframe2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_4.addData('tree1_5.started', tree1_5.tStartRefresh)
        trials_4.addData('tree1_5.stopped', tree1_5.tStopRefresh)
        trials_4.addData('tree2_5.started', tree2_5.tStartRefresh)
        trials_4.addData('tree2_5.stopped', tree2_5.tStopRefresh)
        trials_4.addData('tree3_5.started', tree3_5.tStartRefresh)
        trials_4.addData('tree3_5.stopped', tree3_5.tStopRefresh)
        trials_4.addData('tree4_5.started', tree4_5.tStartRefresh)
        trials_4.addData('tree4_5.stopped', tree4_5.tStopRefresh)
        trials_4.addData('circle_5.started', circle_5.tStartRefresh)
        trials_4.addData('circle_5.stopped', circle_5.tStopRefresh)
        trials_4.addData('reward_3.started', reward_3.tStartRefresh)
        trials_4.addData('reward_3.stopped', reward_3.tStopRefresh)
        # store data for trials_4 (TrialHandler)
        x, y = mouse_6.getPos()
        buttons = mouse_6.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            try:
                iter(tree2_5)
                clickableList = tree2_5
            except:
                clickableList = [tree2_5]
            for obj in clickableList:
                if obj.contains(mouse_6):
                    gotValidClick = True
                    mouse_6.clicked_name.append(obj.name)
        trials_4.addData('mouse_6.x', x)
        trials_4.addData('mouse_6.y', y)
        trials_4.addData('mouse_6.leftButton', buttons[0])
        trials_4.addData('mouse_6.midButton', buttons[1])
        trials_4.addData('mouse_6.rightButton', buttons[2])
        if len(mouse_6.clicked_name):
            trials_4.addData('mouse_6.clicked_name', mouse_6.clicked_name[0])
        trials_4.addData('mouse_6.started', mouse_6.tStart)
        trials_4.addData('mouse_6.stopped', mouse_6.tStop)
        trials_4.addData('forward_7.started', forward_7.tStartRefresh)
        trials_4.addData('forward_7.stopped', forward_7.tStopRefresh)
        # store data for trials_4 (TrialHandler)
        x, y = sol_2.getPos()
        buttons = sol_2.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            try:
                iter(skipsq_2, tree2_5)
                clickableList = skipsq_2, tree2_5
            except:
                clickableList = [skipsq_2, tree2_5]
            for obj in clickableList:
                if obj.contains(sol_2):
                    gotValidClick = True
                    sol_2.clicked_name.append(obj.name)
        trials_4.addData('sol_2.x', x)
        trials_4.addData('sol_2.y', y)
        trials_4.addData('sol_2.leftButton', buttons[0])
        trials_4.addData('sol_2.midButton', buttons[1])
        trials_4.addData('sol_2.rightButton', buttons[2])
        if len(sol_2.clicked_name):
            trials_4.addData('sol_2.clicked_name', sol_2.clicked_name[0])
        trials_4.addData('sol_2.started', sol_2.tStart)
        trials_4.addData('sol_2.stopped', sol_2.tStop)
        trials_4.addData('gcircle_5.started', gcircle_5.tStartRefresh)
        trials_4.addData('gcircle_5.stopped', gcircle_5.tStopRefresh)
        trials_4.addData('skipsq_2.started', skipsq_2.tStartRefresh)
        trials_4.addData('skipsq_2.stopped', skipsq_2.tStopRefresh)
        # the Routine "rewardframe2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "rewardframe2_4"-------
        continueRoutine = True
        routineTimer.add(1.000001)
        # update component parameters for each repeat
        display=17
        if random_seed==1:
            if a1i>5:
                display=0
            else:
                display=a1[a1i];
            a1i=a1i+1;
        elif random_seed==2:
            if a2i>5:
                display=0
            else:
                display=a2[a2i];
            a2i=a2i+1;
        elif random_seed==3:
            if a3i>5:
                display=0
            else:
                display=a3[a3i];
            a3i=a3i+1;
        elif random_seed==4:
            if a4i>5:
                display=0
            else:
                display=a4[a4i];
            a4i=a4i+1;
        else:
            if a5i>5:
                display=0
            else:
                display=a5[a5i];
            a5i=a5i+1;
        if sol_2.clicked_name[0] =='skipsq_2':
            reward2.finished = True
        tree1_21.setPos((-0.5, -0.6))
        tree2_21.setPos((0.5, -0.2))
        tree3_21.setPos((-0.5, 0.2))
        tree4_21.setPos((0.5, 0.6))
        reward_9.setText(display)
        # keep track of which components have finished
        rewardframe2_4Components = [tree1_21, tree2_21, tree3_21, tree4_21, wait1, forward_15, square5, gcircle1, reward_9, circle_6]
        for thisComponent in rewardframe2_4Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        rewardframe2_4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "rewardframe2_4"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = rewardframe2_4Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=rewardframe2_4Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *tree1_21* updates
            if tree1_21.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree1_21.frameNStart = frameN  # exact frame index
                tree1_21.tStart = t  # local t and not account for scr refresh
                tree1_21.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree1_21, 'tStartRefresh')  # time at next scr refresh
                tree1_21.setAutoDraw(True)
            if tree1_21.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree1_21.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree1_21.tStop = t  # not accounting for scr refresh
                    tree1_21.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree1_21, 'tStopRefresh')  # time at next scr refresh
                    tree1_21.setAutoDraw(False)
            
            # *tree2_21* updates
            if tree2_21.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree2_21.frameNStart = frameN  # exact frame index
                tree2_21.tStart = t  # local t and not account for scr refresh
                tree2_21.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree2_21, 'tStartRefresh')  # time at next scr refresh
                tree2_21.setAutoDraw(True)
            if tree2_21.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree2_21.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    tree2_21.tStop = t  # not accounting for scr refresh
                    tree2_21.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree2_21, 'tStopRefresh')  # time at next scr refresh
                    tree2_21.setAutoDraw(False)
            
            # *tree3_21* updates
            if tree3_21.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree3_21.frameNStart = frameN  # exact frame index
                tree3_21.tStart = t  # local t and not account for scr refresh
                tree3_21.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree3_21, 'tStartRefresh')  # time at next scr refresh
                tree3_21.setAutoDraw(True)
            if tree3_21.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree3_21.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree3_21.tStop = t  # not accounting for scr refresh
                    tree3_21.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree3_21, 'tStopRefresh')  # time at next scr refresh
                    tree3_21.setAutoDraw(False)
            
            # *tree4_21* updates
            if tree4_21.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree4_21.frameNStart = frameN  # exact frame index
                tree4_21.tStart = t  # local t and not account for scr refresh
                tree4_21.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree4_21, 'tStartRefresh')  # time at next scr refresh
                tree4_21.setAutoDraw(True)
            if tree4_21.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree4_21.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree4_21.tStop = t  # not accounting for scr refresh
                    tree4_21.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree4_21, 'tStopRefresh')  # time at next scr refresh
                    tree4_21.setAutoDraw(False)
            
            # *wait1* updates
            if wait1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wait1.frameNStart = frameN  # exact frame index
                wait1.tStart = t  # local t and not account for scr refresh
                wait1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wait1, 'tStartRefresh')  # time at next scr refresh
                wait1.setAutoDraw(True)
            if wait1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > wait1.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    wait1.tStop = t  # not accounting for scr refresh
                    wait1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(wait1, 'tStopRefresh')  # time at next scr refresh
                    wait1.setAutoDraw(False)
            
            # *forward_15* updates
            if forward_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                forward_15.frameNStart = frameN  # exact frame index
                forward_15.tStart = t  # local t and not account for scr refresh
                forward_15.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(forward_15, 'tStartRefresh')  # time at next scr refresh
                forward_15.setAutoDraw(True)
            if forward_15.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > forward_15.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    forward_15.tStop = t  # not accounting for scr refresh
                    forward_15.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(forward_15, 'tStopRefresh')  # time at next scr refresh
                    forward_15.setAutoDraw(False)
            
            # *square5* updates
            if square5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                square5.frameNStart = frameN  # exact frame index
                square5.tStart = t  # local t and not account for scr refresh
                square5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square5, 'tStartRefresh')  # time at next scr refresh
                square5.setAutoDraw(True)
            if square5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > square5.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    square5.tStop = t  # not accounting for scr refresh
                    square5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(square5, 'tStopRefresh')  # time at next scr refresh
                    square5.setAutoDraw(False)
            
            # *gcircle1* updates
            if gcircle1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                gcircle1.frameNStart = frameN  # exact frame index
                gcircle1.tStart = t  # local t and not account for scr refresh
                gcircle1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(gcircle1, 'tStartRefresh')  # time at next scr refresh
                gcircle1.setAutoDraw(True)
            if gcircle1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > gcircle1.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    gcircle1.tStop = t  # not accounting for scr refresh
                    gcircle1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(gcircle1, 'tStopRefresh')  # time at next scr refresh
                    gcircle1.setAutoDraw(False)
            
            # *reward_9* updates
            if reward_9.status == NOT_STARTED and tThisFlip >= 0.000001-frameTolerance:
                # keep track of start time/frame for later
                reward_9.frameNStart = frameN  # exact frame index
                reward_9.tStart = t  # local t and not account for scr refresh
                reward_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(reward_9, 'tStartRefresh')  # time at next scr refresh
                reward_9.setAutoDraw(True)
            if reward_9.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > reward_9.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    reward_9.tStop = t  # not accounting for scr refresh
                    reward_9.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(reward_9, 'tStopRefresh')  # time at next scr refresh
                    reward_9.setAutoDraw(False)
            
            # *circle_6* updates
            if circle_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                circle_6.frameNStart = frameN  # exact frame index
                circle_6.tStart = t  # local t and not account for scr refresh
                circle_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle_6, 'tStartRefresh')  # time at next scr refresh
                circle_6.setAutoDraw(True)
            if circle_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > circle_6.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    circle_6.tStop = t  # not accounting for scr refresh
                    circle_6.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(circle_6, 'tStopRefresh')  # time at next scr refresh
                    circle_6.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rewardframe2_4Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "rewardframe2_4"-------
        for thisComponent in rewardframe2_4Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData("randint",display)
        print(display)
        trials_4.addData('tree1_21.started', tree1_21.tStartRefresh)
        trials_4.addData('tree1_21.stopped', tree1_21.tStopRefresh)
        trials_4.addData('tree2_21.started', tree2_21.tStartRefresh)
        trials_4.addData('tree2_21.stopped', tree2_21.tStopRefresh)
        trials_4.addData('tree3_21.started', tree3_21.tStartRefresh)
        trials_4.addData('tree3_21.stopped', tree3_21.tStopRefresh)
        trials_4.addData('tree4_21.started', tree4_21.tStartRefresh)
        trials_4.addData('tree4_21.stopped', tree4_21.tStopRefresh)
        trials_4.addData('wait1.started', wait1.tStartRefresh)
        trials_4.addData('wait1.stopped', wait1.tStopRefresh)
        trials_4.addData('forward_15.started', forward_15.tStartRefresh)
        trials_4.addData('forward_15.stopped', forward_15.tStopRefresh)
        trials_4.addData('square5.started', square5.tStartRefresh)
        trials_4.addData('square5.stopped', square5.tStopRefresh)
        trials_4.addData('gcircle1.started', gcircle1.tStartRefresh)
        trials_4.addData('gcircle1.stopped', gcircle1.tStopRefresh)
        trials_4.addData('reward_9.started', reward_9.tStartRefresh)
        trials_4.addData('reward_9.stopped', reward_9.tStopRefresh)
        trials_4.addData('circle_6.started', circle_6.tStartRefresh)
        trials_4.addData('circle_6.stopped', circle_6.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_4'
    
    
    # set up handler to look after randomisation of conditions etc
    pos4 = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('pos.xlsx'),
        seed=None, name='pos4')
    thisExp.addLoop(pos4)  # add the loop to the experiment
    thisPos4 = pos4.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPos4.rgb)
    if thisPos4 != None:
        for paramName in thisPos4:
            exec('{} = thisPos4[paramName]'.format(paramName))
    
    for thisPos4 in pos4:
        currentLoop = pos4
        # abbreviate parameter names if possible (e.g. rgb = thisPos4.rgb)
        if thisPos4 != None:
            for paramName in thisPos4:
                exec('{} = thisPos4[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "movetrees_3"-------
        continueRoutine = True
        routineTimer.add(0.100000)
        # update component parameters for each repeat
        tree1_9.setPos((-0.5, tree1_n))
        tree2_9.setPos((0.5, tree2_p))
        tree3_9.setPos((-0.5, 0))
        tree4_9.setPos((0.5, 0))
        # keep track of which components have finished
        movetrees_3Components = [tree1_9, tree2_9, tree3_9, tree4_9, square_9]
        for thisComponent in movetrees_3Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        movetrees_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "movetrees_3"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = movetrees_3Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=movetrees_3Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *tree1_9* updates
            if tree1_9.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree1_9.frameNStart = frameN  # exact frame index
                tree1_9.tStart = t  # local t and not account for scr refresh
                tree1_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree1_9, 'tStartRefresh')  # time at next scr refresh
                tree1_9.setAutoDraw(True)
            if tree1_9.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree1_9.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    tree1_9.tStop = t  # not accounting for scr refresh
                    tree1_9.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree1_9, 'tStopRefresh')  # time at next scr refresh
                    tree1_9.setAutoDraw(False)
            
            # *tree2_9* updates
            if tree2_9.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree2_9.frameNStart = frameN  # exact frame index
                tree2_9.tStart = t  # local t and not account for scr refresh
                tree2_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree2_9, 'tStartRefresh')  # time at next scr refresh
                tree2_9.setAutoDraw(True)
            if tree2_9.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree2_9.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    tree2_9.tStop = t  # not accounting for scr refresh
                    tree2_9.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree2_9, 'tStopRefresh')  # time at next scr refresh
                    tree2_9.setAutoDraw(False)
            
            # *tree3_9* updates
            if tree3_9.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree3_9.frameNStart = frameN  # exact frame index
                tree3_9.tStart = t  # local t and not account for scr refresh
                tree3_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree3_9, 'tStartRefresh')  # time at next scr refresh
                tree3_9.setAutoDraw(True)
            if tree3_9.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree3_9.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree3_9.tStop = t  # not accounting for scr refresh
                    tree3_9.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree3_9, 'tStopRefresh')  # time at next scr refresh
                    tree3_9.setAutoDraw(False)
            
            # *tree4_9* updates
            if tree4_9.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree4_9.frameNStart = frameN  # exact frame index
                tree4_9.tStart = t  # local t and not account for scr refresh
                tree4_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree4_9, 'tStartRefresh')  # time at next scr refresh
                tree4_9.setAutoDraw(True)
            if tree4_9.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree4_9.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree4_9.tStop = t  # not accounting for scr refresh
                    tree4_9.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree4_9, 'tStopRefresh')  # time at next scr refresh
                    tree4_9.setAutoDraw(False)
            
            # *square_9* updates
            if square_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                square_9.frameNStart = frameN  # exact frame index
                square_9.tStart = t  # local t and not account for scr refresh
                square_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square_9, 'tStartRefresh')  # time at next scr refresh
                square_9.setAutoDraw(True)
            if square_9.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > square_9.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    square_9.tStop = t  # not accounting for scr refresh
                    square_9.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(square_9, 'tStopRefresh')  # time at next scr refresh
                    square_9.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in movetrees_3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "movetrees_3"-------
        for thisComponent in movetrees_3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        pos4.addData('tree1_9.started', tree1_9.tStartRefresh)
        pos4.addData('tree1_9.stopped', tree1_9.tStopRefresh)
        pos4.addData('tree2_9.started', tree2_9.tStartRefresh)
        pos4.addData('tree2_9.stopped', tree2_9.tStopRefresh)
        pos4.addData('tree3_9.started', tree3_9.tStartRefresh)
        pos4.addData('tree3_9.stopped', tree3_9.tStopRefresh)
        pos4.addData('tree4_9.started', tree4_9.tStartRefresh)
        pos4.addData('tree4_9.stopped', tree4_9.tStopRefresh)
        pos4.addData('square_9.started', square_9.tStartRefresh)
        pos4.addData('square_9.stopped', square_9.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'pos4'
    
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'time2'


# ------Prepare to start Routine "end"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [text]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)

# ------Prepare to start Routine "random_seed"-------
continueRoutine = True
# update component parameters for each repeat
from random import randint
random_seed= randint(1,5)
a1i=0
a2i=0
a3i=0
a4i=0
a5i=0
a1=[7.5,7.1,6.2,5.9,5.1,4.8,4,3.1,2.6,2.1,1.3,0.7,0]
a2=[7.3,6.9,6.2,5.8,5.1,4.6,4,3.2,2.4,1.3,0]
a3=[7.6,7.1,6.8,6.3,5.9,5.4,4.6,3.9,3.2,2.4,1.7,1.1,0]
a4=[7.1,6.6,6.1,5.8,5.3,4.8,4,3.6,3.1,2.7,2.1,1.3,0]
a5=[7.4,6.8,6.1,5.8,5.1,4.6,4.1,3.6,2.8,2.1,1.4,0]
display=14
# keep track of which components have finished
random_seedComponents = []
for thisComponent in random_seedComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
random_seedClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "random_seed"-------
while continueRoutine:
    # get current time
    t = random_seedClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=random_seedClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in random_seedComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "random_seed"-------
for thisComponent in random_seedComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "random_seed" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=5.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('pos.xlsx'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=5.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "rewardframe1_3"-------
        continueRoutine = True
        # update component parameters for each repeat
        tree1_18.setPos((-0.5, -0.2))
        tree2_18.setPos((0.5, 0.2))
        tree3_18.setPos((-0.5, 0.6))
        tree4_18.setPos((0.5, -0.6))
        # setup some python lists for storing info about the mouse_3
        mouse_3.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        rewardframe1_3Components = [tree1_18, tree2_18, tree3_18, tree4_18, circle1, forward_11, squaree_3, mouse_3]
        for thisComponent in rewardframe1_3Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        rewardframe1_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "rewardframe1_3"-------
        while continueRoutine:
            # get current time
            t = rewardframe1_3Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=rewardframe1_3Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *tree1_18* updates
            if tree1_18.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree1_18.frameNStart = frameN  # exact frame index
                tree1_18.tStart = t  # local t and not account for scr refresh
                tree1_18.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree1_18, 'tStartRefresh')  # time at next scr refresh
                tree1_18.setAutoDraw(True)
            
            # *tree2_18* updates
            if tree2_18.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree2_18.frameNStart = frameN  # exact frame index
                tree2_18.tStart = t  # local t and not account for scr refresh
                tree2_18.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree2_18, 'tStartRefresh')  # time at next scr refresh
                tree2_18.setAutoDraw(True)
            if tree2_18.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree2_18.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree2_18.tStop = t  # not accounting for scr refresh
                    tree2_18.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree2_18, 'tStopRefresh')  # time at next scr refresh
                    tree2_18.setAutoDraw(False)
            
            # *tree3_18* updates
            if tree3_18.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree3_18.frameNStart = frameN  # exact frame index
                tree3_18.tStart = t  # local t and not account for scr refresh
                tree3_18.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree3_18, 'tStartRefresh')  # time at next scr refresh
                tree3_18.setAutoDraw(True)
            if tree3_18.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree3_18.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree3_18.tStop = t  # not accounting for scr refresh
                    tree3_18.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree3_18, 'tStopRefresh')  # time at next scr refresh
                    tree3_18.setAutoDraw(False)
            
            # *tree4_18* updates
            if tree4_18.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree4_18.frameNStart = frameN  # exact frame index
                tree4_18.tStart = t  # local t and not account for scr refresh
                tree4_18.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree4_18, 'tStartRefresh')  # time at next scr refresh
                tree4_18.setAutoDraw(True)
            if tree4_18.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree4_18.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree4_18.tStop = t  # not accounting for scr refresh
                    tree4_18.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree4_18, 'tStopRefresh')  # time at next scr refresh
                    tree4_18.setAutoDraw(False)
            
            # *circle1* updates
            if circle1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                circle1.frameNStart = frameN  # exact frame index
                circle1.tStart = t  # local t and not account for scr refresh
                circle1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle1, 'tStartRefresh')  # time at next scr refresh
                circle1.setAutoDraw(True)
            
            # *forward_11* updates
            if forward_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                forward_11.frameNStart = frameN  # exact frame index
                forward_11.tStart = t  # local t and not account for scr refresh
                forward_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(forward_11, 'tStartRefresh')  # time at next scr refresh
                forward_11.setAutoDraw(True)
            
            # *squaree_3* updates
            if squaree_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                squaree_3.frameNStart = frameN  # exact frame index
                squaree_3.tStart = t  # local t and not account for scr refresh
                squaree_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(squaree_3, 'tStartRefresh')  # time at next scr refresh
                squaree_3.setAutoDraw(True)
            if squaree_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > squaree_3.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    squaree_3.tStop = t  # not accounting for scr refresh
                    squaree_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(squaree_3, 'tStopRefresh')  # time at next scr refresh
                    squaree_3.setAutoDraw(False)
            # *mouse_3* updates
            if mouse_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_3.frameNStart = frameN  # exact frame index
                mouse_3.tStart = t  # local t and not account for scr refresh
                mouse_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_3, 'tStartRefresh')  # time at next scr refresh
                mouse_3.status = STARTED
                mouse_3.mouseClock.reset()
                prevButtonState = mouse_3.getPressed()  # if button is down already this ISN'T a new click
            if mouse_3.status == STARTED:  # only update if started and not finished!
                buttons = mouse_3.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter(circle1)
                            clickableList = circle1
                        except:
                            clickableList = [circle1]
                        for obj in clickableList:
                            if obj.contains(mouse_3):
                                gotValidClick = True
                                mouse_3.clicked_name.append(obj.name)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rewardframe1_3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "rewardframe1_3"-------
        for thisComponent in rewardframe1_3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('tree1_18.started', tree1_18.tStartRefresh)
        trials.addData('tree1_18.stopped', tree1_18.tStopRefresh)
        trials.addData('tree2_18.started', tree2_18.tStartRefresh)
        trials.addData('tree2_18.stopped', tree2_18.tStopRefresh)
        trials.addData('tree3_18.started', tree3_18.tStartRefresh)
        trials.addData('tree3_18.stopped', tree3_18.tStopRefresh)
        trials.addData('tree4_18.started', tree4_18.tStartRefresh)
        trials.addData('tree4_18.stopped', tree4_18.tStopRefresh)
        trials.addData('circle1.started', circle1.tStartRefresh)
        trials.addData('circle1.stopped', circle1.tStopRefresh)
        trials.addData('forward_11.started', forward_11.tStartRefresh)
        trials.addData('forward_11.stopped', forward_11.tStopRefresh)
        trials.addData('squaree_3.started', squaree_3.tStartRefresh)
        trials.addData('squaree_3.stopped', squaree_3.tStopRefresh)
        # store data for trials (TrialHandler)
        x, y = mouse_3.getPos()
        buttons = mouse_3.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            try:
                iter(circle1)
                clickableList = circle1
            except:
                clickableList = [circle1]
            for obj in clickableList:
                if obj.contains(mouse_3):
                    gotValidClick = True
                    mouse_3.clicked_name.append(obj.name)
        trials.addData('mouse_3.x', x)
        trials.addData('mouse_3.y', y)
        trials.addData('mouse_3.leftButton', buttons[0])
        trials.addData('mouse_3.midButton', buttons[1])
        trials.addData('mouse_3.rightButton', buttons[2])
        if len(mouse_3.clicked_name):
            trials.addData('mouse_3.clicked_name', mouse_3.clicked_name[0])
        trials.addData('mouse_3.started', mouse_3.tStart)
        trials.addData('mouse_3.stopped', mouse_3.tStop)
        # the Routine "rewardframe1_3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "rewardframe1_2"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        tree1_12.setPos((-0.5, -0.2))
        tree2_12.setPos((0.5, 0.2))
        tree3_12.setPos((-0.5, 0.6))
        tree4_12.setPos((0.5, -0.6))
        wait_3.setText('wait')
        # keep track of which components have finished
        rewardframe1_2Components = [tree1_12, tree2_12, tree3_12, tree4_12, circle2, wait_3, forward_2, squaree_2, gcircle]
        for thisComponent in rewardframe1_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        rewardframe1_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "rewardframe1_2"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = rewardframe1_2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=rewardframe1_2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *tree1_12* updates
            if tree1_12.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree1_12.frameNStart = frameN  # exact frame index
                tree1_12.tStart = t  # local t and not account for scr refresh
                tree1_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree1_12, 'tStartRefresh')  # time at next scr refresh
                tree1_12.setAutoDraw(True)
            if tree1_12.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree1_12.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    tree1_12.tStop = t  # not accounting for scr refresh
                    tree1_12.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree1_12, 'tStopRefresh')  # time at next scr refresh
                    tree1_12.setAutoDraw(False)
            
            # *tree2_12* updates
            if tree2_12.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree2_12.frameNStart = frameN  # exact frame index
                tree2_12.tStart = t  # local t and not account for scr refresh
                tree2_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree2_12, 'tStartRefresh')  # time at next scr refresh
                tree2_12.setAutoDraw(True)
            if tree2_12.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree2_12.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree2_12.tStop = t  # not accounting for scr refresh
                    tree2_12.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree2_12, 'tStopRefresh')  # time at next scr refresh
                    tree2_12.setAutoDraw(False)
            
            # *tree3_12* updates
            if tree3_12.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree3_12.frameNStart = frameN  # exact frame index
                tree3_12.tStart = t  # local t and not account for scr refresh
                tree3_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree3_12, 'tStartRefresh')  # time at next scr refresh
                tree3_12.setAutoDraw(True)
            if tree3_12.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree3_12.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree3_12.tStop = t  # not accounting for scr refresh
                    tree3_12.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree3_12, 'tStopRefresh')  # time at next scr refresh
                    tree3_12.setAutoDraw(False)
            
            # *tree4_12* updates
            if tree4_12.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree4_12.frameNStart = frameN  # exact frame index
                tree4_12.tStart = t  # local t and not account for scr refresh
                tree4_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree4_12, 'tStartRefresh')  # time at next scr refresh
                tree4_12.setAutoDraw(True)
            if tree4_12.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree4_12.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree4_12.tStop = t  # not accounting for scr refresh
                    tree4_12.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree4_12, 'tStopRefresh')  # time at next scr refresh
                    tree4_12.setAutoDraw(False)
            
            # *circle2* updates
            if circle2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                circle2.frameNStart = frameN  # exact frame index
                circle2.tStart = t  # local t and not account for scr refresh
                circle2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle2, 'tStartRefresh')  # time at next scr refresh
                circle2.setAutoDraw(True)
            if circle2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > circle2.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    circle2.tStop = t  # not accounting for scr refresh
                    circle2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(circle2, 'tStopRefresh')  # time at next scr refresh
                    circle2.setAutoDraw(False)
            
            # *wait_3* updates
            if wait_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wait_3.frameNStart = frameN  # exact frame index
                wait_3.tStart = t  # local t and not account for scr refresh
                wait_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wait_3, 'tStartRefresh')  # time at next scr refresh
                wait_3.setAutoDraw(True)
            if wait_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > wait_3.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    wait_3.tStop = t  # not accounting for scr refresh
                    wait_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(wait_3, 'tStopRefresh')  # time at next scr refresh
                    wait_3.setAutoDraw(False)
            
            # *forward_2* updates
            if forward_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                forward_2.frameNStart = frameN  # exact frame index
                forward_2.tStart = t  # local t and not account for scr refresh
                forward_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(forward_2, 'tStartRefresh')  # time at next scr refresh
                forward_2.setAutoDraw(True)
            if forward_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > forward_2.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    forward_2.tStop = t  # not accounting for scr refresh
                    forward_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(forward_2, 'tStopRefresh')  # time at next scr refresh
                    forward_2.setAutoDraw(False)
            
            # *squaree_2* updates
            if squaree_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                squaree_2.frameNStart = frameN  # exact frame index
                squaree_2.tStart = t  # local t and not account for scr refresh
                squaree_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(squaree_2, 'tStartRefresh')  # time at next scr refresh
                squaree_2.setAutoDraw(True)
            if squaree_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > squaree_2.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    squaree_2.tStop = t  # not accounting for scr refresh
                    squaree_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(squaree_2, 'tStopRefresh')  # time at next scr refresh
                    squaree_2.setAutoDraw(False)
            
            # *gcircle* updates
            if gcircle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                gcircle.frameNStart = frameN  # exact frame index
                gcircle.tStart = t  # local t and not account for scr refresh
                gcircle.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(gcircle, 'tStartRefresh')  # time at next scr refresh
                gcircle.setAutoDraw(True)
            if gcircle.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > gcircle.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    gcircle.tStop = t  # not accounting for scr refresh
                    gcircle.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(gcircle, 'tStopRefresh')  # time at next scr refresh
                    gcircle.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rewardframe1_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "rewardframe1_2"-------
        for thisComponent in rewardframe1_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('tree1_12.started', tree1_12.tStartRefresh)
        trials.addData('tree1_12.stopped', tree1_12.tStopRefresh)
        trials.addData('tree2_12.started', tree2_12.tStartRefresh)
        trials.addData('tree2_12.stopped', tree2_12.tStopRefresh)
        trials.addData('tree3_12.started', tree3_12.tStartRefresh)
        trials.addData('tree3_12.stopped', tree3_12.tStopRefresh)
        trials.addData('tree4_12.started', tree4_12.tStartRefresh)
        trials.addData('tree4_12.stopped', tree4_12.tStopRefresh)
        trials.addData('circle2.started', circle2.tStartRefresh)
        trials.addData('circle2.stopped', circle2.tStopRefresh)
        trials.addData('wait_3.started', wait_3.tStartRefresh)
        trials.addData('wait_3.stopped', wait_3.tStopRefresh)
        trials.addData('forward_2.started', forward_2.tStartRefresh)
        trials.addData('forward_2.stopped', forward_2.tStopRefresh)
        trials.addData('squaree_2.started', squaree_2.tStartRefresh)
        trials.addData('squaree_2.stopped', squaree_2.tStopRefresh)
        trials.addData('gcircle.started', gcircle.tStartRefresh)
        trials.addData('gcircle.stopped', gcircle.tStopRefresh)
        
        # ------Prepare to start Routine "rewardframe1"-------
        continueRoutine = True
        # update component parameters for each repeat
        tree1_4.setPos((-0.5, -0.2))
        tree2_4.setPos((0.5, 0.2))
        tree3_4.setPos((-0.5, 0.6))
        tree4_4.setPos((0.5, -0.6))
        reward_2.setText('')
        # setup some python lists for storing info about the resp
        resp.x = []
        resp.y = []
        resp.leftButton = []
        resp.midButton = []
        resp.rightButton = []
        resp.time = []
        resp.clicked_name = []
        gotValidClick = False  # until a click is received
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # setup some python lists for storing info about the sol
        sol.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        rewardframe1Components = [tree1_4, tree2_4, tree3_4, tree4_4, circle3, reward_2, resp, forward, key_resp, sol, gcircle_2, skipsq]
        for thisComponent in rewardframe1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        rewardframe1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "rewardframe1"-------
        while continueRoutine:
            # get current time
            t = rewardframe1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=rewardframe1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *tree1_4* updates
            if tree1_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree1_4.frameNStart = frameN  # exact frame index
                tree1_4.tStart = t  # local t and not account for scr refresh
                tree1_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree1_4, 'tStartRefresh')  # time at next scr refresh
                tree1_4.setAutoDraw(True)
            
            # *tree2_4* updates
            if tree2_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree2_4.frameNStart = frameN  # exact frame index
                tree2_4.tStart = t  # local t and not account for scr refresh
                tree2_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree2_4, 'tStartRefresh')  # time at next scr refresh
                tree2_4.setAutoDraw(True)
            if tree2_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree2_4.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree2_4.tStop = t  # not accounting for scr refresh
                    tree2_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree2_4, 'tStopRefresh')  # time at next scr refresh
                    tree2_4.setAutoDraw(False)
            
            # *tree3_4* updates
            if tree3_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree3_4.frameNStart = frameN  # exact frame index
                tree3_4.tStart = t  # local t and not account for scr refresh
                tree3_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree3_4, 'tStartRefresh')  # time at next scr refresh
                tree3_4.setAutoDraw(True)
            if tree3_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree3_4.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree3_4.tStop = t  # not accounting for scr refresh
                    tree3_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree3_4, 'tStopRefresh')  # time at next scr refresh
                    tree3_4.setAutoDraw(False)
            
            # *tree4_4* updates
            if tree4_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree4_4.frameNStart = frameN  # exact frame index
                tree4_4.tStart = t  # local t and not account for scr refresh
                tree4_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree4_4, 'tStartRefresh')  # time at next scr refresh
                tree4_4.setAutoDraw(True)
            if tree4_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree4_4.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree4_4.tStop = t  # not accounting for scr refresh
                    tree4_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree4_4, 'tStopRefresh')  # time at next scr refresh
                    tree4_4.setAutoDraw(False)
            
            # *circle3* updates
            if circle3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                circle3.frameNStart = frameN  # exact frame index
                circle3.tStart = t  # local t and not account for scr refresh
                circle3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle3, 'tStartRefresh')  # time at next scr refresh
                circle3.setAutoDraw(True)
            
            # *reward_2* updates
            if reward_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                reward_2.frameNStart = frameN  # exact frame index
                reward_2.tStart = t  # local t and not account for scr refresh
                reward_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(reward_2, 'tStartRefresh')  # time at next scr refresh
                reward_2.setAutoDraw(True)
            if reward_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > reward_2.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    reward_2.tStop = t  # not accounting for scr refresh
                    reward_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(reward_2, 'tStopRefresh')  # time at next scr refresh
                    reward_2.setAutoDraw(False)
            # *resp* updates
            if resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                resp.frameNStart = frameN  # exact frame index
                resp.tStart = t  # local t and not account for scr refresh
                resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
                resp.status = STARTED
                resp.mouseClock.reset()
                prevButtonState = resp.getPressed()  # if button is down already this ISN'T a new click
            if resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > resp.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    resp.tStop = t  # not accounting for scr refresh
                    resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(resp, 'tStopRefresh')  # time at next scr refresh
                    resp.status = FINISHED
            if resp.status == STARTED:  # only update if started and not finished!
                buttons = resp.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter(tree1_4)
                            clickableList = tree1_4
                        except:
                            clickableList = [tree1_4]
                        for obj in clickableList:
                            if obj.contains(resp):
                                gotValidClick = True
                                resp.clicked_name.append(obj.name)
                        x, y = resp.getPos()
                        resp.x.append(x)
                        resp.y.append(y)
                        buttons = resp.getPressed()
                        resp.leftButton.append(buttons[0])
                        resp.midButton.append(buttons[1])
                        resp.rightButton.append(buttons[2])
                        resp.time.append(resp.mouseClock.getTime())
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # *forward* updates
            if forward.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                forward.frameNStart = frameN  # exact frame index
                forward.tStart = t  # local t and not account for scr refresh
                forward.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(forward, 'tStartRefresh')  # time at next scr refresh
                forward.setAutoDraw(True)
            
            # *key_resp* updates
            waitOnFlip = False
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp.tStop = t  # not accounting for scr refresh
                    key_resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                    key_resp.status = FINISHED
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            # *sol* updates
            if sol.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sol.frameNStart = frameN  # exact frame index
                sol.tStart = t  # local t and not account for scr refresh
                sol.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sol, 'tStartRefresh')  # time at next scr refresh
                sol.status = STARTED
                sol.mouseClock.reset()
                prevButtonState = sol.getPressed()  # if button is down already this ISN'T a new click
            if sol.status == STARTED:  # only update if started and not finished!
                buttons = sol.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter(skipsq, tree1_4)
                            clickableList = skipsq, tree1_4
                        except:
                            clickableList = [skipsq, tree1_4]
                        for obj in clickableList:
                            if obj.contains(sol):
                                gotValidClick = True
                                sol.clicked_name.append(obj.name)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # *gcircle_2* updates
            if gcircle_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                gcircle_2.frameNStart = frameN  # exact frame index
                gcircle_2.tStart = t  # local t and not account for scr refresh
                gcircle_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(gcircle_2, 'tStartRefresh')  # time at next scr refresh
                gcircle_2.setAutoDraw(True)
            
            # *skipsq* updates
            if skipsq.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                skipsq.frameNStart = frameN  # exact frame index
                skipsq.tStart = t  # local t and not account for scr refresh
                skipsq.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(skipsq, 'tStartRefresh')  # time at next scr refresh
                skipsq.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rewardframe1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "rewardframe1"-------
        for thisComponent in rewardframe1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('tree1_4.started', tree1_4.tStartRefresh)
        trials.addData('tree1_4.stopped', tree1_4.tStopRefresh)
        trials.addData('tree2_4.started', tree2_4.tStartRefresh)
        trials.addData('tree2_4.stopped', tree2_4.tStopRefresh)
        trials.addData('tree3_4.started', tree3_4.tStartRefresh)
        trials.addData('tree3_4.stopped', tree3_4.tStopRefresh)
        trials.addData('tree4_4.started', tree4_4.tStartRefresh)
        trials.addData('tree4_4.stopped', tree4_4.tStopRefresh)
        trials.addData('circle3.started', circle3.tStartRefresh)
        trials.addData('circle3.stopped', circle3.tStopRefresh)
        trials.addData('reward_2.started', reward_2.tStartRefresh)
        trials.addData('reward_2.stopped', reward_2.tStopRefresh)
        # store data for trials (TrialHandler)
        if len(resp.x): trials.addData('resp.x', resp.x[0])
        if len(resp.y): trials.addData('resp.y', resp.y[0])
        if len(resp.leftButton): trials.addData('resp.leftButton', resp.leftButton[0])
        if len(resp.midButton): trials.addData('resp.midButton', resp.midButton[0])
        if len(resp.rightButton): trials.addData('resp.rightButton', resp.rightButton[0])
        if len(resp.time): trials.addData('resp.time', resp.time[0])
        if len(resp.clicked_name): trials.addData('resp.clicked_name', resp.clicked_name[0])
        trials.addData('resp.started', resp.tStart)
        trials.addData('resp.stopped', resp.tStop)
        trials.addData('forward.started', forward.tStartRefresh)
        trials.addData('forward.stopped', forward.tStopRefresh)
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        trials.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            trials.addData('key_resp.rt', key_resp.rt)
        trials.addData('key_resp.started', key_resp.tStartRefresh)
        trials.addData('key_resp.stopped', key_resp.tStopRefresh)
        # store data for trials (TrialHandler)
        x, y = sol.getPos()
        buttons = sol.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            try:
                iter(skipsq, tree1_4)
                clickableList = skipsq, tree1_4
            except:
                clickableList = [skipsq, tree1_4]
            for obj in clickableList:
                if obj.contains(sol):
                    gotValidClick = True
                    sol.clicked_name.append(obj.name)
        trials.addData('sol.x', x)
        trials.addData('sol.y', y)
        trials.addData('sol.leftButton', buttons[0])
        trials.addData('sol.midButton', buttons[1])
        trials.addData('sol.rightButton', buttons[2])
        if len(sol.clicked_name):
            trials.addData('sol.clicked_name', sol.clicked_name[0])
        trials.addData('sol.started', sol.tStart)
        trials.addData('sol.stopped', sol.tStop)
        trials.addData('gcircle_2.started', gcircle_2.tStartRefresh)
        trials.addData('gcircle_2.stopped', gcircle_2.tStopRefresh)
        trials.addData('skipsq.started', skipsq.tStartRefresh)
        trials.addData('skipsq.stopped', skipsq.tStopRefresh)
        # the Routine "rewardframe1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "rewardframe1_4"-------
        continueRoutine = True
        routineTimer.add(1.000100)
        # update component parameters for each repeat
        display=17
        if random_seed==1:
            if a1i>5:
                display=0
            else:
                display=a1[a1i];
            a1i=a1i+1;
        elif random_seed==2:
            if a2i>5:
                display=0
            else:
                display=a2[a2i];
            a2i=a2i+1;
        elif random_seed==3:
            if a3i>5:
                display=0
            else:
                display=a3[a3i];
            a3i=a3i+1;
        elif random_seed==4:
            if a4i>5:
                display=0
            else:
                display=a4[a4i];
            a4i=a4i+1;
        else:
            if a5i>5:
                display=0
            else:
                display=a5[a5i];
            a5i=a5i+1;
        if sol.clicked_name[0] =='skipsq':
            continueRoutine = False
            reward1.finished = True
        tree1_19.setPos((-0.5, -0.2))
        tree2_19.setPos((0.5, 0.2))
        tree3_19.setPos((-0.5, 0.6))
        tree4_19.setPos((0.5, -0.6))
        wait_8.setText('wait')
        reward_7.setText(display)
        # keep track of which components have finished
        rewardframe1_4Components = [tree1_19, tree2_19, tree3_19, tree4_19, circle4, wait_8, forward_12, squaree_4, gcircle_3, reward_7, gcircle_4]
        for thisComponent in rewardframe1_4Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        rewardframe1_4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "rewardframe1_4"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = rewardframe1_4Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=rewardframe1_4Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *tree1_19* updates
            if tree1_19.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree1_19.frameNStart = frameN  # exact frame index
                tree1_19.tStart = t  # local t and not account for scr refresh
                tree1_19.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree1_19, 'tStartRefresh')  # time at next scr refresh
                tree1_19.setAutoDraw(True)
            if tree1_19.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree1_19.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    tree1_19.tStop = t  # not accounting for scr refresh
                    tree1_19.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree1_19, 'tStopRefresh')  # time at next scr refresh
                    tree1_19.setAutoDraw(False)
            
            # *tree2_19* updates
            if tree2_19.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree2_19.frameNStart = frameN  # exact frame index
                tree2_19.tStart = t  # local t and not account for scr refresh
                tree2_19.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree2_19, 'tStartRefresh')  # time at next scr refresh
                tree2_19.setAutoDraw(True)
            if tree2_19.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree2_19.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree2_19.tStop = t  # not accounting for scr refresh
                    tree2_19.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree2_19, 'tStopRefresh')  # time at next scr refresh
                    tree2_19.setAutoDraw(False)
            
            # *tree3_19* updates
            if tree3_19.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree3_19.frameNStart = frameN  # exact frame index
                tree3_19.tStart = t  # local t and not account for scr refresh
                tree3_19.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree3_19, 'tStartRefresh')  # time at next scr refresh
                tree3_19.setAutoDraw(True)
            if tree3_19.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree3_19.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree3_19.tStop = t  # not accounting for scr refresh
                    tree3_19.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree3_19, 'tStopRefresh')  # time at next scr refresh
                    tree3_19.setAutoDraw(False)
            
            # *tree4_19* updates
            if tree4_19.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree4_19.frameNStart = frameN  # exact frame index
                tree4_19.tStart = t  # local t and not account for scr refresh
                tree4_19.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree4_19, 'tStartRefresh')  # time at next scr refresh
                tree4_19.setAutoDraw(True)
            if tree4_19.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree4_19.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree4_19.tStop = t  # not accounting for scr refresh
                    tree4_19.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree4_19, 'tStopRefresh')  # time at next scr refresh
                    tree4_19.setAutoDraw(False)
            
            # *circle4* updates
            if circle4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                circle4.frameNStart = frameN  # exact frame index
                circle4.tStart = t  # local t and not account for scr refresh
                circle4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle4, 'tStartRefresh')  # time at next scr refresh
                circle4.setAutoDraw(True)
            if circle4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > circle4.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    circle4.tStop = t  # not accounting for scr refresh
                    circle4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(circle4, 'tStopRefresh')  # time at next scr refresh
                    circle4.setAutoDraw(False)
            
            # *wait_8* updates
            if wait_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wait_8.frameNStart = frameN  # exact frame index
                wait_8.tStart = t  # local t and not account for scr refresh
                wait_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wait_8, 'tStartRefresh')  # time at next scr refresh
                wait_8.setAutoDraw(True)
            if wait_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > wait_8.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    wait_8.tStop = t  # not accounting for scr refresh
                    wait_8.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(wait_8, 'tStopRefresh')  # time at next scr refresh
                    wait_8.setAutoDraw(False)
            
            # *forward_12* updates
            if forward_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                forward_12.frameNStart = frameN  # exact frame index
                forward_12.tStart = t  # local t and not account for scr refresh
                forward_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(forward_12, 'tStartRefresh')  # time at next scr refresh
                forward_12.setAutoDraw(True)
            if forward_12.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > forward_12.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    forward_12.tStop = t  # not accounting for scr refresh
                    forward_12.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(forward_12, 'tStopRefresh')  # time at next scr refresh
                    forward_12.setAutoDraw(False)
            
            # *squaree_4* updates
            if squaree_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                squaree_4.frameNStart = frameN  # exact frame index
                squaree_4.tStart = t  # local t and not account for scr refresh
                squaree_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(squaree_4, 'tStartRefresh')  # time at next scr refresh
                squaree_4.setAutoDraw(True)
            if squaree_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > squaree_4.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    squaree_4.tStop = t  # not accounting for scr refresh
                    squaree_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(squaree_4, 'tStopRefresh')  # time at next scr refresh
                    squaree_4.setAutoDraw(False)
            
            # *gcircle_3* updates
            if gcircle_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                gcircle_3.frameNStart = frameN  # exact frame index
                gcircle_3.tStart = t  # local t and not account for scr refresh
                gcircle_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(gcircle_3, 'tStartRefresh')  # time at next scr refresh
                gcircle_3.setAutoDraw(True)
            if gcircle_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > gcircle_3.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    gcircle_3.tStop = t  # not accounting for scr refresh
                    gcircle_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(gcircle_3, 'tStopRefresh')  # time at next scr refresh
                    gcircle_3.setAutoDraw(False)
            
            # *reward_7* updates
            if reward_7.status == NOT_STARTED and tThisFlip >= 0.0001-frameTolerance:
                # keep track of start time/frame for later
                reward_7.frameNStart = frameN  # exact frame index
                reward_7.tStart = t  # local t and not account for scr refresh
                reward_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(reward_7, 'tStartRefresh')  # time at next scr refresh
                reward_7.setAutoDraw(True)
            if reward_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > reward_7.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    reward_7.tStop = t  # not accounting for scr refresh
                    reward_7.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(reward_7, 'tStopRefresh')  # time at next scr refresh
                    reward_7.setAutoDraw(False)
            
            # *gcircle_4* updates
            if gcircle_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                gcircle_4.frameNStart = frameN  # exact frame index
                gcircle_4.tStart = t  # local t and not account for scr refresh
                gcircle_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(gcircle_4, 'tStartRefresh')  # time at next scr refresh
                gcircle_4.setAutoDraw(True)
            if gcircle_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > gcircle_4.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    gcircle_4.tStop = t  # not accounting for scr refresh
                    gcircle_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(gcircle_4, 'tStopRefresh')  # time at next scr refresh
                    gcircle_4.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rewardframe1_4Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "rewardframe1_4"-------
        for thisComponent in rewardframe1_4Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData("randint",display)
        print(display)
        trials.addData('tree1_19.started', tree1_19.tStartRefresh)
        trials.addData('tree1_19.stopped', tree1_19.tStopRefresh)
        trials.addData('tree2_19.started', tree2_19.tStartRefresh)
        trials.addData('tree2_19.stopped', tree2_19.tStopRefresh)
        trials.addData('tree3_19.started', tree3_19.tStartRefresh)
        trials.addData('tree3_19.stopped', tree3_19.tStopRefresh)
        trials.addData('tree4_19.started', tree4_19.tStartRefresh)
        trials.addData('tree4_19.stopped', tree4_19.tStopRefresh)
        trials.addData('circle4.started', circle4.tStartRefresh)
        trials.addData('circle4.stopped', circle4.tStopRefresh)
        trials.addData('wait_8.started', wait_8.tStartRefresh)
        trials.addData('wait_8.stopped', wait_8.tStopRefresh)
        trials.addData('forward_12.started', forward_12.tStartRefresh)
        trials.addData('forward_12.stopped', forward_12.tStopRefresh)
        trials.addData('squaree_4.started', squaree_4.tStartRefresh)
        trials.addData('squaree_4.stopped', squaree_4.tStopRefresh)
        trials.addData('gcircle_3.started', gcircle_3.tStartRefresh)
        trials.addData('gcircle_3.stopped', gcircle_3.tStopRefresh)
        trials.addData('reward_7.started', reward_7.tStartRefresh)
        trials.addData('reward_7.stopped', reward_7.tStopRefresh)
        trials.addData('gcircle_4.started', gcircle_4.tStartRefresh)
        trials.addData('gcircle_4.stopped', gcircle_4.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 5.0 repeats of 'trials'
    
    
    # set up handler to look after randomisation of conditions etc
    trials_3 = data.TrialHandler(nReps=5.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_3')
    thisExp.addLoop(trials_3)  # add the loop to the experiment
    thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    for thisTrial_3 in trials_3:
        currentLoop = trials_3
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
        if thisTrial_3 != None:
            for paramName in thisTrial_3:
                exec('{} = thisTrial_3[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "movetrees5"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        tree1_24.setPos((0, 0))
        # keep track of which components have finished
        movetrees5Components = [tree1_24]
        for thisComponent in movetrees5Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        movetrees5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "movetrees5"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = movetrees5Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=movetrees5Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *tree1_24* updates
            if tree1_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                tree1_24.frameNStart = frameN  # exact frame index
                tree1_24.tStart = t  # local t and not account for scr refresh
                tree1_24.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree1_24, 'tStartRefresh')  # time at next scr refresh
                tree1_24.setAutoDraw(True)
            if tree1_24.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree1_24.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree1_24.tStop = t  # not accounting for scr refresh
                    tree1_24.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree1_24, 'tStopRefresh')  # time at next scr refresh
                    tree1_24.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in movetrees5Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "movetrees5"-------
        for thisComponent in movetrees5Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_3.addData('tree1_24.started', tree1_24.tStartRefresh)
        trials_3.addData('tree1_24.stopped', tree1_24.tStopRefresh)
        
        # ------Prepare to start Routine "movetrees"-------
        continueRoutine = True
        routineTimer.add(0.200000)
        # update component parameters for each repeat
        tree1_6.setPos((-0.5, tree1_n))
        tree2_6.setPos((0.5, tree2_p))
        tree3_6.setPos((-0.5,0))
        tree4_6.setPos((0.5, 0))
        # keep track of which components have finished
        movetreesComponents = [tree1_6, tree2_6, tree3_6, tree4_6, circle5]
        for thisComponent in movetreesComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        movetreesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "movetrees"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = movetreesClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=movetreesClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *tree1_6* updates
            if tree1_6.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree1_6.frameNStart = frameN  # exact frame index
                tree1_6.tStart = t  # local t and not account for scr refresh
                tree1_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree1_6, 'tStartRefresh')  # time at next scr refresh
                tree1_6.setAutoDraw(True)
            if tree1_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree1_6.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    tree1_6.tStop = t  # not accounting for scr refresh
                    tree1_6.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree1_6, 'tStopRefresh')  # time at next scr refresh
                    tree1_6.setAutoDraw(False)
            
            # *tree2_6* updates
            if tree2_6.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree2_6.frameNStart = frameN  # exact frame index
                tree2_6.tStart = t  # local t and not account for scr refresh
                tree2_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree2_6, 'tStartRefresh')  # time at next scr refresh
                tree2_6.setAutoDraw(True)
            if tree2_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree2_6.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    tree2_6.tStop = t  # not accounting for scr refresh
                    tree2_6.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree2_6, 'tStopRefresh')  # time at next scr refresh
                    tree2_6.setAutoDraw(False)
            
            # *tree3_6* updates
            if tree3_6.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree3_6.frameNStart = frameN  # exact frame index
                tree3_6.tStart = t  # local t and not account for scr refresh
                tree3_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree3_6, 'tStartRefresh')  # time at next scr refresh
                tree3_6.setAutoDraw(True)
            if tree3_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree3_6.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree3_6.tStop = t  # not accounting for scr refresh
                    tree3_6.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree3_6, 'tStopRefresh')  # time at next scr refresh
                    tree3_6.setAutoDraw(False)
            
            # *tree4_6* updates
            if tree4_6.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tree4_6.frameNStart = frameN  # exact frame index
                tree4_6.tStart = t  # local t and not account for scr refresh
                tree4_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree4_6, 'tStartRefresh')  # time at next scr refresh
                tree4_6.setAutoDraw(True)
            if tree4_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tree4_6.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    tree4_6.tStop = t  # not accounting for scr refresh
                    tree4_6.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tree4_6, 'tStopRefresh')  # time at next scr refresh
                    tree4_6.setAutoDraw(False)
            
            # *circle5* updates
            if circle5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                circle5.frameNStart = frameN  # exact frame index
                circle5.tStart = t  # local t and not account for scr refresh
                circle5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle5, 'tStartRefresh')  # time at next scr refresh
                circle5.setAutoDraw(True)
            if circle5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > circle5.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    circle5.tStop = t  # not accounting for scr refresh
                    circle5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(circle5, 'tStopRefresh')  # time at next scr refresh
                    circle5.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in movetreesComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "movetrees"-------
        for thisComponent in movetreesComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_3.addData('tree1_6.started', tree1_6.tStartRefresh)
        trials_3.addData('tree1_6.stopped', tree1_6.tStopRefresh)
        trials_3.addData('tree2_6.started', tree2_6.tStartRefresh)
        trials_3.addData('tree2_6.stopped', tree2_6.tStopRefresh)
        trials_3.addData('tree3_6.started', tree3_6.tStartRefresh)
        trials_3.addData('tree3_6.stopped', tree3_6.tStopRefresh)
        trials_3.addData('tree4_6.started', tree4_6.tStartRefresh)
        trials_3.addData('tree4_6.stopped', tree4_6.tStopRefresh)
        trials_3.addData('circle5.started', circle5.tStartRefresh)
        trials_3.addData('circle5.stopped', circle5.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 5.0 repeats of 'trials_3'
    
    thisExp.nextEntry()
    
# completed 5.0 repeats of 'trials_2'


# ------Prepare to start Routine "end"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [text]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
