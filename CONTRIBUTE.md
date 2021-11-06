> This section is not complete. Thank you for understanding :)

### Local Development
As you make changes, In repository:
pip install .

Then in tests/ directory, you can run all the tests, test out development versions and so on

### AUTOMATED TESTING COMING SOON
Automated testing using unittest


### Publishing a new version of ms-collect
Note, if you are not marked as a collaborator in the package registry, you will not be allowed to
publish a new version.

First ensure that you build:
```sh
python -m build
```

Then use twine to upload the archives under dist:
```sh
python -m twine upload dist/*
```

When prompted for credentials, enter your pypi creds or access token.