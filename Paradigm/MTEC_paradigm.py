#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.3),
    on August 22, 2019, at 15:59
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
from datetime import datetime

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.1.3'
expName = 'MTEC_paradigm'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001', 'startTime': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['startTime'] = datetime.now().time()
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='E:\\GitHub\\MTEC\\Paradigm\\MTEC_paradigm.py',
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
    monitor='testMonitor', color=[0.85,0.85,0.85], colorSpace='rgb',
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

# Initialize components for Routine "Welcome_Screen"
Welcome_ScreenClock = core.Clock()
text_welcome_screen = visual.TextStim(win=win, name='text_welcome_screen',
    text='  Welcome \n     to the \nExperiment\n\n\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_instructions_welcome_screen = visual.TextStim(win=win, name='text_instructions_welcome_screen',
    text="(Press 'Space' to continue)",
    font='Arial',
    pos=(0, -0.2), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()

# Initialize components for Routine "Baseline_Screen"
Baseline_ScreenClock = core.Clock()
text_baseline_screen = visual.TextStim(win=win, name='text_baseline_screen',
    text='    Baseline \nMeasurement',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_baseline_screen_title = visual.TextStim(win=win, name='text_baseline_screen_title',
    text='Segment One:',
    font='Arial',
    pos=(0, 0.2), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()

# Initialize components for Routine "Baseline_Instructions"
Baseline_InstructionsClock = core.Clock()
text_baseline_instructions = visual.TextStim(win=win, name='text_baseline_instructions',
    text='Please try to relax.\n\nThe Measurement will\nstart shortly.',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_baseline_countdown = visual.TextStim(win=win, name='text_baseline_countdown',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_baseline_instructions_title = visual.TextStim(win=win, name='text_baseline_instructions_title',
    text='Instructions:',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()

# Initialize components for Routine "Baseline_Measurement"
Baseline_MeasurementClock = core.Clock()
text_baseline_measurement = visual.TextStim(win=win, name='text_baseline_measurement',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.4, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()

# Initialize components for Routine "Baseline_Evaluation"
Baseline_EvaluationClock = core.Clock()
rating_baseline = visual.RatingScale(win=win, name='rating_baseline', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=10, labels=['completely relaxed', ' stressed out'], scale='', markerStart='5')
text_baseline_evaluation_title = visual.TextStim(win=win, name='text_baseline_evaluation_title',
    text='Task finished:',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_baseline_evaluation = visual.TextStim(win=win, name='text_baseline_evaluation',
    text='Please enter your current\n        stress level.',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()

# Initialize components for Routine "Baseline_End"
Baseline_EndClock = core.Clock()
text_baseline_end = visual.TextStim(win=win, name='text_baseline_end',
    text='Ending Segment One.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_baseline_end_instructions = visual.TextStim(win=win, name='text_baseline_end_instructions',
    text="(Press 'Space' to continue)",
    font='Arial',
    pos=(0, -0.2), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()

# Initialize components for Routine "Stress_Screen"
Stress_ScreenClock = core.Clock()
text_stress_screen_title = visual.TextStim(win=win, name='text_stress_screen_title',
    text='Segment Two:',
    font='Arial',
    pos=(0, 0.2), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_stress_screen = visual.TextStim(win=win, name='text_stress_screen',
    text='Stress Measurement',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()

# Initialize components for Routine "Stress_Part_One"
Stress_Part_OneClock = core.Clock()
text_stress_part_one_title = visual.TextStim(win=win, name='text_stress_part_one_title',
    text='Part One:',
    font='Arial',
    pos=(0, 0.2), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_stress_part_one = visual.TextStim(win=win, name='text_stress_part_one',
    text='7-Row',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()

# Initialize components for Routine "Stress_Part_One_Instructions"
Stress_Part_One_InstructionsClock = core.Clock()
text_stress_part_one_instructions_title = visual.TextStim(win=win, name='text_stress_part_one_instructions_title',
    text='Instructions:',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_stress_part_one_instructions = visual.TextStim(win=win, name='text_stress_part_one_instructions',
    text="Count down aloud from 700 \nin steps of 7.\nTry to match the speed of the \nmetronome dot.\n\n(Press 'Space' to start)",
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()

# Initialize components for Routine "Stress_Part_One_Measurement"
Stress_Part_One_MeasurementClock = core.Clock()
metronome = visual.Polygon(
    win=win, name='metronome',
    edges=32, size=(0.2, 0.2),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "Metronom_Tic"
Metronom_TicClock = core.Clock()
text_metronom_tic = visual.TextStim(win=win, name='text_metronom_tic',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()

# Initialize components for Routine "Stress_Evaluation"
Stress_EvaluationClock = core.Clock()
text_part_one_evaluation = visual.TextStim(win=win, name='text_part_one_evaluation',
    text='Task finished:\n\n',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
rating_stress_part_one = visual.RatingScale(win=win, name='rating_stress_part_one', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=10, labels=['very easy', ' very hard'], scale='', markerStart='5')
text_part_one_evaluation_2 = visual.TextStim(win=win, name='text_part_one_evaluation_2',
    text='Please rate the difficulty \n       of the task.',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()

# Initialize components for Routine "Stress_Part_One_End"
Stress_Part_One_EndClock = core.Clock()
text_part_one_end = visual.TextStim(win=win, name='text_part_one_end',
    text='Ending Part One.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_par_one_end_instructions = visual.TextStim(win=win, name='text_par_one_end_instructions',
    text="(Press 'Space' to continue)",
    font='Arial',
    pos=(0, -0.2), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()

# Initialize components for Routine "Stress_Part_Two"
Stress_Part_TwoClock = core.Clock()
text_part_two_title = visual.TextStim(win=win, name='text_part_two_title',
    text='Part Two:',
    font='Arial',
    pos=(0, 0.2), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_part_two = visual.TextStim(win=win, name='text_part_two',
    text='Stroop Test',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()

# Initialize components for Routine "Stress_Part_Two_Instructions"
Stress_Part_Two_InstructionsClock = core.Clock()
text_part_two_instructions_title = visual.TextStim(win=win, name='text_part_two_instructions_title',
    text='Instructions:',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_part_two_instructions = visual.TextStim(win=win, name='text_part_two_instructions',
    text="Choose the color of the word by using the arrow keys.\n\n(Press 'Space' to start)",
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()

# Initialize components for Routine "Stress_Part_Two_Measurement"
Stress_Part_Two_MeasurementClock = core.Clock()
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
    pos=(-0.6, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_right_ans = visual.TextStim(win=win, name='text_right_ans',
    text='default text',
    font='Arial',
    pos=(0.6, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()

# Initialize components for Routine "Stress_Evaluation_2"
Stress_Evaluation_2Clock = core.Clock()
text_part_two_evaluation = visual.TextStim(win=win, name='text_part_two_evaluation',
    text='Task finished:',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_part_two_evaluation_2 = visual.TextStim(win=win, name='text_part_two_evaluation_2',
    text='Please rate the difficulty \n       of the task.',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
rating_stress_part_two = visual.RatingScale(win=win, name='rating_stress_part_two', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=10, labels=['very easy', ' very hard'], scale='', markerStart='5')

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()

# Initialize components for Routine "Stress_Part_Two_End"
Stress_Part_Two_EndClock = core.Clock()
text_stress_part_two_end = visual.TextStim(win=win, name='text_stress_part_two_end',
    text='Ending part two.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_stress_part_two_end_instructions = visual.TextStim(win=win, name='text_stress_part_two_end_instructions',
    text="(Press 'Space' to continue)",
    font='Arial',
    pos=(0, -0.2), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()

# Initialize components for Routine "Cooldown_Screen"
Cooldown_ScreenClock = core.Clock()
text_cooldown_title = visual.TextStim(win=win, name='text_cooldown_title',
    text='Intermission:',
    font='Arial',
    pos=(0, 0.2), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_cooldown = visual.TextStim(win=win, name='text_cooldown',
    text='Cooldown Phase',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()

# Initialize components for Routine "Cooldown_Instructions"
Cooldown_InstructionsClock = core.Clock()
text_cooldown_instructions = visual.TextStim(win=win, name='text_cooldown_instructions',
    text='Please try to relax.\n\nThe Measurement will\nstart shortly.',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_cooldown_countdown = visual.TextStim(win=win, name='text_cooldown_countdown',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_cooldown_instructions_title = visual.TextStim(win=win, name='text_cooldown_instructions_title',
    text='Instructions:',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()

# Initialize components for Routine "Cooldown_Measurement"
Cooldown_MeasurementClock = core.Clock()
text_cooldown_measurement = visual.TextStim(win=win, name='text_cooldown_measurement',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.4, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()

# Initialize components for Routine "Cooldown_Evaluation"
Cooldown_EvaluationClock = core.Clock()
rating_cooldown = visual.RatingScale(win=win, name='rating_cooldown', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=10, labels=['completely relaxed', ' stressed out'], scale='', markerStart='5')
text_cooldown_evaluation_title = visual.TextStim(win=win, name='text_cooldown_evaluation_title',
    text='Task finished:',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_cooldown_evaluation = visual.TextStim(win=win, name='text_cooldown_evaluation',
    text='Please enter your current\n        stress level.',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()

# Initialize components for Routine "Cooldown_End"
Cooldown_EndClock = core.Clock()
text_cooldown_end = visual.TextStim(win=win, name='text_cooldown_end',
    text='Ending Intermission.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_cooldown_end_instructions = visual.TextStim(win=win, name='text_cooldown_end_instructions',
    text="(Press 'Space' to continue)",
    font='Arial',
    pos=(0, -0.2), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()

# Initialize components for Routine "Emotion_Screen"
Emotion_ScreenClock = core.Clock()
text_emotion_screen_title = visual.TextStim(win=win, name='text_emotion_screen_title',
    text='Segment Three:',
    font='Arial',
    pos=(0, 0.2), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_emotion_screen = visual.TextStim(win=win, name='text_emotion_screen',
    text='Visual Stimulation Test',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()

# Initialize components for Routine "Emotion_Screen_Pos"
Emotion_Screen_PosClock = core.Clock()
text_emotion_screen_pos_title = visual.TextStim(win=win, name='text_emotion_screen_pos_title',
    text='Part One:',
    font='Arial',
    pos=(0, 0.2), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_emotion_pos_screen = visual.TextStim(win=win, name='text_emotion_pos_screen',
    text='Positive',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()

# Initialize components for Routine "Emotion_Instructions_Pos"
Emotion_Instructions_PosClock = core.Clock()
text_emotion_instruction_pos_title = visual.TextStim(win=win, name='text_emotion_instruction_pos_title',
    text='Instructions:',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_emotion_instructions_pos = visual.TextStim(win=win, name='text_emotion_instructions_pos',
    text="Please focus on the following\npictures.\n\nYou will have to rate each picture\nafter it has been presented.\n\n(Press 'Space' to start)",
    font='Arial',
    pos=(0, -0.2), height=0.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()

# Initialize components for Routine "Emotion_Measurement_Pos"
Emotion_Measurement_PosClock = core.Clock()
image_emotion_meas_pos = visual.ImageStim(
    win=win,
    name='image_emotion_meas_pos', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()

# Initialize components for Routine "Emotion_Evaluation_Pos"
Emotion_Evaluation_PosClock = core.Clock()
image_emotion_evaluation_pos = visual.ImageStim(
    win=win,
    name='image_emotion_evaluation_pos', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.2), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
rating_emotion_evaluation_pos = visual.RatingScale(win=win, name='rating_emotion_evaluation_pos', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=4, labels=['negative', 'positive'], scale='', markerStart='2')

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()

# Initialize components for Routine "Cooldown_Screen"
Cooldown_ScreenClock = core.Clock()
text_cooldown_title = visual.TextStim(win=win, name='text_cooldown_title',
    text='Intermission:',
    font='Arial',
    pos=(0, 0.2), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_cooldown = visual.TextStim(win=win, name='text_cooldown',
    text='Cooldown Phase',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()

# Initialize components for Routine "Cooldown_Instructions"
Cooldown_InstructionsClock = core.Clock()
text_cooldown_instructions = visual.TextStim(win=win, name='text_cooldown_instructions',
    text='Please try to relax.\n\nThe Measurement will\nstart shortly.',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_cooldown_countdown = visual.TextStim(win=win, name='text_cooldown_countdown',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_cooldown_instructions_title = visual.TextStim(win=win, name='text_cooldown_instructions_title',
    text='Instructions:',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()

# Initialize components for Routine "Cooldown_Evaluation"
Cooldown_EvaluationClock = core.Clock()
rating_cooldown = visual.RatingScale(win=win, name='rating_cooldown', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=10, labels=['completely relaxed', ' stressed out'], scale='', markerStart='5')
text_cooldown_evaluation_title = visual.TextStim(win=win, name='text_cooldown_evaluation_title',
    text='Task finished:',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_cooldown_evaluation = visual.TextStim(win=win, name='text_cooldown_evaluation',
    text='Please enter your current\n        stress level.',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()

# Initialize components for Routine "Cooldown_End"
Cooldown_EndClock = core.Clock()
text_cooldown_end = visual.TextStim(win=win, name='text_cooldown_end',
    text='Ending Intermission.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_cooldown_end_instructions = visual.TextStim(win=win, name='text_cooldown_end_instructions',
    text="(Press 'Space' to continue)",
    font='Arial',
    pos=(0, -0.2), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()

# Initialize components for Routine "Emotion_Screen_Neg"
Emotion_Screen_NegClock = core.Clock()
text_emotion_screen_neg_title = visual.TextStim(win=win, name='text_emotion_screen_neg_title',
    text='Part Two:',
    font='Arial',
    pos=(0, 0.2), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_emotion_neg_screen = visual.TextStim(win=win, name='text_emotion_neg_screen',
    text='Negative',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()

# Initialize components for Routine "Emotion_Instructions_Neg"
Emotion_Instructions_NegClock = core.Clock()
text_emotion_instruction_neg_title = visual.TextStim(win=win, name='text_emotion_instruction_neg_title',
    text='Instructions:',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_emotion_instructions_neg = visual.TextStim(win=win, name='text_emotion_instructions_neg',
    text="Please focus on the following\npictures.\n\nYou will have to rate each picture\nafter it has been presented.\n\n(Press 'Space' to start)",
    font='Arial',
    pos=(0, -0.2), height=0.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()

# Initialize components for Routine "Emotion_Measurement_Neg"
Emotion_Measurement_NegClock = core.Clock()
image_emotion_meas_neg = visual.ImageStim(
    win=win,
    name='image_emotion_meas_neg', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()

# Initialize components for Routine "Emotion_Evaluation_Neg"
Emotion_Evaluation_NegClock = core.Clock()
image_emotion_evaluation_neg = visual.ImageStim(
    win=win,
    name='image_emotion_evaluation_neg', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.2), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
rating_emotion_evaluation_neg = visual.RatingScale(win=win, name='rating_emotion_evaluation_neg', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=4, labels=['negative', 'positive'], scale='', markerStart='2')

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()

# Initialize components for Routine "Cooldown_Screen"
Cooldown_ScreenClock = core.Clock()
text_cooldown_title = visual.TextStim(win=win, name='text_cooldown_title',
    text='Intermission:',
    font='Arial',
    pos=(0, 0.2), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_cooldown = visual.TextStim(win=win, name='text_cooldown',
    text='Cooldown Phase',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()

# Initialize components for Routine "Cooldown_Instructions"
Cooldown_InstructionsClock = core.Clock()
text_cooldown_instructions = visual.TextStim(win=win, name='text_cooldown_instructions',
    text='Please try to relax.\n\nThe Measurement will\nstart shortly.',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_cooldown_countdown = visual.TextStim(win=win, name='text_cooldown_countdown',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_cooldown_instructions_title = visual.TextStim(win=win, name='text_cooldown_instructions_title',
    text='Instructions:',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()

# Initialize components for Routine "Cooldown_Measurement"
Cooldown_MeasurementClock = core.Clock()
text_cooldown_measurement = visual.TextStim(win=win, name='text_cooldown_measurement',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.4, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()

# Initialize components for Routine "Cooldown_Evaluation"
Cooldown_EvaluationClock = core.Clock()
rating_cooldown = visual.RatingScale(win=win, name='rating_cooldown', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=10, labels=['completely relaxed', ' stressed out'], scale='', markerStart='5')
text_cooldown_evaluation_title = visual.TextStim(win=win, name='text_cooldown_evaluation_title',
    text='Task finished:',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_cooldown_evaluation = visual.TextStim(win=win, name='text_cooldown_evaluation',
    text='Please enter your current\n        stress level.',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()

# Initialize components for Routine "Cooldown_End"
Cooldown_EndClock = core.Clock()
text_cooldown_end = visual.TextStim(win=win, name='text_cooldown_end',
    text='Ending Intermission.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_cooldown_end_instructions = visual.TextStim(win=win, name='text_cooldown_end_instructions',
    text="(Press 'Space' to continue)",
    font='Arial',
    pos=(0, -0.2), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()

# Initialize components for Routine "Ending_Screen"
Ending_ScreenClock = core.Clock()
text_ending_screen = visual.TextStim(win=win, name='text_ending_screen',
    text='The End\n\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_ending_subtitle = visual.TextStim(win=win, name='text_ending_subtitle',
    text='Thank you for participating!',
    font='Arial',
    pos=(0, -0.2), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Welcome_Screen"-------
t = 0
Welcome_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_welcome_screen = keyboard.Keyboard()
# keep track of which components have finished
Welcome_ScreenComponents = [text_welcome_screen, key_resp_welcome_screen, text_instructions_welcome_screen]
for thisComponent in Welcome_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Welcome_Screen"-------
while continueRoutine:
    # get current time
    t = Welcome_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_welcome_screen* updates
    if t >= 0.0 and text_welcome_screen.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_welcome_screen.tStart = t  # not accounting for scr refresh
        text_welcome_screen.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_welcome_screen, 'tStartRefresh')  # time at next scr refresh
        text_welcome_screen.setAutoDraw(True)
    
    # *key_resp_welcome_screen* updates
    if t >= 0.0 and key_resp_welcome_screen.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_welcome_screen.tStart = t  # not accounting for scr refresh
        key_resp_welcome_screen.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_welcome_screen, 'tStartRefresh')  # time at next scr refresh
        key_resp_welcome_screen.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_welcome_screen.clock.reset)  # t=0 on next screen flip
        key_resp_welcome_screen.clearEvents(eventType='keyboard')
    if key_resp_welcome_screen.status == STARTED:
        theseKeys = key_resp_welcome_screen.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_welcome_screen.keys = theseKeys.name  # just the last key pressed
            key_resp_welcome_screen.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_instructions_welcome_screen* updates
    if t >= 0.0 and text_instructions_welcome_screen.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_instructions_welcome_screen.tStart = t  # not accounting for scr refresh
        text_instructions_welcome_screen.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_instructions_welcome_screen, 'tStartRefresh')  # time at next scr refresh
        text_instructions_welcome_screen.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Welcome_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Welcome_Screen"-------
for thisComponent in Welcome_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_welcome_screen.started', text_welcome_screen.tStartRefresh)
thisExp.addData('text_welcome_screen.stopped', text_welcome_screen.tStopRefresh)
# check responses
if key_resp_welcome_screen.keys in ['', [], None]:  # No response was made
    key_resp_welcome_screen.keys = None
thisExp.addData('key_resp_welcome_screen.keys',key_resp_welcome_screen.keys)
if key_resp_welcome_screen.keys != None:  # we had a response
    thisExp.addData('key_resp_welcome_screen.rt', key_resp_welcome_screen.rt)
thisExp.addData('key_resp_welcome_screen.started', key_resp_welcome_screen.tStartRefresh)
thisExp.addData('key_resp_welcome_screen.stopped', key_resp_welcome_screen.tStopRefresh)
thisExp.nextEntry()
# the Routine "Welcome_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = []
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
# the Routine "Blank_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Baseline_Screen"-------
t = 0
Baseline_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
Baseline_ScreenComponents = [text_baseline_screen, text_baseline_screen_title]
for thisComponent in Baseline_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Baseline_Screen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Baseline_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_baseline_screen* updates
    if t >= 0.0 and text_baseline_screen.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_baseline_screen.tStart = t  # not accounting for scr refresh
        text_baseline_screen.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_baseline_screen, 'tStartRefresh')  # time at next scr refresh
        text_baseline_screen.setAutoDraw(True)
    frameRemains = 0.0 + 5.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_baseline_screen.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_baseline_screen.tStop = t  # not accounting for scr refresh
        text_baseline_screen.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_baseline_screen, 'tStopRefresh')  # time at next scr refresh
        text_baseline_screen.setAutoDraw(False)
    
    # *text_baseline_screen_title* updates
    if t >= 0.0 and text_baseline_screen_title.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_baseline_screen_title.tStart = t  # not accounting for scr refresh
        text_baseline_screen_title.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_baseline_screen_title, 'tStartRefresh')  # time at next scr refresh
        text_baseline_screen_title.setAutoDraw(True)
    frameRemains = 0.0 + 5.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_baseline_screen_title.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_baseline_screen_title.tStop = t  # not accounting for scr refresh
        text_baseline_screen_title.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_baseline_screen_title, 'tStopRefresh')  # time at next scr refresh
        text_baseline_screen_title.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Baseline_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Baseline_Screen"-------
for thisComponent in Baseline_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_baseline_screen.started', text_baseline_screen.tStartRefresh)
thisExp.addData('text_baseline_screen.stopped', text_baseline_screen.tStopRefresh)

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = []
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
# the Routine "Blank_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Baseline_Instructions"-------
t = 0
Baseline_InstructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(15.500000)
# update component parameters for each repeat
# keep track of which components have finished
Baseline_InstructionsComponents = [text_baseline_instructions, text_baseline_countdown, text_baseline_instructions_title]
for thisComponent in Baseline_InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Baseline_Instructions"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Baseline_InstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_baseline_instructions* updates
    if t >= 0.0 and text_baseline_instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_baseline_instructions.tStart = t  # not accounting for scr refresh
        text_baseline_instructions.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_baseline_instructions, 'tStartRefresh')  # time at next scr refresh
        text_baseline_instructions.setAutoDraw(True)
    frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_baseline_instructions.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_baseline_instructions.tStop = t  # not accounting for scr refresh
        text_baseline_instructions.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_baseline_instructions, 'tStopRefresh')  # time at next scr refresh
        text_baseline_instructions.setAutoDraw(False)
    
    # *text_baseline_countdown* updates
    if t >= 5.5 and text_baseline_countdown.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_baseline_countdown.tStart = t  # not accounting for scr refresh
        text_baseline_countdown.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_baseline_countdown, 'tStartRefresh')  # time at next scr refresh
        text_baseline_countdown.setAutoDraw(True)
    frameRemains = 5.5 + 10- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_baseline_countdown.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_baseline_countdown.tStop = t  # not accounting for scr refresh
        text_baseline_countdown.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_baseline_countdown, 'tStopRefresh')  # time at next scr refresh
        text_baseline_countdown.setAutoDraw(False)
    if text_baseline_countdown.status == STARTED:  # only update if drawing
        text_baseline_countdown.setText(str(round(routineTimer.getTime(),0)) , log=False)
    
    # *text_baseline_instructions_title* updates
    if t >= 0.0 and text_baseline_instructions_title.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_baseline_instructions_title.tStart = t  # not accounting for scr refresh
        text_baseline_instructions_title.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_baseline_instructions_title, 'tStartRefresh')  # time at next scr refresh
        text_baseline_instructions_title.setAutoDraw(True)
    frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_baseline_instructions_title.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_baseline_instructions_title.tStop = t  # not accounting for scr refresh
        text_baseline_instructions_title.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_baseline_instructions_title, 'tStopRefresh')  # time at next scr refresh
        text_baseline_instructions_title.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Baseline_InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Baseline_Instructions"-------
for thisComponent in Baseline_InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = []
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
# the Routine "Blank_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Baseline_Measurement"-------
t = 0
Baseline_MeasurementClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
Baseline_MeasurementComponents = [text_baseline_measurement]
for thisComponent in Baseline_MeasurementComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Baseline_Measurement"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Baseline_MeasurementClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_baseline_measurement* updates
    if t >= 0.0 and text_baseline_measurement.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_baseline_measurement.tStart = t  # not accounting for scr refresh
        text_baseline_measurement.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_baseline_measurement, 'tStartRefresh')  # time at next scr refresh
        text_baseline_measurement.setAutoDraw(True)
    frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_baseline_measurement.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_baseline_measurement.tStop = t  # not accounting for scr refresh
        text_baseline_measurement.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_baseline_measurement, 'tStopRefresh')  # time at next scr refresh
        text_baseline_measurement.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Baseline_MeasurementComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Baseline_Measurement"-------
for thisComponent in Baseline_MeasurementComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_baseline_measurement.started', text_baseline_measurement.tStartRefresh)
thisExp.addData('text_baseline_measurement.stopped', text_baseline_measurement.tStopRefresh)

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = []
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
# the Routine "Blank_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Baseline_Evaluation"-------
t = 0
Baseline_EvaluationClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
rating_baseline.reset()
# keep track of which components have finished
Baseline_EvaluationComponents = [rating_baseline, text_baseline_evaluation_title, text_baseline_evaluation]
for thisComponent in Baseline_EvaluationComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Baseline_Evaluation"-------
while continueRoutine:
    # get current time
    t = Baseline_EvaluationClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *rating_baseline* updates
    if t >= 0.0 and rating_baseline.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating_baseline.tStart = t  # not accounting for scr refresh
        rating_baseline.frameNStart = frameN  # exact frame index
        win.timeOnFlip(rating_baseline, 'tStartRefresh')  # time at next scr refresh
        rating_baseline.setAutoDraw(True)
    continueRoutine &= rating_baseline.noResponse  # a response ends the trial
    
    # *text_baseline_evaluation_title* updates
    if t >= 0.0 and text_baseline_evaluation_title.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_baseline_evaluation_title.tStart = t  # not accounting for scr refresh
        text_baseline_evaluation_title.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_baseline_evaluation_title, 'tStartRefresh')  # time at next scr refresh
        text_baseline_evaluation_title.setAutoDraw(True)
    
    # *text_baseline_evaluation* updates
    if t >= 0.0 and text_baseline_evaluation.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_baseline_evaluation.tStart = t  # not accounting for scr refresh
        text_baseline_evaluation.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_baseline_evaluation, 'tStartRefresh')  # time at next scr refresh
        text_baseline_evaluation.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Baseline_EvaluationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Baseline_Evaluation"-------
for thisComponent in Baseline_EvaluationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('rating_baseline.response', rating_baseline.getRating())
thisExp.addData('rating_baseline.rt', rating_baseline.getRT())
thisExp.nextEntry()
# the Routine "Baseline_Evaluation" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = []
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
# the Routine "Blank_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Baseline_End"-------
t = 0
Baseline_EndClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_baseline_end = keyboard.Keyboard()
# keep track of which components have finished
Baseline_EndComponents = [text_baseline_end, text_baseline_end_instructions, key_resp_baseline_end]
for thisComponent in Baseline_EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Baseline_End"-------
while continueRoutine:
    # get current time
    t = Baseline_EndClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_baseline_end* updates
    if t >= 0.0 and text_baseline_end.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_baseline_end.tStart = t  # not accounting for scr refresh
        text_baseline_end.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_baseline_end, 'tStartRefresh')  # time at next scr refresh
        text_baseline_end.setAutoDraw(True)
    
    # *text_baseline_end_instructions* updates
    if t >= 0.0 and text_baseline_end_instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_baseline_end_instructions.tStart = t  # not accounting for scr refresh
        text_baseline_end_instructions.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_baseline_end_instructions, 'tStartRefresh')  # time at next scr refresh
        text_baseline_end_instructions.setAutoDraw(True)
    
    # *key_resp_baseline_end* updates
    if t >= 0.0 and key_resp_baseline_end.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_baseline_end.tStart = t  # not accounting for scr refresh
        key_resp_baseline_end.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_baseline_end, 'tStartRefresh')  # time at next scr refresh
        key_resp_baseline_end.status = STARTED
        # keyboard checking is just starting
        key_resp_baseline_end.clearEvents(eventType='keyboard')
    if key_resp_baseline_end.status == STARTED:
        theseKeys = key_resp_baseline_end.getKeys(keyList=['space'], waitRelease=False)
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
    for thisComponent in Baseline_EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Baseline_End"-------
for thisComponent in Baseline_EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Baseline_End" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = []
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
# the Routine "Blank_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
    frameRemains = 0.0 + 5.0- win.monitorFramePeriod * 0.75  # most of one frame period left
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
    frameRemains = 0.0 + 5.0- win.monitorFramePeriod * 0.75  # most of one frame period left
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
thisExp.addData('text_stress_screen.started', text_stress_screen.tStartRefresh)
thisExp.addData('text_stress_screen.stopped', text_stress_screen.tStopRefresh)

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = []
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
# the Routine "Blank_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Stress_Part_One"-------
t = 0
Stress_Part_OneClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
Stress_Part_OneComponents = [text_stress_part_one_title, text_stress_part_one]
for thisComponent in Stress_Part_OneComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Stress_Part_One"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Stress_Part_OneClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_stress_part_one_title* updates
    if t >= 0.0 and text_stress_part_one_title.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_stress_part_one_title.tStart = t  # not accounting for scr refresh
        text_stress_part_one_title.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_stress_part_one_title, 'tStartRefresh')  # time at next scr refresh
        text_stress_part_one_title.setAutoDraw(True)
    frameRemains = 0.0 + 5.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_stress_part_one_title.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_stress_part_one_title.tStop = t  # not accounting for scr refresh
        text_stress_part_one_title.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_stress_part_one_title, 'tStopRefresh')  # time at next scr refresh
        text_stress_part_one_title.setAutoDraw(False)
    
    # *text_stress_part_one* updates
    if t >= 0.0 and text_stress_part_one.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_stress_part_one.tStart = t  # not accounting for scr refresh
        text_stress_part_one.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_stress_part_one, 'tStartRefresh')  # time at next scr refresh
        text_stress_part_one.setAutoDraw(True)
    frameRemains = 0.0 + 5.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_stress_part_one.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_stress_part_one.tStop = t  # not accounting for scr refresh
        text_stress_part_one.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_stress_part_one, 'tStopRefresh')  # time at next scr refresh
        text_stress_part_one.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Stress_Part_OneComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Stress_Part_One"-------
for thisComponent in Stress_Part_OneComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = []
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
# the Routine "Blank_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Stress_Part_One_Instructions"-------
t = 0
Stress_Part_One_InstructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_text_stress_part_one_instructions = keyboard.Keyboard()
# keep track of which components have finished
Stress_Part_One_InstructionsComponents = [text_stress_part_one_instructions_title, text_stress_part_one_instructions, key_resp_text_stress_part_one_instructions]
for thisComponent in Stress_Part_One_InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Stress_Part_One_Instructions"-------
while continueRoutine:
    # get current time
    t = Stress_Part_One_InstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_stress_part_one_instructions_title* updates
    if t >= 0.0 and text_stress_part_one_instructions_title.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_stress_part_one_instructions_title.tStart = t  # not accounting for scr refresh
        text_stress_part_one_instructions_title.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_stress_part_one_instructions_title, 'tStartRefresh')  # time at next scr refresh
        text_stress_part_one_instructions_title.setAutoDraw(True)
    
    # *text_stress_part_one_instructions* updates
    if t >= 0.0 and text_stress_part_one_instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_stress_part_one_instructions.tStart = t  # not accounting for scr refresh
        text_stress_part_one_instructions.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_stress_part_one_instructions, 'tStartRefresh')  # time at next scr refresh
        text_stress_part_one_instructions.setAutoDraw(True)
    
    # *key_resp_text_stress_part_one_instructions* updates
    if t >= 0.0 and key_resp_text_stress_part_one_instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_text_stress_part_one_instructions.tStart = t  # not accounting for scr refresh
        key_resp_text_stress_part_one_instructions.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_text_stress_part_one_instructions, 'tStartRefresh')  # time at next scr refresh
        key_resp_text_stress_part_one_instructions.status = STARTED
        # keyboard checking is just starting
        key_resp_text_stress_part_one_instructions.clearEvents(eventType='keyboard')
    if key_resp_text_stress_part_one_instructions.status == STARTED:
        theseKeys = key_resp_text_stress_part_one_instructions.getKeys(keyList=['space'], waitRelease=False)
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
    for thisComponent in Stress_Part_One_InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Stress_Part_One_Instructions"-------
for thisComponent in Stress_Part_One_InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Stress_Part_One_Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = []
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
# the Routine "Blank_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
tick = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimuli files\\metronome.xlsx', selection='1:10'),
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
    
    # ------Prepare to start Routine "Stress_Part_One_Measurement"-------
    t = 0
    Stress_Part_One_MeasurementClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    metronome.setFillColor(Color)
    # keep track of which components have finished
    Stress_Part_One_MeasurementComponents = [metronome]
    for thisComponent in Stress_Part_One_MeasurementComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Stress_Part_One_Measurement"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Stress_Part_One_MeasurementClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *metronome* updates
        if t >= 0.0 and metronome.status == NOT_STARTED:
            # keep track of start time/frame for later
            metronome.tStart = t  # not accounting for scr refresh
            metronome.frameNStart = frameN  # exact frame index
            win.timeOnFlip(metronome, 'tStartRefresh')  # time at next scr refresh
            metronome.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if metronome.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            metronome.tStop = t  # not accounting for scr refresh
            metronome.frameNStop = frameN  # exact frame index
            win.timeOnFlip(metronome, 'tStopRefresh')  # time at next scr refresh
            metronome.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Stress_Part_One_MeasurementComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Stress_Part_One_Measurement"-------
    for thisComponent in Stress_Part_One_MeasurementComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "Metronom_Tic"-------
    t = 0
    Metronom_TicClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    Metronom_TicComponents = [text_metronom_tic]
    for thisComponent in Metronom_TicComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Metronom_Tic"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Metronom_TicClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_metronom_tic* updates
        if t >= 0.0 and text_metronom_tic.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_metronom_tic.tStart = t  # not accounting for scr refresh
            text_metronom_tic.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_metronom_tic, 'tStartRefresh')  # time at next scr refresh
            text_metronom_tic.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_metronom_tic.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            text_metronom_tic.tStop = t  # not accounting for scr refresh
            text_metronom_tic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_metronom_tic, 'tStopRefresh')  # time at next scr refresh
            text_metronom_tic.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Metronom_TicComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Metronom_Tic"-------
    for thisComponent in Metronom_TicComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
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

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = []
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
# the Routine "Blank_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Stress_Evaluation"-------
t = 0
Stress_EvaluationClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
rating_stress_part_one.reset()
# keep track of which components have finished
Stress_EvaluationComponents = [text_part_one_evaluation, rating_stress_part_one, text_part_one_evaluation_2]
for thisComponent in Stress_EvaluationComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Stress_Evaluation"-------
while continueRoutine:
    # get current time
    t = Stress_EvaluationClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_part_one_evaluation* updates
    if t >= 0.0 and text_part_one_evaluation.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_part_one_evaluation.tStart = t  # not accounting for scr refresh
        text_part_one_evaluation.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_part_one_evaluation, 'tStartRefresh')  # time at next scr refresh
        text_part_one_evaluation.setAutoDraw(True)
    # *rating_stress_part_one* updates
    if t >= 0.0 and rating_stress_part_one.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating_stress_part_one.tStart = t  # not accounting for scr refresh
        rating_stress_part_one.frameNStart = frameN  # exact frame index
        win.timeOnFlip(rating_stress_part_one, 'tStartRefresh')  # time at next scr refresh
        rating_stress_part_one.setAutoDraw(True)
    continueRoutine &= rating_stress_part_one.noResponse  # a response ends the trial
    
    # *text_part_one_evaluation_2* updates
    if t >= 0.0 and text_part_one_evaluation_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_part_one_evaluation_2.tStart = t  # not accounting for scr refresh
        text_part_one_evaluation_2.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_part_one_evaluation_2, 'tStartRefresh')  # time at next scr refresh
        text_part_one_evaluation_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Stress_EvaluationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Stress_Evaluation"-------
for thisComponent in Stress_EvaluationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('rating_stress_part_one.response', rating_stress_part_one.getRating())
thisExp.addData('rating_stress_part_one.rt', rating_stress_part_one.getRT())
thisExp.nextEntry()
thisExp.addData('rating_stress_part_one.started', rating_stress_part_one.tStart)
thisExp.addData('rating_stress_part_one.stopped', rating_stress_part_one.tStop)
# the Routine "Stress_Evaluation" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = []
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
# the Routine "Blank_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Stress_Part_One_End"-------
t = 0
Stress_Part_One_EndClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_part_one_end = keyboard.Keyboard()
# keep track of which components have finished
Stress_Part_One_EndComponents = [text_part_one_end, text_par_one_end_instructions, key_resp_part_one_end]
for thisComponent in Stress_Part_One_EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Stress_Part_One_End"-------
while continueRoutine:
    # get current time
    t = Stress_Part_One_EndClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_part_one_end* updates
    if t >= 0.0 and text_part_one_end.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_part_one_end.tStart = t  # not accounting for scr refresh
        text_part_one_end.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_part_one_end, 'tStartRefresh')  # time at next scr refresh
        text_part_one_end.setAutoDraw(True)
    
    # *text_par_one_end_instructions* updates
    if t >= 0.0 and text_par_one_end_instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_par_one_end_instructions.tStart = t  # not accounting for scr refresh
        text_par_one_end_instructions.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_par_one_end_instructions, 'tStartRefresh')  # time at next scr refresh
        text_par_one_end_instructions.setAutoDraw(True)
    
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
    for thisComponent in Stress_Part_One_EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Stress_Part_One_End"-------
for thisComponent in Stress_Part_One_EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Stress_Part_One_End" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = []
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
# the Routine "Blank_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Stress_Part_Two"-------
t = 0
Stress_Part_TwoClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
Stress_Part_TwoComponents = [text_part_two_title, text_part_two]
for thisComponent in Stress_Part_TwoComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Stress_Part_Two"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Stress_Part_TwoClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_part_two_title* updates
    if t >= 0.0 and text_part_two_title.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_part_two_title.tStart = t  # not accounting for scr refresh
        text_part_two_title.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_part_two_title, 'tStartRefresh')  # time at next scr refresh
        text_part_two_title.setAutoDraw(True)
    frameRemains = 0.0 + 5.0- win.monitorFramePeriod * 0.75  # most of one frame period left
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
    frameRemains = 0.0 + 5.0- win.monitorFramePeriod * 0.75  # most of one frame period left
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
    for thisComponent in Stress_Part_TwoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Stress_Part_Two"-------
for thisComponent in Stress_Part_TwoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = []
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
# the Routine "Blank_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Stress_Part_Two_Instructions"-------
t = 0
Stress_Part_Two_InstructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_stress_part_two_instructions = keyboard.Keyboard()
# keep track of which components have finished
Stress_Part_Two_InstructionsComponents = [text_part_two_instructions_title, text_part_two_instructions, key_resp_stress_part_two_instructions]
for thisComponent in Stress_Part_Two_InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Stress_Part_Two_Instructions"-------
while continueRoutine:
    # get current time
    t = Stress_Part_Two_InstructionsClock.getTime()
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
    
    # *key_resp_stress_part_two_instructions* updates
    if t >= 0.0 and key_resp_stress_part_two_instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_stress_part_two_instructions.tStart = t  # not accounting for scr refresh
        key_resp_stress_part_two_instructions.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_stress_part_two_instructions, 'tStartRefresh')  # time at next scr refresh
        key_resp_stress_part_two_instructions.status = STARTED
        # keyboard checking is just starting
        key_resp_stress_part_two_instructions.clearEvents(eventType='keyboard')
    if key_resp_stress_part_two_instructions.status == STARTED:
        theseKeys = key_resp_stress_part_two_instructions.getKeys(keyList=['space'], waitRelease=False)
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
    for thisComponent in Stress_Part_Two_InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Stress_Part_Two_Instructions"-------
for thisComponent in Stress_Part_Two_InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Stress_Part_Two_Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = []
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
# the Routine "Blank_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
stroop_trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimuli files\\stroop_stimuli.xlsx', selection='1:6'),
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
    
    # ------Prepare to start Routine "Stress_Part_Two_Measurement"-------
    t = 0
    Stress_Part_Two_MeasurementClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    text_word_item.setColor(WordColor, colorSpace='rgb')
    text_word_item.setText(WordItem)
    text_left_ans.setText(AnsLeft)
    text_right_ans.setText(AnsRight)
    key_resp_stress_part_two = keyboard.Keyboard()
    # keep track of which components have finished
    Stress_Part_Two_MeasurementComponents = [text_word_item, text_left_ans, text_right_ans, key_resp_stress_part_two]
    for thisComponent in Stress_Part_Two_MeasurementComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Stress_Part_Two_Measurement"-------
    while continueRoutine:
        # get current time
        t = Stress_Part_Two_MeasurementClock.getTime()
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
        
        # *key_resp_stress_part_two* updates
        if t >= 0.0 and key_resp_stress_part_two.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_stress_part_two.tStart = t  # not accounting for scr refresh
            key_resp_stress_part_two.frameNStart = frameN  # exact frame index
            win.timeOnFlip(key_resp_stress_part_two, 'tStartRefresh')  # time at next scr refresh
            key_resp_stress_part_two.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_stress_part_two.clock.reset)  # t=0 on next screen flip
            key_resp_stress_part_two.clearEvents(eventType='keyboard')
        if key_resp_stress_part_two.status == STARTED:
            theseKeys = key_resp_stress_part_two.getKeys(keyList=['left', 'right'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp_stress_part_two.keys = theseKeys.name  # just the last key pressed
                key_resp_stress_part_two.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Stress_Part_Two_MeasurementComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Stress_Part_Two_Measurement"-------
    for thisComponent in Stress_Part_Two_MeasurementComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_stress_part_two.keys in ['', [], None]:  # No response was made
        key_resp_stress_part_two.keys = None
    stroop_trials.addData('key_resp_stress_part_two.keys',key_resp_stress_part_two.keys)
    if key_resp_stress_part_two.keys != None:  # we had a response
        stroop_trials.addData('key_resp_stress_part_two.rt', key_resp_stress_part_two.rt)
    stroop_trials.addData('key_resp_stress_part_two.started', key_resp_stress_part_two.tStartRefresh)
    stroop_trials.addData('key_resp_stress_part_two.stopped', key_resp_stress_part_two.tStopRefresh)
    # the Routine "Stress_Part_Two_Measurement" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Blank_Screen"-------
    t = 0
    Blank_ScreenClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    Blank_ScreenComponents = []
    for thisComponent in Blank_ScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Blank_Screen"-------
    while continueRoutine:
        # get current time
        t = Blank_ScreenClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
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
    # the Routine "Blank_Screen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
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

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = []
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
# the Routine "Blank_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Stress_Evaluation_2"-------
t = 0
Stress_Evaluation_2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
rating_stress_part_two.reset()
# keep track of which components have finished
Stress_Evaluation_2Components = [text_part_two_evaluation, text_part_two_evaluation_2, rating_stress_part_two]
for thisComponent in Stress_Evaluation_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Stress_Evaluation_2"-------
while continueRoutine:
    # get current time
    t = Stress_Evaluation_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_part_two_evaluation* updates
    if t >= 0.0 and text_part_two_evaluation.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_part_two_evaluation.tStart = t  # not accounting for scr refresh
        text_part_two_evaluation.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_part_two_evaluation, 'tStartRefresh')  # time at next scr refresh
        text_part_two_evaluation.setAutoDraw(True)
    
    # *text_part_two_evaluation_2* updates
    if t >= 0.0 and text_part_two_evaluation_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_part_two_evaluation_2.tStart = t  # not accounting for scr refresh
        text_part_two_evaluation_2.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_part_two_evaluation_2, 'tStartRefresh')  # time at next scr refresh
        text_part_two_evaluation_2.setAutoDraw(True)
    # *rating_stress_part_two* updates
    if t >= 0.0 and rating_stress_part_two.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating_stress_part_two.tStart = t  # not accounting for scr refresh
        rating_stress_part_two.frameNStart = frameN  # exact frame index
        win.timeOnFlip(rating_stress_part_two, 'tStartRefresh')  # time at next scr refresh
        rating_stress_part_two.setAutoDraw(True)
    continueRoutine &= rating_stress_part_two.noResponse  # a response ends the trial
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Stress_Evaluation_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Stress_Evaluation_2"-------
for thisComponent in Stress_Evaluation_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('rating_stress_part_two.response', rating_stress_part_two.getRating())
thisExp.addData('rating_stress_part_two.rt', rating_stress_part_two.getRT())
thisExp.nextEntry()
thisExp.addData('rating_stress_part_two.started', rating_stress_part_two.tStart)
thisExp.addData('rating_stress_part_two.stopped', rating_stress_part_two.tStop)
# the Routine "Stress_Evaluation_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = []
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
# the Routine "Blank_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Stress_Part_Two_End"-------
t = 0
Stress_Part_Two_EndClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_stress_part_two_end = keyboard.Keyboard()
# keep track of which components have finished
Stress_Part_Two_EndComponents = [text_stress_part_two_end, text_stress_part_two_end_instructions, key_resp_stress_part_two_end]
for thisComponent in Stress_Part_Two_EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Stress_Part_Two_End"-------
while continueRoutine:
    # get current time
    t = Stress_Part_Two_EndClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_stress_part_two_end* updates
    if t >= 0.0 and text_stress_part_two_end.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_stress_part_two_end.tStart = t  # not accounting for scr refresh
        text_stress_part_two_end.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_stress_part_two_end, 'tStartRefresh')  # time at next scr refresh
        text_stress_part_two_end.setAutoDraw(True)
    
    # *text_stress_part_two_end_instructions* updates
    if t >= 0.0 and text_stress_part_two_end_instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_stress_part_two_end_instructions.tStart = t  # not accounting for scr refresh
        text_stress_part_two_end_instructions.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_stress_part_two_end_instructions, 'tStartRefresh')  # time at next scr refresh
        text_stress_part_two_end_instructions.setAutoDraw(True)
    
    # *key_resp_stress_part_two_end* updates
    if t >= 0.0 and key_resp_stress_part_two_end.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_stress_part_two_end.tStart = t  # not accounting for scr refresh
        key_resp_stress_part_two_end.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_stress_part_two_end, 'tStartRefresh')  # time at next scr refresh
        key_resp_stress_part_two_end.status = STARTED
        # keyboard checking is just starting
        key_resp_stress_part_two_end.clearEvents(eventType='keyboard')
    if key_resp_stress_part_two_end.status == STARTED:
        theseKeys = key_resp_stress_part_two_end.getKeys(keyList=['space'], waitRelease=False)
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
    for thisComponent in Stress_Part_Two_EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Stress_Part_Two_End"-------
for thisComponent in Stress_Part_Two_EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Stress_Part_Two_End" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = []
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
# the Routine "Blank_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = []
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
# the Routine "Blank_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Cooldown_Instructions"-------
t = 0
Cooldown_InstructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(15.500000)
# update component parameters for each repeat
# keep track of which components have finished
Cooldown_InstructionsComponents = [text_cooldown_instructions, text_cooldown_countdown, text_cooldown_instructions_title]
for thisComponent in Cooldown_InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Cooldown_Instructions"-------
while continueRoutine and routineTimer.getTime() > 0:
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
    frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_cooldown_instructions.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_cooldown_instructions.tStop = t  # not accounting for scr refresh
        text_cooldown_instructions.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_cooldown_instructions, 'tStopRefresh')  # time at next scr refresh
        text_cooldown_instructions.setAutoDraw(False)
    
    # *text_cooldown_countdown* updates
    if t >= 5.5 and text_cooldown_countdown.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_cooldown_countdown.tStart = t  # not accounting for scr refresh
        text_cooldown_countdown.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_cooldown_countdown, 'tStartRefresh')  # time at next scr refresh
        text_cooldown_countdown.setAutoDraw(True)
    frameRemains = 5.5 + 10- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_cooldown_countdown.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_cooldown_countdown.tStop = t  # not accounting for scr refresh
        text_cooldown_countdown.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_cooldown_countdown, 'tStopRefresh')  # time at next scr refresh
        text_cooldown_countdown.setAutoDraw(False)
    if text_cooldown_countdown.status == STARTED:  # only update if drawing
        text_cooldown_countdown.setText(str(round(routineTimer.getTime(),0)) , log=False)
    
    # *text_cooldown_instructions_title* updates
    if t >= 0.0 and text_cooldown_instructions_title.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_cooldown_instructions_title.tStart = t  # not accounting for scr refresh
        text_cooldown_instructions_title.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_cooldown_instructions_title, 'tStartRefresh')  # time at next scr refresh
        text_cooldown_instructions_title.setAutoDraw(True)
    frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_cooldown_instructions_title.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_cooldown_instructions_title.tStop = t  # not accounting for scr refresh
        text_cooldown_instructions_title.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_cooldown_instructions_title, 'tStopRefresh')  # time at next scr refresh
        text_cooldown_instructions_title.setAutoDraw(False)
    
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
thisExp.addData('text_cooldown_countdown.started', text_cooldown_countdown.tStartRefresh)
thisExp.addData('text_cooldown_countdown.stopped', text_cooldown_countdown.tStopRefresh)

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = []
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
# the Routine "Blank_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Cooldown_Measurement"-------
t = 0
Cooldown_MeasurementClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
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
    frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
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
thisExp.addData('text_cooldown_measurement.started', text_cooldown_measurement.tStartRefresh)
thisExp.addData('text_cooldown_measurement.stopped', text_cooldown_measurement.tStopRefresh)

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = []
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
# the Routine "Blank_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Cooldown_Evaluation"-------
t = 0
Cooldown_EvaluationClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
rating_cooldown.reset()
# keep track of which components have finished
Cooldown_EvaluationComponents = [rating_cooldown, text_cooldown_evaluation_title, text_cooldown_evaluation]
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
    # *rating_cooldown* updates
    if t >= 0.0 and rating_cooldown.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating_cooldown.tStart = t  # not accounting for scr refresh
        rating_cooldown.frameNStart = frameN  # exact frame index
        win.timeOnFlip(rating_cooldown, 'tStartRefresh')  # time at next scr refresh
        rating_cooldown.setAutoDraw(True)
    continueRoutine &= rating_cooldown.noResponse  # a response ends the trial
    
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
thisExp.addData('rating_cooldown.response', rating_cooldown.getRating())
thisExp.addData('rating_cooldown.rt', rating_cooldown.getRT())
thisExp.nextEntry()
thisExp.addData('rating_cooldown.started', rating_cooldown.tStart)
thisExp.addData('rating_cooldown.stopped', rating_cooldown.tStop)
# the Routine "Cooldown_Evaluation" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = []
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
# the Routine "Blank_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = []
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
# the Routine "Blank_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = []
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
# the Routine "Blank_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Emotion_Screen_Pos"-------
t = 0
Emotion_Screen_PosClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
Emotion_Screen_PosComponents = [text_emotion_screen_pos_title, text_emotion_pos_screen]
for thisComponent in Emotion_Screen_PosComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Emotion_Screen_Pos"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Emotion_Screen_PosClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_emotion_screen_pos_title* updates
    if t >= 0.0 and text_emotion_screen_pos_title.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_emotion_screen_pos_title.tStart = t  # not accounting for scr refresh
        text_emotion_screen_pos_title.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_emotion_screen_pos_title, 'tStartRefresh')  # time at next scr refresh
        text_emotion_screen_pos_title.setAutoDraw(True)
    frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_emotion_screen_pos_title.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_emotion_screen_pos_title.tStop = t  # not accounting for scr refresh
        text_emotion_screen_pos_title.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_emotion_screen_pos_title, 'tStopRefresh')  # time at next scr refresh
        text_emotion_screen_pos_title.setAutoDraw(False)
    
    # *text_emotion_pos_screen* updates
    if t >= 0.0 and text_emotion_pos_screen.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_emotion_pos_screen.tStart = t  # not accounting for scr refresh
        text_emotion_pos_screen.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_emotion_pos_screen, 'tStartRefresh')  # time at next scr refresh
        text_emotion_pos_screen.setAutoDraw(True)
    frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_emotion_pos_screen.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_emotion_pos_screen.tStop = t  # not accounting for scr refresh
        text_emotion_pos_screen.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_emotion_pos_screen, 'tStopRefresh')  # time at next scr refresh
        text_emotion_pos_screen.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Emotion_Screen_PosComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Emotion_Screen_Pos"-------
for thisComponent in Emotion_Screen_PosComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = []
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
# the Routine "Blank_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Emotion_Instructions_Pos"-------
t = 0
Emotion_Instructions_PosClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_emotion_instr_pos = keyboard.Keyboard()
# keep track of which components have finished
Emotion_Instructions_PosComponents = [text_emotion_instruction_pos_title, text_emotion_instructions_pos, key_resp_emotion_instr_pos]
for thisComponent in Emotion_Instructions_PosComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Emotion_Instructions_Pos"-------
while continueRoutine:
    # get current time
    t = Emotion_Instructions_PosClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_emotion_instruction_pos_title* updates
    if t >= 0.0 and text_emotion_instruction_pos_title.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_emotion_instruction_pos_title.tStart = t  # not accounting for scr refresh
        text_emotion_instruction_pos_title.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_emotion_instruction_pos_title, 'tStartRefresh')  # time at next scr refresh
        text_emotion_instruction_pos_title.setAutoDraw(True)
    
    # *text_emotion_instructions_pos* updates
    if t >= 0.0 and text_emotion_instructions_pos.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_emotion_instructions_pos.tStart = t  # not accounting for scr refresh
        text_emotion_instructions_pos.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_emotion_instructions_pos, 'tStartRefresh')  # time at next scr refresh
        text_emotion_instructions_pos.setAutoDraw(True)
    
    # *key_resp_emotion_instr_pos* updates
    if t >= 0.0 and key_resp_emotion_instr_pos.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_emotion_instr_pos.tStart = t  # not accounting for scr refresh
        key_resp_emotion_instr_pos.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_emotion_instr_pos, 'tStartRefresh')  # time at next scr refresh
        key_resp_emotion_instr_pos.status = STARTED
        # keyboard checking is just starting
        key_resp_emotion_instr_pos.clearEvents(eventType='keyboard')
    if key_resp_emotion_instr_pos.status == STARTED:
        theseKeys = key_resp_emotion_instr_pos.getKeys(keyList=['space'], waitRelease=False)
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
    for thisComponent in Emotion_Instructions_PosComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Emotion_Instructions_Pos"-------
for thisComponent in Emotion_Instructions_PosComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Emotion_Instructions_Pos" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = []
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
# the Routine "Blank_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
emotion_trials_pos = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimuli files\\picture_list.xlsx', selection='32:36'),
    seed=None, name='emotion_trials_pos')
thisExp.addLoop(emotion_trials_pos)  # add the loop to the experiment
thisEmotion_trials_po = emotion_trials_pos.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEmotion_trials_po.rgb)
if thisEmotion_trials_po != None:
    for paramName in thisEmotion_trials_po:
        exec('{} = thisEmotion_trials_po[paramName]'.format(paramName))

for thisEmotion_trials_po in emotion_trials_pos:
    currentLoop = emotion_trials_pos
    # abbreviate parameter names if possible (e.g. rgb = thisEmotion_trials_po.rgb)
    if thisEmotion_trials_po != None:
        for paramName in thisEmotion_trials_po:
            exec('{} = thisEmotion_trials_po[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Emotion_Measurement_Pos"-------
    t = 0
    Emotion_Measurement_PosClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    image_emotion_meas_pos.setSize((new_width, new_height))
    image_emotion_meas_pos.setImage(pictures)
    # keep track of which components have finished
    Emotion_Measurement_PosComponents = [image_emotion_meas_pos]
    for thisComponent in Emotion_Measurement_PosComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Emotion_Measurement_Pos"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Emotion_Measurement_PosClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_emotion_meas_pos* updates
        if t >= 0.0 and image_emotion_meas_pos.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_emotion_meas_pos.tStart = t  # not accounting for scr refresh
            image_emotion_meas_pos.frameNStart = frameN  # exact frame index
            win.timeOnFlip(image_emotion_meas_pos, 'tStartRefresh')  # time at next scr refresh
            image_emotion_meas_pos.setAutoDraw(True)
        frameRemains = 0.0 + 10- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_emotion_meas_pos.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            image_emotion_meas_pos.tStop = t  # not accounting for scr refresh
            image_emotion_meas_pos.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_emotion_meas_pos, 'tStopRefresh')  # time at next scr refresh
            image_emotion_meas_pos.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Emotion_Measurement_PosComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Emotion_Measurement_Pos"-------
    for thisComponent in Emotion_Measurement_PosComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    emotion_trials_pos.addData('image_emotion_meas_pos.started', image_emotion_meas_pos.tStartRefresh)
    emotion_trials_pos.addData('image_emotion_meas_pos.stopped', image_emotion_meas_pos.tStopRefresh)
    
    # ------Prepare to start Routine "Blank_Screen"-------
    t = 0
    Blank_ScreenClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    Blank_ScreenComponents = []
    for thisComponent in Blank_ScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Blank_Screen"-------
    while continueRoutine:
        # get current time
        t = Blank_ScreenClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
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
    # the Routine "Blank_Screen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Emotion_Evaluation_Pos"-------
    t = 0
    Emotion_Evaluation_PosClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    image_emotion_evaluation_pos.setImage(pictures)
    rating_emotion_evaluation_pos.reset()
    # keep track of which components have finished
    Emotion_Evaluation_PosComponents = [image_emotion_evaluation_pos, rating_emotion_evaluation_pos]
    for thisComponent in Emotion_Evaluation_PosComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Emotion_Evaluation_Pos"-------
    while continueRoutine:
        # get current time
        t = Emotion_Evaluation_PosClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_emotion_evaluation_pos* updates
        if t >= 0.0 and image_emotion_evaluation_pos.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_emotion_evaluation_pos.tStart = t  # not accounting for scr refresh
            image_emotion_evaluation_pos.frameNStart = frameN  # exact frame index
            win.timeOnFlip(image_emotion_evaluation_pos, 'tStartRefresh')  # time at next scr refresh
            image_emotion_evaluation_pos.setAutoDraw(True)
        # *rating_emotion_evaluation_pos* updates
        if t >= 0.0 and rating_emotion_evaluation_pos.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating_emotion_evaluation_pos.tStart = t  # not accounting for scr refresh
            rating_emotion_evaluation_pos.frameNStart = frameN  # exact frame index
            win.timeOnFlip(rating_emotion_evaluation_pos, 'tStartRefresh')  # time at next scr refresh
            rating_emotion_evaluation_pos.setAutoDraw(True)
        continueRoutine &= rating_emotion_evaluation_pos.noResponse  # a response ends the trial
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Emotion_Evaluation_PosComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Emotion_Evaluation_Pos"-------
    for thisComponent in Emotion_Evaluation_PosComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for emotion_trials_pos (TrialHandler)
    emotion_trials_pos.addData('rating_emotion_evaluation_pos.response', rating_emotion_evaluation_pos.getRating())
    emotion_trials_pos.addData('rating_emotion_evaluation_pos.rt', rating_emotion_evaluation_pos.getRT())
    emotion_trials_pos.addData('rating_emotion_evaluation_pos.started', rating_emotion_evaluation_pos.tStart)
    emotion_trials_pos.addData('rating_emotion_evaluation_pos.stopped', rating_emotion_evaluation_pos.tStop)
    # the Routine "Emotion_Evaluation_Pos" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'emotion_trials_pos'

# get names of stimulus parameters
if emotion_trials_pos.trialList in ([], [None], None):
    params = []
else:
    params = emotion_trials_pos.trialList[0].keys()
# save data for this loop
emotion_trials_pos.saveAsExcel(filename + '.xlsx', sheetName='emotion_trials_pos',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
emotion_trials_pos.saveAsText(filename + 'emotion_trials_pos.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = []
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
# the Routine "Blank_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = []
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
# the Routine "Blank_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Cooldown_Instructions"-------
t = 0
Cooldown_InstructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(15.500000)
# update component parameters for each repeat
# keep track of which components have finished
Cooldown_InstructionsComponents = [text_cooldown_instructions, text_cooldown_countdown, text_cooldown_instructions_title]
for thisComponent in Cooldown_InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Cooldown_Instructions"-------
while continueRoutine and routineTimer.getTime() > 0:
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
    frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_cooldown_instructions.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_cooldown_instructions.tStop = t  # not accounting for scr refresh
        text_cooldown_instructions.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_cooldown_instructions, 'tStopRefresh')  # time at next scr refresh
        text_cooldown_instructions.setAutoDraw(False)
    
    # *text_cooldown_countdown* updates
    if t >= 5.5 and text_cooldown_countdown.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_cooldown_countdown.tStart = t  # not accounting for scr refresh
        text_cooldown_countdown.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_cooldown_countdown, 'tStartRefresh')  # time at next scr refresh
        text_cooldown_countdown.setAutoDraw(True)
    frameRemains = 5.5 + 10- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_cooldown_countdown.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_cooldown_countdown.tStop = t  # not accounting for scr refresh
        text_cooldown_countdown.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_cooldown_countdown, 'tStopRefresh')  # time at next scr refresh
        text_cooldown_countdown.setAutoDraw(False)
    if text_cooldown_countdown.status == STARTED:  # only update if drawing
        text_cooldown_countdown.setText(str(round(routineTimer.getTime(),0)) , log=False)
    
    # *text_cooldown_instructions_title* updates
    if t >= 0.0 and text_cooldown_instructions_title.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_cooldown_instructions_title.tStart = t  # not accounting for scr refresh
        text_cooldown_instructions_title.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_cooldown_instructions_title, 'tStartRefresh')  # time at next scr refresh
        text_cooldown_instructions_title.setAutoDraw(True)
    frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_cooldown_instructions_title.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_cooldown_instructions_title.tStop = t  # not accounting for scr refresh
        text_cooldown_instructions_title.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_cooldown_instructions_title, 'tStopRefresh')  # time at next scr refresh
        text_cooldown_instructions_title.setAutoDraw(False)
    
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
thisExp.addData('text_cooldown_countdown.started', text_cooldown_countdown.tStartRefresh)
thisExp.addData('text_cooldown_countdown.stopped', text_cooldown_countdown.tStopRefresh)

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = []
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
# the Routine "Blank_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Cooldown_Evaluation"-------
t = 0
Cooldown_EvaluationClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
rating_cooldown.reset()
# keep track of which components have finished
Cooldown_EvaluationComponents = [rating_cooldown, text_cooldown_evaluation_title, text_cooldown_evaluation]
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
    # *rating_cooldown* updates
    if t >= 0.0 and rating_cooldown.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating_cooldown.tStart = t  # not accounting for scr refresh
        rating_cooldown.frameNStart = frameN  # exact frame index
        win.timeOnFlip(rating_cooldown, 'tStartRefresh')  # time at next scr refresh
        rating_cooldown.setAutoDraw(True)
    continueRoutine &= rating_cooldown.noResponse  # a response ends the trial
    
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
thisExp.addData('rating_cooldown.response', rating_cooldown.getRating())
thisExp.addData('rating_cooldown.rt', rating_cooldown.getRT())
thisExp.nextEntry()
thisExp.addData('rating_cooldown.started', rating_cooldown.tStart)
thisExp.addData('rating_cooldown.stopped', rating_cooldown.tStop)
# the Routine "Cooldown_Evaluation" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = []
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
# the Routine "Blank_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = []
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
# the Routine "Blank_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Emotion_Screen_Neg"-------
t = 0
Emotion_Screen_NegClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
Emotion_Screen_NegComponents = [text_emotion_screen_neg_title, text_emotion_neg_screen]
for thisComponent in Emotion_Screen_NegComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Emotion_Screen_Neg"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Emotion_Screen_NegClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_emotion_screen_neg_title* updates
    if t >= 0.0 and text_emotion_screen_neg_title.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_emotion_screen_neg_title.tStart = t  # not accounting for scr refresh
        text_emotion_screen_neg_title.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_emotion_screen_neg_title, 'tStartRefresh')  # time at next scr refresh
        text_emotion_screen_neg_title.setAutoDraw(True)
    frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_emotion_screen_neg_title.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_emotion_screen_neg_title.tStop = t  # not accounting for scr refresh
        text_emotion_screen_neg_title.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_emotion_screen_neg_title, 'tStopRefresh')  # time at next scr refresh
        text_emotion_screen_neg_title.setAutoDraw(False)
    
    # *text_emotion_neg_screen* updates
    if t >= 0.0 and text_emotion_neg_screen.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_emotion_neg_screen.tStart = t  # not accounting for scr refresh
        text_emotion_neg_screen.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_emotion_neg_screen, 'tStartRefresh')  # time at next scr refresh
        text_emotion_neg_screen.setAutoDraw(True)
    frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_emotion_neg_screen.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_emotion_neg_screen.tStop = t  # not accounting for scr refresh
        text_emotion_neg_screen.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_emotion_neg_screen, 'tStopRefresh')  # time at next scr refresh
        text_emotion_neg_screen.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Emotion_Screen_NegComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Emotion_Screen_Neg"-------
for thisComponent in Emotion_Screen_NegComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = []
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
# the Routine "Blank_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Emotion_Instructions_Neg"-------
t = 0
Emotion_Instructions_NegClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_emotion_instr_neg = keyboard.Keyboard()
# keep track of which components have finished
Emotion_Instructions_NegComponents = [text_emotion_instruction_neg_title, text_emotion_instructions_neg, key_resp_emotion_instr_neg]
for thisComponent in Emotion_Instructions_NegComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Emotion_Instructions_Neg"-------
while continueRoutine:
    # get current time
    t = Emotion_Instructions_NegClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_emotion_instruction_neg_title* updates
    if t >= 0.0 and text_emotion_instruction_neg_title.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_emotion_instruction_neg_title.tStart = t  # not accounting for scr refresh
        text_emotion_instruction_neg_title.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_emotion_instruction_neg_title, 'tStartRefresh')  # time at next scr refresh
        text_emotion_instruction_neg_title.setAutoDraw(True)
    
    # *text_emotion_instructions_neg* updates
    if t >= 0.0 and text_emotion_instructions_neg.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_emotion_instructions_neg.tStart = t  # not accounting for scr refresh
        text_emotion_instructions_neg.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_emotion_instructions_neg, 'tStartRefresh')  # time at next scr refresh
        text_emotion_instructions_neg.setAutoDraw(True)
    
    # *key_resp_emotion_instr_neg* updates
    if t >= 0.0 and key_resp_emotion_instr_neg.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_emotion_instr_neg.tStart = t  # not accounting for scr refresh
        key_resp_emotion_instr_neg.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_emotion_instr_neg, 'tStartRefresh')  # time at next scr refresh
        key_resp_emotion_instr_neg.status = STARTED
        # keyboard checking is just starting
        key_resp_emotion_instr_neg.clearEvents(eventType='keyboard')
    if key_resp_emotion_instr_neg.status == STARTED:
        theseKeys = key_resp_emotion_instr_neg.getKeys(keyList=['space'], waitRelease=False)
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
    for thisComponent in Emotion_Instructions_NegComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Emotion_Instructions_Neg"-------
for thisComponent in Emotion_Instructions_NegComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Emotion_Instructions_Neg" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = []
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
# the Routine "Blank_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
emotion_trials_neg = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimuli files\\picture_list.xlsx', selection='37:40'),
    seed=None, name='emotion_trials_neg')
thisExp.addLoop(emotion_trials_neg)  # add the loop to the experiment
thisEmotion_trials_neg = emotion_trials_neg.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEmotion_trials_neg.rgb)
if thisEmotion_trials_neg != None:
    for paramName in thisEmotion_trials_neg:
        exec('{} = thisEmotion_trials_neg[paramName]'.format(paramName))

for thisEmotion_trials_neg in emotion_trials_neg:
    currentLoop = emotion_trials_neg
    # abbreviate parameter names if possible (e.g. rgb = thisEmotion_trials_neg.rgb)
    if thisEmotion_trials_neg != None:
        for paramName in thisEmotion_trials_neg:
            exec('{} = thisEmotion_trials_neg[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Emotion_Measurement_Neg"-------
    t = 0
    Emotion_Measurement_NegClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    image_emotion_meas_neg.setSize((new_width, new_height))
    image_emotion_meas_neg.setImage(pictures)
    # keep track of which components have finished
    Emotion_Measurement_NegComponents = [image_emotion_meas_neg]
    for thisComponent in Emotion_Measurement_NegComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Emotion_Measurement_Neg"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Emotion_Measurement_NegClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_emotion_meas_neg* updates
        if t >= 0.0 and image_emotion_meas_neg.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_emotion_meas_neg.tStart = t  # not accounting for scr refresh
            image_emotion_meas_neg.frameNStart = frameN  # exact frame index
            win.timeOnFlip(image_emotion_meas_neg, 'tStartRefresh')  # time at next scr refresh
            image_emotion_meas_neg.setAutoDraw(True)
        frameRemains = 0.0 + 10- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_emotion_meas_neg.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            image_emotion_meas_neg.tStop = t  # not accounting for scr refresh
            image_emotion_meas_neg.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_emotion_meas_neg, 'tStopRefresh')  # time at next scr refresh
            image_emotion_meas_neg.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Emotion_Measurement_NegComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Emotion_Measurement_Neg"-------
    for thisComponent in Emotion_Measurement_NegComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    emotion_trials_neg.addData('image_emotion_meas_neg.started', image_emotion_meas_neg.tStartRefresh)
    emotion_trials_neg.addData('image_emotion_meas_neg.stopped', image_emotion_meas_neg.tStopRefresh)
    
    # ------Prepare to start Routine "Blank_Screen"-------
    t = 0
    Blank_ScreenClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    Blank_ScreenComponents = []
    for thisComponent in Blank_ScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Blank_Screen"-------
    while continueRoutine:
        # get current time
        t = Blank_ScreenClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
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
    # the Routine "Blank_Screen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Emotion_Evaluation_Neg"-------
    t = 0
    Emotion_Evaluation_NegClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    image_emotion_evaluation_neg.setImage(pictures)
    rating_emotion_evaluation_neg.reset()
    # keep track of which components have finished
    Emotion_Evaluation_NegComponents = [image_emotion_evaluation_neg, rating_emotion_evaluation_neg]
    for thisComponent in Emotion_Evaluation_NegComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Emotion_Evaluation_Neg"-------
    while continueRoutine:
        # get current time
        t = Emotion_Evaluation_NegClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_emotion_evaluation_neg* updates
        if t >= 0.0 and image_emotion_evaluation_neg.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_emotion_evaluation_neg.tStart = t  # not accounting for scr refresh
            image_emotion_evaluation_neg.frameNStart = frameN  # exact frame index
            win.timeOnFlip(image_emotion_evaluation_neg, 'tStartRefresh')  # time at next scr refresh
            image_emotion_evaluation_neg.setAutoDraw(True)
        # *rating_emotion_evaluation_neg* updates
        if t >= 0.0 and rating_emotion_evaluation_neg.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating_emotion_evaluation_neg.tStart = t  # not accounting for scr refresh
            rating_emotion_evaluation_neg.frameNStart = frameN  # exact frame index
            win.timeOnFlip(rating_emotion_evaluation_neg, 'tStartRefresh')  # time at next scr refresh
            rating_emotion_evaluation_neg.setAutoDraw(True)
        continueRoutine &= rating_emotion_evaluation_neg.noResponse  # a response ends the trial
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Emotion_Evaluation_NegComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Emotion_Evaluation_Neg"-------
    for thisComponent in Emotion_Evaluation_NegComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for emotion_trials_neg (TrialHandler)
    emotion_trials_neg.addData('rating_emotion_evaluation_neg.response', rating_emotion_evaluation_neg.getRating())
    emotion_trials_neg.addData('rating_emotion_evaluation_neg.rt', rating_emotion_evaluation_neg.getRT())
    emotion_trials_neg.addData('rating_emotion_evaluation_neg.started', rating_emotion_evaluation_neg.tStart)
    emotion_trials_neg.addData('rating_emotion_evaluation_neg.stopped', rating_emotion_evaluation_neg.tStop)
    # the Routine "Emotion_Evaluation_Neg" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'emotion_trials_neg'

# get names of stimulus parameters
if emotion_trials_neg.trialList in ([], [None], None):
    params = []
else:
    params = emotion_trials_neg.trialList[0].keys()
# save data for this loop
emotion_trials_neg.saveAsExcel(filename + '.xlsx', sheetName='emotion_trials_neg',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
emotion_trials_neg.saveAsText(filename + 'emotion_trials_neg.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = []
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
# the Routine "Blank_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = []
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
# the Routine "Blank_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Cooldown_Instructions"-------
t = 0
Cooldown_InstructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(15.500000)
# update component parameters for each repeat
# keep track of which components have finished
Cooldown_InstructionsComponents = [text_cooldown_instructions, text_cooldown_countdown, text_cooldown_instructions_title]
for thisComponent in Cooldown_InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Cooldown_Instructions"-------
while continueRoutine and routineTimer.getTime() > 0:
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
    frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_cooldown_instructions.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_cooldown_instructions.tStop = t  # not accounting for scr refresh
        text_cooldown_instructions.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_cooldown_instructions, 'tStopRefresh')  # time at next scr refresh
        text_cooldown_instructions.setAutoDraw(False)
    
    # *text_cooldown_countdown* updates
    if t >= 5.5 and text_cooldown_countdown.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_cooldown_countdown.tStart = t  # not accounting for scr refresh
        text_cooldown_countdown.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_cooldown_countdown, 'tStartRefresh')  # time at next scr refresh
        text_cooldown_countdown.setAutoDraw(True)
    frameRemains = 5.5 + 10- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_cooldown_countdown.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_cooldown_countdown.tStop = t  # not accounting for scr refresh
        text_cooldown_countdown.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_cooldown_countdown, 'tStopRefresh')  # time at next scr refresh
        text_cooldown_countdown.setAutoDraw(False)
    if text_cooldown_countdown.status == STARTED:  # only update if drawing
        text_cooldown_countdown.setText(str(round(routineTimer.getTime(),0)) , log=False)
    
    # *text_cooldown_instructions_title* updates
    if t >= 0.0 and text_cooldown_instructions_title.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_cooldown_instructions_title.tStart = t  # not accounting for scr refresh
        text_cooldown_instructions_title.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_cooldown_instructions_title, 'tStartRefresh')  # time at next scr refresh
        text_cooldown_instructions_title.setAutoDraw(True)
    frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_cooldown_instructions_title.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_cooldown_instructions_title.tStop = t  # not accounting for scr refresh
        text_cooldown_instructions_title.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_cooldown_instructions_title, 'tStopRefresh')  # time at next scr refresh
        text_cooldown_instructions_title.setAutoDraw(False)
    
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
thisExp.addData('text_cooldown_countdown.started', text_cooldown_countdown.tStartRefresh)
thisExp.addData('text_cooldown_countdown.stopped', text_cooldown_countdown.tStopRefresh)

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = []
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
# the Routine "Blank_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Cooldown_Measurement"-------
t = 0
Cooldown_MeasurementClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
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
    frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
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
thisExp.addData('text_cooldown_measurement.started', text_cooldown_measurement.tStartRefresh)
thisExp.addData('text_cooldown_measurement.stopped', text_cooldown_measurement.tStopRefresh)

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = []
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
# the Routine "Blank_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Cooldown_Evaluation"-------
t = 0
Cooldown_EvaluationClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
rating_cooldown.reset()
# keep track of which components have finished
Cooldown_EvaluationComponents = [rating_cooldown, text_cooldown_evaluation_title, text_cooldown_evaluation]
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
    # *rating_cooldown* updates
    if t >= 0.0 and rating_cooldown.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating_cooldown.tStart = t  # not accounting for scr refresh
        rating_cooldown.frameNStart = frameN  # exact frame index
        win.timeOnFlip(rating_cooldown, 'tStartRefresh')  # time at next scr refresh
        rating_cooldown.setAutoDraw(True)
    continueRoutine &= rating_cooldown.noResponse  # a response ends the trial
    
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
thisExp.addData('rating_cooldown.response', rating_cooldown.getRating())
thisExp.addData('rating_cooldown.rt', rating_cooldown.getRT())
thisExp.nextEntry()
thisExp.addData('rating_cooldown.started', rating_cooldown.tStart)
thisExp.addData('rating_cooldown.stopped', rating_cooldown.tStop)
# the Routine "Cooldown_Evaluation" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = []
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
# the Routine "Blank_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = []
for thisComponent in Blank_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Blank_Screen"-------
while continueRoutine:
    # get current time
    t = Blank_ScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
# the Routine "Blank_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Ending_Screen"-------
t = 0
Ending_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(10.000000)
# update component parameters for each repeat
# keep track of which components have finished
Ending_ScreenComponents = [text_ending_screen, text_ending_subtitle]
for thisComponent in Ending_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Ending_Screen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Ending_ScreenClock.getTime()
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
    for thisComponent in Ending_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Ending_Screen"-------
for thisComponent in Ending_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_ending_screen.started', text_ending_screen.tStartRefresh)
thisExp.addData('text_ending_screen.stopped', text_ending_screen.tStopRefresh)

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
