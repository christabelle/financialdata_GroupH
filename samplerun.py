"""
GITHUB: https://github.com/christabelle/financialdata_GroupH
INSTALLATION: pip install financialdata
"""
import pandas as pd

dev = pd.read_csv("https://dl.dropboxusercontent.com/u/28535341/dev.csv")
oot = pd.read_csv("https://dl.dropboxusercontent.com/u/28535341/oot0.csv")

from financialdata import autodataclean, manudataclean, autobindummy, automodel, manumodel

# Automated Data Cleaning with one dataset
# autodataclean(dev)

# Automated Data Cleaning with two dataset
# autodataclean(dev,oot)

# Human-Assisted Data Cleaning with one dataset
# manudataclean(dev)

# Human-Assisted Data Cleaning with two dataset
# manudataclean(dev,oot)

# Automated Dummy Creation with Automated Supervised Binning
# autobindummy(dev,oot,'ob_target')

# Automated Model Comparison
# automodel(dev,oot,'ob_target')

# Human-Assisted Model Selection
# manumodel(dev,oot,'ob_target')


