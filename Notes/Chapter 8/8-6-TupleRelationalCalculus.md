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

A tuple variable is usually denoted by a single letter such as t, u, or v. The range relation of a tuple variable is the relation over which the variable ranges. The range relation is specified by the user in the query. An example of a tuple variable is :
`{t | t ∈ EMPLOYEE}` where t is the tuple variable and EMPLOYEE is the range relation. The element of symbol, ∈, is used to denote that t is an element of EMPLOYEE.

