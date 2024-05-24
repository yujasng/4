# TODO 1: Import numpy
import numpy as np

def apply_filter(input_, filter_):
    # TODO 2: Define the output as a zero array with the appropriate size
    lenth  = len(input_)-len(filter_) + 1
    output = np.zeros(lenth)
    print (output[0])
    # TODO 3: Apply the filter to the input using a loop
    for i in len(output):
        for j in len(filter_):
            output[i] = input_[i+j]*filter_[j]


    return output
    
if __name__ == '__main__':

    # Define the input and filter
    input_ = np.array([1, 2, 3, 4, 5])
    filter_ = np.array([1, 2, 3])
    
    # Print the output
    output = apply_filter(input_, filter_)
    print(output)
    