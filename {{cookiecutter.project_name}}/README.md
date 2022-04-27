# {{cookiecutter.project_name}}

{{ cookiecutter.project_description }}

## Requisitos

- [poetry](https://pypi.org/project/poetry/1.2.0a2/)

## Instalando Dependências

```shell
poetry install -vv
```

## Ativando Ambiente virtual do Python (venv)

```shell
poetry env use python
```

### Instalando pre-commit

```shell
git config --global http.sslverify "false" && \
poetry run pre-commit install
```
