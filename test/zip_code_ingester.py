from zip_code_ingester import create_table, import_data, db


def unit_tests():
    """
    Run unit tests for the database operations
    :param:
    :return
    :TODO: why is there a unit test in the ingestor, move to 'test/'
    """
    # Create a test table
    create_table()

    # Import test data
    # :TODO: why does it work that test_data.tsv works but doesn't exist
    file_path = 'test_data.tsv'
    import_data(file_path)

    # Perform database queries and assertions here
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM real_estate")
    count = cursor.fetchone()[0]
    # :TODO: need to be reconfigured if once row count == 9
    assert count == 9, "Invalid row count"

    # Clean up test data and table
    # :TODO: test and show off inserting fake data and removing it
    cursor.execute("DELETE FROM real_estate")
    db.commit()
    cursor.execute("DROP TABLE IF EXISTS real_estate")
    db.commit()
