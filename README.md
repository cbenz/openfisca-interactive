# openfisca-interactive

Test OpenFisca with Jupyter interactive widgets

Click on this badge to open the demo Jupyter notebook: [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/cbenz/openfisca-interactive/master?urlpath=lab)

## Install

```
pip install -r requirements.txt
./postBuild
```

If you have trouble with interactive widgets, try:

```
jupyter lab clean
jupyter lab build
```

See also:

* https://ipywidgets.readthedocs.io/en/stable/user_install.html
* https://github.com/plotly/plotly.py/blob/master/README.md#jupyterlab-support-python-35

## Start notebook

```bash
jupyter lab
```

Then open `index.ipynb`

## Start voila app

```bash
voila interactive_waterfall.ipynb
```

## Evolution

* aspect édition du cas type
* penser une forme de scénarisation des résultats
  * partir d'un éditeur de cas-type simplifié supportant quelques variables d'entrée (salaire de base, âge, nombre d'enfants, conjoint, loyer)
  * partir du salaire de base voire du salaire net
  * afficher le salaire brut déduit approximativement, proposer de le corriger s'il est connu
  * proposer plusieurs étapes avec des graphiques dédiés (facettes)
