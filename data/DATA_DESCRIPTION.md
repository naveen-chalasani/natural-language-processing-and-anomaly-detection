Source for the complete HDFS_1 dataset (HDFS_1.tar.gz) :https://zenodo.org/record/3227177

This log set is generated in a private cloud environment using benchmark workloads, and manually labeled through handcrafted rules to identify the anomalies. The logs are sliced into traces according to block ids. Then each trace associated with a specific block id is assigned a groundtruth label: normal/anomaly (available in ```anomaly_label.csv```). You may find more details of this dataset from the original paper:

> Wei Xu, Ling Huang, Armando Fox, David Patterson, Michael Jordan. Detecting Large-Scale System Problems by Mining Console Logs, in Proc. of the 22nd ACM Symposium on Operating Systems Principles (SOSP), 2009.
