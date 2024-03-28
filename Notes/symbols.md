# Symbols found in the textbook that might make it easier to understand what is being said.


### ∈, Element Of

The element of symbol, ∈, is used to denote that t is an element of EMPLOYEE.

### ∃, There Exists, Existential Quantifier

The existential quantifier, ∃, is used to denote that there exists a tuple t in a relation such that the condition specified is true. It is used to specify the existence of a tuple that satisfies a condition. Unlike the universal quantifier, the existential quantifier does not require that all tuples satisfy the condition.

It is most similar to the 'there exists' quantifier in mathematics. It is used to specify the existence of a tuple that satisfies a condition. Unlike the universal quantifier, the existential quantifier does not require that all tuples satisfy the condition. Whenever the existential quantifier is used, the condition must be true for at least one tuple in the relation. If the condition is true for any tuple, the entire condition is true.

Further, wherever the existential quantifier appears in a tuple relational calculus expression, it must obey the following syntax:
```{t | ∃t ∈ R (condition(t))}```
where R is the relation over which the existential quantifier ranges, and condition(t) is the condition that must be true for at least one tuple t in R. 


### ∀, For All, Universal Quantifier

The universal quantifier, ∀, is used to denote that for all tuples t in a relation, the condition specified is true. It is used to specify that a condition is true for all tuples in a relation. The universal quantifier requires that all tuples satisfy the condition.

It is most similar to the 'for all' quantifier in mathematics. It is used to specify that a condition is true for all tuples in a relation. The universal quantifier requires that all tuples satisfy the condition. Whenever the universal quantifier is used, the condition must be true for all tuples in the relation. If the condition is false for any tuple, the entire condition is false. 

Further, wherever the universal quantifier appears in a tuple relational calculus expression, it must obey the following syntax:
```
{t | ∀t ∈ R (condition(t))}
```
where R is the relation over which the universal quantifier ranges, and condition(t) is the condition that must be true for all tuples t in R.  Additionally, the universal quantifier typically is preceded by set difference - {t | t ∈ R - condition(t)} - to denote that the condition must be true for all tuples in R.