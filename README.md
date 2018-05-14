# LCG-in-ASP

Heuristic analyzer ASPReach

This program is aimed to solve the problem of inconclusiveness during the use of pure static analysis. Our analyzer also avoids global searching. It launches heuristics based on static analysis. ASP-based approach gives possible firing order of local states, which is at the same time efficient and conclusive.

- Before running, pyasp package is required (can be downloaded via pip3)
- Automata Network format:
```
a [0,1]
b [0,1]
a 0 -> 1 when b=0
initial_state a=0, b=0
```
- Run by python3.6 main.py
- Useful functions which could be put in main.py:
```
generateFiles(models, size, num_tran)
```
Create a folder containing Automata Networks with the number of models ```model```, number of automata ```size``` and the number of transitions ```num_transition``` , models are saved in the folder ```model_size```.





### Author
Xinwei Chai, if you have any questions, please contact xinwei.chai@ls2n.fr


