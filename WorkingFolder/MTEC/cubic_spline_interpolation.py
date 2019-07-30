import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt


def main():
    pass


def csi_resampling(data, time, sampling_frequency, resampling_frequency, interpolation_mode='cubic'):
    # 7 Hz recommended by GD Clifford
    print('rec length [method=sum] = ', sum(time))
    print('rec length [method=len/fs] = ', round(len(time) / sampling_frequency))
    new_num_of_samples = round(len(time) / sampling_frequency) * resampling_frequency
    new_time = np.linspace(time[0], time[-1], new_num_of_samples)

    f = interpolate.interp1d(data, time, kind=interpolation_mode)
    new_data = f(new_time)

    return new_data, new_time


if __name__ == '__main__':
    main()
