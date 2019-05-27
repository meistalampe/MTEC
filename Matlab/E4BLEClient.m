%%
clc;
close all;
%% Establish connection to the streaming server
% 1. establish tcp connection
% 2. subscribe to all data streams
% 3. enter loop

%% Data Acquisition Loop
allData = [];
hrData = [];
hrFs = 64;
t = 30;

while connected == true
    
    while length(hrData)< t*hrFs
    % scan streams and write it to all data array
    % sort streams by tag and build stream array
    % when hrData array reached the equivalent of 3sec -> loop breaks
    end
    % if the loop ran 10 times analyze data
    %   analyze data
    %   run classification
    %
    %   if state changes
    %       adapt, run control script for robot
    %   else do nothing
    %
    %   reset data arrays and loop counter
    % else dont analyse data
end 

% running a smaller interval makes it more reactive 
% also 5 min is defined as short term and is sufficient for classification