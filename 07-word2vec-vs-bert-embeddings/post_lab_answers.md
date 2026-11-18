# Post Lab Answers — Experiment 07

## 1. What is a natural join? When is it used?

A **NATURAL JOIN** is an SQL join that automatically matches tables on **all columns that share the same name** (and compatible types). You do not write an `ON` clause.

**When to use**

- Tables share clearly named common keys (e.g. both have `customer_id`)
- You want a short query without listing join conditions
- Schema is controlled so accidental same-named columns will not join wrongly

**Example**

```sql
SELECT *
FROM customers
NATURAL JOIN orders;
```

| customer_id | customer_name | city   | order_no | order_date | purchase_amount |
|-------------|---------------|--------|----------|------------|-----------------|
| 101         | Brishty Moni  | Delhi  | 5001     | 2024-02-10 | 1000.50         |
| 102         | Ayan Khan     | Mumbai | 5002     | 2024-02-12 | 2500.00         |

**Caution:** If two tables share a column name that is *not* a key (e.g. both have `name`), NATURAL JOIN can produce wrong results. Prefer explicit `JOIN ... ON` in production.

---

## 2. How to map many-to-many relationships using joins?

A **many-to-many (M:N)** link needs an **intermediate (junction) table** that stores pairs of foreign keys.

**Example:** salesman ↔ customers via `salesman_customer`

```sql
SELECT s.salesman_id, s.salesman_name, c.customer_id, c.customer_name
FROM salesman s
JOIN salesman_customer sc ON s.salesman_id = sc.salesman_id
JOIN customers c ON sc.customer_id = c.customer_id;
```

| salesman_id | salesman_name | customer_id | customer_name |
|-------------|---------------|-------------|---------------|
| 201         | Alex Brown    | 101         | Brishty Moni  |
| 201         | Alex Brown    | 102         | Ayan Khan     |
| 202         | Sarah Lee     | 101         | Brishty Moni  |

One salesman can appear with many customers, and one customer with many salesmen.
