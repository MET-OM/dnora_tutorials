import xarray as xr
import matplotlib.pyplot as plt

ds = xr.open_dataset("Ex1_Sula500_SWAN/Ex1_Sula500_20200120.nc")
ds.isel(time=20).hs.plot()
plt.savefig("example_fig.png")

plt.show()
