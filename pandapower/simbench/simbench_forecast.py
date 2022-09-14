import simbench as sb

grid_code = "1-HV-urban--0-sw"
net = sb.get_simbench_net(grid_code)
profiles = sb.get_absolute_values(net, profiles_instead_of_study_cases=True)

sgen_p = profiles[("sgen", "p_mw")]
load_p = profiles[("load", "p_mw")]
load_q = profiles[("load", "q_mvar")]

import pandas as pd
x = pd.concat([sgen_p, load_p, load_q], axis=1)

y = pd.read_csv("./pandapower/simbench/res_line/loading_percent.csv")

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.1)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.fit_transform(x_test)

import numpy as np
np.save("x_train.npy", x_train)
np.save("x_test.npy", x_test)
np.save("y_train.npy", y_train)
np.save("y_test.npy", y_test)

print(x.shape)
print(x_train.shape)
print(x_test.shape)