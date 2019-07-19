import numpy as np


def main():
    pass


def feature_extraction_time_domain(ibi_data):
    # SDNN = standard deviation of the NN interval
    #   - the square root of variance
    #   - depending on record length
    #   - therefore only appropriate measure for comparing recordings of equal length
    #   - rec lengths 5 min, 24 h
    tf_sdnn = np.std(ibi_data)

    # RMSSD = square root of the mean squared differences of successive NN intervals

    return tf_sdnn


def feature_extraction_frequency_domain():
    pass


def feature_extraction_non_linear():
    pass


if __name__ == '__main__':
    main()
