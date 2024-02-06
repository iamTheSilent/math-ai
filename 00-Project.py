import random
import time

def f(x):               #function: x^4 + 2x^2 - x + 1
    return ((x*x*x*x)-(2*x*x)-(x)+(1))

def df(x):              #gradient (the derivative, as this is a single-variable function): 4x^3 - 4x - 1
    return ((4*x*x*x)-(4*x)-(1))

def random_num(a, b):   #random number generator
    return (random.uniform(a, b))

def minimum(a, b):

    x_mins = [0]*11                                         #use 11 points to generate 11 minima

    for i in range(11):

        point = random_num(a, b)                            #initialize the point at a random coordinate

        for j in range(10000):

            old_point = point                               #remember prev step
            point = point - df(point)*random_num(0,1)*0.1   #move the point opposite of gradient, each step includes an additional randomizer element
            delta = abs(point - old_point)                  #calculate precision

            if delta < 0.00000000000001: break              #stop when precision is desirable

        x_mins[i] = point
    
    #reduce accuracy to 6 decimals and use set to remove duplicates
    x_mins = (list(set(map(lambda x: round(x,6),(x_mins)))))

    #print
    for i in range(len(x_mins)):
        print("A minimum: [", str(x_mins[i]), ",", str(round(f(x_mins[i]),6)), "]")


def maximum(a, b):                                          #similar to minimum function

    x_maxs = [0]*11

    for i in range(11):

        point = random_num(a, b)

        for j in range(10000):

            old_point = point
            point = point + df(point)*random_num(0,1)*0.1   #move towards the gradient
            delta = abs(point - old_point)

            if point < a or point > b: break                #break loop if the point escapes domain towards infinity
            if delta < 0.00000000000001: break
        
        x_maxs[i] = point
    
    x_maxs = (list(set(map(lambda x: round(x,6),(x_maxs)))))

    for i in range(len(x_maxs)):
        if x_maxs[i] >= a and x_maxs[i] <= b:               #only print maxima within the domain
            print("A maximum: [", str(x_maxs[i]), ",", str(round(f(x_maxs[i]),6)), "]")


if __name__ == "__main__":

    #get randomizer seed from system time
    random.seed(time.time())

    #find and print extrema within [-2, 2]
    minimum(-2, 2)
    maximum(-2, 2)