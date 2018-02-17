from sklearn.linear_model import LogisticRegression
from sklearn.metrics import explained_variance_score
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, \
    AdaBoostRegressor, ExtraTreesRegressor
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.model_selection import GridSearchCV


def regression(X, Y, x, y, regr):
    regr.fit(X, Y.values.ravel())
    Y_pred = regr.predict(x)
    print("explained_variance_score:", explained_variance_score(y, Y_pred))
    print('Score:', regr.score(x, y), "\n")


import pandas
import os

cwd = os.getcwd()
X_test = pandas.read_csv(cwd + "/X_test.csv", index_col=0)
X_learn = pandas.read_csv(cwd + "/X_learn.csv", index_col=0)
Y_test = pandas.read_csv(cwd + "/Y_test.csv", index_col=0)[["Avg. Time on Page"]]
Y_learn = pandas.read_csv(cwd + "/Y_learn.csv", index_col=0)[["Avg. Time on Page"]]
#
regr = LinearRegression()
print("LinearRegression:")
regression(X_learn, Y_learn, X_test, Y_test, regr)
#
regr = Ridge()
print("Ridge:")
regression(X_learn, Y_learn, X_test, Y_test, regr)
#
regr = SVR(C=1000)
print("SVR:")
regression(X_learn, Y_learn, X_test, Y_test, regr)
#
regr = ExtraTreesRegressor(bootstrap=True)
print("ExtraTreesRegressor:")
regression(X_learn, Y_learn, X_test, Y_test, regr)
#
regr = RandomForestRegressor()
print("RandomForestRegressor:")
regression(X_learn, Y_learn, X_test, Y_test, regr)
#
regr = GradientBoostingRegressor()
print("GradientBoostingRegressor:")
regression(X_learn, Y_learn, X_test, Y_test, regr)
#
regr = AdaBoostRegressor()
print("AdaBoostRegressor:")
regression(X_learn, Y_learn, X_test, Y_test, regr)
