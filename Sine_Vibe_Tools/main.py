"""
Python script to evaluate accelerometers that measured more output than expected.

This is for sine vibration of structures.
"""

from pandas import read_csv
import plotting


def read_data_file(filename):
    """
    Function that reads input file and returns the accel reading data in form of a dataframe.
    """
    df = read_csv(filename, sep='\t', lineterminator='\n', header=[0, 1], index_col=0)
    return df

def get_design_loads(fname):  # passes back a list of 51 loads for each accel
    with open('design_loads.txt', 'r') as text_file:
        loads_list = text_file.read().split('\n')
        loads_list = loads_list[0:-1]
        loads_list = [float(load) for load in loads_list]
    return loads_list

def compute_Overtest_ratio(data_df, loads_list):
    peak_val =[]
    ratio = []
    for i in range(10):
        peak_val.append(max(data_df.ix[:, i].tolist()))
        ratio.append(peak_val[i] / loads_list[i])

    peak_val = ["%.2lf" % p for p in peak_val] # turned to strings
    ratio = ["%.2lf" % r for r in ratio] # turned to strings
    peak_axis = ['X','X','X','X','Z','Y','Z','Z','Z','Y']
    return peak_val, ratio, peak_axis

def main():
    fname_data = 'Sine_Overtest_Data.txt'
    fname_design_loads = 'design_loads.txt'

    data_df = read_data_file(fname_data)  # create data object that will keep all variables from file, raw and processed
    loads_list = get_design_loads(fname_design_loads)
    peak_val, ratio, peak_axis = compute_Overtest_ratio(data_df, loads_list)
    accel_names = data_df.columns.tolist()
    for i in range(10):
        print(str(accel_names[i]) + " overtested during " +peak_axis[i]+ " axis vibe with, a " + peak_val[i]
              + " [g] peak acceleration, which is " + ratio[i]+ " times the design load.")

    plotting.make_plots(data_df)

if __name__ == '__main__':
    main()