# [Poetry](https://poetry.eustace.io)

Poetry manages python packages

1. [Macosx]((https://github.com/jeanettejin/HelpfulGuides/blob/master/Managers/poetry.md#macos))
2. [Ubuntu (Linux)]((https://github.com/jeanettejin/HelpfulGuides/blob/master/Managers/poetry.md#ubuntu))


## MacOS
1. Install Poetry with 

    ```bash
    curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python3
   
   ```
2. Edit `~/.bash_profile` and `~/.bash_rc`

    ```bash 
   echo 'source $HOME/.poetry/env' >> ~/.bash_rc
    
   echo 'source $HOME/.poetry/env' >> ~/.bash_profile
   echo 'export PATH="$HOME/.poetry/bin:$PATH"' >> ~/.bash_profile 
   ```
   Restart Terminal
## Ubuntu

1. Install Poetry with 

    ```bash
    curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python3
   
   ```
2. Edit `~/.profile` and `~/.bashrc`

    ```bash 
   echo 'source $HOME/.poetry/env' >> ~/.bashrc
    
   echo 'source $HOME/.poetry/env' >> ~/.profile
   echo 'export PATH="$HOME/.poetry/bin:$PATH"' >> ~/.profile 
   ```
   Restart Terminal
