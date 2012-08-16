~~~~~~~~~
coin-toss
~~~~~~~~~

Intent
------

These scripts were created to assist with internet voting in the event of a
tie, such that election officials could perform a verifiable, repeatable
tie-breaking procedure: a remote coin toss.

Usage
-----

First, you'll need to generate a seed that can be shared with anyone who will
be verifying the coin toss::

  $ ./bin/get_seed
  3641f821-6fb4-7d51-94e1-dce0e92f4571

With the seed, you can now do a coin toss::

  $ ./bin/toss 3641f821-6fb4-7d51-94e1-dce0e92f4571 Alice,Bob
  ['Bob']

This also supports multi-way ties and multiple winners::

  $ ./bin/toss 3641f821-6fb4-7d51-94e1-dce0e92f4571 Alice,Bob,Carol \
        --winner-count=2
  ['Bob', 'Carol']
