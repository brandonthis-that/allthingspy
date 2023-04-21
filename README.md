This is a simple project using Python to generate **secure** passwords using the users specifications.

To run on a virtual environment by default, the following procedure can be followed:
1. Create a file and name it `run.sh` 
2. Edit the file as follows:
 ```bash
  #!/bin/bash

# Activating the virtual environment
source myenv/bin/activate

# Runing the Python script
python generate_password.py

```

`myenv` should be replaced with the actual name of your virtual environment. My Python file was named `generate_password.py` but you can name yours as you wish.

3. Save and close the file.

4. Run the following code to make the file executable:
```bash
chmod +x run.sh
```
5. Now execute the `run.sh` file to run the code in a virtual environment.
```bash 
./run.sh
```
