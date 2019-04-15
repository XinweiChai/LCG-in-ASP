# Reachability Analysis and Model Revision

A Python 3.6 program
## Input Model

Automata Network (AN) uses extension ``.an``. A typic ``.an`` file contains three parts: variable declaration, transition and initial states. 

Example:
```
a [0,1]
b [0,1]
c [0,1]
a 0 -> 1 when b=0 and c=0
initial_state a=0, b=0, c=0
```
For now the program only supports Boolean variables, so that each variable need to be declared with **[0,1]**. 

To load a model, use  **variable, transitions, transitions_by_hitter, initial_state, start_node = read_ban(*path_of_model*)** where **start_node** designates the local state to be reached, for example **("a", 1)**.

## Generate Random Models

**generate_files(*models, size, num_tran*)** in ``generate_model.py`` creates a folder containing Automata Networks with the number of models ***model***,  each model containing the number of automata ***size*** and the number of transitions ***num_transition***,  models are saved in folder ``data//model_#size``.

## Reachability Analyzers

PermReach and ASPReach aim at solving reachability problem efficiently and deal with inconclusive cases during the use of pure static analysis. They launch heuristics based on static analysis. 

- Package ``pyasp``  is required (download via ``pip3``)

Call **one_run_with_options(*f_network, input_init, change_state, start, return_dict, option*)** with ***f_network*** the file name, ***input_init*** the initial state,  ***change_state*** to change the initial state when there are multiple tests,  ***start*** the target state, ***option*** the execution mode, ***option=0*** using pure ASP solver  ***option=1*** using ASPReach ***option=2*** using PermReach.

PermReach uses a weaker heuristics, which is strong in runtime but weak in conclusiveness while ASPReach costs more runtime but more conclusive.

## Revision

### Diverse Tools
In ``crac/models.py``,
- **generate_random_continuous_model(*num_var*)** is used to generate a linear differential equation model.
- **evolve(*initial_state, period, eq, noise*)** is a time-series data generator based on the model done by **generate_random_continuous_model**

``m2rit/reach.lp`` and ``m2rit/reach_global.lp`` are respectively local/global model checkers for 3 components.

### Cut Set

Given an AN and a reachable local state different from initial state,  **rev_cut_set(*filename, start_node*):** returns the cut set to inhibit the reachability of ***start_node*** in the model in ***filename***.

### Completion set

Likewise,  **rev_completion_set(*filename, start_node*):** returns the completion set to guarantee the reachability of ***start_node*** in the model in ***filename***.

### LFIT (Learning From Interpretation Transitions)

Usage of asynchronous LF1T by Tony Ribeiro ([https://hal.archives-ouvertes.fr/hal-01826564/document](https://hal.archives-ouvertes.fr/hal-01826564/document)):

	``./AS_LFIT -i <input filename> > <output filename>``

### CRAC (Completion via Reachability And Correlations)
In ``crac/revsion``, **overall(*filename, re, un*)** returns a completed model based on the original model ***filename***, reachable set ***reachable*** and unreachable set ***unreachable***.
### M2RIT (Model Revision via Reachability and Interpretation Transitions)
In ``m2rit/util``, **overall(*filename, re, un*)** returns a completed model based on the original model ***filename***, reachable set ***reachable*** and unreachable set ***unreachable***.

### Author
Xinwei Chai, if you have any questions, please contact xinwei.chai@ls2n.fr

or more information at https://pagesperso.ls2n.fr/~chai-x/