# GT20SC3


## Clone repository

After finish setting up your private repository, run the following in your local machine
```
cd <base_folder_path>
git clone https://gitlab.com/<your_gitlab_username>/startup-campus-backend.git
```
then authenticate with your Gitlab credentials.

## Sync repository

[Original repository](https://github.com/GT20timBEAI/GT20SC3) will be periodically updated and you will need to manually sync new changes from your forked, private repository.

In your local machine, set the upstream to original repository
```
cd <base_folder_path>
git remote add upstream https://github.com/GT20timBEAI/GT20SC3.git

```

then checkout to `main` branch and pull new changes from upstream to your remote repository
```
git checkout main
git pull upstream main
```

New changes (if any) should now be on your local machine. Finally, push these changes back to the `main` branch on your private repository
```
git push origin main
```

## Python installation

To install python 3.9, [follow this instruction](https://linuxhint.com/install-python-ubuntu-22-04/).

After completing the installation, check that Python is already installed by running
```
which python3.9
```

Then, you need to install [pip](https://pypi.org/project/pip/) which will be used to install other useful Python packages
```
sudo apt install python3.9-distutils
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.9 get-pip.py

# clean up the installation file
rm get-pip.py
```

Finally, check that the pip is installed by running
```
which pip3.9
```

## Virtual environment

After installing Python, **enable virtual environment** to *isolate your working environment* as you might use different set of Python packages and versions for other projects.

First, run the following
```
pip install virtualenv
```
Then choose **a name for your environment**. For instance, if the environment name is `gt20` then run the following
```
cd <working_folder_path>
virtualenv gt20
```

To start using your new environment, run the following command
```
source <environment_name>/bin/activate
```
If it's successfull, you will see `[environment_name]` on the left side 


Make sure that you are using this environment when you are working on your assignments locally.

To stop using virtual environment, just run
```
deactivate
```
and check that the prefix `[environment_name]` is now gone as well.
