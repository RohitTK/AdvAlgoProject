# Reduction of general Steiner tree problem to metric Steiner tree

"""
Algorithm Steps:

Step 1: For the given graph input, a new complete graph needs to be created where
        the cost of edge (u,v) needs to be the shortest u-v path. (Metric Closure)
Step 2: To find the shortest path, we can use the Dijkstra algorithm.

Expected Input: Weighted Graph and Required Vertices
Expected Output: A complete weighted graph (Satisfying triangle inequality) and a set of required vertices
"""