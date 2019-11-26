  
# Running Something in Screen Session

[What is a screen session?](https://linoxide.com/linux-command/15-examples-screen-command-linux-terminal/)
> The screen is a terminal multiplexer. Using this, you can run any number of console-based-applications, interactive command shells, course-based applications, etc. You can use screen to keep running program after you accidentally close the terminal, or even after you log out and later resume right wherever you are.
>
> When screen is called, it creates a single window with a shell in it (or the specified command) and then gets out of your way so that you can use the program as you normally would. Then, at any time, you can create new (full-screen) windows with other programs in them (including more shells), kill the current window, view a list of the active windows, copy text between windows, switch between windows, etc.

>


1. Start a Screen Session

   ```bash 
   screen -S name_of_screen 
   ```
   Note that if you get the following error
   ```bash
    Cannot open your terminal '/dev/pts/0' - please check.
   ```
   Excute
   ```bash
   script /dev/null
   ```

2. Run whatever you want to run

   ```bash
   python3 -m path.to.your.script.py
   ```

3. Detach from screen and allow script to keep running with the shortcut Ctrl + A, D

4. Reopen screen session with

   ```bash 
   screen -r name_of_screen
   ```
   
This is an awesome resource: [screen_cheatsheet](https://gist.github.com/jctosta/af918e1618682638aa82)