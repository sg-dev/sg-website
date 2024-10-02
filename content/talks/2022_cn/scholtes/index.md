---
title: "De Bruijn Goes Neural: Towards Causality-Aware Graph Neural Networks for Time Series Data"

draft: false
featured: false
featured_image: ingo.png
speaker_image:
description:
speaker: Ingo Scholtes
affiliation: CAIDAS, Julius-Maximilians-Universität Würzburg
where: LEE E 101
from: 2022-11-24T11:15:00
to: 2022-11-24T12:00:00
events:
- SG Symposium November 2022
---

### Abstract

Graph Neural Networks (GNNs) have become a cornerstone for the application of deep learning to data on complex networks, i.e. relational data that capture interactions between nodes. However, we increasingly have access to time-resolved data that not only capture which nodes are connected to each other, but also when and in which temporal order those connections occur. A number of works have shown how the timing and ordering of links shapes the causal topology of networked systems, i.e. which nodes can possibly influence each other over time. Moreover, higher-order network models have been developed that allow us to model patterns in the resulting causal topology. While those works have shed light on the question how the time dimension of dynamic graphs influences node centralities, community structures, or the evolution of dynamical processes, we lack methods to incorporate those insights into state-of-the-art deep graph learning techniques.

Addressing this gap, we introduce De Bruijn Graph Neural Networks (DBGNNs), a novel time-aware graph neural network architecture for time-resolved data on dynamic graphs. Our approach accounts for temporal-topological patterns that unfold via causal walks, i.e. temporally ordered sequences of links by which nodes can influence each other over time. We develop a graph neural network architecture that utilizes De Bruijn graphs of multiple orders to implement a message passing scheme that follows a non-Markovian dynamics, which enables us to learn patterns in the causal topology of dynamic graphs.
