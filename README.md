

## Installation

Install with pip:

```
$ pip install -r requirements.txt
```

##  Application Structure 
```
|──────app/
| |────__init__.py
| |────main/
| | |────__init__.py
| | |────controller/
| | |────service/
| | |────util/
| | |────config
| |────test/
|──────manage.py
```


## Run Flask
### Run flask for develop
```
$ python mange.py run
```
In flask, Default port is `5000`

Swagger document page:  `http://127.0.0.1:5000`

[comment]: <> (##SWAGGER settings)

[comment]: <> (SWAGGER_DOC_URL = '/')


## Unittest and Pytest

```
$  python -m pytest -v -s
```

## Author
kamta- knt.kamta1@gmail.com