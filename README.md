# surfgreendjango

case study job challenge

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

License: MIT

## Local Installation

1. Clone repository
```bash
git clone https://github.com/Khroxx/surfdjango.git
```
2. Install environment
```bash
python3 -m venv env
```
3. Enter environment
- **Unix-like (Linux/macOS)**: source env/bin/activate
- **Windows**: .\env\Scripts\activate
4. Install requirements
```bash
pip install -r requirements/base.txt
```
```bash
pip install -r requirements/local.txt
```
5. Create Postgres Database:
```bash
 createdb --username=postgres surfdjango
```
- with username debug and password debug
6. create .env  with:
- DATABASE_URL=postgres://debug:debug@localhost:5432/surfdjango
- USE_DOCKER=yes
7. Start local server
```bash
python3 manage.py runserver
```


### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create a **superuser account**, use this command:

      $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy surfdjango

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest
