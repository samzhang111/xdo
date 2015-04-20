xdo
======

"Oh God, what did I do?"

You should probably never use this, unless you are so desperate to rename
all your files, which I was. And in that case, make a backup. 

The idea is to have a Unix-y tool to propogate actions across globbed
arguments. This was made for executables that takes a variable length
list of positional arguments, and feeds output into the last positional
argument (such as `mv` and `cp`) or writes to standard out (such as
`head` or `tail`).

In the case of `mv` and `cp`, the command is executed on each of the input
files, with the final argument remaining constant (in that case, it is a
directory). `xdo` allows these commands to be executed with different outputs,
defined with a simplified wildcard substitution.

An optional argument for redirecting standard output allows commands like `head`
to be used with the same wildcard syntax.

##Examples:
- I wanted to rename a folder full of wordcounts to reflect the fact that they were all
unigrams, since I was about to add bigrams.

`xdo mv "ngrams/*.csv" "ngrams/*_unigrams.csv"`

- I wanted to slice off the first hundred listings from them, and store them
each into their own files.

`xdo head "ngrams/*.csv" "-n 100" -o "ngrams/*_head.csv"`

Note: The glob and the arguments have to be quoted.

- The file extension can be accessed as a wildcard too.


##Wildcard expansion syntax
####Reserved characters: (these should not be present in filenames)
* `*`: The original filename, or a part of the filename, if used with a dot.
* `#`: The index of the globbing loop, an integer to add prefixes/suffixes 
to files

####Assumptions about usage:

* Rewriting original file extensions is something the user would want to do.
If the destination has a file extension, it will be used to overwrite the
file extension of the input. This allows transformations like
`xdo mv "*.csv" "*.tsv"`, if you misspelled all of your tab-delimited files,
or some DUMB thing you would do.

* Rewriting filenames while preserving file extensions is NOT something the user
would do. They are much more likely to be prepending to the filename. For that
reason, `xdo mv "*.*" "test.*"` prepends all of the files with `test`. I have
no idea if this is a good idea or not. It seems like a stupid edge case in
retrospect, why did I waste my night on this?

* All paths are absolute from the current working directory, and substitition
only happens at the file level, not the directory level.

##Testing

`pip install nosetests`. Run `nosetests` to test.

The symlink to xdo.py is there to facilitate testing.
