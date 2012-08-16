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

``toss`` also supports multi-way ties and multiple winners::

  $ ./bin/toss 3641f821-6fb4-7d51-94e1-dce0e92f4571 Alice,Bob,Carol \
        --winner-count=2
  ['Bob', 'Carol']

Abuse
-----

When Steven Berler reviewed this, he noted that a corrupt election official
could generate seeds until one was obtained that broke the tie according to
personal preference.

One want to mitigate this would be to announce ahead of time the seed or a
means of deriving the seed, based on information available to all the election
officials only after a tie had been announced.

For instance, the election data itself could serve as the seed. If Alice and
Bob are clear winners, but there is a tie for third between Carol and Dave, we
could use the following data to generate a seed:

* Carol: looses to Alice by 40-47; looses to Bob by 38-45; beats Dave 41-40;
  looses to Eve 40-41

* Dave: loses to Alice 29-54; looses to Bob by 26-48; loses to Carol; 40-41;
  beats Eve 44-42

Then define a policy for using this data. An example of this might be:

* Get the pre-announced seed.

* In alphabetical order of the candidate names, list the candidate scores in
  descending order.

* Using these two known and (combined) unique pieces of data, generate a new
  seed::

     $ ./bin/get_seed --as-uuid \
        --data=3641f821-6fb4-7d51-94e1-dce0e92f4571
        --data=40-47:38-45:41-40:40-41
        --data=29-54:26-48:40-41:44-42
