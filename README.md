# Python Project Boiler Plate V2

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
