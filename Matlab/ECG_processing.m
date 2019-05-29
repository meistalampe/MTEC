%% file header

% filename:     ECG_processing
% author:       dominik limbach
% date:         25.03.18

% description:  Fs= 100, channel = 7
%               -load data
%               -call ecg_filt
%               -call ecg_feature
%               -match histograms
%               -save results

%% Load Data
clc;
clear;
close all;  

% dialogbox settings
prompt = {'Enter signal name:','Enter Sampling Frequency:','Enter Channel Number:','Enter baseline name:'};
dlg_title = 'Input';
num_lines = 1;
answer = inputdlg(prompt,dlg_title,num_lines);

st = '.txt';

% answers
s1 = 'F:\GitHubRepositories\Work-\ClosedLoopVirtualRealityfortheTreatmentofPhobias\Matlab\Raw Data Archive\';
%s1 = 'C:\Users\Dominik\Desktop\GitRepositories\Work-\ClosedLoopVirtualRealityfortheTreatmentofPhobias\Matlab\Raw Data Archive\';
s2 = answer{1,1};
signalname = strcat(s1,s2,st);

b1 ='F:\GitHubRepositories\Work-\ClosedLoopVirtualRealityfortheTreatmentofPhobias\Matlab\Raw Data Archive\';
%b1 = 'C:\Users\Dominik\Desktop\GitRepositories\Work-\ClosedLoopVirtualRealityfortheTreatmentofPhobias\Matlab\Raw Data Archive\';
b2 = answer{4,1};
baselinename = strcat(b1,b2,st);

Fs = str2double(answer{2,1});
channel = str2double(answer(3,1));

% save to filepath
sLocal = 'F:\GitHubRepositories\Work-\ClosedLoopVirtualRealityfortheTreatmentofPhobias\Matlab\Save folder\';
%sLocal = 'C:\Users\Dominik\Desktop\GitRepositories\Work-\ClosedLoopVirtualRealityfortheTreatmentofPhobias\Matlab\Save folder';
sFolder = 'Results-';
sMeas = '\ECG';
filepath = strcat(sLocal,sFolder,s2,sMeas);

% load raw data
% dlmread needs a filename, the delimiter, the number of rows of the
% header, and the starting row to read

% tab separated read
% signal_data = dlmread(signalname,'\t', 3, 0);
% baseline_data = dlmread(baselinename,'\t', 3, 0);

% comma separated read
signal_data = dlmread(signalname,',', 3, 0);
baseline_data = dlmread(baselinename,',', 3, 0);

% the signal is extracted from the data matrix, channel number needed
signal = signal_data(:,channel);
nSamples = length(signal_data);

baseline = baseline_data(:,channel);
bSamples = length(baseline_data);

nSignalTime = nSamples/Fs;
bSignalTime = bSamples/Fs;  % baseline must be sampled with the same frequency

% create a timeline starting at 0 and with the length of the signal
ntime = linspace(0,nSignalTime,nSamples);
btime = linspace(0,bSignalTime,bSamples);

% signal filt and feature
% ########################################################################
s3 = '_VR';
[signal_filt, ntime_co,signal_adj] = ecg_filter(signal,ntime,Fs,filepath,s3);
% cut artifacts that fake maxima
%    signal_filt(35900:end) = [];
%    ntime_co(35900:end) = [];

[niHR,niHR_mean,nHRV,ntHRV,nsignal_norm,nRR_int,nRR_mean,nHR,nHR_min,nHR_max] = ecg_features(signal_filt,Fs,filepath,s3);
% ########################################################################

% baseline filt and feature
% ########################################################################
s3 = '_BL';
[baseline_filt, btime_co] = ecg_filter(baseline,btime,Fs,filepath,s3);

% cut artifacts that fake maxima
% baseline_filt(1:1200) = [];
% btime_co(1:1200) = [];

[biHR,biHR_mean,bHRV,btHRV,bsignal_norm,bRR_int,bRR_mean,bHR,bHR_min,bHR_max] = ecg_features(baseline_filt,Fs,filepath,s3);
% ########################################################################

% calculate min and max HR
% HR min is set to 50 bpm
RR_max = 60/50;
% HR max is set to MHR = 217 – (0.85 x Age)(miller et al 1993) , Age = med
% age of all subjects = 27
MHR = 217-(0.85 * 27);
RR_min = 60/MHR;

figure;
hold on;
subplot(2,1,1);
hist(bRR_int);
grid on;
xlim([RR_min RR_max]);
title(sprintf('avg. RR = %f s, avg. Heart Rate = %f bpm',bRR_mean, bHR));
ylabel('RR distribution');
legend ('Baseline');

subplot(2,1,2); 
hist(nRR_int);
grid on;
xlim([RR_min RR_max]);
title(sprintf('avg. RR = %f s, avg. Heart Rate = %f bpm',nRR_mean, nHR));
xlabel('sampling interval [s]');
ylabel('RR distribution');
legend ('Exposure');
hold off;

s1 = 'RR Histogram BL vs EXP';
s3 = '_VR';
savename = strcat(s1,s3);
savefig([filepath filesep savename]);
saveas(gcf, [filepath filesep savename], 'png')
% ########################################################################


%% Code Storage
% % filtering ecg
% ecgfilter = filterECG(signal,timeline ,Fs,filepath);
% % call function heartrate 
% [heartrate,MeanRR,SDNN,RMSSD,mean_heartrate,std_heartrate,heartrate_coe,peakInterval,peakInterval_time] = heartrate(ecgfilter,timeline,Fs,filepath);
% % call function ellipse
% ellipse(peakInterval_time,filepath);

% %% lomb scargle power plot
% of the RR Interval data with gaps
% The typical frequency bands of interest in HRV spectra are:
% 
% Very Low Frequency (VLF), from 3.3 to 40 mHz,
% Low Frequency (LF), from 40 to 150 mHz,
% High Frequency (HF), from 150 to 400 mHz.

% These bands approximately confine the frequency ranges of the distinct 
% biological regulatory mechanisms that contribute to HRV.
% Fluctuations in any of these bands have biological significance.

% figure;
% plomb(HRV,tHRV,'Pd',[0.95, 0.5]);

% The dashed lines denote 95
% and 50% detection probabilities.
%These thresholds measure the statistical significance of peaks. 
%The spectrum shows peaks in all three bands of interest listed above.


%% Saving Data

% Saving workspace
saveFilename = 'ECG_';
saveFilename = strcat(saveFilename,s2);
% clear runtime variables
clear dlg_title num_lines prompt 

save([filepath filesep saveFilename '.mat'], '-v7.3');
fprintf('Done.\n');
