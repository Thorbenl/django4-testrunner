# django4-testrunner

### Success:

- `python3 -m venv venv`
- `source ./dev-env.sh`
- `pip3 install -r requirements.txt`
- `./manage.py test --timing --keepdb --verbosity 2`

Passing

### Error:

- Change MARKET value inside `dev.env` to `market_b`
- `source ./dev-env.sh`
- `./manage.py test --tag=market_b --timing --keepdb --verbosity 2`

See the error
```python
RuntimeError: Model class market_a_app.models.AdvertisementIdMapping doesn't declare an explicit app_label and isn't in an application in INSTALLED_APPS.
```

``

