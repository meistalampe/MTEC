function [iHR,iHR_mean,HRV,tHRV,signal_norm,RR_int,RR_mean,aHR,aHR_min,aHR_max] = ecg_features(signal,Fs,filepath,s3)


% ########################################################################
% normalize
% ########################################################################
signal(signal >= 1) = 1;
signal(signal <= -0.2) = -0.2;

signal_min = min(signal);
signal_max = max(signal);
signal_mag = abs(signal_min-signal_max);
signal_norm = (signal - signal_min)./signal_mag;


% square
% signal_square = signal_norm .^2;

%% Feature extraction own

[pks,locs] = findpeaks(signal_norm,'MinPeakProminence',0.25,'MinpeakDistance', 31);
%[pks,locs] = findpeaks(signal_norm,'MinPeakHeight',0.5,'MinpeakDistance', 45);

figure;
hold on;
plot(signal_norm);
plot(locs,pks,'rv','MarkerFaceColor','r');
%plot(locs,pks,'o');
title 'R-Peaks'
xlabel 'samples'
ylabel 'normalized amplitude'
hold off;

s1 = 'R-Peaks';
savename = strcat(s1,s3);
savefig([filepath filesep savename]);
saveas(gcf, [filepath filesep savename], 'png');

%% RR-distance

signal_diff = diff(locs);
RR_int = signal_diff ./Fs ; % time

% calculate min and max HR
% HR min is set to 50 bpm
RR_max = 60/50;
% HR max is set to MHR = 217 – (0.85 x Age)(miller et al 1993) , Age = med
% age of all subjects = 27
%MHR = 217-(0.85 * 27);
MHR = 220-27;
RR_min = 60/MHR;

counter = 0;
locs_time = locs./Fs;

for i = 1:length(RR_int)
    if RR_int(i) <= RR_min || RR_int(i) >= RR_max
        RR_int(i) = -1;
        locs_time(i) = -1;
        counter = counter+1;        
    end
end
RR_int(RR_int == -1) = [];
locs_time(locs_time == -1) = [];

% average HR
RR_mean = mean(RR_int);     % time
aHR = 60/ RR_mean;
aHR_min = 60/ max(RR_int);
aHR_max = 60/ min(RR_int);
%% instantaneous HR
iHR = zeros(1,length(RR_int));
for i = 1:length(RR_int)
iHR(i) = 60 / RR_int(i);
end

iHR_mean = mean(iHR);
figure;
hold on;
plot(iHR);
title 'iHR [bpm]'
xlabel 'RR samples'
ylabel 'iHR'
hold off;

s1 = 'iHR (bpm)';
savename = strcat(s1,s3);
savefig([filepath filesep savename]);
saveas(gcf, [filepath filesep savename], 'png');

% Derive the HRV signal
tHRV = locs_time(2:end);
HRV = 1./RR_int;

% Plot the signals
figure;
hold on;
plot(tHRV,HRV)
title('Heart Rate Variation');
xlabel('Time[s]')
ylabel('HRV [Hz]')

s1 = 'Heart Rate Variation';
savename = strcat(s1,s3);
savefig([filepath filesep savename]);
saveas(gcf, [filepath filesep savename], 'png');

figure;
hist(RR_int);
title 'RR interval Histogram';
grid on;
xlabel('sampling interval [s]');
ylabel('RR distribution');

s1 = 'RR interval Histogram';
savename = strcat(s1,s3);
savefig([filepath filesep savename]);
saveas(gcf, [filepath filesep savename], 'png');


end
