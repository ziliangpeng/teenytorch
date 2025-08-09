def test_import_and_version():
    import teenytorch

    assert isinstance(teenytorch.__version__, str)
    assert len(teenytorch.__version__) > 0

