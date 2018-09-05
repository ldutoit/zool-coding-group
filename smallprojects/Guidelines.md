# Guidelines

## Summary

This document summarizes the 3 phases of our little project as well as the objectives and the timeline. It can be something from your own research, biology or not. Something fun is fine too!


## Objectives
 
 The main pobjective is that your project should be shareable. If it is a data visualisation script, it should be usable by someone else provided similar data formats. If it is a video game, it should be playable by someone else, etc...
 To achieve this: 
 * You will share your poject as a github repository. You will also share example data if it is something that requires special data format or files.
 * You will document your code
 * You will try to write nice code as much as possible:
    * Write functions
    * Avoid repetitions
    

## Process

### Timeline


This is a one month project. Keep it reasonably sized! We'll have individual interaction once you start writing your code but here is the timeline:

* September 13 : present your idea and your pseudocode in an informal way, 5mn.
* September 27 : You should have a running project and share the code with me so that I can comment.
* October 4: Small presentation of your project using your github, I'll bring cookies!



###  1. Get an idea and write the pseudocode

Once you have an idea of a project, you will try to deconstruct your project into smaller step to write the *pseudocode*. This is code written in plain english to help you lay down the structure of your project. It could start by simply being big steps like:

```
# Read the sequence
# Output basic statistics
```

and slowly become something much more precise:

```
#Read the data
## Ask user for input file
### create a sequence dictionnary that will store all my sequences
### Read file line by lin
  if  the line starts with ">":
    this a new sequence... store it
  else:
    add this line to the last sequence
### Calculate statistics
 for sequence in sequences:
        print gc content and length 
  

```
The more [precise](http://www.unf.edu/~broggio/cop2221/2221pseu.htm) it is, the more structured your ideas are andthe easier the coding will be!
To help you do this, do it iteratively getting slowly more precise.
Keep questions in mind like:

* What will be the input and the output for your project?
* What should be the main functions?
* What should be the main objects and what will they contain or do?


### 2. Transform it into code

Take your pseudo code and start filling in code. Use google a lot for the problems and also our [slack](https://www.google.com/url?q=https://bioinfo-grouptalk.slack.com/&source=gmail&ust=1536201497630000&usg=AFQjCNGgd_DKvBsG7ekm55enZGI4t2p9-w) project channel ( also use me!). I'll meet you once a week individually (more if needed) during this time so we can keep it going. Once it is ready, share it with me as a slef contained github repository containing a README, a case example if relevant and the actual code.

### 3. Present it to everyone

Once you shared the code with me, you can prepare a small presentation for everyone. You will present to everyone on our regular thursday meeting October 4.

