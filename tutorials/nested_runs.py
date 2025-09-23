import dnora as dn


def main() -> None:
    # Define the area and set the grid resolution and bathymetry
    sula500 = dn.grid.EMODNET(lon=(5.21, 6.66), lat=(62.25, 62.89), name="sula500")
    sula500.set_spacing(dm=500)
    sula500.import_topo()
    sula500.mesh_grid()
    sula500.set_boundary_points(dn.grid.mask.Edges(edges=["N", "W"]))

    sula200 = dn.grid.EMODNET(lon=(5.5, 6.66), lat=(62.25, 62.6), name="sula200")
    sula200.set_spacing(dm=200)
    sula200.import_topo()
    sula200.mesh_grid()

    sula50 = dn.grid.EMODNET(lon=(5.8, 6.1), lat=(62.4, 62.5), name="sula50")
    sula50.set_spacing(dm=50)
    sula50.import_topo()
    sula50.mesh_grid()

    sula100 = dn.grid.EMODNET(lon=(5.3, 5.4), lat=(62.4, 62.5), name="sula100")
    sula100.set_spacing(dm=50)
    sula100.import_topo()
    sula100.mesh_grid()

    model = dn.modelrun.NORA3(
        sula500, start_time="2020-01-20T00:00", end_time="2020-01-20T02:00"
    )
    model.set_nested_grid(sula200)
    model.set_nested_grid(sula100)
    # If you only have one nest, model.nest() will return that
    # model.nest(get_dict=True) will always return a dictionary regardless of the number of nests
    model.nest()["sula200"].set_nested_grid(sula50)

    model.import_wind()
    model.import_spectra()
    model.nest()["sula200"].import_current(dn.read.current.metno.NorKyst800())

    exporter = dn.export.SWAN(model)
    exporter.export_grid()
    exporter.export_wind()
    exporter.export_spectra()
    exporter.export_current()

    exe = dn.executer.SWAN(model)
    exe.write_input_file()
    exe.run_model()


if __name__ == "__main__":
    main()
