# !/bin/sh
git init && \
git add . && \
git commit -m "first commit" && \
git branch -M main && \
git remote add origin git@github.com:{{cookiecutter.organization}}/{{cookiecutter.project_name}}.git && \
git config --global http.sslverify "false" && \
python -m pip install poetry==1.2.0a2 && \
poetry install && \
poetry run pre-commit install && \
git add . && \
git commit -m "feat: Repo Configuration with Cookiecutter" && \
git push origin main
