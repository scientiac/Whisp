# Testing Whisp

Whisp uses the Meson build system's native testing framework to ensure that the application is stable and complies with Flathub distribution rules.

## Automated CI Pipeline

Whisp uses GitHub Actions for Continuous Integration. Every time you push a commit or open a Pull Request, the CI pipeline will automatically run all tests to ensure nothing is broken. You can check the status of these tests in the "Actions" tab of the repository, or by looking for the green checkmark next to your commit!

## Running Tests Locally

If you are developing a new feature or fixing a bug, you can run the test suite locally on your machine before submitting a Pull Request.

### Prerequisites
Make sure you have the following installed on your system:
- `meson` and `ninja`
- `desktop-file-utils` (for `desktop-file-validate`)
- `appstream` (for `appstreamcli`)

### Execution
From the root of the repository, set up the build directory (you only need to do this once):
```bash
meson setup builddir
```

Then, run the tests:
```bash
meson test -C builddir
```

This will run:
1. **Desktop File Validation**: Ensures the `.desktop` file meets all specifications.
2. **AppStream Validation**: Validates the `metainfo.xml` against Flathub's strict guidelines.
3. **Python Unit Tests**: Runs the automated test suite in the `tests/` directory to verify core application logic (such as the text search algorithms).

## Writing New Tests

If you are contributing new core logic (like parsers or utility functions), please consider adding a test for it!
1. Add your test script to the `tests/` directory (e.g., `test_my_feature.py`).
2. Register the test inside `tests/meson.build` so the CI pipeline knows to run it.
