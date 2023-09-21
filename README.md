<h1 align="center">
    Test task
  <br>
</h1>

<h4 align="center">
    Handel CSV file and put results in PostgreSQL.
    <br>
</h4>

<div align="center">

[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?logo=conventionalcommits&logoColor=white)](https://conventionalcommits.org)

</div>
<hr>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="https://github.com/DenisPonizovkin/rc-task-back1#readme">Test assignment</a>
</p>


## Features
* Reading and handling CSV file with Pandas
* Saving handel data in PostgreSQL (using Docker container)


## How To Use
To clone and run this project, you'll need:
- [Git](https://git-scm.com)
- [Python](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/#installation)
- [Docker](https://www.docker.com/)


<details>

<summary><strong>Local run with docker</strong></summary>

1. Firstly clone repo
   ```bash
   git clone git@github.com:mrKazzila/test_task_5.git
   ```

2. Setup poetry
   ```bash
   poetry config virtualenvs.in-project true
   poetry shell
   poetry install
   ```

3. Create Postgres container
   ```bash
   docker run -d \
    --name test_task \
    -e POSTGRES_PASSWORD=postgres \
    -p 6432:5432 \
    postgres
   ```

4. Create DB for results
   ```bash
   docker exec -it test_task \
   psql -U postgres -c 'CREATE DATABASE test_task_result;'
   ```

5. Run script
   ```bash
   python main.py
   ```

6. Check result in Postgres container
   ```bash
   docker exec -it test_task psql -U postgres -d test_task_result -c 'SELECT * FROM results;'
   ```

7. Delete Postgres container
   ```bash
   docker stop test_task && docker rm test_task
   ```

</details>

<br>
