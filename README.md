---
Virtualenv - Python
---

# Virtual Env

## How to use
### Installation and activation
```bash
// Installation
pip install virtualenv

// Create venv with name venv
// option1
virtualenv venv
// option2
virtualenv -p python3 myvenv

// Activate venv
. venv/bin/activate

// DeActivate venv
deactivate
```

### Packages export and import
```bash
pip list
pip freeze > requirements.txt
type requirements.txt
virtualenv mydev
. venv/bin/activate
pip list
pip install -r requirements.txt
pip list
deactivate
```

## Install Flask
```bash
pip install Flask
```

## Run App
```
python app.py

// Change env from Prod to Dev
export FLASK_ENV=development
```
