import pytest
from libraryhub.library import Library, LibraryIOError


def test_export_catalog_writes_expected_content(mocker):
    # Arrange
    library = Library()
    library.add_book("ISBN001", 2)
    library.add_book("ISBN002", 3)

    mock_open = mocker.patch(
        "libraryhub.library.open",
        mocker.mock_open()
    )

    # Act
    library.export_catalog("catalog.txt")

    # Assert
    mock_open.assert_called_once_with("catalog.txt", "w")

    file_handle = mock_open()
    file_handle.write.assert_called_once_with(
        "ISBN001,2\nISBN002,3\n"
    )


def test_export_catalog_handles_oserror(mocker):
    # Arrange
    library = Library()
    library.add_book("ISBN001", 2)

    mocker.patch(
        "libraryhub.library.open",
        side_effect=OSError("Disk error")
    )

    # Act & Assert
    with pytest.raises(LibraryIOError, match="Unable to export catalog"):
        library.export_catalog("catalog.txt")
