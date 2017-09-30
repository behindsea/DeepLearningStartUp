import numpy

def cut_negative(f):
    if f < 0.0:
        return 0.0
    else:
        return f


flo_arr = numpy.random.normal(0.0,1.0,100)

print(flo_arr)

vec_fun = numpy.vectorize(cut_negative)

print(vec_fun(flo_arr))
