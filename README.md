# GraphStreamSummarization
Code for the paper: Tang, Nan, Qing Chen, and Prasenjit Mitra. "Graph stream summarization: From big bang to big crunch." Proceedings of the 2016 International Conference on Management of Data. ACM, 2016.

# Data:

Since it was inefficient to store the large datasets of the study in the repo, I've included links to the datasets here.
You can download the datasets from the links below, extract them and put them in the data/ folder right next to the src folder.

1- DBLP: http://projects.csail.mit.edu/dnd/DBLP/dblp_coauthorship.json.gz

2- superuser: https://snap.stanford.edu/data/sx-superuser.txt.gz

3- stackoverflow (for scalibility experiment): https://snap.stanford.edu/data/sx-stackoverflow.txt.gz

# Running the Code:
All code is in Python 3 and no external libraries are required to run it.

## Experiment 1-a:
For the main replicated experiment (which is experiment 1-a), 
simply run python exp1-a.py. The default setup in the code runs the experiment for the superuser dataset which is the
smaller dataset and won't take very long to run. If you want to run the code for the DBLP dataset, simply change the 
data_path variable on line 14 of exp1-a.py to point the DBLP dataset. You should also change the compression rates 
to 160 (lowest_compression_rate) and 40 (highest_compression_rate) if you want to get the same results in the replication study.
The results are saved in the data folder.

## Scalibility Experiment
Simply run python scalibility.py and you should be good to go. The results are saved in the data folder.

