import numpy as np
x_train = np.load("./pandapower/simbench/x_train.npy", allow_pickle=True)
x_test = np.load("./pandapower/simbench/x_test.npy", allow_pickle=True)
y_train = np.load("./pandapower/simbench/y_train.npy", allow_pickle=True)
y_test = np.load("./pandapower/simbench/y_test.npy", allow_pickle=True)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
y_train = scaler.fit_transform(y_train)

from sklearn.neural_network import MLPRegressor
ann = MLPRegressor(verbose=1)

ann.fit(x_train, y_train)
y_predict = ann.predict(x_test)
y_predict = scaler.inverse_transform(y_predict)

import matplotlib.pyplot as plt
plt.plot(y_test[:96, 53], alpha=.5, linestyle='--', label="correct line loading values")
plt.plot(y_predict[:96, 53], alpha=.5, linestyle='-', label="predicted line loading values")
