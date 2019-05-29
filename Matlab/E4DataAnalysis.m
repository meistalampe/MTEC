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
hrv_features = analyzeDataStream(BVP_TAG, bvpData, bvpTime);

