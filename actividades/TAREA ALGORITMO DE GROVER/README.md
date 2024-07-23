# TAREA ALGORITMO DE GROVER 

## Investigation

The 3-SAT problem, short for 3-Satisfiability problem, is a classic example of a computational problem categorized as NP-complete, a classification indicating both its complexity and intractability under current computational paradigms. Here’s why the 3-SAT problem is considered intractable:

## Definition of 3-SAT

The 3-SAT problem is a specific type of Boolean satisfiability problem where one must determine whether there exists an assignment of truth values (true or false) to variables that makes a Boolean formula true. The formula is expressed in Conjunctive Normal Form (CNF) and consists exclusively of clauses with exactly three literals (variables or their negations).

## NP-Completeness

The designation of NP-complete is pivotal in understanding the intractability of the 3-SAT problem. A problem is in NP (Nondeterministic Polynomial time) if a solution can be verified in polynomial time given a candidate solution. A problem is NP-complete if it is in NP and as hard as any problem in NP, meaning any NP problem can be reduced to it in polynomial time.

## Exponential Growth of Possible Assignments

The number of possible assignments of truth values to variables grows exponentially with the number of variables. For instance, if a 3-SAT problem has \(n\) variables, there are \(2^n\) possible combinations of truth values to check. As \(n\) increases, even by small amounts, the size of the problem space explodes, making exhaustive search methods impractical.

## Lack of Efficient Algorithms

Despite extensive research, no polynomial-time algorithm has been discovered for solving 3-SAT problems (or any NP-complete problems) on classical computers. This limitation isn't just a temporary gap in algorithm development; it's tied to the foundational constraints of how problems scale and how resources (like time and computational power) scale in response.

## Implications of the P vs NP Problem

The intractability of the 3-SAT problem is closely linked to the unresolved question in computer science known as the P vs NP problem. If it were possible to solve 3-SAT problems in polynomial time, it would imply \(P = NP\), meaning every problem whose solution can be verified quickly can also be solved quickly. However, the prevailing belief among computer scientists is that \(P \neq NP\), suggesting that problems like 3-SAT inherently require superpolynomial time to solve in the worst case.

## Practical Impact

The intractability of the 3-SAT problem has practical implications in fields like cryptography, where the hardness of certain computational tasks is used to secure data and communications. It also influences how algorithms are designed, directing focus toward approximate solutions or probabilistic algorithms rather than exact solutions for large instances.

In summary, the 3-SAT problem's classification as NP-complete highlights its intractability, making it a quintessential example of problems that are easy to define and check but potentially extremely hard to solve.

# Workshop
To prepare 3-SAT example exercises for solving with Grover's algorithm, we'll create three Boolean satisfiability problems with three variables each. These problems are defined using clauses in conjunctive normal form (CNF), where each clause is a disjunction (OR) of three literals (variables or their negations). Here are three examples:

### Example 1: 3-SAT Problem

#### Variables: x, y, z

##### Clauses:
1. (x OR NOT y OR z)
2. (NOT x OR y OR NOT z)
3. (x OR y OR NOT z)

##### Task:
Determine the truth values of x, y, and z that satisfy all clauses.

### Example 2: 3-SAT Problem

#### Variables: a, b, c

##### Clauses:
1. (a OR NOT b OR c)
2. (NOT a OR NOT b OR c)
3. (a OR b OR NOT c)

##### Task:
Determine the truth values of a, b, and c that satisfy all clauses.

### Example 3: 3-SAT Problem

#### Variables: p, q, r

##### Clauses:
1. (NOT p OR q OR r)
2. (p OR NOT q OR r)
3. (p OR q OR NOT r)

##### Task:
Determine the truth values of p, q, and r that satisfy all clauses.

---

## SOLVING WITH GROVER'S ALGORITHM

To solve these using Grover's algorithm:
1. Represent each variable and its negation as quantum states.
2. Use Grover's algorithm to amplify the probability amplitude of states that satisfy all clauses.
3. Measure the quantum register to observe the solution.
4. Write a report showing the experiments.

   
Grover's algorithm is particularly suited for these problems as it can efficiently search through all possible assignments of truth values to find those that satisfy the CNF formula, especially when the number of solutions is small relative to the total search space.
