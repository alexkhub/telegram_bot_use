# tg-use
### tg-use bot for saving exam points

![PyPI - Version](https://img.shields.io/pypi/v/aiogram?label=aiogram)
![PyPI - Version](https://img.shields.io/pypi/v/python-dotenv?label=python-dotenv)
![PyPI - Version](https://img.shields.io/pypi/v/sqlalchemy?label=sqlalchemy)
![PyPI - Version](https://img.shields.io/pypi/v/aiosqlite?label=aiosqlite&color=blue)

### Python version = 3.11

## Install packages

```shell
pip install requirements.txt
```

## Project structure
### 
![img.png](docs/img.png)


- #### core - package containing the main logic
   - #### database - stores models DB and queries
   - #### handlers - stores  business logic
   - #### keyboards - stores keyboards
   - #### utils - stores utils
- #### env - stores secret data (cannot be sent 😢  )
- #### main - point of entry
