---
title: "Data Science on Knowledge Graphs"
date:
draft: false
featured: false
featured_image: giona.png
description:
speaker: Giona Casiraghi
affiliation: Chair of Systems Design, ETH Zürich
where: LEE E 101
from: 2022-11-24T10:00:00
to: 2022-11-24T10:45:00
events:
- SG Symposium November 2022
---

### Abstract

One of the most typical properties of network data is the presence of homophily, i.e. the increased tendency of an edge to exist between two nodes if they share the same underlying characteristic, such as a social parameter, metabolic role, etc. More broadly, when the underlying similarity parameter is not specified a priori, the same homophily pattern is known as community structure. Another pervasive pattern encountered in the same kinds of networks is transitivity, i.e. the increased tendency of observing an edge between two nodes if they share a neighbor in common. Although these patterns are indicative of two distinct mechanisms of network formation, namely choice or constraint homophily and triadic closure, respectively, they are generically conflated in non-longitudinal data. This is because both processes can result in the same kinds of observation: 1. the preferred connection between nodes of the same kind can induce the presence of triangles involving similar nodes, and 2. the tendency of triangles to be formed can induce the formation of groups of nodes with a higher density of connections between them, when compared to the rest of the network. This conflation means we cannot reliably interpret the underlying mechanisms of network formation merely from the abundance of triangles or observed community structure in network data.
In this talk I present a solution to this problem, consisting in a principled method to disentangle homophily and community structure from triadic closure in network data. This is achieved by formulating a generative model that includes community structure in a first instance, and an iterated process of triadic closure in a second. Based on this model, we develop a Bayesian inference algorithm that is capable of identifying which edges are more likely to be due to community structure or triadic closure, in addition to the underlying community structure itself. As I show, this reconstruction yields a detailed interpretation of the underlying mechanisms of network formation, allowing us to identify macro-scale structures that emerge spontaneously from micro-scale higher-order interactions, and in this way we can separate them from inherently macro-scale structures. I show how the method can evade the detection of spurious communities caused solely by the formation of triangles in the network, and how it can improve the performance of link prediction when compared to the pure version of the model without triadic closure.
