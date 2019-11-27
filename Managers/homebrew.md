
# [Homebrew](https://brew.sh)

Homebrew is a package manager for macOS/Linux

1. [Macosx]((https://github.com/jeanettejin/HelpfulGuides/blob/master/Managers/homebrew.md#macos))
2. [Ubuntu (Linux)]((https://github.com/jeanettejin/HelpfulGuides/blob/master/Managers/homebrew.md#ubuntu))


## MacOs


1. Install Homebrew
   ```bash
   /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" 
   ```
  
2. Add lines to `.bash_profile` by executing:

   ```bash
    echo 'export LDFLAGS="${LDFLAGS} -L$(brew --prefix openssl)/lib"' >> ~/.bash_profile
    echo 'export CFLAGS="${CFLAGS} -I$(brew --prefix openssl)/include"' >> ~/.bash_profile
    
    echo 'export LDFLAGS="${LDFLAGS} -L/usr/local/opt/zlib/lib"' >> ~/.bash_profile
    echo 'export CPPFLAGS="${CPPFLAGS} -I/usr/local/opt/zlib/include"' >> ~/.bash_profile
    echo 'export PKG_CONFIG_PATH="${PKG_CONFIG_PATH} /usr/local/opt/zlib/lib/pkgconfig"' >> ~/.bash_profile
    
    echo 'export LDFLAGS="${LDFLAGS} -L/usr/local/opt/sqlite/lib"' >> ~/.bash_profile
    echo 'export CPPFLAGS="${CPPFLAGS} -I/usr/local/opt/sqlite/include"' >> ~/.bash_profile   
   ```
3. Install:

   ```bash
    brew install libomp
    brew install libxml2
    brew install libxslt
    brew install openssl
    brew install postgresql
    brew install pre-commit
    brew install readline
    brew install sqlite3
    brew install xz
    brew install zlib 
   
   ```
   
   
## Ubuntu 

1. Download necessary packages for build

    ```bash 
   sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
   ```
2. Homebrew for Linux

    ```bash
    git clone https://github.com/Homebrew/brew ~/.linuxbrew/Homebrew
    mkdir ~/.linuxbrew/bin
    ln -s ../Homebrew/bin/brew ~/.linuxbrew/bin
    eval $(~/.linuxbrew/bin/brew shellenv) 
   ```
3. Edit ~./profile so path includes the user’s private bin directories

   ```bash 
    echo 'export LDFLAGS="${LDFLAGS} -L$(brew --prefix openssl)/lib"' >> ~/.profile
    echo 'export CFLAGS="${CFLAGS} -I$(brew --prefix openssl)/include"' >> ~/.profile
    
    echo 'export LDFLAGS="${LDFLAGS} -L/usr/local/opt/zlib/lib"' >> ~/.profile
    echo 'export CPPFLAGS="${CPPFLAGS} -I/usr/local/opt/zlib/include"' >> ~/.profile
    echo 'export PKG_CONFIG_PATH="${PKG_CONFIG_PATH} /usr/local/opt/zlib/lib/pkgconfig"' >> ~/.profile
    
    echo 'export LDFLAGS="${LDFLAGS} -L/usr/local/opt/sqlite/lib"' >> ~/.profile
    echo 'export CPPFLAGS="${CPPFLAGS} -I/usr/local/opt/sqlite/include"' >> ~/.profile
   ```
4. Install:

    ```bash
    brew install libompbrew 
    brew install libxml2
    brew install libxslt
    brew install openssl
    brew install postgresql
    brew install pre-commit
    brew install readline
    brew install sqlite3
    brew install xz
    brew install zlib
   ```

