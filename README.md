# word-diff-filter

Dealing with diff is a hard thing. You want to focus on big picture, what changes, what matters, but there's a lot to remove from a simple diff to make it usable (at least for a review)

Alghorithms like patience try to reorder diffs but thats not enough. 

One of the most disrupting noise inside diffs is about indentation changes. They generate a lot of attention in a diff but in almost all code they are just a step further to ignore-whitespace, I want to take that step!

By now this is a filter for **git diff --word-diff=porcelain** which works on **--color** or plain output, I will work to provide an ecosystem to ease it use.

# Test

```bash
$ git clone https://github.com/albfan/filter-word-diff.git
$ cd filter-word-diff/
$ ln -s $(pwd)/filter-word-diff.py ~/bin/filter-word-diff
$ cd <path-to-your-repo>
$ git diff --word-diff=porcelain --color master feature | filter-word-diff
```

