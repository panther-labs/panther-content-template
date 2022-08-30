# panther-content-template
Panther Config SDK template repo for content modules.


## Setup a new repo
Clone this repo:
```shell
git clone git@github.com:panther-labs/panther-content-template.git my-panther-content
cd my-panther-content
```

Reset the git history:
```shell
rm -rf .git
git init
```

Run the install command to bootstrap the python environment
```shell
make install
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

## Using Automation
This repo includes configuration for GitHub Actions in `.github/workflows`. You can either use these as-is or use them as a reference while setting up your own automation pipeline.


## Publish as a content library
If you want to make your `panther_config` based content available to other repositories, you can do so by publishing to [PyPi](pypi.org) or another PIP-based pacakge host. As with any published PIP package, you will have to include configuration to do so. See [Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/) for more details. You can refer to the source code of [panther-utils](https://github.com/panther-labs/panther-utils) for a Panther-provided example of doing this.