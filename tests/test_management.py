

def test_create_data_package():
    from pyLithoSurferAPI.management.tables import DataPackage
    from pyLithoSurferAPI import select_database
    select_database("test")
    DataPackage(name="Test_romain").new()
