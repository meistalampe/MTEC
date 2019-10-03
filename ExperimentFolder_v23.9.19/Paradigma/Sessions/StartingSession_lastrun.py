#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.3),
    on September 28, 2019, at 10:51
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
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
psychopyVersion = '3.2.3'
expName = 'StartingSession'  # from the Builder filename that created this script
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
    originPath='E:\\Master Thesis\\ExperimentFolder_v23.9.19\\Paradigma\\Sessions\\StartingSession_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

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

# Initialize components for Routine "Welcome_Screen"
Welcome_ScreenClock = core.Clock()
text_welcome_screen = visual.TextStim(win=win, name='text_welcome_screen',
    text='  Welcome \n     to the \nExperiment',
    font='Arial',
    pos=(0, 0.1), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_welcome_screen_continue = visual.TextStim(win=win, name='text_welcome_screen_continue',
    text="(Press 'SPACE' to continue)",
    font='Arial',
    pos=(0, -0.3), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_welcome_screen = keyboard.Keyboard()
import time
thisExp.addData("start_session_one", time.strftime("%Y-%m-%d_%H:%M:%S")) 

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
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_baseline_screen_title = visual.TextStim(win=win, name='text_baseline_screen_title',
    text='Session One:',
    font='Arial',
    pos=(0, 0.2), height=0.04, wrapWidth=None, ori=0, 
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

# Initialize components for Routine "Baseline_Instructions"
Baseline_InstructionsClock = core.Clock()
text_baseline_instructions_title = visual.TextStim(win=win, name='text_baseline_instructions_title',
    text='Instructions:',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_baseline_instructions = visual.TextStim(win=win, name='text_baseline_instructions',
    text='Please try to relax as much as possible.\n\nWhen you are ready please tell your instructor to start the measurement.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_baseline_instructions = keyboard.Keyboard()

# Initialize components for Routine "Blank_Screen"
Blank_ScreenClock = core.Clock()
text_blank_screen = visual.TextStim(win=win, name='text_blank_screen',
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
    pos=(0, 0), height=0.4, wrapWidth=None, ori=0, 
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

# Initialize components for Routine "Baseline_Evaluation"
Baseline_EvaluationClock = core.Clock()
text_baseline_evaluation_title = visual.TextStim(win=win, name='text_baseline_evaluation_title',
    text='Task finished:',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_baseline_evaluation = visual.TextStim(win=win, name='text_baseline_evaluation',
    text='Please rate your current stress level.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
rating_baseline = visual.RatingScale(win=win, name='rating_baseline', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=10, labels=['completely relaxed', ' stressed out'], scale='', markerStart='5')

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
    text='Ending Session One.',
    font='Arial',
    pos=(0, 0.1), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_baseline_end_instructions = visual.TextStim(win=win, name='text_baseline_end_instructions',
    text="(Press 'SPACE' to exit)",
    font='Arial',
    pos=(0, -0.3), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_baseline_end = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Welcome_Screen"-------
# update component parameters for each repeat
key_resp_welcome_screen.keys = []
key_resp_welcome_screen.rt = []
# keep track of which components have finished
Welcome_ScreenComponents = [text_welcome_screen, text_welcome_screen_continue, key_resp_welcome_screen]
for thisComponent in Welcome_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Welcome_ScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Welcome_Screen"-------
while continueRoutine:
    # get current time
    t = Welcome_ScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Welcome_ScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_welcome_screen* updates
    if text_welcome_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_welcome_screen.frameNStart = frameN  # exact frame index
        text_welcome_screen.tStart = t  # local t and not account for scr refresh
        text_welcome_screen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_welcome_screen, 'tStartRefresh')  # time at next scr refresh
        text_welcome_screen.setAutoDraw(True)
    
    # *text_welcome_screen_continue* updates
    if text_welcome_screen_continue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_welcome_screen_continue.frameNStart = frameN  # exact frame index
        text_welcome_screen_continue.tStart = t  # local t and not account for scr refresh
        text_welcome_screen_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_welcome_screen_continue, 'tStartRefresh')  # time at next scr refresh
        text_welcome_screen_continue.setAutoDraw(True)
    
    # *key_resp_welcome_screen* updates
    waitOnFlip = False
    if key_resp_welcome_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_welcome_screen.frameNStart = frameN  # exact frame index
        key_resp_welcome_screen.tStart = t  # local t and not account for scr refresh
        key_resp_welcome_screen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_welcome_screen, 'tStartRefresh')  # time at next scr refresh
        key_resp_welcome_screen.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_welcome_screen.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_welcome_screen.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_welcome_screen.getKeys(keyList=['space'], waitRelease=False)
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
# the Routine "Welcome_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank_Screen"-------
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
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Blank_ScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Blank_Screen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank_ScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Blank_ScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_blank_screen* updates
    if text_blank_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_blank_screen.frameNStart = frameN  # exact frame index
        text_blank_screen.tStart = t  # local t and not account for scr refresh
        text_blank_screen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_blank_screen, 'tStartRefresh')  # time at next scr refresh
        text_blank_screen.setAutoDraw(True)
    if text_blank_screen.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_blank_screen.tStartRefresh + 0.5-frameTolerance:
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
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Baseline_ScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Baseline_Screen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Baseline_ScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Baseline_ScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_baseline_screen* updates
    if text_baseline_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_baseline_screen.frameNStart = frameN  # exact frame index
        text_baseline_screen.tStart = t  # local t and not account for scr refresh
        text_baseline_screen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_baseline_screen, 'tStartRefresh')  # time at next scr refresh
        text_baseline_screen.setAutoDraw(True)
    if text_baseline_screen.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_baseline_screen.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            text_baseline_screen.tStop = t  # not accounting for scr refresh
            text_baseline_screen.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_baseline_screen, 'tStopRefresh')  # time at next scr refresh
            text_baseline_screen.setAutoDraw(False)
    
    # *text_baseline_screen_title* updates
    if text_baseline_screen_title.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_baseline_screen_title.frameNStart = frameN  # exact frame index
        text_baseline_screen_title.tStart = t  # local t and not account for scr refresh
        text_baseline_screen_title.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_baseline_screen_title, 'tStartRefresh')  # time at next scr refresh
        text_baseline_screen_title.setAutoDraw(True)
    if text_baseline_screen_title.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_baseline_screen_title.tStartRefresh + 5-frameTolerance:
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
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Blank_ScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Blank_Screen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank_ScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Blank_ScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_blank_screen* updates
    if text_blank_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_blank_screen.frameNStart = frameN  # exact frame index
        text_blank_screen.tStart = t  # local t and not account for scr refresh
        text_blank_screen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_blank_screen, 'tStartRefresh')  # time at next scr refresh
        text_blank_screen.setAutoDraw(True)
    if text_blank_screen.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_blank_screen.tStartRefresh + 0.5-frameTolerance:
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
# update component parameters for each repeat
key_resp_baseline_instructions.keys = []
key_resp_baseline_instructions.rt = []
# keep track of which components have finished
Baseline_InstructionsComponents = [text_baseline_instructions_title, text_baseline_instructions, key_resp_baseline_instructions]
for thisComponent in Baseline_InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Baseline_InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Baseline_Instructions"-------
while continueRoutine:
    # get current time
    t = Baseline_InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Baseline_InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_baseline_instructions_title* updates
    if text_baseline_instructions_title.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_baseline_instructions_title.frameNStart = frameN  # exact frame index
        text_baseline_instructions_title.tStart = t  # local t and not account for scr refresh
        text_baseline_instructions_title.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_baseline_instructions_title, 'tStartRefresh')  # time at next scr refresh
        text_baseline_instructions_title.setAutoDraw(True)
    
    # *text_baseline_instructions* updates
    if text_baseline_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_baseline_instructions.frameNStart = frameN  # exact frame index
        text_baseline_instructions.tStart = t  # local t and not account for scr refresh
        text_baseline_instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_baseline_instructions, 'tStartRefresh')  # time at next scr refresh
        text_baseline_instructions.setAutoDraw(True)
    
    # *key_resp_baseline_instructions* updates
    waitOnFlip = False
    if key_resp_baseline_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_baseline_instructions.frameNStart = frameN  # exact frame index
        key_resp_baseline_instructions.tStart = t  # local t and not account for scr refresh
        key_resp_baseline_instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_baseline_instructions, 'tStartRefresh')  # time at next scr refresh
        key_resp_baseline_instructions.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_baseline_instructions.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_baseline_instructions.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_baseline_instructions.getKeys(keyList=['space'], waitRelease=False)
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
# the Routine "Baseline_Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank_Screen"-------
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
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Blank_ScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Blank_Screen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank_ScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Blank_ScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_blank_screen* updates
    if text_blank_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_blank_screen.frameNStart = frameN  # exact frame index
        text_blank_screen.tStart = t  # local t and not account for scr refresh
        text_blank_screen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_blank_screen, 'tStartRefresh')  # time at next scr refresh
        text_blank_screen.setAutoDraw(True)
    if text_blank_screen.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_blank_screen.tStartRefresh + 0.5-frameTolerance:
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

# ------Prepare to start Routine "Countdown_Screen_10"-------
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
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Countdown_Screen_10Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Countdown_Screen_10"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Countdown_Screen_10Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Countdown_Screen_10Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_countdown* updates
    if text_countdown.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_countdown.frameNStart = frameN  # exact frame index
        text_countdown.tStart = t  # local t and not account for scr refresh
        text_countdown.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_countdown, 'tStartRefresh')  # time at next scr refresh
        text_countdown.setAutoDraw(True)
    if text_countdown.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_countdown.tStartRefresh + 10-frameTolerance:
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
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Blank_ScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Blank_Screen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank_ScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Blank_ScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_blank_screen* updates
    if text_blank_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_blank_screen.frameNStart = frameN  # exact frame index
        text_blank_screen.tStart = t  # local t and not account for scr refresh
        text_blank_screen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_blank_screen, 'tStartRefresh')  # time at next scr refresh
        text_blank_screen.setAutoDraw(True)
    if text_blank_screen.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_blank_screen.tStartRefresh + 0.5-frameTolerance:
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
routineTimer.add(300.000000)
# update component parameters for each repeat
thisExp.addData("start_baseline_measurement", time.strftime("%Y-%m-%d_%H:%M:%S"))
# keep track of which components have finished
Baseline_MeasurementComponents = [text_baseline_measurement]
for thisComponent in Baseline_MeasurementComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Baseline_MeasurementClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Baseline_Measurement"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Baseline_MeasurementClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Baseline_MeasurementClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_baseline_measurement* updates
    if text_baseline_measurement.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_baseline_measurement.frameNStart = frameN  # exact frame index
        text_baseline_measurement.tStart = t  # local t and not account for scr refresh
        text_baseline_measurement.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_baseline_measurement, 'tStartRefresh')  # time at next scr refresh
        text_baseline_measurement.setAutoDraw(True)
    if text_baseline_measurement.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_baseline_measurement.tStartRefresh + 300-frameTolerance:
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
thisExp.addData("end_baseline_measurement", time.strftime("%Y-%m-%d_%H:%M:%S"))

# ------Prepare to start Routine "Blank_Screen"-------
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
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Blank_ScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Blank_Screen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank_ScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Blank_ScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_blank_screen* updates
    if text_blank_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_blank_screen.frameNStart = frameN  # exact frame index
        text_blank_screen.tStart = t  # local t and not account for scr refresh
        text_blank_screen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_blank_screen, 'tStartRefresh')  # time at next scr refresh
        text_blank_screen.setAutoDraw(True)
    if text_blank_screen.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_blank_screen.tStartRefresh + 0.5-frameTolerance:
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

# ------Prepare to start Routine "Baseline_Evaluation"-------
# update component parameters for each repeat
rating_baseline.reset()
# keep track of which components have finished
Baseline_EvaluationComponents = [text_baseline_evaluation_title, text_baseline_evaluation, rating_baseline]
for thisComponent in Baseline_EvaluationComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Baseline_EvaluationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Baseline_Evaluation"-------
while continueRoutine:
    # get current time
    t = Baseline_EvaluationClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Baseline_EvaluationClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_baseline_evaluation_title* updates
    if text_baseline_evaluation_title.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_baseline_evaluation_title.frameNStart = frameN  # exact frame index
        text_baseline_evaluation_title.tStart = t  # local t and not account for scr refresh
        text_baseline_evaluation_title.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_baseline_evaluation_title, 'tStartRefresh')  # time at next scr refresh
        text_baseline_evaluation_title.setAutoDraw(True)
    
    # *text_baseline_evaluation* updates
    if text_baseline_evaluation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_baseline_evaluation.frameNStart = frameN  # exact frame index
        text_baseline_evaluation.tStart = t  # local t and not account for scr refresh
        text_baseline_evaluation.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_baseline_evaluation, 'tStartRefresh')  # time at next scr refresh
        text_baseline_evaluation.setAutoDraw(True)
    # *rating_baseline* updates
    if rating_baseline.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rating_baseline.frameNStart = frameN  # exact frame index
        rating_baseline.tStart = t  # local t and not account for scr refresh
        rating_baseline.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rating_baseline, 'tStartRefresh')  # time at next scr refresh
        rating_baseline.setAutoDraw(True)
    continueRoutine &= rating_baseline.noResponse  # a response ends the trial
    
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
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Blank_ScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Blank_Screen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank_ScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Blank_ScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_blank_screen* updates
    if text_blank_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_blank_screen.frameNStart = frameN  # exact frame index
        text_blank_screen.tStart = t  # local t and not account for scr refresh
        text_blank_screen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_blank_screen, 'tStartRefresh')  # time at next scr refresh
        text_blank_screen.setAutoDraw(True)
    if text_blank_screen.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_blank_screen.tStartRefresh + 0.5-frameTolerance:
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
# update component parameters for each repeat
key_resp_baseline_end.keys = []
key_resp_baseline_end.rt = []
# keep track of which components have finished
Baseline_EndComponents = [text_baseline_end, text_baseline_end_instructions, key_resp_baseline_end]
for thisComponent in Baseline_EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Baseline_EndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Baseline_End"-------
while continueRoutine:
    # get current time
    t = Baseline_EndClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Baseline_EndClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_baseline_end* updates
    if text_baseline_end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_baseline_end.frameNStart = frameN  # exact frame index
        text_baseline_end.tStart = t  # local t and not account for scr refresh
        text_baseline_end.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_baseline_end, 'tStartRefresh')  # time at next scr refresh
        text_baseline_end.setAutoDraw(True)
    
    # *text_baseline_end_instructions* updates
    if text_baseline_end_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_baseline_end_instructions.frameNStart = frameN  # exact frame index
        text_baseline_end_instructions.tStart = t  # local t and not account for scr refresh
        text_baseline_end_instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_baseline_end_instructions, 'tStartRefresh')  # time at next scr refresh
        text_baseline_end_instructions.setAutoDraw(True)
    
    # *key_resp_baseline_end* updates
    waitOnFlip = False
    if key_resp_baseline_end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_baseline_end.frameNStart = frameN  # exact frame index
        key_resp_baseline_end.tStart = t  # local t and not account for scr refresh
        key_resp_baseline_end.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_baseline_end, 'tStartRefresh')  # time at next scr refresh
        key_resp_baseline_end.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_baseline_end.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_baseline_end.status == STARTED and not waitOnFlip:
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
thisExp.addData("end_session_one", time.strftime("%Y-%m-%d_%H:%M:%S")) 

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
