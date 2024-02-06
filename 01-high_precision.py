import random
import time

def f(x):
    return ((x*x*x*x)-(2*x*x)-(x)+(1))

def df(x):
    return ((4*x*x*x)-(4*x)-(1))

def random_num(a, b):
    return (random.uniform(a, b))

def minimum(a, b):
    global errors
    x_mins = [0]*11
    for i in range(11):
        point = random_num(a, b)
        for j in range(10000):
            old_point = point
            point = point - df(point)*random_num(0,1)*0.1
            delta = abs(point - old_point)
            if delta < 0.00000000000001: break
        x_mins[i] = point
    
    x_mins = (list(set(map(lambda x: round(x,6),(x_mins)))))
    for i in range(len(x_mins)):
        #print("A minimum: [", str(x_mins[i]), ",", str(round(f(x_mins[i]),5)), "]")
        if x_mins[i] != 1.10716 and x_mins[i] != -0.837565:
            errors = errors + 1


def maximum(a, b):
    global errors
    x_maxs = [0]*11
    for i in range(11):
        point = random_num(a, b)
        for j in range(10000):
            old_point = point
            point = point + df(point)*random_num(0,1)*0.1
            delta = abs(point - old_point)
            if point < a or point > b:break
            if delta < 0.00000000000001: break
        x_maxs[i] = point
    x_maxs = (list(set(map(lambda x: round(x,6),(x_maxs)))))
    for i in range(len(x_maxs)):
        if x_maxs[i] >= a and x_maxs[i] <= b:
            #print("A maximum: [", str(x_maxs[i]), ",", str(round(f(x_maxs[i]),5)), "]")
            if x_maxs[i] != -0.269594:
                errors = errors + 1
    

if __name__ == "__main__":

    init_time = time.time()
    errors = 0

    for i in range(10000):
        random.seed(time.time())
        minimum(-2, 2)
        maximum(-2, 2)

    fin_time = time.time()
    runtime = ( fin_time - init_time ) * 1000

    print("Runtime: ", int(runtime), "ms")
    print("Accuracy: ", 100.00-round((errors/300),2), "%")