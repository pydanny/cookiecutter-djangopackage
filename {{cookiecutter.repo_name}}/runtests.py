import sys

try:
    import pytest
except ImportError:
    print(
        "\n"
        "------------------- MISSING DEPENDENCIES -------------------\n"
        "To fix this error, run: pip install -r requirements-test.txt\n"
        "------------------------------------------------------------\n"
    )
    sys.exit(1)


def run_tests(*test_args):
    test_args = list(test_args) or ['tests']

    # Run tests
    failures = pytest.main(test_args)

    if failures:
        sys.exit(failures)


if __name__ == '__main__':
    run_tests(*sys.argv[1:])
