import numpy as np

def calculate(list):

    # raising exception is list length is not 9
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    # for storing result
    calculations = {}

    # reshaping
    arr = np.array(list).reshape(3, 3)

    # mean

    m_axis_0 = np.mean(arr,axis=0).tolist()

    m_axis_1 = np.mean(arr,axis=1).tolist()

    mean = np.mean(arr)

    # storing mean in result dictionary
    calculations['mean'] = [m_axis_0,m_axis_1,mean]


    # variance
    v_axis_0 = np.var(arr,axis=0).tolist()
    v_axis_1 = np.var(arr,axis=1).tolist()
    var = np.var(arr)
    # storing result
    calculations['variance'] = [v_axis_0,v_axis_1,var]


    # std dev
    s_axis_0 = np.std(arr,axis=0).tolist()
    s_axis_1 = np.std(arr,axis=1).tolist()
    stdDev = np.std(arr)
    # storing result
    calculations['standard deviation'] = [s_axis_0,s_axis_1,stdDev]


    # max
    max_0 = np.max(arr,axis=0).tolist()
    print("Printing max_0")
    # print(max_0)
    max_1 = np.max(arr,axis=1).tolist()
    maximum = np.max(arr)
    # storing result
    calculations['max'] = [max_0,max_1,maximum]
    # print("Max calculations: ",calculations)


    # min
    min_0 = np.min(arr,axis=0).tolist()
    min_1 = np.min(arr,axis=1).tolist()
    minimum = np.min(arr)
    # storing result
    calculations['min'] = [min_0,min_1,minimum]


    # sum
    sum_0 = np.sum(arr,axis=0).tolist()
    sum_1 = np.sum(arr,axis=1).tolist()
    sum_all = np.sum(arr)
    # storing result
    calculations['sum'] = [sum_0,sum_1,sum_all]

    return calculations