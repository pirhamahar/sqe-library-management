# Unit Testing Notes

## Pytest Output

### Verbose Output

Command:

pytest -v tests/

Verbose output shows each test separately with its pass or fail result.

It is useful when we want to see which specific tests are running and
which test has failed.

### Short Traceback

Command:

pytest --tb=short

Short traceback shows a shorter error message when a test fails.

It is useful when we want to quickly understand a failure without a long
error traceback.

## Fixture Scopes

### Function Scope

Function scope is the default scope for a pytest fixture.

A new fixture is created for every test. It is useful when every test
needs fresh and independent data.

Example:

@pytest.fixture
def library():
    return Library()

### Module Scope

Module scope creates the fixture once for the whole test module.

It is useful for expensive setup that can safely be shared by multiple
tests.

Example:

@pytest.fixture(scope="module")
def expensive_library():
    return Library()

## Arrange-Act-Assert

Arrange means preparing the test data.

Act means calling the function or method being tested.

Assert means checking that the result is correct.

## Mocking

Mocking allows us to test file operations without creating a real file.

The export_catalog tests mock the open() function and check that the
expected catalog content is written.

The error test also checks that an OSError is converted into the custom
LibraryIOError exception.

## Parametrized Testing

The borrow_book tests use pytest.mark.parametrize.

Six different borrowing cases are tested using one test function.

Each case has a descriptive id so the test output clearly shows which
case is being tested.

## Summary

The Library Management System test suite uses fixtures, Arrange-Act-Assert,
mocking, and parametrized tests to make testing more organized and
maintainable.
