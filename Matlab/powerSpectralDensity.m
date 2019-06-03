
% Filename : powerSpectralDensity.m
% Date     : 20.06.2016
% Author   : Manuel C. Kohl

function [] = powerSpectralDensity(signals, samplingRate, varargin)

    [nSignals, nSamples] = size(signals);
	nVarargs = length(varargin);
    for k = 1:nVarargs-1
        if strcmp(varargin{k}, 'frequencyWindow')
                frequencyWindow = varargin{k+1};
        elseif strcmp(varargin{k}, 'frequencyAxis')
                frequencyAxis = varargin{k+1};
        elseif strcmp(varargin{k}, 'magnitudeAxis')
                magnitudeAxis = varargin{k+1};
        elseif strcmp(varargin{k}, 'figureTitle')
                figureTitle = varargin{k+1};
        elseif strcmp(varargin{k}, 'signalDimension')
                signalDimension = varargin{k+1};
        elseif strcmp(varargin{k}, 'legendEntries')
                legendEntries = varargin{k+1};
        end
    end
    if ~exist('frequencyWindow', 'var')
        frequencyWindow = [samplingRate/nSamples, samplingRate/2];
    end
    if ~exist('frequencyAxis', 'var')
        frequencyAxis = 'logarithmic';
    end
    if ~exist('magnitudeAxis', 'var')
        magnitudeAxis = 'dB';
    end
    if ~exist('figureTitle', 'var')
        figureTitle = 'Power spectral density';
    end
    if ~exist('signalDimension', 'var')
        signalDimension = '1';
    end
    if ~exist('legendEntries', 'var')
        legendEntries = {};
    end

    if mod(nSamples, 2)
        signals = signals(:, 1:end-1);
        nSamples = nSamples - 1;
    end
    figure;
    hold on;
    for k = 1:nSignals
        signalFFT = fft(signals(k, :));
        nFFTsamples = round(nSamples/2)+1;
        frequencies = linspace(0, samplingRate/2, nFFTsamples);
        signalFFT = signalFFT(1:nFFTsamples);
        powerSpectralDensity = abs(signalFFT).^2/(samplingRate*nSamples);
        powerSpectralDensity(2:end-1) = 2*powerSpectralDensity(2:end-1);
        switch magnitudeAxis
            case 'linear'
                plot(frequencies, powerSpectralDensity);
            case 'dB'
                plot(frequencies, 10*log10(powerSpectralDensity));
        end
    end
    hold off;
    switch magnitudeAxis
        case 'linear'
            ylabel(['PSD [', signalDimension, '/Hz]']);
        case 'dB'
			if strcmp(signalDimension, '1')
				ylabel('PSD [dB/Hz]');
			else
				ylabel(['PSD [dB', signalDimension, '/Hz]']);
			end
    end
    xlim(frequencyWindow);
    if strcmp(frequencyAxis, 'logarithmic')
        set(gca, 'xscale', 'log');
    end
    grid on;
    title(figureTitle);
    xlabel('Frequency f [Hz]');
    if (nSignals > 1) || ~isempty(legendEntries)
        legend(legendEntries);
    end

end