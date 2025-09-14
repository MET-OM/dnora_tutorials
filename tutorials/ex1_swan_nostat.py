import dnora as dn

# User definitions for run
NAME = "Ex1_Sula500"
START_TIME = "2020-01-20T00:00"
END_TIME = "2020-01-20T23:00"
DM = 500  # Grid resolution in meters
LON = (5.21, 6.66)
LAT = (62.25, 62.89)
BOUNDARY_EDGES = ["N", "W"]
SPECTRAL_OUTPUT_LON = [5.89, 5.46]
SPECTRAL_OUTPUT_LAT = [62.48, 62.75]


def main() -> None:
    # Define the area and set the grid resolution and bathymetry
    grid = dn.grid.EMODNET(lon=LON, lat=LAT, name=NAME)
    grid.import_topo()
    grid.set_spacing(dm=DM)
    grid.mesh_grid()
    grid.set_boundary_points(dn.grid.mask.Edges(edges=BOUNDARY_EDGES))
    grid.set_output_points(
        dn.grid.mask.LonLat(lon=SPECTRAL_OUTPUT_LON, lat=SPECTRAL_OUTPUT_LAT)
    )
    # Define a ModelRun for the desired area
    model = dn.modelrun.NORA3(grid, start_time=START_TIME, end_time=END_TIME)
    model.import_wind()
    model.import_spectra(max_dist=15) # for max. 15 km from the boundary
    model.plot.grid()

    # Write grid file for SWAN
    exporter = dn.export.SWAN(model)
    exporter.export_grid()
    exporter.export_wind()
    exporter.export_spectra()

    # Write input file for model and execute SWAN
    exe = dn.executer.SWAN(model)
    exe.write_input_file()
    #exe.run_model() 


if __name__ == "__main__":
    main()
