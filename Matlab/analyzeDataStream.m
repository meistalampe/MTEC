function [tFeatures, fFeatures, nlFeatures] = analyzeDataStream(streamTag, streamData, streamTime)
    if ~isempty(streamData)
        switch(streamTag)
            case 'E4_Gsr'

            case 'E4_Bvp'
                
                %% RAW DATA

%                 figure;
%                 plot(streamTime, streamData);
%                 xlabel ('time');
%                 ylabel ('amplitude');
%                 title ('"Raw" BVP data');
%                 
%                 Fs = 64;                    % Sampling frequency
%                 % T = 1/Fs;                   % Sample time
%                 L = length(streamData);        % Length of signal
%                 % t = streamTime;                % Time vector
%                 NFFT = 2^nextpow2(L);       % Next power of 2 from length of y
%                 y = bvpData;
%                 Y = fft(y,NFFT)/L;
%                 f = Fs/2*linspace(0,1,NFFT/2+1);
% 
%                 % Plot single-sided amplitude spectrum.
%                 figure;
%                 plot(f,2*abs(Y(1:NFFT/2+1))) 
%                 title('Single-Sided Amplitude Spectrum of y(t)')
%                 xlabel('Frequency (Hz)')
%                 ylabel('|Y(f)|')
                
                %% PREPROCESSING

                %% filtering
                
                % low pass Butterworth filter
                % cut off frequency
                Fc = 7;
                % sampling frequency
                Fs = 64;
                % generate filter coefficients
                [b, a] = butter(8, Fc/ (Fs/2), 'low');
                % show bode diagramm
                % freqz(b, a);

                % apply filter 
                filtData = filter(b, a, streamData);
                % display filtered data

                figure;
                plot(streamTime, filtData);
                xlabel ('time');
                ylabel ('amplitude');
                title ('Filtered BVP data');

                %% detrending
                detrendData = detrend(filtData);
                
                %% Feature Extraction
                
                % locate blood volume pulse peaks
                % inverse data 
                invData = -detrendData;
                % find minima (as peaks in the inverse signal)
                [n_pks, n_locs] = findpeaks(invData,'MinPeakDistance', 0.3*Fs, 'MinPeakProminence', 25);
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
                plot(displayThreshold);
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
                maxPeak = avgPeak * 5;
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

                % find the "systolic" peaks 
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
                    end

                    if ~isempty(i_locs)
                        iLocs(k) = i_locs(1);
                        iPks(k) = p_pks(p_locs == i_locs(1));
                    end
                end

                i_locs = p_locs(p_locs >= n_locs(k));

                if ~isempty(i_locs)
                    iLocs(k+1) = i_locs(1);
                    iPks(k+1) = p_pks(p_locs == i_locs(1));
                end

                sysPks = iPks(iPks ~= 0);
                sysLocs = iLocs(iLocs ~= 0);
                % get "systolic" peak values
                systolicPeaks = detrendData(sysLocs);
                % display "systolic" peaks
                figure;
                hold on;
                plot(displayThreshold);
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
                ibiT = ibi./Fs;
                
                unfilteredIbi = length(ibiT);
                
                figure;
                histogram(ibiT);
                xlabel('time [s]');
                ylabel('n');
                meanIbi = mean(ibiT);
                str = {'Mean Ibi:', num2str(meanIbi) };
                annotation('textbox', [0.15,0.8,0.1,0.1],...
                           'String', str)
                title('IBI distribution (unfiltered)');
                % check ibi validity (filter)
                minHr = 50;
                maxHr = 200;
                minInterval = 60/ maxHr;
                maxInterval = 60/ minHr;
                ibiT(ibiT >= maxInterval) = [];
                ibiT(ibiT <= minInterval) = [];
                
                filteredIbi = length(ibiT);
                throwOut = unfilteredIbi - filteredIbi;
                if throwOut > 0
                    throwPerc = (throwOut / unfilteredIbi)*100;
                else
                    throwPerc = 0;
                end
                
                figure;
                histogram(ibiT);
                xlabel('time [s]');
                ylabel('n');
                meanIbi = mean(ibiT);                       % equals AVNN
                str = {'Mean Ibi:', num2str(meanIbi) };
                annotation('textbox', [0.15,0.8,0.1,0.1],...
                           'String', str)
                title('IBI distribution (filtered)');

                %% FEATURES
                
                %% Time Domain
                
                % AVNN, average of all NN intevals (avg of als IBI)
                AV_IBI = meanIbi * 1000;
                AV_Hr = 60/meanIbi;
                % SDNN, standard deviation of all NN intervals (all IBIs)
                SD_IBI = std(ibiT);
                % RMSSD 
                N = length(ibiT)-1;
                
                SS = 0;
                
                for m = 1:(N)
                    SS = SS + (ibiT(m+1) - ibiT(m))^2;
                end
                RMSSD = sqrt(SS/N);
          
                %% Frequency Domain
                % band power approach
                y = ibiT;   
                L =length(y);
                NFFT = 2^nextpow2(L); % Next power of 2 from length of y
                Y = fft(y,NFFT)/L;
                f = Fs/2*linspace(0,1,NFFT/2+1);

                % Plot single-sided amplitude spectrum.
                figure;
                plot(f,2*abs(Y(1:NFFT/2+1))) 
                title('Single-Sided Amplitude Spectrum of y(t)')
                xlabel('Frequency (Hz)')
                ylabel('|Y(f)|')
                
                % create signal bands by filtering
                % total spectral power of all NN intervals below 0,4 Hz
                S_POW = bandpower(y);
                
                T_POW = bandpower(y, Fs, [0 0.4]);
                T_PERC = 100* (T_POW/S_POW);
                
                UVLF_POW = bandpower(y, Fs, [0 0.003]);
                UVLF_PERC = 100* (UVLF_POW/T_POW);
                
                VLF_POW = bandpower(y, Fs, [0.003 0.04]);
                VLF_PERC = 100* (VLF_POW/T_POW);
                
                LF_POW = bandpower(y, Fs, [0.04 0.15]);
                LF_PERC = 100* (LF_POW/T_POW);
                
                HF_POW = bandpower(y, Fs, [0.15 0.4]);
                HF_PERC = 100* (HF_POW/T_POW);
                
                LF_HF = LF_POW/HF_POW;
                
                % lomb scargle
                HRV = 1./ibiT;
                sum = 0;
                t = zeros(1,length(ibiT));
                
                for i = 1:length(ibiT)
                    
                    sum = sum + ibiT(i);
                    t(i) = sum;
                end
                figure;
                plot(t,HRV);
                
                [pxx, f] = plomb(HRV,t);
                figure;
                plot(f,pxx)
                xlabel('Frequency')
                title('Power Spectrum')
                grid
                
                %powerSpectralDensity(ibiT, 64)
                figure;
                
                tHRV = t;
                plomb(HRV,tHRV,'Pd',[0.95, 0.5]);
                
                tFeatures = [throwPerc, AV_IBI, SD_IBI, RMSSD, AV_Hr];
                %fFeatures = [S_POW, T_POW, T_PERC, UVLF_POW, UVLF_PERC, VLF_POW, VLF_PERC, LF_POW, LF_PERC, HF_POW, HF_PERC, LF_HF];
                fFeatures = [pxx, f];
                nlFeatures = [];
                
            case 'E4_Ibi'

            case 'E4_Hr'

            case 'E4_Temperature'

            case 'E4_Acc'

        end
    else
        features = [];
    end
            
end