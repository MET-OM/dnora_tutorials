import dnora as dn

# User definitions for run
NAME = "Ex3_Svea500i"
START_TIME = "1980-02-20T00:00"
END_TIME = "1980-02-20T23:00"
DM = 500  # Grid resolution in meters
LON = (13.27, 17.25)
LAT = (77.31, 78.23)
BOUNDARY_EDGES = ["N", "W", "S"]


def main() -> None:
    # Define the area and set the grid resolution and bathymetry
    grid = dn.grid.EMODNET(lon=LON, lat=LAT, name=NAME)
    grid.import_topo()
    grid.set_spacing(dm=DM)
    grid.mesh_grid()
    grid.set_boundary_points(dn.grid.mask.Edges(edges=BOUNDARY_EDGES))

    # Define a ModelRun for the desired area
    model = dn.modelrun.NORA3(grid, start_time=START_TIME, end_time=END_TIME)
    model.import_wind()
    model.import_spectra()
    model.import_ice()

    # Write grid file for SWAN
    exporter = dn.export.SWAN(model)
    exporter.export_grid()
    exporter.export_wind()
    exporter.export_spectra()
    exporter.export_ice()

    # Write input file for model and execute SWAN
    exe = dn.executer.SWAN(model)
    exe.write_input_file()
    #exe.run_model()


if __name__ == "__main__":
    main()
