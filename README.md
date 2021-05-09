# Anomaly Detection

## A Natural Language Processing technique using LSTM Recurrent Neural Network

## Summary

Modern systems generate huge amounts of data in the form of log files during execution. The information in log files help us understand the system behavior. This is especially true during maintenance and troubleshooting phases where error messages can be analyzed to understand the root causes of system failures. However, this process involves a lot of manual work by experts to parse the log messages and infer system states. This process becomes unrealistic as the systems grow larger and generate vast amounts of data that is unrealistic for manual human intervention.

Machine learning techniques can be very useful in detecting patterns, and therefore a natural choice in inferring system behavior. Given the complexity of systems – with multiple components interacting with each other – domain expertise still plays a vital role in state inference based on these log messages. Ideally, we would want to leverage domain expert knowledge to some extent in designing the patterns and then use machine learning to identify those patterns.

Natural language techniques are very effective at modeling sequences of data. If a system state can be identified at a particular time, the changes in system state over-time can be modeled as sequential data. This allows recurrent neural networks to identify patterns in state changes, which in turn can be used to classify a state into an anomaly or normal state. Leveraging the patterns identified by the LogCluster algorithm, we have successfully implemented a LSTM based recurrent neural network to identify anomalies in Hadoop file system.

__Keywords__ — Anomaly detection, logfile, LogCluster, LSTM, machine learning, NLP, RNN

### Performance metrics

99.98%  Accuracy     
99.67%  Precision      
99.67%  Recall      

Link below for more details of methodology and results:    
https://github.com/naveen-chalasani/natural-language-processing-and-anomaly-detection/blob/main/Anomaly%20Detection%20using%20Sequential%20Data%20Modeling.pdf
