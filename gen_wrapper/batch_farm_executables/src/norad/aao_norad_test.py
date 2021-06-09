#!/bin/python
#cython: language_level=3

"""
This is a mock generator for debugging on local machines where aao_norad.exe is not able to run correctly
This generates a simulated lund file for debugging purposes and is not needed for production
"""
import os
import sys

def test_output_maker():
    outfile = open("aao_norad.lund","w")
    string = """4 1 1 0 0   0.34975770255085675                0   1.27957070      0.407428980      0.620943069    
           1  -1.00000000               1          11           0           0 -0.546691775      0.290380269       9.95983887       9.97905731       5.10999991E-04   0.00000000       0.00000000      -2.35186768    
           2   1.00000000               1        2212           0           0  0.312461555       1.01394057E-02  0.590677738       1.15172958      0.938000023       0.00000000       0.00000000      -2.35186768    
           3           0           1          22           0           0   2.47165710E-02  -3.67661417E-02  -3.89144048E-02   5.89660034E-02           0   0.00000000       0.00000000      -2.35186768    
           4           0           1          22           0           0  0.209512293     -0.263751745       8.83979574E-02  0.348245025               0   0.00000000       0.00000000      -2.35186768    
 4 1 1 0 0   0.34969677824876227                0   1.18793380      0.285726696      0.435538292    
           1  -1.00000000               1          11           0           0  0.129613951      0.506956875       10.1509848       10.1644621       5.10999991E-04   0.00000000       0.00000000      -4.42704010    
           2   1.00000000               1        2212           0           0 -0.153797477     -0.533856511      0.230632022       1.11431241      0.938000023       0.00000000       0.00000000      -4.42704010    
           3           0           1          22           0           0  -3.75631489E-02  -2.23568827E-03   8.58451426E-03   3.85964029E-02           0   0.00000000       0.00000000      -4.42704010    
           4           0           1          22           0           0   6.17466457E-02   2.91353241E-02  0.209799245      0.220629171               0   0.00000000       0.00000000      -4.42704010    
 4 1 1 0 0   0.27722516322069995                0   1.37978995      0.392750978      0.755182266    
           1  -1.00000000               1          11           0           0  0.370223373      0.476824373       9.82629204       9.84481812       5.10999991E-04   0.00000000       0.00000000     -0.822635651    
           2   1.00000000               1        2212           0           0 -0.527823925     -0.107555121      0.581361771       1.22800231      0.938000023       0.00000000       0.00000000     -0.822635651    
           3           0           1          22           0           0  -2.20516622E-02  -4.95023280E-02   4.29314561E-02   6.91365749E-02           0   0.00000000       0.00000000     -0.822635651    
           4           0           1          22           0           0  0.179653794     -0.319770515      0.149416685      0.396048009               0   0.00000000       0.00000000     -0.822635651"""
    outfile.write(string)
    outfile.close()

if __name__ == "__main__":
    # The following is needed since an executable does not have __file__ defined, but when working in interpreted mode,
    # __file__ is needed to specify the relative file path of other packages. In principle strict relative 
    # path usage should be sufficient, but it is easier to debug / more robust if absolute.
    try:
        __file__
    except NameError:
        full_file_path = sys.executable #This sets the path for compiled python
    else:
        full_file_path = os.path.abspath(__file__) #This sets the path for interpreted python

    test_output_maker()