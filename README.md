# panther-content-template
Panther Config SDK template repo for content modules.


### Setup a new repo to manage Panther content
Clone this repo and reset the git history:
```shell
git clone git@github.com:panther-labs/panther-content-template.git my-panther-content
cd my-panther-content

rm -rf .git
git init
```

Run the install command to bootstrap the python environment
```shell
make install
```