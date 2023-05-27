# Tradr
University Marketplace where students and faculty members can connect over their needs


### To run the project locally:
**1. Clone (or pull) the repository to a local machine**

**2. Activate the virtual environment**
```
// Windows
.\test_env\Scripts\activate

//Unix/macOS
source test_env/bin/activate
```
* If you haven't already, run the following codes to **install a virtual environment** before activating it (only needs to be done once when setting up the workplace for the first time):
```
// Windows
py -m pip install --user virtualenv
py -m venv test_env

// Unix/macOS
python3 -m pip install --user virtualenv
python3 -m venv test_env

```


**3. Run the following code**
```
cd Tradr

// Windows
py -m pip install -r requirements.txt
python manage.py migrate

// Unix/macOS
python3 -m pip install -r requirements.txt
python3 manage.py migrate
```
**4. Run the server to open the webpage**
```
// Windows
python manage.py runserver

// Unix/macOS
python3 manage.py runserver
```
Then ctrl+click the link in the terminal

**Leaving the virtual environment**
```
deactivate
```
