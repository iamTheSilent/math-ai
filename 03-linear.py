import random
import time

def f(x):
    return ((x*x*x*x)-(2*x*x)-(x)+(1))

def df(x):
    return ((4*x*x*x)-(4*x)-(1))

def ddf(x):
    return ((12*x*x)-(4))

def random_num(a, b):
    return (random.uniform(a, b))

def extrema(a, b):
    global errors
    x_mins = []
    x_maxs = []
    point = a
    for i in range((b-a)*4000):
        point = point + 0.00025
        if abs(df(point)) < 0.001:
            if ddf(point) > 0:
                x_mins.append(point)
                #print("The: ", df(point))
            elif ddf(point) < 0:
                x_maxs.append(point)
    x_mins = (list(set(map(lambda x: round(x,2),(x_mins)))))
    for i in range(len(x_mins)):
        #print("A minimum: [", str(x_mins[i]), ",", str(round(f(x_mins[i]),2)), "]")
        if x_mins[i] != 1.11 and x_mins[i] != -0.84:
            errors = errors + 1
    x_maxs = (list(set(map(lambda x: round(x,2),(x_maxs)))))
    for i in range(len(x_maxs)):
        #print("A maximum: [", str(x_maxs[i]), ",", str(round(f(x_maxs[i]),2)), "]")
        if x_maxs[i] != -0.27:
            errors = errors + 1
    

if __name__ == "__main__":

    init_time = time.time()
    errors = 0

    for i in range(10000):
        random.seed(time.time())
        extrema(-2, 2)

    fin_time = time.time()
    runtime = ( fin_time - init_time ) * 1000

    print("Runtime: ", int(runtime), "ms")
    print("Accuracy: ", 100.00-round((errors/300),2), "%")