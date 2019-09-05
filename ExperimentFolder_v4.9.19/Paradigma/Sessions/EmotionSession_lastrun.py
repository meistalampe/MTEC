#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.3),
    on September 05, 2019, at 02:21
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
expName = 'EmotionSession'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '003'}
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
    originPath='I:\\Master Thesis\\ExperimentFolder\\Paradigma\\Sessions\\EmotionSession_lastrun.py',
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

# Initialize components for Routine "Emotion_Screen"
Emotion_ScreenClock = core.Clock()
text_emotion_screen_title = visual.TextStim(win=win, name='text_emotion_screen_title',
    text='Session Three:',
    font='Arial',
    pos=(0, 0.2), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_emotion_screen = visual.TextStim(win=win, name='text_emotion_screen',
    text='Visual Stimulation \n          Test',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
import time
thisExp.addData("start_session_three", time.strftime("%Y-%m-%d_%H:%M:%S")) 

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
    text='Positive',
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

# Initialize components for Routine "Emotion_Instructions"
Emotion_InstructionsClock = core.Clock()
text_emotion_instruction_title = visual.TextStim(win=win, name='text_emotion_instruction_title',
    text='Instructions:',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_emotion_instructions = visual.TextStim(win=win, name='text_emotion_instructions',
    text='Please focus on the following\npictures.\n\nYou will have to rate each picture\nafter it has been presented.\n\nWhen you are ready please tell your instructor to start the measurement.',
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

# Initialize components for Routine "Emotion_Measurement_P"
Emotion_Measurement_PClock = core.Clock()
image_emotion_p = visual.ImageStim(
    win=win,
    name='image_emotion_p', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()
text_blank = visual.TextStim(win=win, name='text_blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Fix_Screen"
Fix_ScreenClock = core.Clock()
text_fix = visual.TextStim(win=win, name='text_fix',
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

# Initialize components for Routine "Part_One_Meas_End"
Part_One_Meas_EndClock = core.Clock()
text_part_one_meas_end = visual.TextStim(win=win, name='text_part_one_meas_end',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Emotion_Evaluation_P_O"
Emotion_Evaluation_P_OClock = core.Clock()
image_emotion_p_eval_o = visual.ImageStim(
    win=win,
    name='image_emotion_p_eval_o', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.2), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
text_emotion_p_eval_o = visual.TextStim(win=win, name='text_emotion_p_eval_o',
    text='Please rate the intensity of the picture.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
rating_emotion_p_eval_o = visual.RatingScale(win=win, name='rating_emotion_p_eval_o', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=10, labels=['very weak (low)', ' very strong (high)'], scale='', markerStart='5')

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()
text_blank = visual.TextStim(win=win, name='text_blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Emotion_Evaluation_P_T"
Emotion_Evaluation_P_TClock = core.Clock()
image_emotion_p_eval_t = visual.ImageStim(
    win=win,
    name='image_emotion_p_eval_t', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.2), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
text_emotion_p_eval_t = visual.TextStim(win=win, name='text_emotion_p_eval_t',
    text='please rate the feeling of the picture.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
rating_emotion_p_eval_t = visual.RatingScale(win=win, name='rating_emotion_p_eval_t', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=2, labels=['negative', ' positive'], scale='', markerStart='1')

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()
text_blank = visual.TextStim(win=win, name='text_blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
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

# Initialize components for Routine "Cooldown_Evaluation"
Cooldown_EvaluationClock = core.Clock()
text_cooldown_evaluation_title = visual.TextStim(win=win, name='text_cooldown_evaluation_title',
    text='Task finished:',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_cooldown_evaluation = visual.TextStim(win=win, name='text_cooldown_evaluation',
    text='Please select the feeling closest to your current emotional state.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
rating_cooldown_evaluation = visual.RatingScale(win=win, name='rating_cooldown_evaluation', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=6, labels=[''], scale='sad, disgusted, bored, suprised, pleasant, happy')

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()
text_blank = visual.TextStim(win=win, name='text_blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Cooldown_End"
Cooldown_EndClock = core.Clock()
text_cooldown_end = visual.TextStim(win=win, name='text_cooldown_end',
    text='Ending Intermission',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_cooldown_end_instructions = visual.TextStim(win=win, name='text_cooldown_end_instructions',
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
    text='Part Two:',
    font='Arial',
    pos=(0, 0.2), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_part_two = visual.TextStim(win=win, name='text_part_two',
    text='Negative',
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

# Initialize components for Routine "Emotion_Instructions_Two"
Emotion_Instructions_TwoClock = core.Clock()
text_emotion_instruction_title_2 = visual.TextStim(win=win, name='text_emotion_instruction_title_2',
    text='Instructions:',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_emotion_instructions_2 = visual.TextStim(win=win, name='text_emotion_instructions_2',
    text='Please focus on the following\npictures.\n\nYou will have to rate each picture\nafter it has been presented.\n\nWhen you are ready please tell your instructor to start the measurement.',
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

# Initialize components for Routine "Emotion_Measurement_N"
Emotion_Measurement_NClock = core.Clock()
image_emotion_n = visual.ImageStim(
    win=win,
    name='image_emotion_n', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()
text_blank = visual.TextStim(win=win, name='text_blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Fix_Screen"
Fix_ScreenClock = core.Clock()
text_fix = visual.TextStim(win=win, name='text_fix',
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

# Initialize components for Routine "Part_Two_Meas_End"
Part_Two_Meas_EndClock = core.Clock()
text_part_one_meas_end_2 = visual.TextStim(win=win, name='text_part_one_meas_end_2',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Emotion_Evaluation_N_O"
Emotion_Evaluation_N_OClock = core.Clock()
image_emotion_n_eval_o = visual.ImageStim(
    win=win,
    name='image_emotion_n_eval_o', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.2), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
text_emotion_n_eval_o = visual.TextStim(win=win, name='text_emotion_n_eval_o',
    text='Please rate the intensity of the picture.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
rating_emotion_n_eval_o = visual.RatingScale(win=win, name='rating_emotion_n_eval_o', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=10, labels=['very weak (low)', ' very strong (high)'], scale='', markerStart='5')

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()
text_blank = visual.TextStim(win=win, name='text_blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Emotion_Evaluation_N_T"
Emotion_Evaluation_N_TClock = core.Clock()
image_emotion_n_eval_t = visual.ImageStim(
    win=win,
    name='image_emotion_n_eval_t', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.2), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
text_emotion_n_eval_t = visual.TextStim(win=win, name='text_emotion_n_eval_t',
    text='please rate the feeling of the picture.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
rating_emotion_n_eval_t = visual.RatingScale(win=win, name='rating_emotion_n_eval_t', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=2, labels=['negative', ' positive'], scale='', markerStart='2')

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()
text_blank = visual.TextStim(win=win, name='text_blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
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

# Initialize components for Routine "Cooldown_Evaluation"
Cooldown_EvaluationClock = core.Clock()
text_cooldown_evaluation_title = visual.TextStim(win=win, name='text_cooldown_evaluation_title',
    text='Task finished:',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_cooldown_evaluation = visual.TextStim(win=win, name='text_cooldown_evaluation',
    text='Please select the feeling closest to your current emotional state.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
rating_cooldown_evaluation = visual.RatingScale(win=win, name='rating_cooldown_evaluation', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=6, labels=[''], scale='sad, disgusted, bored, suprised, pleasant, happy')

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()
text_blank = visual.TextStim(win=win, name='text_blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Emotion_End"
Emotion_EndClock = core.Clock()
text_ending_screen = visual.TextStim(win=win, name='text_ending_screen',
    text='The End',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_ending_subtitle = visual.TextStim(win=win, name='text_ending_subtitle',
    text='Thank you for participating!',
    font='Arial',
    pos=(0, -0.2), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Emotion_Screen"-------
t = 0
Emotion_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
Emotion_ScreenComponents = [text_emotion_screen_title, text_emotion_screen]
for thisComponent in Emotion_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Emotion_Screen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Emotion_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_emotion_screen_title* updates
    if t >= 0.0 and text_emotion_screen_title.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_emotion_screen_title.tStart = t  # not accounting for scr refresh
        text_emotion_screen_title.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_emotion_screen_title, 'tStartRefresh')  # time at next scr refresh
        text_emotion_screen_title.setAutoDraw(True)
    frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_emotion_screen_title.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_emotion_screen_title.tStop = t  # not accounting for scr refresh
        text_emotion_screen_title.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_emotion_screen_title, 'tStopRefresh')  # time at next scr refresh
        text_emotion_screen_title.setAutoDraw(False)
    
    # *text_emotion_screen* updates
    if t >= 0.0 and text_emotion_screen.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_emotion_screen.tStart = t  # not accounting for scr refresh
        text_emotion_screen.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_emotion_screen, 'tStartRefresh')  # time at next scr refresh
        text_emotion_screen.setAutoDraw(True)
    frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_emotion_screen.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_emotion_screen.tStop = t  # not accounting for scr refresh
        text_emotion_screen.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_emotion_screen, 'tStopRefresh')  # time at next scr refresh
        text_emotion_screen.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Emotion_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Emotion_Screen"-------
for thisComponent in Emotion_ScreenComponents:
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

# ------Prepare to start Routine "Emotion_Instructions"-------
t = 0
Emotion_InstructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_emotion_instructions = keyboard.Keyboard()
# keep track of which components have finished
Emotion_InstructionsComponents = [text_emotion_instruction_title, text_emotion_instructions, key_resp_emotion_instructions]
for thisComponent in Emotion_InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Emotion_Instructions"-------
while continueRoutine:
    # get current time
    t = Emotion_InstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_emotion_instruction_title* updates
    if t >= 0.0 and text_emotion_instruction_title.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_emotion_instruction_title.tStart = t  # not accounting for scr refresh
        text_emotion_instruction_title.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_emotion_instruction_title, 'tStartRefresh')  # time at next scr refresh
        text_emotion_instruction_title.setAutoDraw(True)
    
    # *text_emotion_instructions* updates
    if t >= 0.0 and text_emotion_instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_emotion_instructions.tStart = t  # not accounting for scr refresh
        text_emotion_instructions.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_emotion_instructions, 'tStartRefresh')  # time at next scr refresh
        text_emotion_instructions.setAutoDraw(True)
    
    # *key_resp_emotion_instructions* updates
    if t >= 0.0 and key_resp_emotion_instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_emotion_instructions.tStart = t  # not accounting for scr refresh
        key_resp_emotion_instructions.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_emotion_instructions, 'tStartRefresh')  # time at next scr refresh
        key_resp_emotion_instructions.status = STARTED
        # keyboard checking is just starting
        key_resp_emotion_instructions.clearEvents(eventType='keyboard')
    if key_resp_emotion_instructions.status == STARTED:
        theseKeys = key_resp_emotion_instructions.getKeys(keyList=['space'], waitRelease=False)
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
    for thisComponent in Emotion_InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Emotion_Instructions"-------
for thisComponent in Emotion_InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData("start_emotion_one", time.strftime("%Y-%m-%d_%H:%M:%S")) 
# the Routine "Emotion_Instructions" was not non-slip safe, so reset the non-slip timer
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
emotion_trials_p = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('..\\Resources\\StimuliFiles\\picture_list_pos.xlsx'),
    seed=None, name='emotion_trials_p')
thisExp.addLoop(emotion_trials_p)  # add the loop to the experiment
thisEmotion_trials_p = emotion_trials_p.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEmotion_trials_p.rgb)
if thisEmotion_trials_p != None:
    for paramName in thisEmotion_trials_p:
        exec('{} = thisEmotion_trials_p[paramName]'.format(paramName))

for thisEmotion_trials_p in emotion_trials_p:
    currentLoop = emotion_trials_p
    # abbreviate parameter names if possible (e.g. rgb = thisEmotion_trials_p.rgb)
    if thisEmotion_trials_p != None:
        for paramName in thisEmotion_trials_p:
            exec('{} = thisEmotion_trials_p[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Emotion_Measurement_P"-------
    t = 0
    Emotion_Measurement_PClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(7.000000)
    # update component parameters for each repeat
    image_emotion_p.setSize((p_new_width, p_new_height))
    image_emotion_p.setImage(p_pictures)
    # keep track of which components have finished
    Emotion_Measurement_PComponents = [image_emotion_p]
    for thisComponent in Emotion_Measurement_PComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Emotion_Measurement_P"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Emotion_Measurement_PClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_emotion_p* updates
        if t >= 0.0 and image_emotion_p.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_emotion_p.tStart = t  # not accounting for scr refresh
            image_emotion_p.frameNStart = frameN  # exact frame index
            win.timeOnFlip(image_emotion_p, 'tStartRefresh')  # time at next scr refresh
            image_emotion_p.setAutoDraw(True)
        frameRemains = 0.0 + 7- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_emotion_p.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            image_emotion_p.tStop = t  # not accounting for scr refresh
            image_emotion_p.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_emotion_p, 'tStopRefresh')  # time at next scr refresh
            image_emotion_p.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Emotion_Measurement_PComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Emotion_Measurement_P"-------
    for thisComponent in Emotion_Measurement_PComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    emotion_trials_p.addData('image_emotion_p.started', image_emotion_p.tStartRefresh)
    emotion_trials_p.addData('image_emotion_p.stopped', image_emotion_p.tStopRefresh)
    
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
    
    # ------Prepare to start Routine "Fix_Screen"-------
    t = 0
    Fix_ScreenClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    Fix_ScreenComponents = [text_fix]
    for thisComponent in Fix_ScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Fix_Screen"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Fix_ScreenClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_fix* updates
        if t >= 0.0 and text_fix.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_fix.tStart = t  # not accounting for scr refresh
            text_fix.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_fix, 'tStartRefresh')  # time at next scr refresh
            text_fix.setAutoDraw(True)
        frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_fix.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            text_fix.tStop = t  # not accounting for scr refresh
            text_fix.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_fix, 'tStopRefresh')  # time at next scr refresh
            text_fix.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Fix_ScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Fix_Screen"-------
    for thisComponent in Fix_ScreenComponents:
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
    thisExp.nextEntry()
    
# completed 1 repeats of 'emotion_trials_p'

# get names of stimulus parameters
if emotion_trials_p.trialList in ([], [None], None):
    params = []
else:
    params = emotion_trials_p.trialList[0].keys()
# save data for this loop
emotion_trials_p.saveAsExcel(filename + '.xlsx', sheetName='emotion_trials_p',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
emotion_trials_p.saveAsText(filename + 'emotion_trials_p.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "Part_One_Meas_End"-------
t = 0
Part_One_Meas_EndClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
thisExp.addData("end_emotion_one", time.strftime("%Y-%m-%d_%H:%M:%S")) 
# keep track of which components have finished
Part_One_Meas_EndComponents = [text_part_one_meas_end]
for thisComponent in Part_One_Meas_EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Part_One_Meas_End"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Part_One_Meas_EndClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_part_one_meas_end* updates
    if t >= 0.0 and text_part_one_meas_end.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_part_one_meas_end.tStart = t  # not accounting for scr refresh
        text_part_one_meas_end.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_part_one_meas_end, 'tStartRefresh')  # time at next scr refresh
        text_part_one_meas_end.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_part_one_meas_end.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_part_one_meas_end.tStop = t  # not accounting for scr refresh
        text_part_one_meas_end.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_part_one_meas_end, 'tStopRefresh')  # time at next scr refresh
        text_part_one_meas_end.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Part_One_Meas_EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Part_One_Meas_End"-------
for thisComponent in Part_One_Meas_EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
emotion_evaluation_p = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('..\\Resources\\StimuliFiles\\picture_list_pos.xlsx'),
    seed=None, name='emotion_evaluation_p')
thisExp.addLoop(emotion_evaluation_p)  # add the loop to the experiment
thisEmotion_evaluation_p = emotion_evaluation_p.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEmotion_evaluation_p.rgb)
if thisEmotion_evaluation_p != None:
    for paramName in thisEmotion_evaluation_p:
        exec('{} = thisEmotion_evaluation_p[paramName]'.format(paramName))

for thisEmotion_evaluation_p in emotion_evaluation_p:
    currentLoop = emotion_evaluation_p
    # abbreviate parameter names if possible (e.g. rgb = thisEmotion_evaluation_p.rgb)
    if thisEmotion_evaluation_p != None:
        for paramName in thisEmotion_evaluation_p:
            exec('{} = thisEmotion_evaluation_p[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Emotion_Evaluation_P_O"-------
    t = 0
    Emotion_Evaluation_P_OClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    image_emotion_p_eval_o.setSize((p_new_width*0.3, p_new_height*0.3))
    image_emotion_p_eval_o.setImage(p_pictures)
    rating_emotion_p_eval_o.reset()
    # keep track of which components have finished
    Emotion_Evaluation_P_OComponents = [image_emotion_p_eval_o, text_emotion_p_eval_o, rating_emotion_p_eval_o]
    for thisComponent in Emotion_Evaluation_P_OComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Emotion_Evaluation_P_O"-------
    while continueRoutine:
        # get current time
        t = Emotion_Evaluation_P_OClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_emotion_p_eval_o* updates
        if t >= 0.0 and image_emotion_p_eval_o.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_emotion_p_eval_o.tStart = t  # not accounting for scr refresh
            image_emotion_p_eval_o.frameNStart = frameN  # exact frame index
            win.timeOnFlip(image_emotion_p_eval_o, 'tStartRefresh')  # time at next scr refresh
            image_emotion_p_eval_o.setAutoDraw(True)
        
        # *text_emotion_p_eval_o* updates
        if t >= 0.0 and text_emotion_p_eval_o.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_emotion_p_eval_o.tStart = t  # not accounting for scr refresh
            text_emotion_p_eval_o.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_emotion_p_eval_o, 'tStartRefresh')  # time at next scr refresh
            text_emotion_p_eval_o.setAutoDraw(True)
        # *rating_emotion_p_eval_o* updates
        if t >= 0.0 and rating_emotion_p_eval_o.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating_emotion_p_eval_o.tStart = t  # not accounting for scr refresh
            rating_emotion_p_eval_o.frameNStart = frameN  # exact frame index
            win.timeOnFlip(rating_emotion_p_eval_o, 'tStartRefresh')  # time at next scr refresh
            rating_emotion_p_eval_o.setAutoDraw(True)
        continueRoutine &= rating_emotion_p_eval_o.noResponse  # a response ends the trial
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Emotion_Evaluation_P_OComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Emotion_Evaluation_P_O"-------
    for thisComponent in Emotion_Evaluation_P_OComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for emotion_evaluation_p (TrialHandler)
    emotion_evaluation_p.addData('rating_emotion_p_eval_o.response', rating_emotion_p_eval_o.getRating())
    emotion_evaluation_p.addData('rating_emotion_p_eval_o.rt', rating_emotion_p_eval_o.getRT())
    # the Routine "Emotion_Evaluation_P_O" was not non-slip safe, so reset the non-slip timer
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
    
    # ------Prepare to start Routine "Emotion_Evaluation_P_T"-------
    t = 0
    Emotion_Evaluation_P_TClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    image_emotion_p_eval_t.setSize((p_new_width*0.3, p_new_height*0.3))
    image_emotion_p_eval_t.setImage(p_pictures)
    rating_emotion_p_eval_t.reset()
    # keep track of which components have finished
    Emotion_Evaluation_P_TComponents = [image_emotion_p_eval_t, text_emotion_p_eval_t, rating_emotion_p_eval_t]
    for thisComponent in Emotion_Evaluation_P_TComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Emotion_Evaluation_P_T"-------
    while continueRoutine:
        # get current time
        t = Emotion_Evaluation_P_TClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_emotion_p_eval_t* updates
        if t >= 0.0 and image_emotion_p_eval_t.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_emotion_p_eval_t.tStart = t  # not accounting for scr refresh
            image_emotion_p_eval_t.frameNStart = frameN  # exact frame index
            win.timeOnFlip(image_emotion_p_eval_t, 'tStartRefresh')  # time at next scr refresh
            image_emotion_p_eval_t.setAutoDraw(True)
        
        # *text_emotion_p_eval_t* updates
        if t >= 0.0 and text_emotion_p_eval_t.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_emotion_p_eval_t.tStart = t  # not accounting for scr refresh
            text_emotion_p_eval_t.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_emotion_p_eval_t, 'tStartRefresh')  # time at next scr refresh
            text_emotion_p_eval_t.setAutoDraw(True)
        # *rating_emotion_p_eval_t* updates
        if t >= 0.0 and rating_emotion_p_eval_t.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating_emotion_p_eval_t.tStart = t  # not accounting for scr refresh
            rating_emotion_p_eval_t.frameNStart = frameN  # exact frame index
            win.timeOnFlip(rating_emotion_p_eval_t, 'tStartRefresh')  # time at next scr refresh
            rating_emotion_p_eval_t.setAutoDraw(True)
        continueRoutine &= rating_emotion_p_eval_t.noResponse  # a response ends the trial
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Emotion_Evaluation_P_TComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Emotion_Evaluation_P_T"-------
    for thisComponent in Emotion_Evaluation_P_TComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for emotion_evaluation_p (TrialHandler)
    emotion_evaluation_p.addData('rating_emotion_p_eval_t.response', rating_emotion_p_eval_t.getRating())
    emotion_evaluation_p.addData('rating_emotion_p_eval_t.rt', rating_emotion_p_eval_t.getRT())
    # the Routine "Emotion_Evaluation_P_T" was not non-slip safe, so reset the non-slip timer
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
    
# completed 1 repeats of 'emotion_evaluation_p'

# get names of stimulus parameters
if emotion_evaluation_p.trialList in ([], [None], None):
    params = []
else:
    params = emotion_evaluation_p.trialList[0].keys()
# save data for this loop
emotion_evaluation_p.saveAsExcel(filename + '.xlsx', sheetName='emotion_evaluation_p',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
emotion_evaluation_p.saveAsText(filename + 'emotion_evaluation_p.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

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
        win.callOnFlip(key_resp_cooldown_instructions.clock.reset)  # t=0 on next screen flip
        key_resp_cooldown_instructions.clearEvents(eventType='keyboard')
    if key_resp_cooldown_instructions.status == STARTED:
        theseKeys = key_resp_cooldown_instructions.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_cooldown_instructions.keys = theseKeys.name  # just the last key pressed
            key_resp_cooldown_instructions.rt = theseKeys.rt
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
# check responses
if key_resp_cooldown_instructions.keys in ['', [], None]:  # No response was made
    key_resp_cooldown_instructions.keys = None
thisExp.addData('key_resp_cooldown_instructions.keys',key_resp_cooldown_instructions.keys)
if key_resp_cooldown_instructions.keys != None:  # we had a response
    thisExp.addData('key_resp_cooldown_instructions.rt', key_resp_cooldown_instructions.rt)
thisExp.nextEntry()
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
routineTimer.add(300.000000)
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
    frameRemains = 0.0 + 300- win.monitorFramePeriod * 0.75  # most of one frame period left
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

# ------Prepare to start Routine "Cooldown_Evaluation"-------
t = 0
Cooldown_EvaluationClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
rating_cooldown_evaluation.reset()
# keep track of which components have finished
Cooldown_EvaluationComponents = [text_cooldown_evaluation_title, text_cooldown_evaluation, rating_cooldown_evaluation]
for thisComponent in Cooldown_EvaluationComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Cooldown_Evaluation"-------
while continueRoutine:
    # get current time
    t = Cooldown_EvaluationClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_cooldown_evaluation_title* updates
    if t >= 0.0 and text_cooldown_evaluation_title.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_cooldown_evaluation_title.tStart = t  # not accounting for scr refresh
        text_cooldown_evaluation_title.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_cooldown_evaluation_title, 'tStartRefresh')  # time at next scr refresh
        text_cooldown_evaluation_title.setAutoDraw(True)
    
    # *text_cooldown_evaluation* updates
    if t >= 0.0 and text_cooldown_evaluation.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_cooldown_evaluation.tStart = t  # not accounting for scr refresh
        text_cooldown_evaluation.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_cooldown_evaluation, 'tStartRefresh')  # time at next scr refresh
        text_cooldown_evaluation.setAutoDraw(True)
    # *rating_cooldown_evaluation* updates
    if t >= 0.0 and rating_cooldown_evaluation.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating_cooldown_evaluation.tStart = t  # not accounting for scr refresh
        rating_cooldown_evaluation.frameNStart = frameN  # exact frame index
        win.timeOnFlip(rating_cooldown_evaluation, 'tStartRefresh')  # time at next scr refresh
        rating_cooldown_evaluation.setAutoDraw(True)
    continueRoutine &= rating_cooldown_evaluation.noResponse  # a response ends the trial
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Cooldown_EvaluationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Cooldown_Evaluation"-------
for thisComponent in Cooldown_EvaluationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('rating_cooldown_evaluation.response', rating_cooldown_evaluation.getRating())
thisExp.addData('rating_cooldown_evaluation.rt', rating_cooldown_evaluation.getRT())
thisExp.nextEntry()
# the Routine "Cooldown_Evaluation" was not non-slip safe, so reset the non-slip timer
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

# ------Prepare to start Routine "Cooldown_End"-------
t = 0
Cooldown_EndClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_cooldown_end = keyboard.Keyboard()
# keep track of which components have finished
Cooldown_EndComponents = [text_cooldown_end, text_cooldown_end_instructions, key_resp_cooldown_end]
for thisComponent in Cooldown_EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Cooldown_End"-------
while continueRoutine:
    # get current time
    t = Cooldown_EndClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_cooldown_end* updates
    if t >= 0.0 and text_cooldown_end.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_cooldown_end.tStart = t  # not accounting for scr refresh
        text_cooldown_end.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_cooldown_end, 'tStartRefresh')  # time at next scr refresh
        text_cooldown_end.setAutoDraw(True)
    
    # *text_cooldown_end_instructions* updates
    if t >= 0.0 and text_cooldown_end_instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_cooldown_end_instructions.tStart = t  # not accounting for scr refresh
        text_cooldown_end_instructions.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_cooldown_end_instructions, 'tStartRefresh')  # time at next scr refresh
        text_cooldown_end_instructions.setAutoDraw(True)
    
    # *key_resp_cooldown_end* updates
    if t >= 0.0 and key_resp_cooldown_end.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_cooldown_end.tStart = t  # not accounting for scr refresh
        key_resp_cooldown_end.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_cooldown_end, 'tStartRefresh')  # time at next scr refresh
        key_resp_cooldown_end.status = STARTED
        # keyboard checking is just starting
        key_resp_cooldown_end.clearEvents(eventType='keyboard')
    if key_resp_cooldown_end.status == STARTED:
        theseKeys = key_resp_cooldown_end.getKeys(keyList=['space'], waitRelease=False)
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
    for thisComponent in Cooldown_EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Cooldown_End"-------
for thisComponent in Cooldown_EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Cooldown_End" was not non-slip safe, so reset the non-slip timer
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

# ------Prepare to start Routine "Emotion_Instructions_Two"-------
t = 0
Emotion_Instructions_TwoClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_emotion_instructions_2 = keyboard.Keyboard()
# keep track of which components have finished
Emotion_Instructions_TwoComponents = [text_emotion_instruction_title_2, text_emotion_instructions_2, key_resp_emotion_instructions_2]
for thisComponent in Emotion_Instructions_TwoComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Emotion_Instructions_Two"-------
while continueRoutine:
    # get current time
    t = Emotion_Instructions_TwoClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_emotion_instruction_title_2* updates
    if t >= 0.0 and text_emotion_instruction_title_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_emotion_instruction_title_2.tStart = t  # not accounting for scr refresh
        text_emotion_instruction_title_2.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_emotion_instruction_title_2, 'tStartRefresh')  # time at next scr refresh
        text_emotion_instruction_title_2.setAutoDraw(True)
    
    # *text_emotion_instructions_2* updates
    if t >= 0.0 and text_emotion_instructions_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_emotion_instructions_2.tStart = t  # not accounting for scr refresh
        text_emotion_instructions_2.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_emotion_instructions_2, 'tStartRefresh')  # time at next scr refresh
        text_emotion_instructions_2.setAutoDraw(True)
    
    # *key_resp_emotion_instructions_2* updates
    if t >= 0.0 and key_resp_emotion_instructions_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_emotion_instructions_2.tStart = t  # not accounting for scr refresh
        key_resp_emotion_instructions_2.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_emotion_instructions_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_emotion_instructions_2.status = STARTED
        # keyboard checking is just starting
        key_resp_emotion_instructions_2.clearEvents(eventType='keyboard')
    if key_resp_emotion_instructions_2.status == STARTED:
        theseKeys = key_resp_emotion_instructions_2.getKeys(keyList=['space'], waitRelease=False)
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
    for thisComponent in Emotion_Instructions_TwoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Emotion_Instructions_Two"-------
for thisComponent in Emotion_Instructions_TwoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData("start_emotion_two", time.strftime("%Y-%m-%d_%H:%M:%S")) 
# the Routine "Emotion_Instructions_Two" was not non-slip safe, so reset the non-slip timer
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
emotion_trials_n = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('..\\Resources\\StimuliFiles\\picture_list_neg.xlsx'),
    seed=None, name='emotion_trials_n')
thisExp.addLoop(emotion_trials_n)  # add the loop to the experiment
thisEmotion_trials_n = emotion_trials_n.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEmotion_trials_n.rgb)
if thisEmotion_trials_n != None:
    for paramName in thisEmotion_trials_n:
        exec('{} = thisEmotion_trials_n[paramName]'.format(paramName))

for thisEmotion_trials_n in emotion_trials_n:
    currentLoop = emotion_trials_n
    # abbreviate parameter names if possible (e.g. rgb = thisEmotion_trials_n.rgb)
    if thisEmotion_trials_n != None:
        for paramName in thisEmotion_trials_n:
            exec('{} = thisEmotion_trials_n[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Emotion_Measurement_N"-------
    t = 0
    Emotion_Measurement_NClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(7.000000)
    # update component parameters for each repeat
    image_emotion_n.setSize((n_new_width, n_new_height))
    image_emotion_n.setImage(n_pictures)
    # keep track of which components have finished
    Emotion_Measurement_NComponents = [image_emotion_n]
    for thisComponent in Emotion_Measurement_NComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Emotion_Measurement_N"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Emotion_Measurement_NClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_emotion_n* updates
        if t >= 0.0 and image_emotion_n.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_emotion_n.tStart = t  # not accounting for scr refresh
            image_emotion_n.frameNStart = frameN  # exact frame index
            win.timeOnFlip(image_emotion_n, 'tStartRefresh')  # time at next scr refresh
            image_emotion_n.setAutoDraw(True)
        frameRemains = 0.0 + 7- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_emotion_n.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            image_emotion_n.tStop = t  # not accounting for scr refresh
            image_emotion_n.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_emotion_n, 'tStopRefresh')  # time at next scr refresh
            image_emotion_n.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Emotion_Measurement_NComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Emotion_Measurement_N"-------
    for thisComponent in Emotion_Measurement_NComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    emotion_trials_n.addData('image_emotion_n.started', image_emotion_n.tStartRefresh)
    emotion_trials_n.addData('image_emotion_n.stopped', image_emotion_n.tStopRefresh)
    
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
    
    # ------Prepare to start Routine "Fix_Screen"-------
    t = 0
    Fix_ScreenClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    Fix_ScreenComponents = [text_fix]
    for thisComponent in Fix_ScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Fix_Screen"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Fix_ScreenClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_fix* updates
        if t >= 0.0 and text_fix.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_fix.tStart = t  # not accounting for scr refresh
            text_fix.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_fix, 'tStartRefresh')  # time at next scr refresh
            text_fix.setAutoDraw(True)
        frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_fix.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            text_fix.tStop = t  # not accounting for scr refresh
            text_fix.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_fix, 'tStopRefresh')  # time at next scr refresh
            text_fix.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Fix_ScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Fix_Screen"-------
    for thisComponent in Fix_ScreenComponents:
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
    thisExp.nextEntry()
    
# completed 1 repeats of 'emotion_trials_n'

# get names of stimulus parameters
if emotion_trials_n.trialList in ([], [None], None):
    params = []
else:
    params = emotion_trials_n.trialList[0].keys()
# save data for this loop
emotion_trials_n.saveAsExcel(filename + '.xlsx', sheetName='emotion_trials_n',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
emotion_trials_n.saveAsText(filename + 'emotion_trials_n.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "Part_Two_Meas_End"-------
t = 0
Part_Two_Meas_EndClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
thisExp.addData("end_emotion_two", time.strftime("%Y-%m-%d_%H:%M:%S")) 
# keep track of which components have finished
Part_Two_Meas_EndComponents = [text_part_one_meas_end_2]
for thisComponent in Part_Two_Meas_EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Part_Two_Meas_End"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Part_Two_Meas_EndClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_part_one_meas_end_2* updates
    if t >= 0.0 and text_part_one_meas_end_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_part_one_meas_end_2.tStart = t  # not accounting for scr refresh
        text_part_one_meas_end_2.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_part_one_meas_end_2, 'tStartRefresh')  # time at next scr refresh
        text_part_one_meas_end_2.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_part_one_meas_end_2.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_part_one_meas_end_2.tStop = t  # not accounting for scr refresh
        text_part_one_meas_end_2.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_part_one_meas_end_2, 'tStopRefresh')  # time at next scr refresh
        text_part_one_meas_end_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Part_Two_Meas_EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Part_Two_Meas_End"-------
for thisComponent in Part_Two_Meas_EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
emotion_evaluation_n = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('..\\Resources\\StimuliFiles\\picture_list_neg.xlsx'),
    seed=None, name='emotion_evaluation_n')
thisExp.addLoop(emotion_evaluation_n)  # add the loop to the experiment
thisEmotion_evaluation_n = emotion_evaluation_n.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEmotion_evaluation_n.rgb)
if thisEmotion_evaluation_n != None:
    for paramName in thisEmotion_evaluation_n:
        exec('{} = thisEmotion_evaluation_n[paramName]'.format(paramName))

for thisEmotion_evaluation_n in emotion_evaluation_n:
    currentLoop = emotion_evaluation_n
    # abbreviate parameter names if possible (e.g. rgb = thisEmotion_evaluation_n.rgb)
    if thisEmotion_evaluation_n != None:
        for paramName in thisEmotion_evaluation_n:
            exec('{} = thisEmotion_evaluation_n[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Emotion_Evaluation_N_O"-------
    t = 0
    Emotion_Evaluation_N_OClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    image_emotion_n_eval_o.setSize((n_new_width*0.3, n_new_height*0.3))
    image_emotion_n_eval_o.setImage(n_pictures)
    rating_emotion_n_eval_o.reset()
    # keep track of which components have finished
    Emotion_Evaluation_N_OComponents = [image_emotion_n_eval_o, text_emotion_n_eval_o, rating_emotion_n_eval_o]
    for thisComponent in Emotion_Evaluation_N_OComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Emotion_Evaluation_N_O"-------
    while continueRoutine:
        # get current time
        t = Emotion_Evaluation_N_OClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_emotion_n_eval_o* updates
        if t >= 0.0 and image_emotion_n_eval_o.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_emotion_n_eval_o.tStart = t  # not accounting for scr refresh
            image_emotion_n_eval_o.frameNStart = frameN  # exact frame index
            win.timeOnFlip(image_emotion_n_eval_o, 'tStartRefresh')  # time at next scr refresh
            image_emotion_n_eval_o.setAutoDraw(True)
        
        # *text_emotion_n_eval_o* updates
        if t >= 0.0 and text_emotion_n_eval_o.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_emotion_n_eval_o.tStart = t  # not accounting for scr refresh
            text_emotion_n_eval_o.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_emotion_n_eval_o, 'tStartRefresh')  # time at next scr refresh
            text_emotion_n_eval_o.setAutoDraw(True)
        # *rating_emotion_n_eval_o* updates
        if t >= 0.0 and rating_emotion_n_eval_o.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating_emotion_n_eval_o.tStart = t  # not accounting for scr refresh
            rating_emotion_n_eval_o.frameNStart = frameN  # exact frame index
            win.timeOnFlip(rating_emotion_n_eval_o, 'tStartRefresh')  # time at next scr refresh
            rating_emotion_n_eval_o.setAutoDraw(True)
        continueRoutine &= rating_emotion_n_eval_o.noResponse  # a response ends the trial
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Emotion_Evaluation_N_OComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Emotion_Evaluation_N_O"-------
    for thisComponent in Emotion_Evaluation_N_OComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for emotion_evaluation_n (TrialHandler)
    emotion_evaluation_n.addData('rating_emotion_n_eval_o.response', rating_emotion_n_eval_o.getRating())
    emotion_evaluation_n.addData('rating_emotion_n_eval_o.rt', rating_emotion_n_eval_o.getRT())
    # the Routine "Emotion_Evaluation_N_O" was not non-slip safe, so reset the non-slip timer
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
    
    # ------Prepare to start Routine "Emotion_Evaluation_N_T"-------
    t = 0
    Emotion_Evaluation_N_TClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    image_emotion_n_eval_t.setSize((n_new_width*0.3, n_new_height*0.3))
    image_emotion_n_eval_t.setImage(n_pictures)
    rating_emotion_n_eval_t.reset()
    # keep track of which components have finished
    Emotion_Evaluation_N_TComponents = [image_emotion_n_eval_t, text_emotion_n_eval_t, rating_emotion_n_eval_t]
    for thisComponent in Emotion_Evaluation_N_TComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Emotion_Evaluation_N_T"-------
    while continueRoutine:
        # get current time
        t = Emotion_Evaluation_N_TClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_emotion_n_eval_t* updates
        if t >= 0.0 and image_emotion_n_eval_t.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_emotion_n_eval_t.tStart = t  # not accounting for scr refresh
            image_emotion_n_eval_t.frameNStart = frameN  # exact frame index
            win.timeOnFlip(image_emotion_n_eval_t, 'tStartRefresh')  # time at next scr refresh
            image_emotion_n_eval_t.setAutoDraw(True)
        
        # *text_emotion_n_eval_t* updates
        if t >= 0.0 and text_emotion_n_eval_t.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_emotion_n_eval_t.tStart = t  # not accounting for scr refresh
            text_emotion_n_eval_t.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_emotion_n_eval_t, 'tStartRefresh')  # time at next scr refresh
            text_emotion_n_eval_t.setAutoDraw(True)
        # *rating_emotion_n_eval_t* updates
        if t >= 0.0 and rating_emotion_n_eval_t.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating_emotion_n_eval_t.tStart = t  # not accounting for scr refresh
            rating_emotion_n_eval_t.frameNStart = frameN  # exact frame index
            win.timeOnFlip(rating_emotion_n_eval_t, 'tStartRefresh')  # time at next scr refresh
            rating_emotion_n_eval_t.setAutoDraw(True)
        continueRoutine &= rating_emotion_n_eval_t.noResponse  # a response ends the trial
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Emotion_Evaluation_N_TComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Emotion_Evaluation_N_T"-------
    for thisComponent in Emotion_Evaluation_N_TComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    emotion_evaluation_n.addData('text_emotion_n_eval_t.started', text_emotion_n_eval_t.tStartRefresh)
    emotion_evaluation_n.addData('text_emotion_n_eval_t.stopped', text_emotion_n_eval_t.tStopRefresh)
    # store data for emotion_evaluation_n (TrialHandler)
    emotion_evaluation_n.addData('rating_emotion_n_eval_t.response', rating_emotion_n_eval_t.getRating())
    emotion_evaluation_n.addData('rating_emotion_n_eval_t.rt', rating_emotion_n_eval_t.getRT())
    # the Routine "Emotion_Evaluation_N_T" was not non-slip safe, so reset the non-slip timer
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
    
# completed 1 repeats of 'emotion_evaluation_n'

# get names of stimulus parameters
if emotion_evaluation_n.trialList in ([], [None], None):
    params = []
else:
    params = emotion_evaluation_n.trialList[0].keys()
# save data for this loop
emotion_evaluation_n.saveAsExcel(filename + '.xlsx', sheetName='emotion_evaluation_n',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
emotion_evaluation_n.saveAsText(filename + 'emotion_evaluation_n.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

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
        win.callOnFlip(key_resp_cooldown_instructions.clock.reset)  # t=0 on next screen flip
        key_resp_cooldown_instructions.clearEvents(eventType='keyboard')
    if key_resp_cooldown_instructions.status == STARTED:
        theseKeys = key_resp_cooldown_instructions.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_cooldown_instructions.keys = theseKeys.name  # just the last key pressed
            key_resp_cooldown_instructions.rt = theseKeys.rt
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
# check responses
if key_resp_cooldown_instructions.keys in ['', [], None]:  # No response was made
    key_resp_cooldown_instructions.keys = None
thisExp.addData('key_resp_cooldown_instructions.keys',key_resp_cooldown_instructions.keys)
if key_resp_cooldown_instructions.keys != None:  # we had a response
    thisExp.addData('key_resp_cooldown_instructions.rt', key_resp_cooldown_instructions.rt)
thisExp.nextEntry()
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
routineTimer.add(300.000000)
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
    frameRemains = 0.0 + 300- win.monitorFramePeriod * 0.75  # most of one frame period left
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

# ------Prepare to start Routine "Cooldown_Evaluation"-------
t = 0
Cooldown_EvaluationClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
rating_cooldown_evaluation.reset()
# keep track of which components have finished
Cooldown_EvaluationComponents = [text_cooldown_evaluation_title, text_cooldown_evaluation, rating_cooldown_evaluation]
for thisComponent in Cooldown_EvaluationComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Cooldown_Evaluation"-------
while continueRoutine:
    # get current time
    t = Cooldown_EvaluationClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_cooldown_evaluation_title* updates
    if t >= 0.0 and text_cooldown_evaluation_title.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_cooldown_evaluation_title.tStart = t  # not accounting for scr refresh
        text_cooldown_evaluation_title.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_cooldown_evaluation_title, 'tStartRefresh')  # time at next scr refresh
        text_cooldown_evaluation_title.setAutoDraw(True)
    
    # *text_cooldown_evaluation* updates
    if t >= 0.0 and text_cooldown_evaluation.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_cooldown_evaluation.tStart = t  # not accounting for scr refresh
        text_cooldown_evaluation.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_cooldown_evaluation, 'tStartRefresh')  # time at next scr refresh
        text_cooldown_evaluation.setAutoDraw(True)
    # *rating_cooldown_evaluation* updates
    if t >= 0.0 and rating_cooldown_evaluation.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating_cooldown_evaluation.tStart = t  # not accounting for scr refresh
        rating_cooldown_evaluation.frameNStart = frameN  # exact frame index
        win.timeOnFlip(rating_cooldown_evaluation, 'tStartRefresh')  # time at next scr refresh
        rating_cooldown_evaluation.setAutoDraw(True)
    continueRoutine &= rating_cooldown_evaluation.noResponse  # a response ends the trial
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Cooldown_EvaluationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Cooldown_Evaluation"-------
for thisComponent in Cooldown_EvaluationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('rating_cooldown_evaluation.response', rating_cooldown_evaluation.getRating())
thisExp.addData('rating_cooldown_evaluation.rt', rating_cooldown_evaluation.getRT())
thisExp.nextEntry()
# the Routine "Cooldown_Evaluation" was not non-slip safe, so reset the non-slip timer
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

# ------Prepare to start Routine "Emotion_End"-------
t = 0
Emotion_EndClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(10.000000)
# update component parameters for each repeat
# keep track of which components have finished
Emotion_EndComponents = [text_ending_screen, text_ending_subtitle]
for thisComponent in Emotion_EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Emotion_End"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Emotion_EndClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_ending_screen* updates
    if t >= 0.0 and text_ending_screen.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_ending_screen.tStart = t  # not accounting for scr refresh
        text_ending_screen.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_ending_screen, 'tStartRefresh')  # time at next scr refresh
        text_ending_screen.setAutoDraw(True)
    frameRemains = 0.0 + 10- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_ending_screen.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_ending_screen.tStop = t  # not accounting for scr refresh
        text_ending_screen.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_ending_screen, 'tStopRefresh')  # time at next scr refresh
        text_ending_screen.setAutoDraw(False)
    
    # *text_ending_subtitle* updates
    if t >= 0.0 and text_ending_subtitle.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_ending_subtitle.tStart = t  # not accounting for scr refresh
        text_ending_subtitle.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_ending_subtitle, 'tStartRefresh')  # time at next scr refresh
        text_ending_subtitle.setAutoDraw(True)
    frameRemains = 0.0 + 10- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_ending_subtitle.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_ending_subtitle.tStop = t  # not accounting for scr refresh
        text_ending_subtitle.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_ending_subtitle, 'tStopRefresh')  # time at next scr refresh
        text_ending_subtitle.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Emotion_EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Emotion_End"-------
for thisComponent in Emotion_EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData("end_session_three", time.strftime("%Y-%m-%d_%H:%M:%S")) 

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
