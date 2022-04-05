# Introduction

Automation test project for Pet store API automation. The project automates the CRUD pet store API and an allure report artefact is generated.

# Project Setup

This project is build with `python 3.8.5`

Use a python virtual environment to run the project. Set it up by following this: https://github.com/pyenv/pyenv-virtualenv

Once your python environment is setup, you need to install the required packages by running

```
pip install -r requirements.txt
```

## Functional Tests

To run functional tests run

```
pytest
```

This runs all of the test files configured in `setup.cgf`

The run also generates result artifacts under the `results` directory. These results can be viewed as an HTML page by running

```
allure serve results/
```




## Framework Organization

```
├── README.md
├── actions
│   ├── base_actions.py     - Base API actions for all other actions file
│   └── pet_actions.py     - API actions related to pets feature
├── configs
│   ├── config.py           - Environment configs
├── e2e_tests
│   ├── pet_crud_tests.py  - e2e functional test file
├── requirements.txt        - Required python libraries
├── results                 - e2e results directory
└── setup.cfg               - Pytest config
```

## Known Bugs
create endpoint failing while testing thus blocking update and delete. Below request details working on postman but failing while executing the script.
{"name": "Doggie", "photoUrls": ["Test url"], "status":"available"}

## Contact Details
For support or collaboration hit me up pkavoo@gmail.com

## License
MIT
