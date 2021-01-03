## Git Config
_set username or email_

    git config --global user.name + username 
    git config --global user.email + email 
_check all configs_

    git config --list

## Get help at using Git
   _add --help at the end of the function name_
   
    git config --help
    git add --help
    git help config

## Some Terminal Commands
    ls - lists all of the folders 
    ls -la - lists all of the files 
    cd .. - returns one dir back 
    cd - enters a directory
    . - just install in the current directory
## Clone a repository to local
- Create a git repository
- Open #cmd
- Type in cd <filename>
    > cd Downloads
- Type in *> git clone + repository URL* to download the repository
- Download finished.

## Check changes between local and git repositories
- Set current workspace to the local git folder
        
        > cd Download/GitTest

- Type in git status to see the difference

        > git status

- Type in git add + new file name to upload the new script.
type with double quotes when there's a space in the filename.

        > git add "SamplePython.py"
    or type with escape char

        > git add Sample\ Python.py
    add all files to the repo

        > git add -A or git add . 

- Restore the changes, if no filename after reset, then all files will be restored.

        > git reset <filename>

## Write commit and update the file in Github.com
- A new commit is necessary as an explanation when making changes to the repository

        > git commit -m "added Sample Python.py to the repo"

- To renew the repo on Github.com, use git push

        > git push
    u will associate the local branch with remote branch

        > git push -u origin GitTest 
        
- Download new changed files to the local repo

        > git pull 

## Git Branch
- Basic command
    
        > git branch <branch name>
        > git branch -a  "see all remote branches"
        > git checkout master "switch the branch to master"
        > git push origin master "push the master branch"
        > git diff "see difference between local and remote file"

- To merge the branch with master branch 

        > git branch --merged "check what branches merged"
        > git merge <branch name>

- Delete a branch

        > git branch -d <branch name>
