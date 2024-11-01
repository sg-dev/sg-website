---
title: A tunable mechanism for identifying trusted nodes in large scale distributed
  networks
date: '2012-01-01'
publishDate: '2021-02-08T11:56:32.906071Z'
authors:
- Joydeep Chandra
- Ingo Scholtes
- Niloy Ganguly
- Frank Schweitzer
abstract: In this paper, we propose a simple randomized protocol for identifying trusted
  nodes based on personalized trust in large scale distributed networks. The problem
  of identifying trusted nodes, based on personalized trust, in a large network setting
  stems from the huge computation and message overhead involved in exhaustively calculating
  and propagating the trust estimates by the remote nodes. However, in any practical
  scenario, nodes generally communicate with a small subset of nodes and thus exhaustively
  estimating the trust of all the nodes can lead to huge resource consumption. In
  contrast, our mechanism can be tuned to locate a desired subset of trusted nodes,
  based on the allowable overhead, with respect to a particular user. The mechanism
  is based on a simple exchange of random walk messages and nodes counting the number
  of times they are being hit by random walkers of nodes in their neighborhood. Simulation
  results to analyze the effectiveness of the algorithm show that using the proposed
  algorithm, nodes identify the top trusted nodes in the network with a very high
  probability by exploring only around 45% of the total nodes, and in turn generates
  nearly 90% less overhead as compared to an exhaustive trust estimation mechanism,
  named TrustWebRank. Finally, we provide a measure of the global trustworthiness
  of a node; simulation results indicate that the measures generated using our mechanism
  differ by only around 0.6% as compared to TrustWebRank.
publication: Proceedings of 11th IEEE International Conference on Trust, Security
  and Privacy in Computing and Communications (TrustCom 2012)
url_pdf: http://dl.acm.org/citation.cfm?id=2360332
doi: 10.1109/TrustCom.2012.63
pages: 722-- 729
featured: false
sg-areas:
research: 
- Reputation Trust Cooperation

---
