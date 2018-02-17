import numpy as np
def parse(path):
    X = []
    Y = []
    for l in open(path):
        l = l.split(",")
        x = [float(l[i]) for i in range(1, len(l))]
        y = float(l[0])
        X.append(x)
        Y.append(y)
    return np.asarray(X), np.asarray(Y)
