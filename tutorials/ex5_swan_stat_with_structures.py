import dnora as dn

# User definitions for run
NAME = "Ex5_Sula500st"
DM = 500  # Grid resolution in meters
LON = (5.21, 6.66)
LAT = (62.25, 62.89)
BOUNDARY_EDGES = ["N", "W"]

# Use stationary forcing
STATIONARY_FORCING = {
    "wind": {"ff": 10, "dd": 330},  # Speed, direction from
    "spectra": {
        "gamma": 2.5,
        "W": {"hs": 5, "tp": 12, "dirp": 270},
        "N": {"hs": 3, "tp": 11, "dirp": 280},
    },
}
STRUCTURES = [
    {
        "lon": (5.91, 5.94),
        "lat": (62.45, 62.46),
        "trans": 0.0,
        "refl": 0.1,
        "name": "breakwater",
    }
]


def main() -> None:
    # Define the area and set the grid resolution and bathymetry
    grid = dn.grid.EMODNET(lon=LON, lat=LAT, name=NAME)
    grid.import_topo()
    grid.set_spacing(dm=DM)
    grid.mesh_grid()
    grid.set_boundary_points(dn.grid.mask.Edges(edges=BOUNDARY_EDGES))

    # Define a ModelRun for the desired area
    model = dn.modelrun.ModelRun(grid)

    # Write grid file for SWAN
    exporter = dn.export.SWAN(model)
    exporter.export_grid()

    # Write input file for model and execute SWAN
    exe = dn.executer.SWAN(model)
    # exe.write_input_file(homog=STATIONARY_FORCING)
    exe.write_input_file(
        homog=STATIONARY_FORCING,
        structures=STRUCTURES,
    )
    exe.run_model()


if __name__ == "__main__":
    main()
