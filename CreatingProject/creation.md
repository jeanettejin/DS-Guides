# Putting it all together and creating a project using poetry and pyenv



1. Create new project with poetry. Make sure you are in the directory that you want your project to be in. For example I would first `cd Projects` and then run the following command
    ```bash
    poetry new new_project
    ```
    ```bash
    cd new_project
    ```
2. Set the python version

   ```bash
   pyenv local 3.7.4
   ```
   
3. Go to github and click on the "+" to create a new repo. 
   
4. Push to Github

   ```bash
   git init
   git add .
   git commit -m "First Commit"
   git remote add origin https://github.com/yourUsername/new_project.git
   git push origin master
   
   ```
   
   


