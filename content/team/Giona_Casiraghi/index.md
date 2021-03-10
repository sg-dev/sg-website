---
firstname: Giona
lastname: Casiraghi
role: Postdoc
honorific: Dr.
weight: 3

room: WEV G 205

image: profile_pic.jpg
email: gcasiraghi@ethz.ch
tel: +41 44 632 06 24
website: https://giona.info
twitter: gi_ona
github: gi0na
orcid: 0000-0003-0233-5747
gscholar: ApW8UuAAAAAJ
---



## <img src="https://ghyper.net/reference/figures/logo.svg" alt="ghypernet logo" width="600"/>

Part of my work revolves around the generalised hypergeometric ensemble of random graphs, gHypEG for short.

In its simplest form, gHypEG provides a model preserving vertices' activities.
Doing so, it maps the standard configuration model to an urn problem.
Pairs of nodes are like balls in an urn.
The more frequent are specific balls, the more likely are edges to be sampled.

In its general form, edge probabilities are again defined by balls' frequencies, but also by independent edge propensities estimated from data.
The higher the propensity, the larger the ball, the easier it is to sample the edge.

Using the urn representation, we find that the hypergeometric distribution describes the simple model, while Wallenius' distribution, the general one.
The main applications of gHypEG, are towards the inference of significant relations from observed interactions, and the analysis of complex networks by means of network regressions.

The R package [ghypernet](https://ghyper.net) provides an Open Source implementation for R of a set of functions to work with gHypEG models.

### GHYPERNET Tutorials and Material

The following links contain a collection of tutorials and material about the ghypernet R package.

Tutorial to network regression models: [https://sg.ethz.ch/nrm-tutorial/](https://sg.ethz.ch/nrm-tutorial/)

Companion git repository for the 2019 EUSN Workshop in Zurich: [https://github.com/sg-dev/EUSN2019_r-ghypernet](https://github.com/sg-dev/EUSN2019_r-ghypernet)

Repository for the EuroCSS Tutorial "Introduction to Multi-edge Network Inference in R Using the Ghypernet-package": [https://github.com/sg-dev/EuroCSS2019_r-ghypernet](https://github.com/sg-dev/EuroCSS2019_r-ghypernet)

GitHub repository for ghypernet: [https://github.com/gi0na/r-ghypernet](https://github.com/gi0na/r-ghypernet)

Manual and Vignettes of the R package: [https://ghyper.net](https://ghyper.net)