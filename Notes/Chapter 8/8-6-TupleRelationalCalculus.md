# Tuple Relational Calculus

** Referencing 'Fundamentals of Database Systems' by Elmasri and Navathe, 7th edition **

## Foreword

This is my own interpretation of Tuple Relational Calculus as described in the book. I have tried to simplify the concepts and provide examples to make it easier to understand as I struggled with it myself. I hope this helps you understand Tuple Relational Calculus better. Glossary terms will be filled in [Chapter 8's Glossary](./8-Glossary.md)

## Introduction

[Tuple Relational Calculus](./8-Glossary.md#tuple-relational-calculus) (TRC) is a non-procedural query language. It is a declarative language that specifies what to do, not how to do it. It is based on the concept of selecting tuples from a relation. The result of a Tuple Relational Calculus query is a set of tuples that satisfy the given condition.

TRC is a nonprocedural language - the focus is on what to retrieve, not how to retrieve it. The user specifies the desired information without specifying the method of getting it. The user provides a formula that describes the desired data, and the system is responsible for converting the formula into a sequence of operations to retrieve the data.

All queries that can be specified in relational algebra may also be specified in TRC, and vice versa. 

## 8.6.1 Tuple Variables and Range Relations

TRC is based on specifying a number of [tuple variables](./8-Glossary.md#tuple-variable) that range over the tuples of a relation. A tuple variable is a variable that 'stands for' a tuple. The relation over which the variable ranges is called the [range relation](./8-Glossary.md#range-relation) of the variable.

A tuple variable is usually denoted by a single letter such as t, u, or v. The range relation of a tuple variable is the relation over which the variable ranges. The range relation is specified by the user in the query. 
An example of a tuple variable is :
`{t | e ∈ EMPLOYEE}` where t is the tuple variable and EMPLOYEE is the range relation. The element of symbol, ∈, is used to denote that t is an element of EMPLOYEE. This query would return all tuples in the EMPLOYEE relation.

In this example, the tuple variable t ranges over the EMPLOYEE relation. The query retrieves all tuples in the EMPLOYEE relation. The result of this query is a set of tuples, each of which is a tuple in the EMPLOYEE relation. It's important to note that the result of a TRC query is a set of tuples, not a relation itself. 

While trying to understand TRC, I found it helpful to analyze the query in parts.

`{t |` : This section of the query specifies that we are defining a tuple variable t. It is very much like the SELECT clause in SQL or relational algebra's π operator.

We can pass it specific attributes we are returning:
`{t: firstname, lastname |` : Here we are saying we want the firstname and last name.
* Note: While doing this, we also assign their value later in the query.

Example:
`{t: firstname, lastname | e ∈ EMPLOYEE AND t.firstname=e.firstname AND t.lastname=e.lastname}`

We also should pass the there exists symbol, ∃, to denote that there is a tuple in the relation that satisfies the condition. So let's update this to be more correct:
`{t: firstname, lastname | ∃ e ∈ EMPLOYEE AND t.firstname=e.firstname AND t.lastname=e.lastname}`

There exists, ∃, is used to denote that there is a tuple in the relation that satisfies the condition. It is used to specify the condition that the tuples in the result must satisfy. It is also known as the existential quantifier.

There is another quantifier that I have struggled with, the universal quantifier, ∀. It is used to specify that all tuples in the relation must satisfy the condition. It is used to specify the condition that the tuples in the result must satisfy.

If we are to use the universal quantifier, we would use the ∀ symbol. For example:
`{t: firstname, lastname | ∀ e ∈ EMPLOYEE AND t.firstname=e.firstname AND t.lastname=e.lastname}`

Note: we use the universal quantifier when we want to retrieve all tuples in the relation that satisfy the condition. The universal quantifier is used similar to sql's WHERE clause.

It has been helpful to think of the universal quantifier and existential quantifier in terms of loops in a programming language. For example, let's say we needed to find ONLY the employees who have worked in the company for more than 5 years. We would use the universal quantifier because we are looking for all employees who have worked for more than 5 years.

### Implies Operator

The implies operator, →, is used to specify that if the condition on the left side of the operator is true, then the condition on the right side of the operator must also be true. It is used to specify the condition that the tuples in the result must satisfy. However, it can *also* be used as a means of negation.

Here is an example of the implies operator:
`{t: firstname, lastname | ∃ e ∈ EMPLOYEE AND t.firstname=e.firstname AND t.lastname=e.lastname AND e.salary > 50000 → e.department = 'HR'}`
Let's break down this query in simple terms. First, we are defining a tuple variable t that has the attributes firstname and lastname. We are saying that there exists a tuple e in the EMPLOYEE relation that has the same firstname and lastname as t. This binds the values of t to the values of e, fulfilling the bound variable concept. We go on to say not only does e have the same firstname and lastname as t, it also says that if e's salary is greater than 50000, then e's department must be HR. This is the implies operator at work.

This is similar to an if statement, but with an exception. 

A ==> B. Let's say 'if A, then B'. So now give A the value of 'it is raining' and b the value of 'the ground is wet.' So if it is raining, then the ground is wet. However, B can be true even if A is false. So if the ground is wet, it doesn't necessarily mean it is raining. This is the same concept with the implies operator.
The truth table for implies looks like this:

```
A | B | A ==> B
T | T | T  
T | F | F  
F | T | T  
F | F | T
```
Implication is any if, then statement. If A, then B. If A is true, then B is also true, thefore A implies B. 

Let's break this down a bit further...

A, sometimes referred to as p, is the antecedent or the conditional. B, sometimes referred to as q, is the consequent. 
The antecedent is the statement that is the premise of the implication. The consequent is the statement that is the conclusion of the implication.
A and B, or p and q, could be any statement at all.
Another example:
Line 1: "I studied" and "I passed the test", therefore it is implied that if you study, then you pass the test.
Line 2: "I studied" and "I failed the test". If I studied, but I failed the test, then the implication here that studying leads to passing tests is false (ask me about my midterm). 
Line 4: "I didn't study" and "I failed the test". If you didn't study, and you failed the test, does A imply B? Yes, because you failed the test. So not studying implies failing the test.
**Okay, those make sense... but what about the third line?**
Line 3: "I didn't study" and "I passed the test". 

This is where I get tripped up. Why does not studying imply passing the test? It doesn't make sense. But it does. The implication is true because the antecedent is false. The antecedent is false, so the implication is true.

A ==> B does not mean that A causes B. It means A does not prevent B or impact B. So if you study and pass, it logically follows that if you study then you pass the exam.

These are two unique concepts in time and space that we are trying to relate. So studying and passing the test are not directly related, but if you study and pass, it is implied that studying leads to passing the test. If you study and you fail, it is not implied that studying leads to failing the test. If you don't study and you pass the test, it is implied that not studying leads to passing the test. If you don't study and you fail the test, it is implied that not studying leads to failing the test.

What made this click for me is think of the third line in inverse. If you studied but you failed, studying can't imply passing. If you didn't study but you passed, not studying can't imply failing because *you did pass*. So studying would only help you pass more (?).

Still confusing, but hey - we're trying, right?




