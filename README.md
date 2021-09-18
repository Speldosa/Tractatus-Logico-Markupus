# Overview

Tractatus-Logico-Markupus is a simple markup language that lets you embed a logical-hierarchical structure in your text that's easy to read and that's easy to remove when you wish to produce more normal looking text. This form of writing is inspired by the style in Ludwig Wittgenstein's book *Tractatus Logico-Philosophicus*, hence the name.

# The Tractatus markup language

The `@` symbol followed by a letter is used to denote a certain category of information. Right now, there are three different type of tags available: `@H`, `@T`, and `@C`. They denote headings, to-dos, and comments. Here's an example of how they can be used in a document:

```
@H This is a heading.
@S This is a summary.
@N This is a note.
@T This is a to-do.
@C This is a comment.
This is some text that's going to be retained in the final document. It can contain other type of markup code such as, for example, Markdown, LaTeX, or HTML.
```

Tabs are used to denote how a certain piece of information fits into the overarching logical structure of the text. For example:

```
@H Winter is great...
I really like the winter. This I do mainly because of three different reasons:
  @H Schadenfreude
  @T I should try to re-write this so that I don't come off as evil.
  I like to laugh at people who get's depressed during winter,
  @H No overheating of my computer
  my computer never overheats no matter how much I throw at it
    @H Caveat
    (given that I keep my balcony door open),
  @H Stars
  @C I earlier referenced that you can see the Orion constellation during winter, but I don't know if it's relevant. Anyhow, I can keep that information here in case I want to add it again.
  and you can see the stars during night much clearer.
```

When removing all the Tractatus markup, the text above would look like this:

```
I really like the winter. This I do mainly because of three different reasons: I like to laugh at people who get's depressed during winter, my computer never overheats no matter how much I throw at it (given that I keep my balcony door open), and you can see the stars during night much clearer.
```

# Running the Tractatus markup removal script

To run the Tractatus removal script, you should have [Python 3](https://www.python.org) installed on your computer. Navigate to the folder where you downloaded Tractatus-Logico-Markupus and write:

```python
python Tractatus.py path_to_input_file path_to_output_file
```

The `path_to_input_file` obviously have to be an existing file but the `path_to_output_file` can be specified freely. If the output file doesn't already exist, it will be created. If it does exist, it will be overwritten.

You can for example run the test file by typing:

```python
python Tractatus.py Input_test/Input_test.txt Output.txt
```

This will create the output file `Output.txt` in the root folder.
