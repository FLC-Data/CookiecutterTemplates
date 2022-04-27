# Cookiecutter Templates

This repository contains the reference template for project development.

## Requirements
- Python 3.8+
- [cookiecutter](https://pypi.org/project/cookiecutter/)
- [WSL (Only Windows Users)](https://pureinfotech.com/install-windows-subsystem-linux-2-windows-10/)

``` shell
$ pip install cookiecutter
```

## To start a new project, run:

``` shell
# HTTPS
$ cookiecutter https://github.com/FLC-Data/CookiecutterTemplates.git
```

or 

``` shell
# SSH
$ cookiecutter git@github.com:FLC-Data/CookiecutterTemplates.git
```

### The resulting directory structure

The directory structure of your new project looks like this: 

```
├── LICENSE
├── README.md <- The top-level README for developers using this project.
├── .github                     
│   ├── workflows <- The pipelines for the github actions.
│   │  └── pull_request_opened.yaml <- Linter & Unit Tests Pipeline.
│   └── PULL_REQUEST_TEMPLATE.md
├── .vscode      
│   └── settings.json <- The VS Code Settings .
├── data      
│   ├── staging <- The final, canonical data sets for modeling.
│   ├── wrangling <- Intermediate data that has been transformed.
│   └── raw <- The original, immutable data dump.
├── models <- Trained and serialized models, model predictions, or model summaries
├── modules <- Modules with utils for the repository.  
│   ├── cli
│   │  └── issue_description.py <- Job that get the Jira's issues descriptions.
│   └── __init__.py
├── docs <- The tecnical documenttation
├── notebooks <- Jupyter notebooks. Naming convention is a number (for ordering),
│                             the creator's initials, and a short `-` delimited description, e.g.
│                             `1.0-flc-initial-data-exploration`.
├── references <- Data dictionaries, manuals, and all other explanatory materials.
├── reports <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures <- Generated graphics and figures to be used in reporting
├── sandbox <- Intended for testing stuff, poc, etc.
├── ml_app <- Flask Structure Application.
│   ├── app <- Flask Application.
│   │   ├── api <- The API module
│   │   │   ├── templates <- HTML templates for Flask Front-end.
│   │   │   ├── routes.py <- The routes for the Flask endpoint.
│   │   │   └── __init__.py <- The Flask blueprint for api module
│   │   └── __init__.py <- The App startup.
│   ├── tests <- Intended for unit testing
│   │   ├── __init__.py
│   │   ├── conftest.py <- The Pytest Fixtures Structure.
│   │   └── test_app.py <- The Minimal Flask Unit Test.
│   ├── .env <- Credentials and Secrets for Flask use.
│   ├── config.py <- The static configuration of the application.
│   ├── entrypoint.sh <- Entrypoint with gunicorn for DOCKERFILE.
│   └── ml_app.py <- App Module Defintion.
├── .dockerignore
├── .editorconfig <- EditorConfig Extension Configuration.
├── .env <- Credentials and Secrets for the project structure use.
├── .flake8 <- Flake8 Linter Configuration.
├── .flaskenv <- Flask App Defintion.
├── .gitignore
├── .gitattributes
├── .pre-commit-config.yaml <- Pre Commit Configuration.
├── CHANGELOG.md
├── DOCKERFILE
├── poetry.toml
├── post-gen.sh <- Entrypoint for autosetup with Cookiecutter
└── pyproject.toml
```

### References
---
- [EditorConfig - (.editorconfig)](https://editorconfig.org/)
- [GitHub Actions - (.github/workflows)](https://docs.github.com/en/actions/learn-github-actions)
- [GitHub Pull Requst Template - (.github/PULL_REQUEST_TEMPLATE.md)](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository)
- [VS Code Settings (.vscode/settings.json)](https://code.visualstudio.com/docs/getstarted/settings)
- [Flake8 - (.flake8)](https://flake8.pycqa.org/en/latest/user/configuration.html)
- [Git - (.gitignore)](https://www.toptal.com/developers/gitignore)
- [Pre Commit - (.pre-commit-config.yaml)](https://pre-commit.com/)
- [ChangeLog - (CHANGELOG.md)](https://keepachangelog.com/en/1.0.0/)
- [Poetry - (pyproject.toml, poetry.lock, poetry.toml)](https://python-poetry.org/docs/)
- [Readme - (README.md)](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)