  
#!/usr/bin/env python3

"""
This is a mock generator for debugging on local machines where aao_norad.exe is not able to run correctly
This generates a simulated lund file for debugging purposes and is not needed for production
"""
import os
import sys

def test_output_maker():
    outfile = open("aao_rad.lund","w")
    string = """ 4 1 1 0 0   0.20682727240518203                0   1.43736362      0.309304863      0.797161102    
           1  -1.00000000               1          11           0           0   3.28156315E-02 -0.533623636       9.78824902       9.80283928       5.10999991E-04   0.00000000       0.00000000      0.866011381    
           2   1.00000000               1        2212           0           0  0.151767194      0.349769771      0.295927584       1.05488813      0.938000023       0.00000000       0.00000000      0.866011381    
           3   0.00000000               1         111           0           0 -0.189823598      0.193657190      0.197113812      0.361369610      0.134900004       0.00000000       0.00000000      0.866011381    
           4   0.00000000               1          22           0           0   5.24078077E-03  -9.80331097E-03  0.318709582      0.318903387       0.00000000       0.00000000       0.00000000      0.866011381    
 4 1 1 0 0    6.9386214984624398E-002           0   2.58513165      0.432674199       3.32395363    
           1  -1.00000000               1          11           0           0  0.382575661      0.387576163       7.25563765       7.27604675       5.10999991E-04   0.00000000       0.00000000      -2.05556583    
           2   1.00000000               1        2212           0           0 -0.406211376     -0.862846851      0.624544621       1.47628331      0.938000023       0.00000000       0.00000000      -2.05556583    
           3   0.00000000               1         111           0           0   6.47804737E-02  0.483335286       1.94552660       2.01024437      0.134900004       0.00000000       0.00000000      -2.05556583    
           4   0.00000000               1          22           0           0  -4.11448255E-02  -8.06467421E-03  0.774291754      0.775426090       0.00000000       0.00000000       0.00000000      -2.05556583    
 4 1 1 0 0   0.22834941329886974                0   1.25223291      0.203668624      0.475435257    
           1  -1.00000000               1          11           0           0  0.271135777      0.347745210       10.1149578       10.1245651       5.10999991E-04   0.00000000       0.00000000      -1.07642531    
           2   1.00000000               1        2212           0           0 -0.374826699     -0.370121479      0.257558584       1.10619545      0.938000023       0.00000000       0.00000000      -1.07642531    
           3   0.00000000               1         111           0           0  0.103757463       2.24575959E-02  0.144861996      0.224617735      0.134900004       0.00000000       0.00000000      -1.07642531    
           4   0.00000000               1          22           0           0  -6.65397092E-05  -8.13178849E-05   8.26219469E-02   8.26220140E-02   0.00000000       0.00000000       0.00000000      -1.07642531    
 4 1 1 0 0   0.27955276481239638                0   1.69620502      0.774991095       1.47774696    
           1  -1.00000000               1          11           0           0  0.791025996     -0.199727312       9.08569717       9.12225342       5.10999991E-04   0.00000000       0.00000000      -1.73947155    
           2   1.00000000               1        2212           0           0  -1.05200374       7.38094300E-02  0.778982997       1.61208439      0.938000023       0.00000000       0.00000000      -1.73947155    
           3   0.00000000               1         111           0           0  0.260835260      0.127203539      0.715578437      0.783878624      0.134900004       0.00000000       0.00000000      -1.73947155    
           4   0.00000000               1          22           0           0   1.42283738E-04  -1.28565135E-03   1.97415482E-02   1.97838787E-02   0.00000000       0.00000000       0.00000000      -1.73947155    
 4 1 1 0 0   0.47501165899884090                0   1.29235411      0.715093672      0.802464485    
           1  -1.00000000               1          11           0           0  -2.01921687E-02 -0.812042296       9.76380539       9.79753590       5.10999991E-04   0.00000000       0.00000000     -0.255496264    
           2   1.00000000               1        2212           0           0  0.221395344      0.600529194      0.849214375       1.41797674      0.938000023       0.00000000       0.00000000     -0.255496264    
           3   0.00000000               1         111           0           0 -0.199250922      0.210914701      -1.19855478E-02  0.320198983      0.134900004       0.00000000       0.00000000     -0.255496264    
           4   0.00000000               1          22           0           0   0.00000000       0.00000000       9.99999975E-06   9.99999975E-06   0.00000000       0.00000000       0.00000000     -0.255496264    
 4 1 1 0 0   0.31982689923953794                0   1.16057193      0.219630420      0.366053581    
           1  -1.00000000               1          11           0           0 -0.389267623      0.245782837       10.2235870       10.2339468       5.10999991E-04   0.00000000       0.00000000      0.156221867    
           2   1.00000000               1        2212           0           0  0.198901176      -8.81260782E-02  0.327117413       1.01694632      0.938000023       0.00000000       0.00000000      0.156221867    
           3   0.00000000               1         111           0           0  0.190920740     -0.157449394       4.99325320E-02  0.286238343      0.134900004       0.00000000       0.00000000      0.156221867    
           4   0.00000000               1          22           0           0   0.00000000       0.00000000       9.99999975E-06   9.99999975E-06   0.00000000       0.00000000       0.00000000      0.156221867    
 4 1 1 0 0   0.21198737049120359                0   1.47917056      0.351898879      0.884860992    
           1  -1.00000000               1          11           0           0  0.135283604     -0.551312983       9.69854069       9.71513939       5.10999991E-04   0.00000000       0.00000000      -2.14532900    
           2   1.00000000               1        2212           0           0  0.319028229      0.467192024      0.652367830       1.27494121      0.938000023       0.00000000       0.00000000      -2.14532900    
           3   0.00000000               1         111           0           0 -0.455989987       8.80281180E-02  0.248187900      0.543572485      0.134900004       0.00000000       0.00000000      -2.14532900    
           4   0.00000000               1          22           0           0   0.00000000       0.00000000       9.99999975E-06   9.99999975E-06   0.00000000       0.00000000       0.00000000      -2.14532900"""
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