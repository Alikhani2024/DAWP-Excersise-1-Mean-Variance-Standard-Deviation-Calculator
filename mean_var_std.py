import numpy as np 

def calculate(list):

    if len(list) != 9 :
        raise ValueError("List must contain nine numbers.")

    list = np.array(list).reshape((3,3))

    calculations = {}

    calculations['Mean'] = [list.mean(axis=0).tolist(), list.mean(axis=1).tolist(), np.mean(list).tolist()]
    calculations['Variance']= [list.var(axis =0).tolist(),list.var(axis =1).tolist(),np.var(list).tolist()] 
    calculations['Standard Deviation'] = [list.std(axis =0).tolist(),list.std(axis =1).tolist(),np.std(list).tolist()]   
    calculations['Max'] = [list.max(axis =0).tolist(),list.max(axis =1).tolist(),np.max(list).tolist()] 
    calculations['Min']= [list.min(axis =0).tolist(),list.min(axis =1).tolist(),np.min(list).tolist()] 
    calculations['Sum'] = [list.sum(axis =0).tolist(),list.sum(axis =1).tolist(),np.sum(list).tolist()]


    return calculations
