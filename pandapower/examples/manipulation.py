import pandapower.networks as nw
import pandapower as pp

net = nw.create_cigre_network_lv()

net.bus.drop(columns="vn_kv", inplace=True)

net.bus.loc[1, "name"] = "whatever"

net.bus.iloc[2, 4] = "whatever"

net.bus.at[3, "name"] = "whatever"

net.bus.iat[4, "name"] = "whatever"

print(net.bus.head())