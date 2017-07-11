# Python DAG Longest Path

An algorithm that finds the length of the longest path starting from vertex 0 in a DAG, done for an Algorithms and Data structures paper.

## Algorithm:

First: Find a topological ordering of the given DAG.
Then: For each vertex v of the DAG, in the topological ordering, compute the length of the longest path ending at v by looking at its incoming neighbors and adding one to the maximum length recorded for those neighbors. If v has no incoming neighbors, set the length of the longest path ending at v to zero. In either case, record this number so that later steps of the algorithm can access it.


## Input:

The input consists of a sequence of one or more DAGs. Each DAG D is represented
by an adjacency list. The first line is an integer n that indicates the order of D. This is followed by n
white space separated lists of adjacencies for vertices labeled 0 to n − 1. The input is terminated by
a line consisting of a single zero. This line should not be processed. Each input DAG may contain up
to 5000 vertices and 10000 arcs.

## Output:

The output is a sequence of lines, one for each input DAG. Each line contains a
single integer indicating the length of the longest path starting from vertex 0.
	
## Usage

To get started with the script, clone the repo and then specify an input file and output file. Example files are provided:

```
$ python3 path.py < test-cases.in > mytestcases.out
```

Compare the result using diff (No differences will return if correct:

```
$ diff test-cases.out mytestcases.out
```