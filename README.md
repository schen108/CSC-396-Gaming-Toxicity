# Toxicity Detection in Online Gaming

This repository contains the code for all of the transformer models we trained in Juypter notebooks. It also contains all the datasets used for training and testing, stored in csv files.

Each of the transformer models (as described in our report) that we trained and tested are found in the following notebooks:
- Dota Model: transformer_dota.ipynb
- League Model (Combined): transformer_league.ipynb
- League Model (Individual): transformer_league_ind.ipynb
- League (Combined) + Cyberbullying Model: transformer_league-cyberb.ipynb
- League (Combined) + Cyberbullying + Dota Model: transformer_league-cyberb-dota.ipynb

Each of the datasets (as described in our report) are in the following csv files:
- League of Legends Tribunal Chat Logs (Combined): dataToxic.csv
- League of Legends Tribunal Chat Logs (Individual): chatupdate.csv
- Dota 2 Game Chat Logs: tagged-data.csv
- Cyberbullying Dataset: kaggle_parsed_dataset.csv

To run the code:
1. Clone this repository's main branch.
2. Open the notebook with the corresponding model that you want to train and test.
3. Run all of the cells in the notebook, and the performance of the model on the data it was tested on will be displayed in the notebook.
