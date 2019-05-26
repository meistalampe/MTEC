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

% parse data 
[bvpData, bvpTime] = parseDataForTag(BVP_TAG, dataCell);
[hrData, hrTime] = parseDataForTag(HR_TAG, dataCell);
[ibiData, ibiTime] = parseDataForTag(IBI_TAG, dataCell);
[gsrData, gsrTime] = parseDataForTag(GSR_TAG, dataCell);
[tmpData, tmpTime] = parseDataForTag(TMP_TAG, dataCell);
[accData, accTime] = parseDataForTag(ACC_TAG, dataCell);

%% Analyze data

% bvp
% figure;
% plot(bvpTime, bvpData);
% xlabel ('time');
% ylabel ('amplitude');
% title ('"Raw" BVP data');
% filter signal
Fc = 7;
Fs = 64;

[b, a] = butter(8, Fc/ (Fs/2), 'low');
% freqz(b, a);

filtData = filter(b, a, bvpData);
% figure;
% plot(bvpTime, filtData);
% xlabel ('time');
% ylabel ('amplitude');
% title ('Filtered BVP data');
detrendData = detrend(filtData);
% find inv peaks aka minima
invData = -detrendData;
[n_pks, n_locs] = findpeaks(invData,'MinPeakDistance', 0.3*Fs, 'MinPeakHeight', 25);
negativePeaks = detrendData(n_locs);
% calculate avg interval between minima
diffMin = diff(n_locs);
avgDiffMin = mean(diffMin);

minPeakDist = avgDiffMin * 0.01;
% find peaks
threshold = ones(1,length(detrendData)) .* 25;
[p_pks, p_locs] = findpeaks(detrendData,'MinPeakDistance', minPeakDist, 'MinPeakHeight', 25);
positivePeaks = detrendData(p_locs);

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

positivePeaks = detrendData(p_locs);

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

% find the first peak (systolic) in every Min to Min interval 

i_locs = [];
i_locs_under = [];
i_locs_over = [];

iPks = zeros(1,length(p_pks));
iLocs = zeros(1,length(p_locs));

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

systolicPeaks = detrendData(sysLocs);

figure;
hold on;
plot(threshold);
plot(detrendData);
plot(sysLocs, systolicPeaks, 'rv', 'MarkerFaceColor', 'r');
grid on;
xlabel('samples');
ylabel('amplitude');
title('Systolic Peaks in BVP signal');
hold off;

% % calculate distances between peeks = ibi
ibi = diff(p_locs);
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

