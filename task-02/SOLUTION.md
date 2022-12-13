# Terminal Hunt 
## Solution 
Firstly i began by cloning the repository using the git clone command in my terminal window.
I then made a new folder called solution using mkdir command and then access the same folder using cd command.
I then created a file named part1.txt using the command ```touch part1.txt ``` and then I edited to the file using ```cat > part1.txt```

### Part-01
Later I used ```cd 06``` to navigate to folder #6 and then I copied the file to my solution file directory.
To rename the file i used mv 1.txt to part2.txt.
used ```cd ..``` a lot of times to circle back and forth folders.

### Part-02
```git log``` command was used to check the commit history which was a clue for finding part3.txt
I copied and renamed the file using ```mv``` command which i found in the previous stage.

### Part-03
Then i committed the files using the command ```git commit -a -m "commit message"```
```git checkout asia``` to swirch branch to asia and then find.-name athens.txt inorder to check if the file was present there.
Then i used ```git checkout main``` to go back to main branch and then ```git merge asia``` to merge the two branches.
Copied the file to solution directory and renamed using ```mv```

### Final Steps
Then inorder to write the final password, I used ```cat > password.txt 'password' to write my password to my file password.txt
And,then finally I used ```rm``` to remove part1.txt,part2.txt,part3.txt and part4.txt.




