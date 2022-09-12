## Learning atlite

Atlite is a tool for converting weather data into usable data for renewables including wind turbines, solar panels, hydro and heat in power system analysis developed by pypsa team.

The most important tool we should use in atlite is class *cutout*, which converts nc (netCDF, typically used in weather data storage) files into data arrays which could be understood and piped into next step for processing in power system analysis.

To get access to a nc file, the most convenient way is through climate data store (CDS) or atmosphere data store (ADS) which is free to be used from Copernicus Climate Change Service (C3S) as long as the register is done and api key obtained.

When a nc file is retrived with permission, then python code will take effect through network to download the nc file into local storage; or if the nc file corresponding to the version stored on the platform is already downloaded locally, then later analysis and conversion could carry on without waiting for downloading process.

After a nc file is retrieved, then call ```cutout.prepare()``` to process the data into features we may need in the next step. When this step is done, everything is ready.

Typically wind speed and solar radiation will be stored in the cutout variable and different functions could be called to calculate needed data such as available factors, combined with capabilities offered by other data sources (most convenient way by powerplantmatching tool from pypsa), the generation power could be obtained thus important data in modern power system analysis which is performance of renewables is obtained.

Current modules are developed for different types of wind turbines and solar panels. Hydro and heat pump are also in development butare much simpler.

## learning materials
Atlite on GitHub: https://github.com/PyPSA/atlite

Atlite documentation: https://atlite.readthedocs.io/

Waiting for implementation!