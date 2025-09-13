import dnora as dn
import dnplot
from dnora.wavegrid import WaveGrid
from dnora.spectra import Spectra

FILENAME = "Ex1_Sula500_SWAN/Ex1_Sula500_20200120.nc"
FILENAME_SPEC = "Ex1_Sula500_SWAN/Ex1_Sula500_20200120_spec.nc"
# FILENAME = "Ex4_Sula500st_SWAN/Ex4_Sula500st_20250912.nc"


def plot_grid(data_var: str = "hs") -> None:
    data = WaveGrid.from_netcdf(FILENAME)
    data_dict = {"wavegrid": data}
    plot = dnplot.Matplotlib(data_dict)
    plot.wavegrid(data_var)


def plot_timeseries(lon: float = None, lat: float = None) -> None:
    """You can define which variables to plot by defining var=['hs',('tp','tm01'), ('dirp','dirm')]"""
    data = WaveGrid.from_netcdf(FILENAME)
    data_dict = {"waveseries": data.sel(lon=lon, lat=lat, method="nearest")}
    plot = dnplot.Matplotlib(data_dict)
    plot.waveseries(var=["hs", ("tp", "tm01"), ("dirp", "dirm")])


def plot_spectra() -> None:
    """Note that the plot is quantitavive, since the normalization probably isn't right.
    Direction is also in radians and therefore not shown correctly."""
    model = dn.modelrun.ModelRun(year=2020)
    model.import_spectra(filename=FILENAME_SPEC)
    model.spectra_to_1d()
    plot = dnplot.Matplotlib(model)
    plot.spectra1d()


def main():
    plot_grid()
    # plot_timeseries(lon=5.25, lat=62.3)  # Plot one point
    # plot_spectra()


if __name__ == "__main__":
    main()
