~~~~~~~~~
coin-toss
~~~~~~~~~

.. contents::
   :local:

Intent
======

These scripts were created to assist with internet voting in the event of a
tie, such that election officials could perform a verifiable, repeatable
tie-breaking procedure: a remote coin toss.


Usage
=====

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
=====

When a fellow employee at DreamHost (Steven Berler) reviewed this, he noted
that a corrupt election official could generate seeds until one was obtained
that broke the tie according to personal preference.


Protection
==========


Avoiding Abuse with Policy
--------------------------

One way to mitigate this would be to announce ahead of time the seed or a
means of deriving the seed, based on information available to all the election
officials only after a tie had been announced.


An Election with a Tie
-----------------------

Let's suppose we have an election where Alice and Bob are clear winners, but
there is a tie for third between Carol and Dave. Eve comes in last. Let's say
that the election data for the tied candidates is as follows:

* Carol: loses to Alice by 40-47; loses to Bob by 38-45; beats Dave 41-40;
  loses to Eve 40-41

* Dave: loses to Alice 29-54; loses to Bob by 26-48; loses to Carol; 40-41;
  beats Eve 44-42


An Example Policy
-----------------

For such occasions, one could -- ahead of time! -- define a policy that would
utilize this data to generate a seed whereby tie-breaking coin-tosses could be
verified by any election official.

An example of this might be:

* Get the pre-announced seed. Ideally, this seed will be generated based on the
  timestamp of the election announcement. With the understanding that only one
  election will be announced at that microsecond with the given set of
  candidates, this date-based seed should help in making a unique seed for
  breaking a possible future tie.

* In the event of a tie, list the candidate scores in descending order (we've
  sepearated each win/loss with a colon). In this example, we append the votes
  in candidate-name alphabetical order (Carol's scores are first, then Dave's).

* Using these known and unique (once combined) pieces of data, generate a new
  seed::

     $ ./bin/get_seed --as-uuid \
        --data=3641f821-6fb4-7d51-94e1-dce0e92f4571
        --data=40-47:38-45:41-40:40-41
        --data=29-54:26-48:40-41:44-42
     c1492281-a8d9-e6c5-03f8-992f9d5331f8

* With this new seed, one could then perform the coin-toss::

     $ ./bin/toss c1492281-a8d9-e6c5-03f8-992f9d5331f8 Carol,Dave
     ['Dave']
