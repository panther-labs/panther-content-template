# panther-content-template
Panther Config SDK template repo for content modules.


## Setup a new repo
1) Clone this repo
```shell
git clone git@github.com:panther-labs/panther-content-template.git my-panther-content
```
```shell
cd my-panther-content
```

2) Initialize the repo. This will remove the existing git data, delete `CODEOWNERS` and start a new git repository:
```shell
make init
```

3) Optionally, start a docker shell to run python 3.9. If docker is not available or you prefer to run on your host operating system, you can skip this step. Pleasure ensure your machine has a proper Python 3.9 environment with `pip` installed.

```shell
make shell
```

4) Run the install command to bootstrap the repository's dependencies. If you are running in docker, there may be warnings about running as a root user. These can be ignored. You can confirm this was successful by running the tests.
```shell
make install
```
```shell
make test
```

### Project structure
While any directory structure that implements a valid python module will work, this template includes a basic directory structure to provide some guidance on how to organize your content. The list below provides a brief description of this included structure:

```
/panther_content
    /__main__.py   # module entry point

    /filters       # reusable filters for use in Panther Rules, Policies and Scheduled Rules
    /rules         # Panther Rule content
    /queries       # Panther Saved/Scheduled Query content

/tests             # directory structure mirroring "panther_content" that includes unit tests.
/Makefile          # sample Makefile provided with lint, format and testing targets
/mypy.ini          # recommened mypy configuration for python type checking
/requirements.txt  # PIP requirements file

/.github           # example automation pipeline using GitHub Actions
```

### Importing & updating content
You can import & update filters, detections and other `panther_config`-based content via PIP modules. As with any other PIP module, this can be done by editing the `requirements.txt` file. Panther-authored content follows [semantic versioning](semver.org). Please refer to the (Py-Pkgs guidance)[https://py-pkgs.org/07-releasing-versioning.html] on how to use this file and to decide how to version. 


## Using Automation
This repo includes configuration for GitHub Actions in `.github/workflows`. You can either use these as-is or use them as a reference while setting up your own automation pipeline.


## Publish as a content library
If you want to make your `panther_config` based content available to other repositories, you can do so by publishing to [PyPi](pypi.org) or another PIP-based pacakge host. As with any published PIP package, you will have to include configuration to do so. See [Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/) for more details. You can refer to the source code of [panther-utils](https://github.com/panther-labs/panther-utils) for a Panther-provided example of doing this.
