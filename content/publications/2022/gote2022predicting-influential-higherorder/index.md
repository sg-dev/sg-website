---
title: Predicting Influential Higher-Order Patterns in Temporal Network Data
date: '2022ß-01-01'
publishDate: '2021-07-28T19:54:28.413438Z'
authors:
- Christoph Gote
- Vincenzo Perri
- Ingo Scholtes
abstract: Networks are frequently used to model complex systems comprised of interacting elements. While edges capture the topology of direct interactions, the true complexity of many systems originates from higher-order patterns in paths by which nodes can indirectly influence each other. Path data, representing ordered sequences of consecutive direct interactions, can be used to model these patterns. On the one hand, to avoid overfitting, such models should only consider those higher-order patterns for which the data provide sufficient statistical evidence. On the other hand, we hypothesise that network models, which capture only direct interactions, underfit higher-order patterns present in data. Consequently, both approaches are likely to misidentify influential nodes in complex networks. We contribute to this issue by proposing five centrality measures based on MOGen, a multi-order generative model that accounts for all indirect influences up to a maximum distance but disregards influences at higher distances. We compare MOGen-based centralities to equivalent measures for network models and path data in a prediction experiment where we aim to identify influential nodes in out-of-sample data. Our results show strong evidence supporting our hypothesis. MOGen consistently outperforms both the network model and path-based prediction. We further show that the performance difference between MOGen and the path-based approach disappears if we have sufficient observations, confirming that the error is due to overfitting.
publication: 2022 IEEE/ACM International Conference on Advances in Social Networks Analysis and Mining (ASONAM)
arxivid: '2107.12100'
featured: false
---