#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.3),
    on September 05, 2019, at 02:41
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.1.3'
expName = 'StressSession'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '002'}
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
    originPath='I:\\Master Thesis\\ExperimentFolder\\Paradigma\\Sessions\\StressSession_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "te"
teClock = core.Clock()
sound_1 = sound.Sound('A', secs=-1, stereo=True)
sound_1.setVolume(1)
sound_2 = sound.Sound('660', secs=-1, stereo=True)
sound_2.setVolume(1)
sound_3 = sound.Sound('880', secs=-1, stereo=True)
sound_3.setVolume(1)
sound_4 = sound.Sound('1100', secs=-1, stereo=True)
sound_4.setVolume(1)

# Initialize components for Routine "Stress_Screen"
Stress_ScreenClock = core.Clock()
text_stress_screen_title = visual.TextStim(win=win, name='text_stress_screen_title',
    text='Session Two:',
    font='Arial',
    pos=(0, 0.2), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_stress_screen = visual.TextStim(win=win, name='text_stress_screen',
    text='Stress Test',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
import time
thisExp.addData("start_session_two", time.strftime("%Y-%m-%d_%H:%M:%S")) 

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()
text_blank = visual.TextStim(win=win, name='text_blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Part_One"
Part_OneClock = core.Clock()
text_part_one_title = visual.TextStim(win=win, name='text_part_one_title',
    text='Part One:',
    font='Arial',
    pos=(0, 0.2), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_part_one = visual.TextStim(win=win, name='text_part_one',
    text='7-Row',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()
text_blank = visual.TextStim(win=win, name='text_blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Part_One_Instructions"
Part_One_InstructionsClock = core.Clock()
text_part_one_instructions_title = visual.TextStim(win=win, name='text_part_one_instructions_title',
    text='Instructions:',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_part_one_instructions = visual.TextStim(win=win, name='text_part_one_instructions',
    text='Count down aloud from 700 in steps of 7 while trying to match the speed of the metronome dot.\n\nWhen you are ready please tell your instructor to start the measurement.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()
text_blank = visual.TextStim(win=win, name='text_blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Part_One_Measurement"
Part_One_MeasurementClock = core.Clock()
metronome_dot = visual.Polygon(
    win=win, name='metronome_dot',
    edges=32, size=(0.2, 0.2),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
metronome_tone = sound.Sound('A', secs=0.5, stereo=True)
metronome_tone.setVolume(0.5)

# Initialize components for Routine "Metronome_Tick"
Metronome_TickClock = core.Clock()
text_metronom_tick = visual.TextStim(win=win, name='text_metronom_tick',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Part_One_Meas_Stop"
Part_One_Meas_StopClock = core.Clock()
text_part_one_meas_stop = visual.TextStim(win=win, name='text_part_one_meas_stop',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Stress_Evaluation_One"
Stress_Evaluation_OneClock = core.Clock()
text_evaluation_one_title = visual.TextStim(win=win, name='text_evaluation_one_title',
    text='Task finished:',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_evaluation_one = visual.TextStim(win=win, name='text_evaluation_one',
    text='Please rate your current stress level.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
rating_evaluation_one = visual.RatingScale(win=win, name='rating_evaluation_one', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=10, labels=['completely relaxed', ' stressed out'], scale='', markerStart='5')

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()
text_blank = visual.TextStim(win=win, name='text_blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Stress_Evaluation_Two"
Stress_Evaluation_TwoClock = core.Clock()
text_evaluation_two = visual.TextStim(win=win, name='text_evaluation_two',
    text='Please rate the difficulty of the task.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
rating_evaluation_two = visual.RatingScale(win=win, name='rating_evaluation_two', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=10, labels=['very easy', ' easy', ' hard', ' very hard'], scale='')

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()
text_blank = visual.TextStim(win=win, name='text_blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Part_One_End"
Part_One_EndClock = core.Clock()
text_part_one_end = visual.TextStim(win=win, name='text_part_one_end',
    text='Ending Part One',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_part_one_end_instructions = visual.TextStim(win=win, name='text_part_one_end_instructions',
    text="(Press 'SPACE' to continue)",
    font='Arial',
    pos=(0, -0.2), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()
text_blank = visual.TextStim(win=win, name='text_blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Part_Two"
Part_TwoClock = core.Clock()
text_part_two_title = visual.TextStim(win=win, name='text_part_two_title',
    text='Part Two',
    font='Arial',
    pos=(0, 0.2), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_part_two = visual.TextStim(win=win, name='text_part_two',
    text='Stroop Test',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()
text_blank = visual.TextStim(win=win, name='text_blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Part_Two_Instructions"
Part_Two_InstructionsClock = core.Clock()
text_part_two_instructions_title = visual.TextStim(win=win, name='text_part_two_instructions_title',
    text='Instructions:',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_part_two_instructions = visual.TextStim(win=win, name='text_part_two_instructions',
    text='Select the color of the word by using the arrow keys [left, right].\n\nWhen you are ready please tell your instructor to start the measurement.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()
text_blank = visual.TextStim(win=win, name='text_blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Color_Instructions"
Color_InstructionsClock = core.Clock()
text_color_instructions = visual.TextStim(win=win, name='text_color_instructions',
    text='Stroop Colors',
    font='Arial',
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
rec_red = visual.Rect(
    win=win, name='rec_red',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0, pos=(-0.8, 0.2),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='red', fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
text_red = visual.TextStim(win=win, name='text_red',
    text='red',
    font='Arial',
    pos=(-0.8, 0.1), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
rec_magenta = visual.Rect(
    win=win, name='rec_magenta',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0, pos=(-0.6, 0.2),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='magenta', fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
text_magenta = visual.TextStim(win=win, name='text_magenta',
    text='magenta',
    font='Arial',
    pos=(-0.6, 0.1), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
rec_orange = visual.Rect(
    win=win, name='rec_orange',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0, pos=(-0.4, 0.2),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='orange', fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
text_orange = visual.TextStim(win=win, name='text_orange',
    text='orange',
    font='Arial',
    pos=(-0.4, 0.1), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
rec_yellow = visual.Rect(
    win=win, name='rec_yellow',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0, pos=(-0.2, 0.2),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='yellow', fillColorSpace='rgb',
    opacity=1, depth=-7.0, interpolate=True)
text_yellow = visual.TextStim(win=win, name='text_yellow',
    text='yellow',
    font='Arial',
    pos=(-0.2, 0.1), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
rec_green = visual.Rect(
    win=win, name='rec_green',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0, pos=(0, 0.2),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='green', fillColorSpace='rgb',
    opacity=1, depth=-9.0, interpolate=True)
text_green = visual.TextStim(win=win, name='text_green',
    text='green',
    font='Arial',
    pos=(0, 0.1), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
rec_cyan = visual.Rect(
    win=win, name='rec_cyan',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0, pos=(0.2, 0.2),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='cyan', fillColorSpace='rgb',
    opacity=1, depth=-11.0, interpolate=True)
text_cyan = visual.TextStim(win=win, name='text_cyan',
    text='cyan',
    font='Arial',
    pos=(0.2, 0.1), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);
rec_blue = visual.Rect(
    win=win, name='rec_blue',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0, pos=(0.4, 0.2),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='blue', fillColorSpace='rgb',
    opacity=1, depth=-13.0, interpolate=True)
text_blue = visual.TextStim(win=win, name='text_blue',
    text='blue',
    font='Arial',
    pos=(0.4, 0.1), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-14.0);
rec_purple = visual.Rect(
    win=win, name='rec_purple',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0, pos=(0.6, 0.2),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='purple', fillColorSpace='rgb',
    opacity=1, depth=-15.0, interpolate=True)
text_purple = visual.TextStim(win=win, name='text_purple',
    text='purple',
    font='Arial',
    pos=(0.6, 0.1), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-16.0);
rec_brown = visual.Rect(
    win=win, name='rec_brown',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0, pos=(0.8, 0.2),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='brown', fillColorSpace='rgb',
    opacity=1, depth=-17.0, interpolate=True)
text_brown = visual.TextStim(win=win, name='text_brown',
    text='brown',
    font='Arial',
    pos=(0.8, 0.1), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-18.0);
text_continue = visual.TextStim(win=win, name='text_continue',
    text='Please let your instructor know when you are ready to start the measurement.',
    font='Arial',
    pos=(0, -0.35), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-19.0);
text_example_middle = visual.TextStim(win=win, name='text_example_middle',
    text='blue',
    font='Arial',
    pos=(0, -0.15), height=0.075, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-22.0);
text_example_left_ans = visual.TextStim(win=win, name='text_example_left_ans',
    text='blue',
    font='Arial',
    pos=(-0.3, -0.15), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-23.0);
text_example_right_ans = visual.TextStim(win=win, name='text_example_right_ans',
    text='red',
    font='Arial',
    pos=(0.3, -0.15), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-24.0);
text_example = visual.TextStim(win=win, name='text_example',
    text='Stroop Example',
    font='Arial',
    pos=(0, -0.05), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-25.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()
text_blank = visual.TextStim(win=win, name='text_blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Part_Two_Measurement"
Part_Two_MeasurementClock = core.Clock()
text_word_item = visual.TextStim(win=win, name='text_word_item',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_left_ans = visual.TextStim(win=win, name='text_left_ans',
    text='default text',
    font='Arial',
    pos=(-0.5, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_right_ans = visual.TextStim(win=win, name='text_right_ans',
    text='default text',
    font='Arial',
    pos=(0.5, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()
text_blank = visual.TextStim(win=win, name='text_blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Part_Two_Meas_Stop"
Part_Two_Meas_StopClock = core.Clock()
text_part_two_meas_stop = visual.TextStim(win=win, name='text_part_two_meas_stop',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Stress_Evaluation_One"
Stress_Evaluation_OneClock = core.Clock()
text_evaluation_one_title = visual.TextStim(win=win, name='text_evaluation_one_title',
    text='Task finished:',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_evaluation_one = visual.TextStim(win=win, name='text_evaluation_one',
    text='Please rate your current stress level.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
rating_evaluation_one = visual.RatingScale(win=win, name='rating_evaluation_one', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=10, labels=['completely relaxed', ' stressed out'], scale='', markerStart='5')

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()
text_blank = visual.TextStim(win=win, name='text_blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Stress_Evaluation_Two"
Stress_Evaluation_TwoClock = core.Clock()
text_evaluation_two = visual.TextStim(win=win, name='text_evaluation_two',
    text='Please rate the difficulty of the task.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
rating_evaluation_two = visual.RatingScale(win=win, name='rating_evaluation_two', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=10, labels=['very easy', ' easy', ' hard', ' very hard'], scale='')

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()
text_blank = visual.TextStim(win=win, name='text_blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Part_Two_End"
Part_Two_EndClock = core.Clock()
text_part_two_end = visual.TextStim(win=win, name='text_part_two_end',
    text='Ending Part Two',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_part_two_end_instructions = visual.TextStim(win=win, name='text_part_two_end_instructions',
    text="(Press 'SPACE' to continue)",
    font='Arial',
    pos=(0, -0.2), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()
text_blank = visual.TextStim(win=win, name='text_blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Cooldown_Screen"
Cooldown_ScreenClock = core.Clock()
text_cooldown_title = visual.TextStim(win=win, name='text_cooldown_title',
    text='Intermission:',
    font='Arial',
    pos=(0, 0.2), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_cooldown = visual.TextStim(win=win, name='text_cooldown',
    text='Cooldown Phase',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()
text_blank = visual.TextStim(win=win, name='text_blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Cooldown_Instructions"
Cooldown_InstructionsClock = core.Clock()
text_cooldown_instructions = visual.TextStim(win=win, name='text_cooldown_instructions',
    text='Please try to relax as much as possible.\n\nWhen you are ready please tell your instructor to start the measurement.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_cooldown_instructions_title = visual.TextStim(win=win, name='text_cooldown_instructions_title',
    text='Instructions:',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()
text_blank = visual.TextStim(win=win, name='text_blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Countdown_Screen_10"
Countdown_Screen_10Clock = core.Clock()
text_countdown = visual.TextStim(win=win, name='text_countdown',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()
text_blank = visual.TextStim(win=win, name='text_blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Cooldown_Measurement"
Cooldown_MeasurementClock = core.Clock()
text_cooldown_measurement = visual.TextStim(win=win, name='text_cooldown_measurement',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.4, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()
text_blank = visual.TextStim(win=win, name='text_blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Stress_Evaluation_One"
Stress_Evaluation_OneClock = core.Clock()
text_evaluation_one_title = visual.TextStim(win=win, name='text_evaluation_one_title',
    text='Task finished:',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_evaluation_one = visual.TextStim(win=win, name='text_evaluation_one',
    text='Please rate your current stress level.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
rating_evaluation_one = visual.RatingScale(win=win, name='rating_evaluation_one', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=10, labels=['completely relaxed', ' stressed out'], scale='', markerStart='5')

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()
text_blank = visual.TextStim(win=win, name='text_blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Stress_End"
Stress_EndClock = core.Clock()
text_stress_end = visual.TextStim(win=win, name='text_stress_end',
    text='Ending Session Two',
    font='Arial',
    pos=(0, 0.1), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_stress_end_instructions = visual.TextStim(win=win, name='text_stress_end_instructions',
    text="(Press 'SPACE' to exit)",
    font='Arial',
    pos=(0, -0.3), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "te"-------
t = 0
teClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(20.000000)
# update component parameters for each repeat
sound_1.setSound('A', secs=5)
sound_1.setVolume(1, log=False)
sound_2.setSound('660', secs=5)
sound_2.setVolume(1, log=False)
sound_3.setSound('880', secs=5)
sound_3.setVolume(1, log=False)
sound_4.setSound('1100', secs=5)
sound_4.setVolume(1, log=False)
# keep track of which components have finished
teComponents = [sound_1, sound_2, sound_3, sound_4]
for thisComponent in teComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "te"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = teClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop sound_1
    if t >= 0.0 and sound_1.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_1.tStart = t  # not accounting for scr refresh
        sound_1.frameNStart = frameN  # exact frame index
        win.timeOnFlip(sound_1, 'tStartRefresh')  # time at next scr refresh
        win.callOnFlip(sound_1.play)  # screen flip
    frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if sound_1.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        sound_1.tStop = t  # not accounting for scr refresh
        sound_1.frameNStop = frameN  # exact frame index
        win.timeOnFlip(sound_1, 'tStopRefresh')  # time at next scr refresh
        if 5 > 0.5:  # don't force-stop brief sounds
            sound_1.stop()
    # start/stop sound_2
    if t >= 5 and sound_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_2.tStart = t  # not accounting for scr refresh
        sound_2.frameNStart = frameN  # exact frame index
        win.timeOnFlip(sound_2, 'tStartRefresh')  # time at next scr refresh
        win.callOnFlip(sound_2.play)  # screen flip
    frameRemains = 5 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if sound_2.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        sound_2.tStop = t  # not accounting for scr refresh
        sound_2.frameNStop = frameN  # exact frame index
        win.timeOnFlip(sound_2, 'tStopRefresh')  # time at next scr refresh
        if 5 > 0.5:  # don't force-stop brief sounds
            sound_2.stop()
    # start/stop sound_3
    if t >= 10 and sound_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_3.tStart = t  # not accounting for scr refresh
        sound_3.frameNStart = frameN  # exact frame index
        win.timeOnFlip(sound_3, 'tStartRefresh')  # time at next scr refresh
        win.callOnFlip(sound_3.play)  # screen flip
    frameRemains = 10 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if sound_3.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        sound_3.tStop = t  # not accounting for scr refresh
        sound_3.frameNStop = frameN  # exact frame index
        win.timeOnFlip(sound_3, 'tStopRefresh')  # time at next scr refresh
        if 5 > 0.5:  # don't force-stop brief sounds
            sound_3.stop()
    # start/stop sound_4
    if t >= 15 and sound_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_4.tStart = t  # not accounting for scr refresh
        sound_4.frameNStart = frameN  # exact frame index
        win.timeOnFlip(sound_4, 'tStartRefresh')  # time at next scr refresh
        win.callOnFlip(sound_4.play)  # screen flip
    frameRemains = 15 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if sound_4.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        sound_4.tStop = t  # not accounting for scr refresh
        sound_4.frameNStop = frameN  # exact frame index
        win.timeOnFlip(sound_4, 'tStopRefresh')  # time at next scr refresh
        if 5 > 0.5:  # don't force-stop brief sounds
            sound_4.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in teComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "te"-------
for thisComponent in teComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sound_1.stop()  # ensure sound has stopped at end of routine
thisExp.addData('sound_1.started', sound_1.tStartRefresh)
thisExp.addData('sound_1.stopped', sound_1.tStopRefresh)
sound_2.stop()  # ensure sound has stopped at end of routine
thisExp.addData('sound_2.started', sound_2.tStartRefresh)
thisExp.addData('sound_2.stopped', sound_2.tStopRefresh)
sound_3.stop()  # ensure sound has stopped at end of routine
thisExp.addData('sound_3.started', sound_3.tStartRefresh)
thisExp.addData('sound_3.stopped', sound_3.tStopRefresh)
sound_4.stop()  # ensure sound has stopped at end of routine
thisExp.addData('sound_4.started', sound_4.tStartRefresh)
thisExp.addData('sound_4.stopped', sound_4.tStopRefresh)

# ------Prepare to start Routine "Stress_Screen"-------
t = 0
Stress_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
Stress_ScreenComponents = [text_stress_screen_title, text_stress_screen]
for thisComponent in Stress_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Stress_Screen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Stress_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_stress_screen_title* updates
    if t >= 0.0 and text_stress_screen_title.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_stress_screen_title.tStart = t  # not accounting for scr refresh
        text_stress_screen_title.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_stress_screen_title, 'tStartRefresh')  # time at next scr refresh
        text_stress_screen_title.setAutoDraw(True)
    frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_stress_screen_title.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_stress_screen_title.tStop = t  # not accounting for scr refresh
        text_stress_screen_title.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_stress_screen_title, 'tStopRefresh')  # time at next scr refresh
        text_stress_screen_title.setAutoDraw(False)
    
    # *text_stress_screen* updates
    if t >= 0.0 and text_stress_screen.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_stress_screen.tStart = t  # not accounting for scr refresh
        text_stress_screen.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_stress_screen, 'tStartRefresh')  # time at next scr refresh
        text_stress_screen.setAutoDraw(True)
    frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_stress_screen.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_stress_screen.tStop = t  # not accounting for scr refresh
        text_stress_screen.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_stress_screen, 'tStopRefresh')  # time at next scr refresh
        text_stress_screen.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Stress_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Stress_Screen"-------
for thisComponent in Stress_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = [text_blank]
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_blank* updates
    if t >= 0.0 and text_blank.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_blank.tStart = t  # not accounting for scr refresh
        text_blank.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_blank, 'tStartRefresh')  # time at next scr refresh
        text_blank.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_blank.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_blank.tStop = t  # not accounting for scr refresh
        text_blank.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_blank, 'tStopRefresh')  # time at next scr refresh
        text_blank.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Blank_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Blank_Screen"-------
for thisComponent in Blank_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "Part_One"-------
t = 0
Part_OneClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
Part_OneComponents = [text_part_one_title, text_part_one]
for thisComponent in Part_OneComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Part_One"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Part_OneClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_part_one_title* updates
    if t >= 0.0 and text_part_one_title.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_part_one_title.tStart = t  # not accounting for scr refresh
        text_part_one_title.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_part_one_title, 'tStartRefresh')  # time at next scr refresh
        text_part_one_title.setAutoDraw(True)
    frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_part_one_title.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_part_one_title.tStop = t  # not accounting for scr refresh
        text_part_one_title.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_part_one_title, 'tStopRefresh')  # time at next scr refresh
        text_part_one_title.setAutoDraw(False)
    
    # *text_part_one* updates
    if t >= 0.0 and text_part_one.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_part_one.tStart = t  # not accounting for scr refresh
        text_part_one.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_part_one, 'tStartRefresh')  # time at next scr refresh
        text_part_one.setAutoDraw(True)
    frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_part_one.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_part_one.tStop = t  # not accounting for scr refresh
        text_part_one.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_part_one, 'tStopRefresh')  # time at next scr refresh
        text_part_one.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Part_OneComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Part_One"-------
for thisComponent in Part_OneComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = [text_blank]
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_blank* updates
    if t >= 0.0 and text_blank.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_blank.tStart = t  # not accounting for scr refresh
        text_blank.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_blank, 'tStartRefresh')  # time at next scr refresh
        text_blank.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_blank.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_blank.tStop = t  # not accounting for scr refresh
        text_blank.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_blank, 'tStopRefresh')  # time at next scr refresh
        text_blank.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Blank_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Blank_Screen"-------
for thisComponent in Blank_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "Part_One_Instructions"-------
t = 0
Part_One_InstructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_part_one_instructions = keyboard.Keyboard()
# keep track of which components have finished
Part_One_InstructionsComponents = [text_part_one_instructions_title, text_part_one_instructions, key_resp_part_one_instructions]
for thisComponent in Part_One_InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Part_One_Instructions"-------
while continueRoutine:
    # get current time
    t = Part_One_InstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_part_one_instructions_title* updates
    if t >= 0.0 and text_part_one_instructions_title.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_part_one_instructions_title.tStart = t  # not accounting for scr refresh
        text_part_one_instructions_title.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_part_one_instructions_title, 'tStartRefresh')  # time at next scr refresh
        text_part_one_instructions_title.setAutoDraw(True)
    
    # *text_part_one_instructions* updates
    if t >= 0.0 and text_part_one_instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_part_one_instructions.tStart = t  # not accounting for scr refresh
        text_part_one_instructions.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_part_one_instructions, 'tStartRefresh')  # time at next scr refresh
        text_part_one_instructions.setAutoDraw(True)
    
    # *key_resp_part_one_instructions* updates
    if t >= 0.0 and key_resp_part_one_instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_part_one_instructions.tStart = t  # not accounting for scr refresh
        key_resp_part_one_instructions.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_part_one_instructions, 'tStartRefresh')  # time at next scr refresh
        key_resp_part_one_instructions.status = STARTED
        # keyboard checking is just starting
        key_resp_part_one_instructions.clearEvents(eventType='keyboard')
    if key_resp_part_one_instructions.status == STARTED:
        theseKeys = key_resp_part_one_instructions.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Part_One_InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Part_One_Instructions"-------
for thisComponent in Part_One_InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData("start_stress_one", time.strftime("%Y-%m-%d_%H:%M:%S")) 
# the Routine "Part_One_Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = [text_blank]
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_blank* updates
    if t >= 0.0 and text_blank.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_blank.tStart = t  # not accounting for scr refresh
        text_blank.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_blank, 'tStartRefresh')  # time at next scr refresh
        text_blank.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_blank.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_blank.tStop = t  # not accounting for scr refresh
        text_blank.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_blank, 'tStopRefresh')  # time at next scr refresh
        text_blank.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Blank_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Blank_Screen"-------
for thisComponent in Blank_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
tick = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('..\\Resources\\StimuliFiles\\metronome.xlsx'),
    seed=None, name='tick')
thisExp.addLoop(tick)  # add the loop to the experiment
thisTick = tick.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTick.rgb)
if thisTick != None:
    for paramName in thisTick:
        exec('{} = thisTick[paramName]'.format(paramName))

for thisTick in tick:
    currentLoop = tick
    # abbreviate parameter names if possible (e.g. rgb = thisTick.rgb)
    if thisTick != None:
        for paramName in thisTick:
            exec('{} = thisTick[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Part_One_Measurement"-------
    t = 0
    Part_One_MeasurementClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    metronome_dot.setFillColor(Color)
    metronome_tone.setSound(Tone, secs=0.5)
    metronome_tone.setVolume(0.5, log=False)
    # keep track of which components have finished
    Part_One_MeasurementComponents = [metronome_dot, metronome_tone]
    for thisComponent in Part_One_MeasurementComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Part_One_Measurement"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Part_One_MeasurementClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *metronome_dot* updates
        if t >= 0.0 and metronome_dot.status == NOT_STARTED:
            # keep track of start time/frame for later
            metronome_dot.tStart = t  # not accounting for scr refresh
            metronome_dot.frameNStart = frameN  # exact frame index
            win.timeOnFlip(metronome_dot, 'tStartRefresh')  # time at next scr refresh
            metronome_dot.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if metronome_dot.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            metronome_dot.tStop = t  # not accounting for scr refresh
            metronome_dot.frameNStop = frameN  # exact frame index
            win.timeOnFlip(metronome_dot, 'tStopRefresh')  # time at next scr refresh
            metronome_dot.setAutoDraw(False)
        # start/stop metronome_tone
        if t >= 0.0 and metronome_tone.status == NOT_STARTED:
            # keep track of start time/frame for later
            metronome_tone.tStart = t  # not accounting for scr refresh
            metronome_tone.frameNStart = frameN  # exact frame index
            win.timeOnFlip(metronome_tone, 'tStartRefresh')  # time at next scr refresh
            win.callOnFlip(metronome_tone.play)  # screen flip
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if metronome_tone.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            metronome_tone.tStop = t  # not accounting for scr refresh
            metronome_tone.frameNStop = frameN  # exact frame index
            win.timeOnFlip(metronome_tone, 'tStopRefresh')  # time at next scr refresh
            if 0.5 > 0.5:  # don't force-stop brief sounds
                metronome_tone.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Part_One_MeasurementComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Part_One_Measurement"-------
    for thisComponent in Part_One_MeasurementComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    metronome_tone.stop()  # ensure sound has stopped at end of routine
    
    # ------Prepare to start Routine "Metronome_Tick"-------
    t = 0
    Metronome_TickClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    Metronome_TickComponents = [text_metronom_tick]
    for thisComponent in Metronome_TickComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Metronome_Tick"-------
    while continueRoutine:
        # get current time
        t = Metronome_TickClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_metronom_tick* updates
        if t >= 0.0 and text_metronom_tick.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_metronom_tick.tStart = t  # not accounting for scr refresh
            text_metronom_tick.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_metronom_tick, 'tStartRefresh')  # time at next scr refresh
            text_metronom_tick.setAutoDraw(True)
        frameRemains = 0.0 + TimeDur- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_metronom_tick.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            text_metronom_tick.tStop = t  # not accounting for scr refresh
            text_metronom_tick.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_metronom_tick, 'tStopRefresh')  # time at next scr refresh
            text_metronom_tick.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Metronome_TickComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Metronome_Tick"-------
    for thisComponent in Metronome_TickComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Metronome_Tick" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'tick'

# get names of stimulus parameters
if tick.trialList in ([], [None], None):
    params = []
else:
    params = tick.trialList[0].keys()
# save data for this loop
tick.saveAsExcel(filename + '.xlsx', sheetName='tick',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
tick.saveAsText(filename + 'tick.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "Part_One_Meas_Stop"-------
t = 0
Part_One_Meas_StopClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
thisExp.addData("end_stress_one", time.strftime("%Y-%m-%d_%H:%M:%S")) 
# keep track of which components have finished
Part_One_Meas_StopComponents = [text_part_one_meas_stop]
for thisComponent in Part_One_Meas_StopComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Part_One_Meas_Stop"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Part_One_Meas_StopClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_part_one_meas_stop* updates
    if t >= 0.0 and text_part_one_meas_stop.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_part_one_meas_stop.tStart = t  # not accounting for scr refresh
        text_part_one_meas_stop.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_part_one_meas_stop, 'tStartRefresh')  # time at next scr refresh
        text_part_one_meas_stop.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_part_one_meas_stop.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_part_one_meas_stop.tStop = t  # not accounting for scr refresh
        text_part_one_meas_stop.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_part_one_meas_stop, 'tStopRefresh')  # time at next scr refresh
        text_part_one_meas_stop.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Part_One_Meas_StopComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Part_One_Meas_Stop"-------
for thisComponent in Part_One_Meas_StopComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "Stress_Evaluation_One"-------
t = 0
Stress_Evaluation_OneClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
rating_evaluation_one.reset()
# keep track of which components have finished
Stress_Evaluation_OneComponents = [text_evaluation_one_title, text_evaluation_one, rating_evaluation_one]
for thisComponent in Stress_Evaluation_OneComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Stress_Evaluation_One"-------
while continueRoutine:
    # get current time
    t = Stress_Evaluation_OneClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_evaluation_one_title* updates
    if t >= 0.0 and text_evaluation_one_title.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_evaluation_one_title.tStart = t  # not accounting for scr refresh
        text_evaluation_one_title.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_evaluation_one_title, 'tStartRefresh')  # time at next scr refresh
        text_evaluation_one_title.setAutoDraw(True)
    
    # *text_evaluation_one* updates
    if t >= 0.0 and text_evaluation_one.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_evaluation_one.tStart = t  # not accounting for scr refresh
        text_evaluation_one.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_evaluation_one, 'tStartRefresh')  # time at next scr refresh
        text_evaluation_one.setAutoDraw(True)
    # *rating_evaluation_one* updates
    if t >= 0.0 and rating_evaluation_one.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating_evaluation_one.tStart = t  # not accounting for scr refresh
        rating_evaluation_one.frameNStart = frameN  # exact frame index
        win.timeOnFlip(rating_evaluation_one, 'tStartRefresh')  # time at next scr refresh
        rating_evaluation_one.setAutoDraw(True)
    continueRoutine &= rating_evaluation_one.noResponse  # a response ends the trial
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Stress_Evaluation_OneComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Stress_Evaluation_One"-------
for thisComponent in Stress_Evaluation_OneComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('rating_evaluation_one.response', rating_evaluation_one.getRating())
thisExp.addData('rating_evaluation_one.rt', rating_evaluation_one.getRT())
thisExp.nextEntry()
# the Routine "Stress_Evaluation_One" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = [text_blank]
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_blank* updates
    if t >= 0.0 and text_blank.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_blank.tStart = t  # not accounting for scr refresh
        text_blank.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_blank, 'tStartRefresh')  # time at next scr refresh
        text_blank.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_blank.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_blank.tStop = t  # not accounting for scr refresh
        text_blank.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_blank, 'tStopRefresh')  # time at next scr refresh
        text_blank.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Blank_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Blank_Screen"-------
for thisComponent in Blank_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "Stress_Evaluation_Two"-------
t = 0
Stress_Evaluation_TwoClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
rating_evaluation_two.reset()
# keep track of which components have finished
Stress_Evaluation_TwoComponents = [text_evaluation_two, rating_evaluation_two]
for thisComponent in Stress_Evaluation_TwoComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Stress_Evaluation_Two"-------
while continueRoutine:
    # get current time
    t = Stress_Evaluation_TwoClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_evaluation_two* updates
    if t >= 0.0 and text_evaluation_two.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_evaluation_two.tStart = t  # not accounting for scr refresh
        text_evaluation_two.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_evaluation_two, 'tStartRefresh')  # time at next scr refresh
        text_evaluation_two.setAutoDraw(True)
    # *rating_evaluation_two* updates
    if t >= 0.0 and rating_evaluation_two.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating_evaluation_two.tStart = t  # not accounting for scr refresh
        rating_evaluation_two.frameNStart = frameN  # exact frame index
        win.timeOnFlip(rating_evaluation_two, 'tStartRefresh')  # time at next scr refresh
        rating_evaluation_two.setAutoDraw(True)
    continueRoutine &= rating_evaluation_two.noResponse  # a response ends the trial
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Stress_Evaluation_TwoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Stress_Evaluation_Two"-------
for thisComponent in Stress_Evaluation_TwoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('rating_evaluation_two.response', rating_evaluation_two.getRating())
thisExp.addData('rating_evaluation_two.rt', rating_evaluation_two.getRT())
thisExp.nextEntry()
# the Routine "Stress_Evaluation_Two" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = [text_blank]
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_blank* updates
    if t >= 0.0 and text_blank.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_blank.tStart = t  # not accounting for scr refresh
        text_blank.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_blank, 'tStartRefresh')  # time at next scr refresh
        text_blank.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_blank.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_blank.tStop = t  # not accounting for scr refresh
        text_blank.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_blank, 'tStopRefresh')  # time at next scr refresh
        text_blank.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Blank_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Blank_Screen"-------
for thisComponent in Blank_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "Part_One_End"-------
t = 0
Part_One_EndClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_part_one_end = keyboard.Keyboard()
# keep track of which components have finished
Part_One_EndComponents = [text_part_one_end, text_part_one_end_instructions, key_resp_part_one_end]
for thisComponent in Part_One_EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Part_One_End"-------
while continueRoutine:
    # get current time
    t = Part_One_EndClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_part_one_end* updates
    if t >= 0.0 and text_part_one_end.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_part_one_end.tStart = t  # not accounting for scr refresh
        text_part_one_end.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_part_one_end, 'tStartRefresh')  # time at next scr refresh
        text_part_one_end.setAutoDraw(True)
    
    # *text_part_one_end_instructions* updates
    if t >= 0.0 and text_part_one_end_instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_part_one_end_instructions.tStart = t  # not accounting for scr refresh
        text_part_one_end_instructions.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_part_one_end_instructions, 'tStartRefresh')  # time at next scr refresh
        text_part_one_end_instructions.setAutoDraw(True)
    
    # *key_resp_part_one_end* updates
    if t >= 0.0 and key_resp_part_one_end.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_part_one_end.tStart = t  # not accounting for scr refresh
        key_resp_part_one_end.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_part_one_end, 'tStartRefresh')  # time at next scr refresh
        key_resp_part_one_end.status = STARTED
        # keyboard checking is just starting
        key_resp_part_one_end.clearEvents(eventType='keyboard')
    if key_resp_part_one_end.status == STARTED:
        theseKeys = key_resp_part_one_end.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Part_One_EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Part_One_End"-------
for thisComponent in Part_One_EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Part_One_End" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = [text_blank]
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_blank* updates
    if t >= 0.0 and text_blank.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_blank.tStart = t  # not accounting for scr refresh
        text_blank.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_blank, 'tStartRefresh')  # time at next scr refresh
        text_blank.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_blank.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_blank.tStop = t  # not accounting for scr refresh
        text_blank.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_blank, 'tStopRefresh')  # time at next scr refresh
        text_blank.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Blank_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Blank_Screen"-------
for thisComponent in Blank_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "Part_Two"-------
t = 0
Part_TwoClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
Part_TwoComponents = [text_part_two_title, text_part_two]
for thisComponent in Part_TwoComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Part_Two"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Part_TwoClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_part_two_title* updates
    if t >= 0.0 and text_part_two_title.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_part_two_title.tStart = t  # not accounting for scr refresh
        text_part_two_title.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_part_two_title, 'tStartRefresh')  # time at next scr refresh
        text_part_two_title.setAutoDraw(True)
    frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_part_two_title.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_part_two_title.tStop = t  # not accounting for scr refresh
        text_part_two_title.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_part_two_title, 'tStopRefresh')  # time at next scr refresh
        text_part_two_title.setAutoDraw(False)
    
    # *text_part_two* updates
    if t >= 0.0 and text_part_two.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_part_two.tStart = t  # not accounting for scr refresh
        text_part_two.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_part_two, 'tStartRefresh')  # time at next scr refresh
        text_part_two.setAutoDraw(True)
    frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_part_two.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_part_two.tStop = t  # not accounting for scr refresh
        text_part_two.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_part_two, 'tStopRefresh')  # time at next scr refresh
        text_part_two.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Part_TwoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Part_Two"-------
for thisComponent in Part_TwoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = [text_blank]
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_blank* updates
    if t >= 0.0 and text_blank.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_blank.tStart = t  # not accounting for scr refresh
        text_blank.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_blank, 'tStartRefresh')  # time at next scr refresh
        text_blank.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_blank.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_blank.tStop = t  # not accounting for scr refresh
        text_blank.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_blank, 'tStopRefresh')  # time at next scr refresh
        text_blank.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Blank_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Blank_Screen"-------
for thisComponent in Blank_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "Part_Two_Instructions"-------
t = 0
Part_Two_InstructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_part_two_instructions = keyboard.Keyboard()
# keep track of which components have finished
Part_Two_InstructionsComponents = [text_part_two_instructions_title, text_part_two_instructions, key_resp_part_two_instructions]
for thisComponent in Part_Two_InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Part_Two_Instructions"-------
while continueRoutine:
    # get current time
    t = Part_Two_InstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_part_two_instructions_title* updates
    if t >= 0.0 and text_part_two_instructions_title.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_part_two_instructions_title.tStart = t  # not accounting for scr refresh
        text_part_two_instructions_title.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_part_two_instructions_title, 'tStartRefresh')  # time at next scr refresh
        text_part_two_instructions_title.setAutoDraw(True)
    
    # *text_part_two_instructions* updates
    if t >= 0.0 and text_part_two_instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_part_two_instructions.tStart = t  # not accounting for scr refresh
        text_part_two_instructions.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_part_two_instructions, 'tStartRefresh')  # time at next scr refresh
        text_part_two_instructions.setAutoDraw(True)
    
    # *key_resp_part_two_instructions* updates
    if t >= 0.0 and key_resp_part_two_instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_part_two_instructions.tStart = t  # not accounting for scr refresh
        key_resp_part_two_instructions.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_part_two_instructions, 'tStartRefresh')  # time at next scr refresh
        key_resp_part_two_instructions.status = STARTED
        # keyboard checking is just starting
        key_resp_part_two_instructions.clearEvents(eventType='keyboard')
    if key_resp_part_two_instructions.status == STARTED:
        theseKeys = key_resp_part_two_instructions.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Part_Two_InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Part_Two_Instructions"-------
for thisComponent in Part_Two_InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Part_Two_Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = [text_blank]
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_blank* updates
    if t >= 0.0 and text_blank.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_blank.tStart = t  # not accounting for scr refresh
        text_blank.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_blank, 'tStartRefresh')  # time at next scr refresh
        text_blank.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_blank.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_blank.tStop = t  # not accounting for scr refresh
        text_blank.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_blank, 'tStopRefresh')  # time at next scr refresh
        text_blank.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Blank_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Blank_Screen"-------
for thisComponent in Blank_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "Color_Instructions"-------
t = 0
Color_InstructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_color_instructions = keyboard.Keyboard()
# keep track of which components have finished
Color_InstructionsComponents = [text_color_instructions, rec_red, text_red, rec_magenta, text_magenta, rec_orange, text_orange, rec_yellow, text_yellow, rec_green, text_green, rec_cyan, text_cyan, rec_blue, text_blue, rec_purple, text_purple, rec_brown, text_brown, text_continue, key_resp_color_instructions, text_example_middle, text_example_left_ans, text_example_right_ans, text_example]
for thisComponent in Color_InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Color_Instructions"-------
while continueRoutine:
    # get current time
    t = Color_InstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_color_instructions* updates
    if t >= 0.0 and text_color_instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_color_instructions.tStart = t  # not accounting for scr refresh
        text_color_instructions.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_color_instructions, 'tStartRefresh')  # time at next scr refresh
        text_color_instructions.setAutoDraw(True)
    
    # *rec_red* updates
    if t >= 0.0 and rec_red.status == NOT_STARTED:
        # keep track of start time/frame for later
        rec_red.tStart = t  # not accounting for scr refresh
        rec_red.frameNStart = frameN  # exact frame index
        win.timeOnFlip(rec_red, 'tStartRefresh')  # time at next scr refresh
        rec_red.setAutoDraw(True)
    
    # *text_red* updates
    if t >= 0.0 and text_red.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_red.tStart = t  # not accounting for scr refresh
        text_red.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_red, 'tStartRefresh')  # time at next scr refresh
        text_red.setAutoDraw(True)
    
    # *rec_magenta* updates
    if t >= 0.0 and rec_magenta.status == NOT_STARTED:
        # keep track of start time/frame for later
        rec_magenta.tStart = t  # not accounting for scr refresh
        rec_magenta.frameNStart = frameN  # exact frame index
        win.timeOnFlip(rec_magenta, 'tStartRefresh')  # time at next scr refresh
        rec_magenta.setAutoDraw(True)
    
    # *text_magenta* updates
    if t >= 0.0 and text_magenta.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_magenta.tStart = t  # not accounting for scr refresh
        text_magenta.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_magenta, 'tStartRefresh')  # time at next scr refresh
        text_magenta.setAutoDraw(True)
    
    # *rec_orange* updates
    if t >= 0.0 and rec_orange.status == NOT_STARTED:
        # keep track of start time/frame for later
        rec_orange.tStart = t  # not accounting for scr refresh
        rec_orange.frameNStart = frameN  # exact frame index
        win.timeOnFlip(rec_orange, 'tStartRefresh')  # time at next scr refresh
        rec_orange.setAutoDraw(True)
    
    # *text_orange* updates
    if t >= 0.0 and text_orange.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_orange.tStart = t  # not accounting for scr refresh
        text_orange.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_orange, 'tStartRefresh')  # time at next scr refresh
        text_orange.setAutoDraw(True)
    
    # *rec_yellow* updates
    if t >= 0.0 and rec_yellow.status == NOT_STARTED:
        # keep track of start time/frame for later
        rec_yellow.tStart = t  # not accounting for scr refresh
        rec_yellow.frameNStart = frameN  # exact frame index
        win.timeOnFlip(rec_yellow, 'tStartRefresh')  # time at next scr refresh
        rec_yellow.setAutoDraw(True)
    
    # *text_yellow* updates
    if t >= 0.0 and text_yellow.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_yellow.tStart = t  # not accounting for scr refresh
        text_yellow.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_yellow, 'tStartRefresh')  # time at next scr refresh
        text_yellow.setAutoDraw(True)
    
    # *rec_green* updates
    if t >= 0.0 and rec_green.status == NOT_STARTED:
        # keep track of start time/frame for later
        rec_green.tStart = t  # not accounting for scr refresh
        rec_green.frameNStart = frameN  # exact frame index
        win.timeOnFlip(rec_green, 'tStartRefresh')  # time at next scr refresh
        rec_green.setAutoDraw(True)
    
    # *text_green* updates
    if t >= 0.0 and text_green.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_green.tStart = t  # not accounting for scr refresh
        text_green.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_green, 'tStartRefresh')  # time at next scr refresh
        text_green.setAutoDraw(True)
    
    # *rec_cyan* updates
    if t >= 0.0 and rec_cyan.status == NOT_STARTED:
        # keep track of start time/frame for later
        rec_cyan.tStart = t  # not accounting for scr refresh
        rec_cyan.frameNStart = frameN  # exact frame index
        win.timeOnFlip(rec_cyan, 'tStartRefresh')  # time at next scr refresh
        rec_cyan.setAutoDraw(True)
    
    # *text_cyan* updates
    if t >= 0.0 and text_cyan.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_cyan.tStart = t  # not accounting for scr refresh
        text_cyan.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_cyan, 'tStartRefresh')  # time at next scr refresh
        text_cyan.setAutoDraw(True)
    
    # *rec_blue* updates
    if t >= 0.0 and rec_blue.status == NOT_STARTED:
        # keep track of start time/frame for later
        rec_blue.tStart = t  # not accounting for scr refresh
        rec_blue.frameNStart = frameN  # exact frame index
        win.timeOnFlip(rec_blue, 'tStartRefresh')  # time at next scr refresh
        rec_blue.setAutoDraw(True)
    
    # *text_blue* updates
    if t >= 0.0 and text_blue.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_blue.tStart = t  # not accounting for scr refresh
        text_blue.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_blue, 'tStartRefresh')  # time at next scr refresh
        text_blue.setAutoDraw(True)
    
    # *rec_purple* updates
    if t >= 0.0 and rec_purple.status == NOT_STARTED:
        # keep track of start time/frame for later
        rec_purple.tStart = t  # not accounting for scr refresh
        rec_purple.frameNStart = frameN  # exact frame index
        win.timeOnFlip(rec_purple, 'tStartRefresh')  # time at next scr refresh
        rec_purple.setAutoDraw(True)
    
    # *text_purple* updates
    if t >= 0.0 and text_purple.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_purple.tStart = t  # not accounting for scr refresh
        text_purple.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_purple, 'tStartRefresh')  # time at next scr refresh
        text_purple.setAutoDraw(True)
    
    # *rec_brown* updates
    if t >= 0.0 and rec_brown.status == NOT_STARTED:
        # keep track of start time/frame for later
        rec_brown.tStart = t  # not accounting for scr refresh
        rec_brown.frameNStart = frameN  # exact frame index
        win.timeOnFlip(rec_brown, 'tStartRefresh')  # time at next scr refresh
        rec_brown.setAutoDraw(True)
    
    # *text_brown* updates
    if t >= 0.0 and text_brown.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_brown.tStart = t  # not accounting for scr refresh
        text_brown.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_brown, 'tStartRefresh')  # time at next scr refresh
        text_brown.setAutoDraw(True)
    
    # *text_continue* updates
    if t >= 0.0 and text_continue.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_continue.tStart = t  # not accounting for scr refresh
        text_continue.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_continue, 'tStartRefresh')  # time at next scr refresh
        text_continue.setAutoDraw(True)
    
    # *key_resp_color_instructions* updates
    if t >= 0.0 and key_resp_color_instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_color_instructions.tStart = t  # not accounting for scr refresh
        key_resp_color_instructions.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_color_instructions, 'tStartRefresh')  # time at next scr refresh
        key_resp_color_instructions.status = STARTED
        # keyboard checking is just starting
        key_resp_color_instructions.clearEvents(eventType='keyboard')
    if key_resp_color_instructions.status == STARTED:
        theseKeys = key_resp_color_instructions.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # *text_example_middle* updates
    if t >= 0.0 and text_example_middle.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_example_middle.tStart = t  # not accounting for scr refresh
        text_example_middle.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_example_middle, 'tStartRefresh')  # time at next scr refresh
        text_example_middle.setAutoDraw(True)
    
    # *text_example_left_ans* updates
    if t >= 0.0 and text_example_left_ans.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_example_left_ans.tStart = t  # not accounting for scr refresh
        text_example_left_ans.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_example_left_ans, 'tStartRefresh')  # time at next scr refresh
        text_example_left_ans.setAutoDraw(True)
    
    # *text_example_right_ans* updates
    if t >= 0.0 and text_example_right_ans.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_example_right_ans.tStart = t  # not accounting for scr refresh
        text_example_right_ans.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_example_right_ans, 'tStartRefresh')  # time at next scr refresh
        text_example_right_ans.setAutoDraw(True)
    
    # *text_example* updates
    if t >= 0.0 and text_example.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_example.tStart = t  # not accounting for scr refresh
        text_example.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_example, 'tStartRefresh')  # time at next scr refresh
        text_example.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Color_InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Color_Instructions"-------
for thisComponent in Color_InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData("start_stress_two", time.strftime("%Y-%m-%d_%H:%M:%S")) 
# the Routine "Color_Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = [text_blank]
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_blank* updates
    if t >= 0.0 and text_blank.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_blank.tStart = t  # not accounting for scr refresh
        text_blank.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_blank, 'tStartRefresh')  # time at next scr refresh
        text_blank.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_blank.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_blank.tStop = t  # not accounting for scr refresh
        text_blank.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_blank, 'tStopRefresh')  # time at next scr refresh
        text_blank.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Blank_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Blank_Screen"-------
for thisComponent in Blank_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
stroop_trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('..\\Resources\\StimuliFiles\\stroop_stimuli.xlsx', selection='1:10'),
    seed=None, name='stroop_trials')
thisExp.addLoop(stroop_trials)  # add the loop to the experiment
thisStroop_trial = stroop_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisStroop_trial.rgb)
if thisStroop_trial != None:
    for paramName in thisStroop_trial:
        exec('{} = thisStroop_trial[paramName]'.format(paramName))

for thisStroop_trial in stroop_trials:
    currentLoop = stroop_trials
    # abbreviate parameter names if possible (e.g. rgb = thisStroop_trial.rgb)
    if thisStroop_trial != None:
        for paramName in thisStroop_trial:
            exec('{} = thisStroop_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Part_Two_Measurement"-------
    t = 0
    Part_Two_MeasurementClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    text_word_item.setColor(WordColor, colorSpace='rgb')
    text_word_item.setText(WordItem)
    text_left_ans.setColor('white', colorSpace='rgb')
    text_left_ans.setText(AnsLeft)
    text_right_ans.setColor('white', colorSpace='rgb')
    text_right_ans.setText(AnsRight)
    key_resp_part_two_meas = keyboard.Keyboard()
    # keep track of which components have finished
    Part_Two_MeasurementComponents = [text_word_item, text_left_ans, text_right_ans, key_resp_part_two_meas]
    for thisComponent in Part_Two_MeasurementComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Part_Two_Measurement"-------
    while continueRoutine:
        # get current time
        t = Part_Two_MeasurementClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_word_item* updates
        if t >= 0.0 and text_word_item.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_word_item.tStart = t  # not accounting for scr refresh
            text_word_item.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_word_item, 'tStartRefresh')  # time at next scr refresh
            text_word_item.setAutoDraw(True)
        
        # *text_left_ans* updates
        if t >= 0.0 and text_left_ans.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_left_ans.tStart = t  # not accounting for scr refresh
            text_left_ans.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_left_ans, 'tStartRefresh')  # time at next scr refresh
            text_left_ans.setAutoDraw(True)
        
        # *text_right_ans* updates
        if t >= 0.0 and text_right_ans.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_right_ans.tStart = t  # not accounting for scr refresh
            text_right_ans.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_right_ans, 'tStartRefresh')  # time at next scr refresh
            text_right_ans.setAutoDraw(True)
        
        # *key_resp_part_two_meas* updates
        if t >= 0.0 and key_resp_part_two_meas.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_part_two_meas.tStart = t  # not accounting for scr refresh
            key_resp_part_two_meas.frameNStart = frameN  # exact frame index
            win.timeOnFlip(key_resp_part_two_meas, 'tStartRefresh')  # time at next scr refresh
            key_resp_part_two_meas.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_part_two_meas.clock.reset)  # t=0 on next screen flip
            key_resp_part_two_meas.clearEvents(eventType='keyboard')
        if key_resp_part_two_meas.status == STARTED:
            theseKeys = key_resp_part_two_meas.getKeys(keyList=['left', 'right'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp_part_two_meas.keys = theseKeys.name  # just the last key pressed
                key_resp_part_two_meas.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Part_Two_MeasurementComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Part_Two_Measurement"-------
    for thisComponent in Part_Two_MeasurementComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_part_two_meas.keys in ['', [], None]:  # No response was made
        key_resp_part_two_meas.keys = None
    stroop_trials.addData('key_resp_part_two_meas.keys',key_resp_part_two_meas.keys)
    if key_resp_part_two_meas.keys != None:  # we had a response
        stroop_trials.addData('key_resp_part_two_meas.rt', key_resp_part_two_meas.rt)
    stroop_trials.addData('key_resp_part_two_meas.started', key_resp_part_two_meas.tStartRefresh)
    stroop_trials.addData('key_resp_part_two_meas.stopped', key_resp_part_two_meas.tStopRefresh)
    # the Routine "Part_Two_Measurement" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Blank_Screen"-------
    t = 0
    Blank_ScreenClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    Blank_ScreenComponents = [text_blank]
    for thisComponent in Blank_ScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Blank_Screen"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Blank_ScreenClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_blank* updates
        if t >= 0.0 and text_blank.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_blank.tStart = t  # not accounting for scr refresh
            text_blank.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_blank, 'tStartRefresh')  # time at next scr refresh
            text_blank.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_blank.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            text_blank.tStop = t  # not accounting for scr refresh
            text_blank.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_blank, 'tStopRefresh')  # time at next scr refresh
            text_blank.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Blank_ScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Blank_Screen"-------
    for thisComponent in Blank_ScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'stroop_trials'

# get names of stimulus parameters
if stroop_trials.trialList in ([], [None], None):
    params = []
else:
    params = stroop_trials.trialList[0].keys()
# save data for this loop
stroop_trials.saveAsExcel(filename + '.xlsx', sheetName='stroop_trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
stroop_trials.saveAsText(filename + 'stroop_trials.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "Part_Two_Meas_Stop"-------
t = 0
Part_Two_Meas_StopClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
thisExp.addData("end_stress_two", time.strftime("%Y-%m-%d_%H:%M:%S")) 
# keep track of which components have finished
Part_Two_Meas_StopComponents = [text_part_two_meas_stop]
for thisComponent in Part_Two_Meas_StopComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Part_Two_Meas_Stop"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Part_Two_Meas_StopClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_part_two_meas_stop* updates
    if t >= 0.0 and text_part_two_meas_stop.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_part_two_meas_stop.tStart = t  # not accounting for scr refresh
        text_part_two_meas_stop.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_part_two_meas_stop, 'tStartRefresh')  # time at next scr refresh
        text_part_two_meas_stop.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_part_two_meas_stop.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_part_two_meas_stop.tStop = t  # not accounting for scr refresh
        text_part_two_meas_stop.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_part_two_meas_stop, 'tStopRefresh')  # time at next scr refresh
        text_part_two_meas_stop.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Part_Two_Meas_StopComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Part_Two_Meas_Stop"-------
for thisComponent in Part_Two_Meas_StopComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "Stress_Evaluation_One"-------
t = 0
Stress_Evaluation_OneClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
rating_evaluation_one.reset()
# keep track of which components have finished
Stress_Evaluation_OneComponents = [text_evaluation_one_title, text_evaluation_one, rating_evaluation_one]
for thisComponent in Stress_Evaluation_OneComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Stress_Evaluation_One"-------
while continueRoutine:
    # get current time
    t = Stress_Evaluation_OneClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_evaluation_one_title* updates
    if t >= 0.0 and text_evaluation_one_title.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_evaluation_one_title.tStart = t  # not accounting for scr refresh
        text_evaluation_one_title.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_evaluation_one_title, 'tStartRefresh')  # time at next scr refresh
        text_evaluation_one_title.setAutoDraw(True)
    
    # *text_evaluation_one* updates
    if t >= 0.0 and text_evaluation_one.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_evaluation_one.tStart = t  # not accounting for scr refresh
        text_evaluation_one.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_evaluation_one, 'tStartRefresh')  # time at next scr refresh
        text_evaluation_one.setAutoDraw(True)
    # *rating_evaluation_one* updates
    if t >= 0.0 and rating_evaluation_one.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating_evaluation_one.tStart = t  # not accounting for scr refresh
        rating_evaluation_one.frameNStart = frameN  # exact frame index
        win.timeOnFlip(rating_evaluation_one, 'tStartRefresh')  # time at next scr refresh
        rating_evaluation_one.setAutoDraw(True)
    continueRoutine &= rating_evaluation_one.noResponse  # a response ends the trial
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Stress_Evaluation_OneComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Stress_Evaluation_One"-------
for thisComponent in Stress_Evaluation_OneComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('rating_evaluation_one.response', rating_evaluation_one.getRating())
thisExp.addData('rating_evaluation_one.rt', rating_evaluation_one.getRT())
thisExp.nextEntry()
# the Routine "Stress_Evaluation_One" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = [text_blank]
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_blank* updates
    if t >= 0.0 and text_blank.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_blank.tStart = t  # not accounting for scr refresh
        text_blank.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_blank, 'tStartRefresh')  # time at next scr refresh
        text_blank.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_blank.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_blank.tStop = t  # not accounting for scr refresh
        text_blank.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_blank, 'tStopRefresh')  # time at next scr refresh
        text_blank.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Blank_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Blank_Screen"-------
for thisComponent in Blank_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "Stress_Evaluation_Two"-------
t = 0
Stress_Evaluation_TwoClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
rating_evaluation_two.reset()
# keep track of which components have finished
Stress_Evaluation_TwoComponents = [text_evaluation_two, rating_evaluation_two]
for thisComponent in Stress_Evaluation_TwoComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Stress_Evaluation_Two"-------
while continueRoutine:
    # get current time
    t = Stress_Evaluation_TwoClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_evaluation_two* updates
    if t >= 0.0 and text_evaluation_two.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_evaluation_two.tStart = t  # not accounting for scr refresh
        text_evaluation_two.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_evaluation_two, 'tStartRefresh')  # time at next scr refresh
        text_evaluation_two.setAutoDraw(True)
    # *rating_evaluation_two* updates
    if t >= 0.0 and rating_evaluation_two.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating_evaluation_two.tStart = t  # not accounting for scr refresh
        rating_evaluation_two.frameNStart = frameN  # exact frame index
        win.timeOnFlip(rating_evaluation_two, 'tStartRefresh')  # time at next scr refresh
        rating_evaluation_two.setAutoDraw(True)
    continueRoutine &= rating_evaluation_two.noResponse  # a response ends the trial
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Stress_Evaluation_TwoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Stress_Evaluation_Two"-------
for thisComponent in Stress_Evaluation_TwoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('rating_evaluation_two.response', rating_evaluation_two.getRating())
thisExp.addData('rating_evaluation_two.rt', rating_evaluation_two.getRT())
thisExp.nextEntry()
# the Routine "Stress_Evaluation_Two" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = [text_blank]
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_blank* updates
    if t >= 0.0 and text_blank.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_blank.tStart = t  # not accounting for scr refresh
        text_blank.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_blank, 'tStartRefresh')  # time at next scr refresh
        text_blank.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_blank.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_blank.tStop = t  # not accounting for scr refresh
        text_blank.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_blank, 'tStopRefresh')  # time at next scr refresh
        text_blank.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Blank_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Blank_Screen"-------
for thisComponent in Blank_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "Part_Two_End"-------
t = 0
Part_Two_EndClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_part_two_end = keyboard.Keyboard()
# keep track of which components have finished
Part_Two_EndComponents = [text_part_two_end, text_part_two_end_instructions, key_resp_part_two_end]
for thisComponent in Part_Two_EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Part_Two_End"-------
while continueRoutine:
    # get current time
    t = Part_Two_EndClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_part_two_end* updates
    if t >= 0.0 and text_part_two_end.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_part_two_end.tStart = t  # not accounting for scr refresh
        text_part_two_end.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_part_two_end, 'tStartRefresh')  # time at next scr refresh
        text_part_two_end.setAutoDraw(True)
    
    # *text_part_two_end_instructions* updates
    if t >= 0.0 and text_part_two_end_instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_part_two_end_instructions.tStart = t  # not accounting for scr refresh
        text_part_two_end_instructions.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_part_two_end_instructions, 'tStartRefresh')  # time at next scr refresh
        text_part_two_end_instructions.setAutoDraw(True)
    
    # *key_resp_part_two_end* updates
    if t >= 0.0 and key_resp_part_two_end.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_part_two_end.tStart = t  # not accounting for scr refresh
        key_resp_part_two_end.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_part_two_end, 'tStartRefresh')  # time at next scr refresh
        key_resp_part_two_end.status = STARTED
        # keyboard checking is just starting
        key_resp_part_two_end.clearEvents(eventType='keyboard')
    if key_resp_part_two_end.status == STARTED:
        theseKeys = key_resp_part_two_end.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Part_Two_EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Part_Two_End"-------
for thisComponent in Part_Two_EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Part_Two_End" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = [text_blank]
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_blank* updates
    if t >= 0.0 and text_blank.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_blank.tStart = t  # not accounting for scr refresh
        text_blank.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_blank, 'tStartRefresh')  # time at next scr refresh
        text_blank.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_blank.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_blank.tStop = t  # not accounting for scr refresh
        text_blank.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_blank, 'tStopRefresh')  # time at next scr refresh
        text_blank.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Blank_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Blank_Screen"-------
for thisComponent in Blank_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "Cooldown_Screen"-------
t = 0
Cooldown_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
Cooldown_ScreenComponents = [text_cooldown_title, text_cooldown]
for thisComponent in Cooldown_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Cooldown_Screen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Cooldown_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_cooldown_title* updates
    if t >= 0.0 and text_cooldown_title.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_cooldown_title.tStart = t  # not accounting for scr refresh
        text_cooldown_title.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_cooldown_title, 'tStartRefresh')  # time at next scr refresh
        text_cooldown_title.setAutoDraw(True)
    frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_cooldown_title.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_cooldown_title.tStop = t  # not accounting for scr refresh
        text_cooldown_title.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_cooldown_title, 'tStopRefresh')  # time at next scr refresh
        text_cooldown_title.setAutoDraw(False)
    
    # *text_cooldown* updates
    if t >= 0.0 and text_cooldown.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_cooldown.tStart = t  # not accounting for scr refresh
        text_cooldown.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_cooldown, 'tStartRefresh')  # time at next scr refresh
        text_cooldown.setAutoDraw(True)
    frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_cooldown.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_cooldown.tStop = t  # not accounting for scr refresh
        text_cooldown.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_cooldown, 'tStopRefresh')  # time at next scr refresh
        text_cooldown.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Cooldown_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Cooldown_Screen"-------
for thisComponent in Cooldown_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = [text_blank]
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_blank* updates
    if t >= 0.0 and text_blank.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_blank.tStart = t  # not accounting for scr refresh
        text_blank.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_blank, 'tStartRefresh')  # time at next scr refresh
        text_blank.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_blank.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_blank.tStop = t  # not accounting for scr refresh
        text_blank.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_blank, 'tStopRefresh')  # time at next scr refresh
        text_blank.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Blank_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Blank_Screen"-------
for thisComponent in Blank_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "Cooldown_Instructions"-------
t = 0
Cooldown_InstructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_cooldown_instructions = keyboard.Keyboard()
# keep track of which components have finished
Cooldown_InstructionsComponents = [text_cooldown_instructions, text_cooldown_instructions_title, key_resp_cooldown_instructions]
for thisComponent in Cooldown_InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Cooldown_Instructions"-------
while continueRoutine:
    # get current time
    t = Cooldown_InstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_cooldown_instructions* updates
    if t >= 0.0 and text_cooldown_instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_cooldown_instructions.tStart = t  # not accounting for scr refresh
        text_cooldown_instructions.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_cooldown_instructions, 'tStartRefresh')  # time at next scr refresh
        text_cooldown_instructions.setAutoDraw(True)
    
    # *text_cooldown_instructions_title* updates
    if t >= 0.0 and text_cooldown_instructions_title.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_cooldown_instructions_title.tStart = t  # not accounting for scr refresh
        text_cooldown_instructions_title.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_cooldown_instructions_title, 'tStartRefresh')  # time at next scr refresh
        text_cooldown_instructions_title.setAutoDraw(True)
    
    # *key_resp_cooldown_instructions* updates
    if t >= 0.0 and key_resp_cooldown_instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_cooldown_instructions.tStart = t  # not accounting for scr refresh
        key_resp_cooldown_instructions.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_cooldown_instructions, 'tStartRefresh')  # time at next scr refresh
        key_resp_cooldown_instructions.status = STARTED
        # keyboard checking is just starting
        key_resp_cooldown_instructions.clearEvents(eventType='keyboard')
    if key_resp_cooldown_instructions.status == STARTED:
        theseKeys = key_resp_cooldown_instructions.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Cooldown_InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Cooldown_Instructions"-------
for thisComponent in Cooldown_InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Cooldown_Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = [text_blank]
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_blank* updates
    if t >= 0.0 and text_blank.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_blank.tStart = t  # not accounting for scr refresh
        text_blank.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_blank, 'tStartRefresh')  # time at next scr refresh
        text_blank.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_blank.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_blank.tStop = t  # not accounting for scr refresh
        text_blank.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_blank, 'tStopRefresh')  # time at next scr refresh
        text_blank.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Blank_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Blank_Screen"-------
for thisComponent in Blank_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "Countdown_Screen_10"-------
t = 0
Countdown_Screen_10Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(10.000000)
# update component parameters for each repeat
# keep track of which components have finished
Countdown_Screen_10Components = [text_countdown]
for thisComponent in Countdown_Screen_10Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Countdown_Screen_10"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Countdown_Screen_10Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_countdown* updates
    if t >= 0.0 and text_countdown.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_countdown.tStart = t  # not accounting for scr refresh
        text_countdown.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_countdown, 'tStartRefresh')  # time at next scr refresh
        text_countdown.setAutoDraw(True)
    frameRemains = 0.0 + 10- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_countdown.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_countdown.tStop = t  # not accounting for scr refresh
        text_countdown.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_countdown, 'tStopRefresh')  # time at next scr refresh
        text_countdown.setAutoDraw(False)
    if text_countdown.status == STARTED:  # only update if drawing
        text_countdown.setText(str(round(routineTimer.getTime(),0)) , log=False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Countdown_Screen_10Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Countdown_Screen_10"-------
for thisComponent in Countdown_Screen_10Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = [text_blank]
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_blank* updates
    if t >= 0.0 and text_blank.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_blank.tStart = t  # not accounting for scr refresh
        text_blank.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_blank, 'tStartRefresh')  # time at next scr refresh
        text_blank.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_blank.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_blank.tStop = t  # not accounting for scr refresh
        text_blank.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_blank, 'tStopRefresh')  # time at next scr refresh
        text_blank.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Blank_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Blank_Screen"-------
for thisComponent in Blank_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "Cooldown_Measurement"-------
t = 0
Cooldown_MeasurementClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(10.000000)
# update component parameters for each repeat
thisExp.addData("start_cooldown_measurement", time.strftime("%Y-%m-%d_%H:%M:%S"))
# keep track of which components have finished
Cooldown_MeasurementComponents = [text_cooldown_measurement]
for thisComponent in Cooldown_MeasurementComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Cooldown_Measurement"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Cooldown_MeasurementClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_cooldown_measurement* updates
    if t >= 0.0 and text_cooldown_measurement.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_cooldown_measurement.tStart = t  # not accounting for scr refresh
        text_cooldown_measurement.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_cooldown_measurement, 'tStartRefresh')  # time at next scr refresh
        text_cooldown_measurement.setAutoDraw(True)
    frameRemains = 0.0 + 10- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_cooldown_measurement.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_cooldown_measurement.tStop = t  # not accounting for scr refresh
        text_cooldown_measurement.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_cooldown_measurement, 'tStopRefresh')  # time at next scr refresh
        text_cooldown_measurement.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Cooldown_MeasurementComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Cooldown_Measurement"-------
for thisComponent in Cooldown_MeasurementComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData("end_cooldown_measurement", time.strftime("%Y-%m-%d_%H:%M:%S"))

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = [text_blank]
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_blank* updates
    if t >= 0.0 and text_blank.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_blank.tStart = t  # not accounting for scr refresh
        text_blank.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_blank, 'tStartRefresh')  # time at next scr refresh
        text_blank.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_blank.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_blank.tStop = t  # not accounting for scr refresh
        text_blank.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_blank, 'tStopRefresh')  # time at next scr refresh
        text_blank.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Blank_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Blank_Screen"-------
for thisComponent in Blank_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "Stress_Evaluation_One"-------
t = 0
Stress_Evaluation_OneClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
rating_evaluation_one.reset()
# keep track of which components have finished
Stress_Evaluation_OneComponents = [text_evaluation_one_title, text_evaluation_one, rating_evaluation_one]
for thisComponent in Stress_Evaluation_OneComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Stress_Evaluation_One"-------
while continueRoutine:
    # get current time
    t = Stress_Evaluation_OneClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_evaluation_one_title* updates
    if t >= 0.0 and text_evaluation_one_title.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_evaluation_one_title.tStart = t  # not accounting for scr refresh
        text_evaluation_one_title.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_evaluation_one_title, 'tStartRefresh')  # time at next scr refresh
        text_evaluation_one_title.setAutoDraw(True)
    
    # *text_evaluation_one* updates
    if t >= 0.0 and text_evaluation_one.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_evaluation_one.tStart = t  # not accounting for scr refresh
        text_evaluation_one.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_evaluation_one, 'tStartRefresh')  # time at next scr refresh
        text_evaluation_one.setAutoDraw(True)
    # *rating_evaluation_one* updates
    if t >= 0.0 and rating_evaluation_one.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating_evaluation_one.tStart = t  # not accounting for scr refresh
        rating_evaluation_one.frameNStart = frameN  # exact frame index
        win.timeOnFlip(rating_evaluation_one, 'tStartRefresh')  # time at next scr refresh
        rating_evaluation_one.setAutoDraw(True)
    continueRoutine &= rating_evaluation_one.noResponse  # a response ends the trial
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Stress_Evaluation_OneComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Stress_Evaluation_One"-------
for thisComponent in Stress_Evaluation_OneComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('rating_evaluation_one.response', rating_evaluation_one.getRating())
thisExp.addData('rating_evaluation_one.rt', rating_evaluation_one.getRT())
thisExp.nextEntry()
# the Routine "Stress_Evaluation_One" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = [text_blank]
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_blank* updates
    if t >= 0.0 and text_blank.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_blank.tStart = t  # not accounting for scr refresh
        text_blank.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_blank, 'tStartRefresh')  # time at next scr refresh
        text_blank.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_blank.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_blank.tStop = t  # not accounting for scr refresh
        text_blank.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_blank, 'tStopRefresh')  # time at next scr refresh
        text_blank.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Blank_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Blank_Screen"-------
for thisComponent in Blank_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "Stress_End"-------
t = 0
Stress_EndClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_stress_end = keyboard.Keyboard()
# keep track of which components have finished
Stress_EndComponents = [text_stress_end, text_stress_end_instructions, key_resp_stress_end]
for thisComponent in Stress_EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Stress_End"-------
while continueRoutine:
    # get current time
    t = Stress_EndClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_stress_end* updates
    if t >= 0.0 and text_stress_end.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_stress_end.tStart = t  # not accounting for scr refresh
        text_stress_end.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_stress_end, 'tStartRefresh')  # time at next scr refresh
        text_stress_end.setAutoDraw(True)
    
    # *text_stress_end_instructions* updates
    if t >= 0.0 and text_stress_end_instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_stress_end_instructions.tStart = t  # not accounting for scr refresh
        text_stress_end_instructions.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_stress_end_instructions, 'tStartRefresh')  # time at next scr refresh
        text_stress_end_instructions.setAutoDraw(True)
    
    # *key_resp_stress_end* updates
    if t >= 0.0 and key_resp_stress_end.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_stress_end.tStart = t  # not accounting for scr refresh
        key_resp_stress_end.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_stress_end, 'tStartRefresh')  # time at next scr refresh
        key_resp_stress_end.status = STARTED
        # keyboard checking is just starting
        key_resp_stress_end.clearEvents(eventType='keyboard')
    if key_resp_stress_end.status == STARTED:
        theseKeys = key_resp_stress_end.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Stress_EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Stress_End"-------
for thisComponent in Stress_EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Stress_End" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
thisExp.addData("end_session_two", time.strftime("%Y-%m-%d_%H:%M:%S")) 

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
