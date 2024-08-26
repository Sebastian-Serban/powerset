## Task
<p>For the given set <code>S</code> its powerset is the set of all possible subsets of <code>S</code>.</p>

<p>Given an array of integers nums, your task is to return the powerset of its elements.</p>

<p>Implement an algorithm that does it in a depth-first search fashion. That is, for every integer in the set, we can either choose to take or not take it. At first, we choose <code>NOT</code> to take it, then we choose to take it(see more details in exampele).</p>

## Example

<p>For <code>nums = [1, 2]</code>, the output should be <code>[[], [2], [1], [1, 2]].</code></p>

<p>Here's how the answer is obtained:</p>

<pre><code>don't take element 1
----don't take element 2
--------add []
----take element 2
--------add [2]
take element 1
----don't take element 2
--------add [1]
----take element 2
--------add [1, 2]
</code></pre>

<p>For <code>nums = [1, 2, 3]</code>, the output should be
<code>[[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]</code>.</p>

## Input/Output
<p><code>[input]</code> integer array <code>nums</code></p>

<p>Array of positive integers, <code>1 ≤ nums.length ≤ 10</code>.</p>

<p>[output] 2D integer array</p>

<p>The powerset of nums.</p>

<p>Run the main.py file</p>

```bash
python main.py
```


