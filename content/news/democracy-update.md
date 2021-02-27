---
title: "Democracy Update"
date: 2021-02-10T15:04:57+01:00
draft: true
projects:
    - Democrasci
areas:
    - Politics
    - Resilience
featured: true
description: This is a description
---

## Top Level Heading

![An alt text](/teaching/complex-networks/mobility-net.png)

- [x] Item 1
- [ ] Item 2
    - 1
    - `5`

## H2

🙂

| Tables   |      Are      |  Cool |
|----------|:-------------:|------:|
| col 1 is |  left-aligned | $1600 |
| col 2 is |    centered   |   $12 |
| col 3 is | right-aligned |    $1 |

### H3
- research area: Politics
  This would be a collection of all pages which are marked with `area: politics`
  post types: (1) news (2) publication

- List level 1
    - List level 2
        - Level 3
            - Level 4

1. 1
2. 3
3. An other item
4. Yes it works


A quote:

> This is a quote.<br>
> A multiline quote

**this**

---

- add taxonomy for proejcts:
  posts with `project: democrasci` are collected in a Project Page with all posts under it

```python {linenos=table,hl_lines=[8,"15-17"]}
payoff_matrix = {
    ("C", "C"): 7,
    ("C", "D"): 0,
    ("D", "D"): 0,
    ("D", "C"): 10,
}

def payoff_gain_if(my_choice, others_choices):
    my_payoff = 0
    for s in others_choices:
        my_payoff += payoff_matrix[(my_choice, s)]

    return my_payoff

def gain_from_switching(my_current_strategy, others_choices):
    payoff_if_c = payoff_gain_if('C', others_choices)
    payoff_if_d = payoff_gain_if('D', others_choices)

    gain_from_d = payoff_if_d - payoff_if_c
    gain_from_c = - gain_from_d

    if my_current_strategy == "C":
        return gain_from_d
    elif my_current_strategy == "D":
        return gain_from_c


neighbor_strategies = ["C", "C", "C", "C", "C"]

gain = gain_from_switching("D", neighbor_strategies)
print(gain)
```

