# openfisca-interactive

Test OpenFisca with Jupyter interactive widgets

Click on this badge to open the demo Jupyter notebook: [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/cbenz/openfisca-interactive/master?filepath=index.ipynb)

## Installation

```bash
# Install long-term support NodeJS with [nvm](https://github.com/creationix/nvm)
nvm install --lts

# Install Jupyter lab extension for widgets (see [doc](http://ipywidgets.readthedocs.io/en/latest/user_install.html#installing-the-jupyterlab-extension))
jupyter labextension install @jupyter-widgets/jupyterlab-manager
```

## Evolution

- aspect édition du cas type
- aspect dataviz
- technos (Jupyter Notebook)
- penser une forme de scénarisation des résultats
  - partir d'un éditeur de cas-type simplifié supportant quelques variables d'entrée (salaire de base, âge, nombre d'enfants, conjoint, loyer)
  - partir du salaire de base voire du salaire net
  - afficher le salaire brut déduit approximativement, proposer de le corriger s'il est connu
  - proposer plusieurs étapes avec des graphiques dédiés (facettes)
