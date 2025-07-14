# Python Project Boiler Plate V2

## Useful Settings

Change the default terminal when opened

```
Terminal: Select Default Profile
```

Select the python interpreter

```
Python: Select Interpreter
```

Add a conda activated terminal profile

```
Preferences: Open User Settings (JSON)
```

Example profile

```
"Command Prompt (POC)": {
    "path": "C:\\WINDOWS\\System32\\cmd.exe",
    "args": ["/k", "conda activate POC"]
}
```

## Useful Conda Commands

List Conda environments

```
mamba env list
```

List packages installed in an environment

```
mamba list -n POC
```

Create a Conda environment from a configuration file

```
mamba env create -f conda_environment.yml
```

Create a Conda environment from a lock file

```
conda create --name POC --file environment.lock.txt
```

Update an existing Conda environment from a configuration file

```
mamba env update -f conda_environment.yml
```

Export a Conda environment to a lock file

```
conda list --name POC --explicit > conda_environment.lock.txt
```

Delete a Conda environment

```
mamba env remove --name POC
```

## Useful Python Commands

Install a custom Python package as editable in the Conda environment. Must have the Conda environment activated.

```
pip install -e .
```
