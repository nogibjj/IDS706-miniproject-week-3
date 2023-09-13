# IDS706 Miniproject - Week 2

[![Codespaces Prebuilds](https://github.com/nogibjj/python-data-science-template-v2/actions/workflows/codespaces/create_codespaces_prebuilds/badge.svg)](https://github.com/nogibjj/python-data-science-template-v2/actions/workflows/codespaces/create_codespaces_prebuilds) 

[![CI](https://github.com/nogibjj/python-data-science-template-v2/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/python-data-science-template-v2/actions/workflows/main.yml)

This project performs descriptive statistics on [Gapminder World](https://www.gapminder.org/tag/gapminder-world/) dataset. 
The `tests` directory runs sanity checks on the dataset and the `src` directory holds the code to make visualizations.
The visualizations themselves are stored in the `outputs` directory.

# Directory Structure
```
.
├── Dockerfile
├── LICENSE
├── Makefile
├── outputs
│   ├── Literacy Rates.png
│   └── Time series of Metrics (1991 - 2011).png
├── README.md
├── repeat.sh
├── requirements.txt
├── setup.sh
├── src
│   ├── lib
│   │   ├── data_loader.py
│   │   └── __init__.py
│   └── main.py
└── tests
    ├── __init__.py
    └── test_main.py
```

# Visualizations

### Variations of Literacy Rates and GDP Per Capita

![Variation in Metrics](/outputs/Scatterplot.png)

# Descriptive Statistics

A table with the descriptive statistics can be found [here](/outputs/descriptive_stats.csv)