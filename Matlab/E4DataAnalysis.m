%% Header
clc;
close all;
clear all;

%% Load Data

filename = 'TestData/bvp.csv';
fileID = fopen(filename);
delimiter = '\t';
% scanning the file results in a 1x1 cell
dataPackage = textscan(fileID, '%s', 'Delimiter', delimiter);
% extract the data from the Cell, str cell
dataCell = dataPackage{1,1};
%% Sort data

% data stream tags
GSR_TAG = 'E4_Gsr';
BVP_TAG = 'E4_Bvp';
IBI_TAG = 'E4_Ibi';
HR_TAG = 'E4_Hr';
TMP_TAG = 'E4_Temperature';
ACC_TAG = 'E4_Acc';

% parse data for different data streams by their respective tags
[bvpData, bvpTime] = parseDataForTag(BVP_TAG, dataCell);
[hrData, hrTime] = parseDataForTag(HR_TAG, dataCell);
[ibiData, ibiTime] = parseDataForTag(IBI_TAG, dataCell);
[gsrData, gsrTime] = parseDataForTag(GSR_TAG, dataCell);
[tmpData, tmpTime] = parseDataForTag(TMP_TAG, dataCell);
[accData, accTime] = parseDataForTag(ACC_TAG, dataCell);

%% Analyze data
% BVP
% display raw data

% figure;
% plot(bvpTime, bvpData);
% xlabel ('time');
% ylabel ('amplitude');
% title ('"Raw" BVP data');

% filtering

% low pass Butterworth filter
% cut off frequency
Fc = 7;
% sampling frequency for bvp
Fs = 64;
% generate filter coefficients
[b, a] = butter(8, Fc/ (Fs/2), 'low');
% show bode diagramm
% freqz(b, a);

% apply filter 
filtData = filter(b, a, bvpData);
% display filtered data

% figure;
% plot(bvpTime, filtData);
% xlabel ('time');
% ylabel ('amplitude');
% title ('Filtered BVP data');

% detrending
detrendData = detrend(filtData);
% feature extraction
% inverse data 
invData = -detrendData;
% find minima (as peaks in the inverse signal)
[n_pks, n_locs] = findpeaks(invData,'MinPeakDistance', 0.3*Fs, 'MinPeakHeight', 25);
% get peak values
negativePeaks = detrendData(n_locs);
% calculate avg interval between minima
diffMin = diff(n_locs);
avgDiffMin = mean(diffMin);
% derive minPeakDistance for findpeaks from the interval
% the value is changed to no significance because i decided against using
% this method
minPeakDist = avgDiffMin * 0.01;
% find systolic and diastolic peaks 
% using a threshold of 25 (might need a adaptive value later on)
threshold = 25;
% generate threshold array for displaying
displayThreshold = ones(1,length(detrendData)) .* threshold;
% find peaks
[p_pks, p_locs] = findpeaks(detrendData,'MinPeakDistance', minPeakDist, 'MinPeakHeight', threshold);
% get peak values
positivePeaks = detrendData(p_locs);
% display minima, threshold and peaks
figure;
hold on;
plot(threshold);
plot(detrendData);
plot(p_locs, positivePeaks, 'rv', 'MarkerFaceColor', 'r');
plot(n_locs, negativePeaks, 'rv', 'MarkerFaceColor', 'b');
grid on;
xlabel('samples');
ylabel('amplitude');
title('Maxima and Minima in BVP signal');
hold off;

% filter artifacts and invalid peaks
% derive a dismissing threshold from avg peak height
avgPeak = mean(p_pks);
maxPeak = avgPeak * 1.9;
indexArray = ones(1,length(p_pks));
for i = 1:length(p_pks)
    if p_pks(i) > maxPeak
        indexArray(i) = 0;
    end
end
p_pks(indexArray == 0) = [];
p_locs(indexArray == 0) = [];
% get valid peak values
positivePeaks = detrendData(p_locs);
% display artifact "free" signal
figure;
hold on;
plot(threshold);
plot(detrendData);
plot(p_locs, positivePeaks, 'rv', 'MarkerFaceColor', 'r');
grid on;
xlabel('samples');
ylabel('amplitude');
title('Peaks in BVP signal (corrected)');
hold off;

% find the systolic peaks 
i_locs = [];
i_locs_under = [];
i_locs_over = [];

iPks = zeros(1,length(p_pks));
iLocs = zeros(1,length(p_locs));
% check every min2min interval for peaks and derive the systolic peak from
% it ( as the first peak in the interval above threshold)
for k = 1:length(n_locs)
    if k == 1
       i_locs = p_locs(p_locs <= n_locs(k)); 
    elseif k > 1
        i_locs_over = p_locs(p_locs >= n_locs(k-1)); 
        i_locs_under = p_locs(p_locs <= n_locs(k));
        i_locs = intersect(i_locs_over, i_locs_under);
    elseif k == length(n_locs)
        i_locs = p_locs(p_locs >= n_locs(k-1));
    end
    
    if ~isempty(i_locs)
        iLocs(k) = i_locs(1);
        iPks(k) = p_pks(p_locs == i_locs(1));
    end
end
sysPks = iPks(iPks ~= 0);
sysLocs = iLocs(iLocs ~= 0);
% get systolic peak values
systolicPeaks = detrendData(sysLocs);
% display systolic peaks
figure;
hold on;
plot(threshold);
plot(detrendData);
plot(sysLocs, systolicPeaks, '+', 'MarkerFaceColor', 'g');
% plot(p_locs, positivePeaks, '*', 'MarkerFaceColor', 'r');
plot(n_locs, negativePeaks, 'v', 'MarkerFaceColor', 'b');
grid on;
xlabel('samples');
ylabel('amplitude');
title('Systolic Peaks in BVP signal');
hold off;

% calculate distances between peeks = ibi
ibi = diff(sysLocs);
ibiTime = ibi./Fs;
figure;
histogram(ibiTime);
% check ibi validity (filter)
minHr = 50;
maxHr = 200;
minInterval = 60/ maxHr;
maxInterval = 60/ minHr;
ibiTime(ibiTime >= maxInterval) = [];
ibiTime(ibiTime <= minInterval) = [];
figure;
histogram(ibiTime);
xlabel('time [s]');
ylabel('n');
meanIbi = mean(ibiTime);
str = {'Mean Ibi:', num2str(meanIbi) };
annotation('textbox', [0.15,0.8,0.1,0.1],...
           'String', str)
title('IBI distribution');

% calculate HR from IBI
meanHr = 60/meanIbi; 

