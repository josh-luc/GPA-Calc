import sys

def main(a, b, c, d):
    grade = {'A':4.0, 
            'A-':3.66, 
            'B+':3.33, 
            'B':3.0, 
            'B-':2.66, 
            'C+':2.33, 
            'C':2.0, 
            'C-':1.66, 
            'D+':1.33, 
            'D':1.00, 
            'D-':.66, 
            'F':0.00}
    
    y = sum([grade[sys.argv[1].upper()], 
    grade[sys.argv[2].upper()], 
    grade[sys.argv[3].upper()], 
    grade[sys.argv[4].upper()]]) / 4
    
    
    print("My GPA is", f'{y:.2f}')

main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])