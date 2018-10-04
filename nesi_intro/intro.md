# Nesi intro

## Summary

This is a quick quick quick guide of the thing I usually go over with new users of NeSI. It allows me and other users to remember the important bits we talk about. It does not replace an intro to command line and is less complete than NESI guides but it allows a quick overview of the basics.

## 1. A comfy home

When you connect first to mahuika, it is a good idea to make yourself a comfortable home as your project will be away from the place you log in to.

You can create a symbolic link to your project (i.e.) a door to your project.

```
ln -s /nesi/projects/MYPROJECTID/ . # in my case MYPROJECTID is uoo00116
```

Now you have your project at your door. you can just enter it with **cd**.

While we are in the home directory, let's create a **bin/** folder for the software you need to install yourself.

```
mkdir bin
```

And add it to the path so that any software located in there can be found by the machine.


```
nano ~.bash_profile
##ADD the following line at the end, don't delete anything in this file!
PATH=$PATH:~/bin
```

Then **ctrl+x** and **y** to close nano. Now your bin is added to the PATH and you have a comfy home.

## 2. Copy data

If you need to copy data from your computer to Nesi use scp. It works like this

```
scp from to
```

For example, if you have . a folder on your Desktop and you wanted on your NESI home:

```
scp  =r ~/Desktop/test    USERNAME@login.mahuika.nesi.org.nz:/home/lUSERNAME/ # replace USERNAME with your nesi username
```

## 3.Find installed softwares


Let's see if BEAST is already installed:


```
module spider beast
```

```
----------------------------------------------------------------------------
  BEAST:
----------------------------------------------------------------------------
    Description:
      BEAST is a cross-platform program for Bayesian MCMC analysis of
      molecular sequences. It is entirely orientated towards rooted,
      time-measured phylogenies inferred using strict or relaxed molecular
      clock models. It can be used as a method of reconstructing
      phylogenies but is also a framework for testing evolutionary
      hypotheses without conditioning on a single tree topology. BEAST uses
      MCMC to average over tree space, so that each tree is weighted
      proportional to its posterior probability.

     Versions:
        BEAST/1.8.4-gimkl-2017a-no-beagle
        BEAST/2.4.7

----------------------------------------------------------------------------
  For detailed information about a specific "BEAST" module (including how to load the modules) use the module's full name.
  For example:

     $ module spider BEAST/2.4.7
--------------------------------------------
```

We can just load it like this:

```
module load BEAST
```

and check all our loaded modules...

```
module load BEAST
```
Yes

## 4. run jobs
Let's create a  wee script.

Open a text editor and a new script file:

```
nano demoscript.sh
```

and put a simple inside

```
#!/bin/sh
echo "this is myfirstscript" > myfirslog.txt
```

Then first line is telling your machine that this is a shell (bash) script.

Then **ctrl+x** and **y** to close nano.


Let's submit demoscript.sh.

Have a look at the options of the sbatch command that submit obs


```
sbatch --help
```

 to mahuika with 2 days, 1 hours, 2 minutes and 3 secondes on one node with 8 cores and a total of 16Gigs of RAM

``` 
sbatch -A uoo00116 -t 2-01:02:03  -N 1 -c 8 --mem=16G demoscript.sh


```

Visualize my queue of jobs

```
squeue -u $USER 
```

$USER is a variable that contains your username.you can try:
```
try  echo $USER
```
It would take forever to start anyway, lets cancel my jobs

```
scancel -u $USER # you can also cancle jobs directly with jobid (i.e. scancel 3546577)
```
