import pandapower.networks as nw
import pandapower as pp
import pandas as pd

import matplotlib.pyplot as plt
from pandapower.control.controller.const_control import ConstControl
from pandapower.timeseries.data_sources.frame_data import DFData
from pandapower.timeseries.run_time_series import run_timeseries
from pandapower.timeseries.output_writer import OutputWriter

net = nw.example_simple()
net.gen.drop(net.gen.index, inplace=True)
pp.create_sgen(net, 5, p_mw=1)

df = pd.read_json("pandapower/timeseries/cigre_timeseries_15min.json")
ds = DFData(df)
ConstControl(net, "sgen", "p_mw", element_index=net.sgen.index, profile_name=["wind", "pv"], data_sources=ds)
ConstControl(net, "load", "p_mw", element_index=net.load.index, profile_name=["residential"], data_source=ds)

ow = OutputWriter(net, time_steps=(0, 95), output_path="./pandapower/timeseries/", output_file_type=".csv")
ow.log_variable("res_bus", "vm_pu")
ow.log_variable("res_line", "loading_percent")
run_timeseries(net, time_steps=(0, 95))
df = pd.read_csv("pandapower/timeseries/res_line/loading_percent.csv", delimiter=";")
df.plot()
plt.show()