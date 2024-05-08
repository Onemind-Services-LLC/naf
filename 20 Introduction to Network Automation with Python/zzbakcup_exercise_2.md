##  Exercise-2: Set up and activate a virtual environment on your system.


You can install `virtualenv` using `pip`, Python's package manager:

```sh
# Install virtualenv
pip install virtualenv

# Create a virtual environment named "my_env"
virtualenv my_env

# Activate the virtual environment (Windows)
my_env\Scripts\activate

# Activate the virtual environment (Linux)
source my_env/bin/activate

# Now you're in the virtual environment
# Install dependencies using pip
pip install package_name
```

You can deactive this environment using below command
```sh
# Deactivate the virtual environment
deactivate
```
