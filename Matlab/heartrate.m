function [ heartrate,MeanRR,SDNN,RMSSD,mean_heartrate,std_heartrate,heartrate_coe,peakInterval,peakInterval_time ] = heartrate(signal,time,Fs)
% You need the kernel.mat data to run this function!! 
% This function finds R wave peaks in ecg signal and calculates the heartrate signal.
% It analyses the RR Intervals with by doing a lomb spectral analysis.



% % load kernel
% load('kernel.mat','kernelqrs_norm');
% 
% % create logistic sigmoid function
% tu = quantile(signal, 0.99);
% tl = quantile(abs(signal), 0.5);
% f = @(x) 1./(1 + exp(-1e-4*(tu-tl)*(x-tu)));
% 
% xx = linspace(-1000, 1000, 1000);
% ff = f(xx);
% figure; plot(xx, ff);
% grid on;
% title 'logistic function'
% 
% % use logistic sigmoid function
% ecgRspikes = f(conv(signal, kernelqrs_norm, 'same'));
% figure;
% hold on;
% plot(time,signal);
% plot(time,ecgRspikes*max(signal));
% title ''
% xlabel 'Samples';
% ylabel 'voltage [\muV]';
% legend('signal','signal after using kernel and logistic fkt')
% hold off;
% grid on;

% find all R wavemagnitudes
[pks,locs_Rwave] = findpeaks(signal,'MinPeakHeight',0.9,...
                                    'MinPeakDistance',150);
 
                                                                                       
% check if all amplitudes were found  
% -------------------------------------
figure;
hold on 
plot(signal)
plot(locs_Rwave,signal(locs_Rwave),'rv','MarkerFaceColor','r')
grid on
legend('ECG Signal',' R waves')
xlabel('Samples')
ylabel('R waves')
title('R waves')


% locs_Rwave in time domain
locs_time = locs_Rwave ./ Fs;

% calculate the distances between the R waves in Samples
peakInterval = diff(locs_Rwave);
peakInterval_time = diff(locs_time);

% create a vector with heartrate data
heartrate_calc = zeros(1,length(peakInterval));

% calculate the heartrate
for u = 1:length(peakInterval)
    
    heartrate_calc(u) = (Fs/peakInterval(u))*60;
end


% create a vector heartrateSample
heartrateSample  = zeros(1,length(peakInterval));

% position the calculated heartarte value to the right sample
for v = 1:length(peakInterval)
    
    heartrateSample(v) = ceil(locs_Rwave(v) + (peakInterval(v)/2));
end



% create vector with the same length as trial with the heartrate data
% fill it with the heartrate values at the right sample points

 counter = 1;
 heart_int = zeros(1,length(signal));
 
 
 for z = 1:max(heartrateSample)
     
    if (heartrateSample(counter) == z)
     
       heart_int(z) = heartrate_calc(counter);
       counter = counter +1;
        
    end   
 end
 
 valuepositions = find(heart_int > 0);
 first_position = valuepositions(1);
 last_position  = valuepositions(end);
 
 % Fill the rest of the vector with interpolated values for displaying
for l =  first_position : last_position

    % values smaller than 50 b/m  -> bradykardie (heart_int(l) < 50)
    if heart_int(l+1) == 0   
        
        heart_int(l+1) = heart_int(l);
    end

end


heartrate = heart_int;



%% lomb scargle power plot
% of the RR Interval data with gaps
% The typical frequency bands of interest in HRV spectra are:
% 
% Very Low Frequency (VLF), from 3.3 to 40 mHz,
% Low Frequency (LF), from 40 to 150 mHz,
% High Frequency (HF), from 150 to 400 mHz.

% These bands approximately confine the frequency ranges of the distinct 
% biological regulatory mechanisms that contribute to HRV.
% Fluctuations in any of these bands have biological significance.


% Derive the HRV signal
tHRV = locs_time(2:end);
HRV = 1./peakInterval_time;


% Plot the signals
figure
a1 = subplot(2,1,1); 
plot(time,signal,'b',locs_time,pks,'*r')
grid
a2 = subplot(2,1,2);
plot(tHRV,HRV)
grid
xlabel(a2,'Time(s)')
ylabel(a1,'ECG')
ylabel(a2,'HRV (Hz)')


figure;
hist(peakInterval_time);
title 'histogram of the peak separations in seconds';
grid on;
xlabel('Sampling interval (s)');
ylabel('RR distribution');


figure;
plomb(HRV,tHRV,'Pd',[0.95, 0.5]);


% The dashed lines denote 95
% and 50% detection probabilities.
%These thresholds measure the statistical significance of peaks. 
%The spectrum shows peaks in all three bands of interest listed above.



%% statistic values RR Interval

% heartrate mean value and standard deviation of NN(RR) intervals(SDNN)
MeanRR = mean(peakInterval);
SDNN = std(peakInterval);

% root mean square of successive differences (RMSSD)
% big variation of HR often shows artefacts, so the HR changes much 
% from beat to beat
% the RMSSD is very sensitive for artefacts. If the standard deviation is
% low but the RMSSD is high, you better check your signal for artefacts.

N = length(peakInterval)-1 ;

RMSSD = 0;
for k = 1:N
    
    RMSSD = RMSSD + (peakInterval(k+1) - peakInterval(k))^2; 
    
end

RMSSD =sqrt( (1/N) * RMSSD);



% plotting heartrate of the required trial
% -----------------------------------------

start_stop = find(heartrate >0);
start = start_stop(3)/512;
stop = start_stop(end-2)/512;

% % heartrate befor median filtering
% figure;
% plot(trial_time,heartrate);
% title 'heartrate variability';
% xlabel 'time [sec]';
% ylabel 'heartrate [beats/min]';
% xlim([start stop]);


% filtered heartrate with median filter 

figure;
% median filtering  1500 ca 3 sec.
heartrate = medfilt1(heartrate,1500);
plot(time,heartrate);
title 'heartrate variability';
xlabel 'time [sec]';
ylabel 'heartrate [beats/min]';
xlim([start stop]);


%% statistic values heartrate
% calculate the variation coefficient,mean value and standard deviation of the heartrate
mean_heartrate = mean(heartrate);
std_heartrate = std(heartrate);
heartrate_coe = (std_heartrate * 100) /mean_heartrate;




end

