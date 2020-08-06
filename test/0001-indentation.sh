#!/bin/bash

# test1 ignore whitespace changes

# For a review all this changes should be mutted, as doesn't make a difference
# in logic only indentation

TMPDIR=$(mktemp -d)
git init $TMPDIR
cd $TMPDIR
cat >main <<EOF
int main(string a, int b) {
	print("hello");
}
EOF
git add .
git commit -m "first commit"
cat >main <<EOF
int main (string a, int b)
{
  print ("hello");
}
EOF
git add .
git commit -m "change indentation"

cat <<EOF
---
 Expected an empty diff
---
EOF

git show | filter-word-diff

rm -rf TMPDIR
