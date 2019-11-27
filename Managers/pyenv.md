# [Pyenv](https://github.com/pyenv/pyenv)

Pyenv manages Python versions 

1. [Macosx]((https://github.com/jeanettejin/HelpfulGuides/blob/master/Managers/pyenv.md#macos))
2. [Ubuntu (Linux)]((https://github.com/jeanettejin/HelpfulGuides/blob/master/Managers/pyenv.md#ubuntu))


## MacOS

1. [Install Homebrew]((https://github.com/jeanettejin/HelpfulGuides/blob/master/Managers/homebrew.md))

2. Use homebrew to install pyenv

   ```bash 
   brew install pyenv
   ```
3. Add lines to `~/.bashrc` and `~/.bash_profile` with:

    ```bash
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
   
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
    echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
   ```  
   Restart Terminal
4. Install whatever version of python you want. Here we install Python 3.7.4

    ```bash
    pyenv install 3.7.4
    ```
5. Set the python version for a given project by `cd project` and running

    ```bash
    pyenv local 3.7.4
   ```

## Ubuntu
1. Install pyenv with

    ```bash
    git clone git://github.com/yyuu/pyenv.git .pyenv
    ```
2. Add to ~/.bashrc
    ```bash
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
    echo 'eval "$(pyenv init -)"' >> ~/.bashrc
    source ~/.bashrc
    ```
   Restart Terminal
   
3. Install whatever version of python you want. Here we install Python 3.7.4
    ```bash
    pyenv install 3.7.4
   ```
   
