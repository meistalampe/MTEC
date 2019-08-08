#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.3),
    on August 08, 2019, at 20:30
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock, hardware
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
expName = 'MTEC_paradigm'  # from the Builder filename that created this script
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
    originPath='E:\\GitHub\\MTEC\\Paradigm\\MTEC_paradigm_lastrun.py',
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
text_blank_screen = visual.TextStim(win=win, name='text_blank_screen',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

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
text_blank_screen = visual.TextStim(win=win, name='text_blank_screen',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Baseline_Instructions"
Baseline_InstructionsClock = core.Clock()
text_baseline_instructions = visual.TextStim(win=win, name='text_baseline_instructions',
    text='  Please try to relax.\n\nThe Measurement will\n       start shortly.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_baseline_countdown = visual.TextStim(win=win, name='text_baseline_countdown',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()
text_blank_screen = visual.TextStim(win=win, name='text_blank_screen',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Baseline_Measurement"
Baseline_MeasurementClock = core.Clock()
text_baseline_measurement = visual.TextStim(win=win, name='text_baseline_measurement',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()
text_blank_screen = visual.TextStim(win=win, name='text_blank_screen',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

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
text_blank_screen = visual.TextStim(win=win, name='text_blank_screen',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

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
text_blank_screen = visual.TextStim(win=win, name='text_blank_screen',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

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
text_blank_screen = visual.TextStim(win=win, name='text_blank_screen',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Stress_Part_One_Instructions"
Stress_Part_One_InstructionsClock = core.Clock()
text_stress_part_one_instructions_title = visual.TextStim(win=win, name='text_stress_part_one_instructions_title',
    text='Instructions:',
    font='Arial',
    pos=(0, 0.2), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_stress_part_one_instructions = visual.TextStim(win=win, name='text_stress_part_one_instructions',
    text="Count down from 1400 in steps of 7.\n\nTry to match the speed of the metronome dot on the screen.\n\n(Press 'Space' to start)",
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()
text_blank_screen = visual.TextStim(win=win, name='text_blank_screen',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Stress_Part_One_Measurement"
Stress_Part_One_MeasurementClock = core.Clock()
metronome = visual.Polygon(
    win=win, name='metronome',
    edges=32, size=(0.25, 0.25),
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
text_blank_screen = visual.TextStim(win=win, name='text_blank_screen',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Stress_Evaluation"
Stress_EvaluationClock = core.Clock()
text_part_one_evaluation = visual.TextStim(win=win, name='text_part_one_evaluation',
    text='Task finished.\n\nPlease rate the difficulty of the task.',
    font='Arial',
    pos=(0, 0.2), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
rating_part_one = visual.RatingScale(win=win, name='rating_part_one', marker='triangle', size=1.0, pos=[0.0, -0.2], low=1, high=10, labels=['very easy', ' very hard'], scale='', markerStart='5')

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
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()
text_blank_screen = visual.TextStim(win=win, name='text_blank_screen',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

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
text_blank_screen = visual.TextStim(win=win, name='text_blank_screen',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Stress_Part_Two_Instructions"
Stress_Part_Two_InstructionsClock = core.Clock()
text_part_two_instructions_title = visual.TextStim(win=win, name='text_part_two_instructions_title',
    text='Instructions:',
    font='Arial',
    pos=(0, 0.2), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_part_two_instructions = visual.TextStim(win=win, name='text_part_two_instructions',
    text="Choose the color of the word by using the arrow keys.\n\n(Press 'Space' to start)",
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()
text_blank_screen = visual.TextStim(win=win, name='text_blank_screen',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Stress_Part_Two_Measurement"
Stress_Part_Two_MeasurementClock = core.Clock()

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()
text_blank_screen = visual.TextStim(win=win, name='text_blank_screen',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Stress_Part_Two_End"
Stress_Part_Two_EndClock = core.Clock()

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()
text_blank_screen = visual.TextStim(win=win, name='text_blank_screen',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

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
        key_resp_welcome_screen.clearEvents(eventType='keyboard')
    if key_resp_welcome_screen.status == STARTED:
        theseKeys = key_resp_welcome_screen.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
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
# the Routine "Welcome_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = [text_blank_screen]
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
    
    # *text_blank_screen* updates
    if t >= 0.0 and text_blank_screen.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_blank_screen.tStart = t  # not accounting for scr refresh
        text_blank_screen.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_blank_screen, 'tStartRefresh')  # time at next scr refresh
        text_blank_screen.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_blank_screen.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_blank_screen.tStop = t  # not accounting for scr refresh
        text_blank_screen.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_blank_screen, 'tStopRefresh')  # time at next scr refresh
        text_blank_screen.setAutoDraw(False)
    
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

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = [text_blank_screen]
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
    
    # *text_blank_screen* updates
    if t >= 0.0 and text_blank_screen.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_blank_screen.tStart = t  # not accounting for scr refresh
        text_blank_screen.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_blank_screen, 'tStartRefresh')  # time at next scr refresh
        text_blank_screen.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_blank_screen.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_blank_screen.tStop = t  # not accounting for scr refresh
        text_blank_screen.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_blank_screen, 'tStopRefresh')  # time at next scr refresh
        text_blank_screen.setAutoDraw(False)
    
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

# ------Prepare to start Routine "Baseline_Instructions"-------
t = 0
Baseline_InstructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(15.500000)
# update component parameters for each repeat
# keep track of which components have finished
Baseline_InstructionsComponents = [text_baseline_instructions, text_baseline_countdown]
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
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = [text_blank_screen]
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
    
    # *text_blank_screen* updates
    if t >= 0.0 and text_blank_screen.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_blank_screen.tStart = t  # not accounting for scr refresh
        text_blank_screen.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_blank_screen, 'tStartRefresh')  # time at next scr refresh
        text_blank_screen.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_blank_screen.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_blank_screen.tStop = t  # not accounting for scr refresh
        text_blank_screen.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_blank_screen, 'tStopRefresh')  # time at next scr refresh
        text_blank_screen.setAutoDraw(False)
    
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
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = [text_blank_screen]
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
    
    # *text_blank_screen* updates
    if t >= 0.0 and text_blank_screen.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_blank_screen.tStart = t  # not accounting for scr refresh
        text_blank_screen.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_blank_screen, 'tStartRefresh')  # time at next scr refresh
        text_blank_screen.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_blank_screen.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_blank_screen.tStop = t  # not accounting for scr refresh
        text_blank_screen.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_blank_screen, 'tStopRefresh')  # time at next scr refresh
        text_blank_screen.setAutoDraw(False)
    
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
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = [text_blank_screen]
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
    
    # *text_blank_screen* updates
    if t >= 0.0 and text_blank_screen.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_blank_screen.tStart = t  # not accounting for scr refresh
        text_blank_screen.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_blank_screen, 'tStartRefresh')  # time at next scr refresh
        text_blank_screen.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_blank_screen.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_blank_screen.tStop = t  # not accounting for scr refresh
        text_blank_screen.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_blank_screen, 'tStopRefresh')  # time at next scr refresh
        text_blank_screen.setAutoDraw(False)
    
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

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = [text_blank_screen]
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
    
    # *text_blank_screen* updates
    if t >= 0.0 and text_blank_screen.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_blank_screen.tStart = t  # not accounting for scr refresh
        text_blank_screen.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_blank_screen, 'tStartRefresh')  # time at next scr refresh
        text_blank_screen.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_blank_screen.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_blank_screen.tStop = t  # not accounting for scr refresh
        text_blank_screen.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_blank_screen, 'tStopRefresh')  # time at next scr refresh
        text_blank_screen.setAutoDraw(False)
    
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
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = [text_blank_screen]
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
    
    # *text_blank_screen* updates
    if t >= 0.0 and text_blank_screen.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_blank_screen.tStart = t  # not accounting for scr refresh
        text_blank_screen.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_blank_screen, 'tStartRefresh')  # time at next scr refresh
        text_blank_screen.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_blank_screen.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_blank_screen.tStop = t  # not accounting for scr refresh
        text_blank_screen.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_blank_screen, 'tStopRefresh')  # time at next scr refresh
        text_blank_screen.setAutoDraw(False)
    
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
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = [text_blank_screen]
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
    
    # *text_blank_screen* updates
    if t >= 0.0 and text_blank_screen.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_blank_screen.tStart = t  # not accounting for scr refresh
        text_blank_screen.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_blank_screen, 'tStartRefresh')  # time at next scr refresh
        text_blank_screen.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_blank_screen.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_blank_screen.tStop = t  # not accounting for scr refresh
        text_blank_screen.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_blank_screen, 'tStopRefresh')  # time at next scr refresh
        text_blank_screen.setAutoDraw(False)
    
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
    trialList=data.importConditions('stimuli files\\metronome.xlsx', selection='1:301'),
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
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = [text_blank_screen]
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
    
    # *text_blank_screen* updates
    if t >= 0.0 and text_blank_screen.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_blank_screen.tStart = t  # not accounting for scr refresh
        text_blank_screen.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_blank_screen, 'tStartRefresh')  # time at next scr refresh
        text_blank_screen.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_blank_screen.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_blank_screen.tStop = t  # not accounting for scr refresh
        text_blank_screen.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_blank_screen, 'tStopRefresh')  # time at next scr refresh
        text_blank_screen.setAutoDraw(False)
    
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

# ------Prepare to start Routine "Stress_Evaluation"-------
t = 0
Stress_EvaluationClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
rating_part_one.reset()
# keep track of which components have finished
Stress_EvaluationComponents = [text_part_one_evaluation, rating_part_one]
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
    # *rating_part_one* updates
    if t >= 0.0 and rating_part_one.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating_part_one.tStart = t  # not accounting for scr refresh
        rating_part_one.frameNStart = frameN  # exact frame index
        win.timeOnFlip(rating_part_one, 'tStartRefresh')  # time at next scr refresh
        rating_part_one.setAutoDraw(True)
    continueRoutine &= rating_part_one.noResponse  # a response ends the trial
    
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
thisExp.addData('text_part_one_evaluation.started', text_part_one_evaluation.tStartRefresh)
thisExp.addData('text_part_one_evaluation.stopped', text_part_one_evaluation.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('rating_part_one.response', rating_part_one.getRating())
thisExp.addData('rating_part_one.rt', rating_part_one.getRT())
thisExp.nextEntry()
# the Routine "Stress_Evaluation" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Stress_Part_One_End"-------
t = 0
Stress_Part_One_EndClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Stress_Part_One_EndComponents = [text_part_one_end, text_par_one_end_instructions]
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
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = [text_blank_screen]
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
    
    # *text_blank_screen* updates
    if t >= 0.0 and text_blank_screen.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_blank_screen.tStart = t  # not accounting for scr refresh
        text_blank_screen.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_blank_screen, 'tStartRefresh')  # time at next scr refresh
        text_blank_screen.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_blank_screen.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_blank_screen.tStop = t  # not accounting for scr refresh
        text_blank_screen.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_blank_screen, 'tStopRefresh')  # time at next scr refresh
        text_blank_screen.setAutoDraw(False)
    
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
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = [text_blank_screen]
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
    
    # *text_blank_screen* updates
    if t >= 0.0 and text_blank_screen.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_blank_screen.tStart = t  # not accounting for scr refresh
        text_blank_screen.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_blank_screen, 'tStartRefresh')  # time at next scr refresh
        text_blank_screen.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_blank_screen.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_blank_screen.tStop = t  # not accounting for scr refresh
        text_blank_screen.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_blank_screen, 'tStopRefresh')  # time at next scr refresh
        text_blank_screen.setAutoDraw(False)
    
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

# ------Prepare to start Routine "Stress_Part_Two_Instructions"-------
t = 0
Stress_Part_Two_InstructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Stress_Part_Two_InstructionsComponents = [text_part_two_instructions_title, text_part_two_instructions]
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
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = [text_blank_screen]
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
    
    # *text_blank_screen* updates
    if t >= 0.0 and text_blank_screen.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_blank_screen.tStart = t  # not accounting for scr refresh
        text_blank_screen.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_blank_screen, 'tStartRefresh')  # time at next scr refresh
        text_blank_screen.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_blank_screen.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_blank_screen.tStop = t  # not accounting for scr refresh
        text_blank_screen.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_blank_screen, 'tStopRefresh')  # time at next scr refresh
        text_blank_screen.setAutoDraw(False)
    
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

# ------Prepare to start Routine "Stress_Part_Two_Measurement"-------
t = 0
Stress_Part_Two_MeasurementClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Stress_Part_Two_MeasurementComponents = []
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
# the Routine "Stress_Part_Two_Measurement" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank_Screen"-------
t = 0
Blank_ScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = [text_blank_screen]
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
    
    # *text_blank_screen* updates
    if t >= 0.0 and text_blank_screen.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_blank_screen.tStart = t  # not accounting for scr refresh
        text_blank_screen.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_blank_screen, 'tStartRefresh')  # time at next scr refresh
        text_blank_screen.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_blank_screen.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_blank_screen.tStop = t  # not accounting for scr refresh
        text_blank_screen.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_blank_screen, 'tStopRefresh')  # time at next scr refresh
        text_blank_screen.setAutoDraw(False)
    
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

# ------Prepare to start Routine "Stress_Part_Two_End"-------
t = 0
Stress_Part_Two_EndClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Stress_Part_Two_EndComponents = []
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
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank_ScreenComponents = [text_blank_screen]
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
    
    # *text_blank_screen* updates
    if t >= 0.0 and text_blank_screen.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_blank_screen.tStart = t  # not accounting for scr refresh
        text_blank_screen.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_blank_screen, 'tStartRefresh')  # time at next scr refresh
        text_blank_screen.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_blank_screen.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_blank_screen.tStop = t  # not accounting for scr refresh
        text_blank_screen.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_blank_screen, 'tStopRefresh')  # time at next scr refresh
        text_blank_screen.setAutoDraw(False)
    
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
