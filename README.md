# Behavior_net 

Artificial neural network to predict motor deficits in video recordings of rodents.

## Abstract

Behaviour provides important insights into neuronal processes. For example, analysis of reaching movements can give a 
reliable indication of neurological disorders like stroke, Parkinson disease, or Huntington disease. However, analyses 
of fine movements are notoriously difficult and require a trained person. Here we show that a deep neuronal network 
scored reaching behavioural impairments in stroke animals with humanan expert accuracy. Our trained network uncovered 
new movement alterations related to stroke, which had higher predictive power of stroke volume than human expert scores. 
The same network was also trained to successfully score movements in a variety of other behavioural tasks and in human 
patients with Parkinson’s disease. Thus, this network could be used for reproducible scoring of complex behaviours, and 
knowledge extraction from a trained network can be used to design more sensitive behavioural indices to detect and 
monitor neurological disorders. 


## Requirements
The code was developed for python 3.5 (tested on Linux and Windows) with the following modules:

- Tensorflow
- Keras>=2.0.2
- numpy>=1.12.1
- pandas>=0.19.2
- tqdm>=4.11.2
- matplotlib>=2.0.0

You can install all the modules using `pip install <module>`.

## Steps to follow:


Instructions for running the pre-trained demo:
1.	Download the repository in your local drive and unzip it.
 
Figure 1. Download the repository and unzip it into a local folder.
2.	Unzip the data.zip file (Figure 1). This folder  contains sample data for training and testing the model in the corresponding ‘data/train/Reach/’ and ‘data/test/Reach/’ folders. Due to the space limitation on of GitHub, we only uploaded test files into ‘data/test/Reach/’ for this demo. This folder contains sample AVI files along with their frames in JPEG format for demonstration purposes. If ones wants to train the network, the training data should be copied to the corresponding folder (see To Run the model on your own data).
3.	To train and test the model, the location of the data files are referenced in the ‘data/data_file.csv’ file.  
 
Figure 2. All the data files are referenced in data_file.csv. The fields in this file describe the location and parameters used to train and test the model.

The structure of this file is as follows: column A denotes the type of data (e.g. training or test), column B describes task (e.g. reaching), column C is the file name, column D is the number of frames of each AVI file. Finally, column E contains the Expert Score assigned to the corresponding dataset which is used as the ground truth (target output). 
4.	The next step is to extract the features using the CNN. For this demo, these files are already included in the folder ‘data/sequences/’. 

 
Figure 3. Feature extraction using a CNN. For this demo, the features are already located in the ‘data/sequences’ folder.  
5.	The next step is to train the model. For this demo, you can download the pre-trained model weights from http://people.uleth.ca/~luczak/BehavNet/g04-features.hdf5 and place them in the '/data/checkpoints/' folder.
6.	To validate the trained model, run validate.py. 


To run the model on your own data
1.	Download the repository to your local drive and unzip it.
2.	Create a folder called ‘data/train/Task’ and another one called ‘data/test/Task’ and place your training and test sets (videos) in the folders respectively for the Task you want to classify. 
Next, you need to slice the videos into frames. To slice video files into frames in JPEG format you can use  extract_files.py. 
 
Figure 4. Slice videos into frames. You can use 'extract_files.py' to slice videos into multiple frames.

3.	The next step is to extract the features from the training images using the CNN. Run extract_features.py. Set ‘seq_length’ and ‘paths’ parameters according to your data (Figure 3). Once you run this python script, the features will be stored in the folder '/data/sequences/'.
4.	Train the model by running train_reg.py. You need to modify this file to select different training options (e.g. nb_epoch, batch_size, seq_length).
5.	To modify the models, you need to edit models.py. The trained model will get stored in folder '/data/checkpoints/'.
6.	Finally, to validate the trained model run validate.py




## Disclaimer
The network and methology presented here has been adapted from https://github.com/harvitronix/five-video-classification-methods.  

See the accompanying blog post for full details: https://blog.coast.ai/five-video-classification-methods-implemented-in-keras-and-tensorflow-99cad29cc0b5 
