# Behavior_net 

Artificial neural network to predict motor deficits in video recordings of rodents.

## Abstract

Behaviour provides important insights into neuronal processes. For example, analysis of reaching movements can give a 
reliable indication of neurological disorders like stroke, Parkinson disease, or Huntington disease. However, analyses 
of fine movements are notoriously difficult and require a trained person. Here we show that a deep neuronal network 
scored reaching behavioural impairments in stroke animals with humanan expert accuracy. Our trained nNetwork uncovered 
new movement alterations related to stroke, which had higher predictive power of stroke volume than human expert scores. 
The same network was also trained to successfully score movements in a variety of other behavioural tasks and in human 
patients with Parkinson’s disease. Thus, this network could be used for reproducible scoring of complex behaviours, and 
knowledge extraction from a trained network can be used to design more sensitive behavioural indices to detect and 
monitor neurological disorders. 



This code has been used to produce the results in the preprint: [Ryait et al, 2019](https://www.biorxiv.org/)

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

1. Download the datasets in '/test/Reach/' and '/train/Reach/' folder respectively into a data folder in your local directory. 
	Put the `data_file.csv` file in the data folder. This file will reference all the files (format must be kept same).
	
2. To extract the features from the images using the CNN, run `extract_features.py`. 
	These features will get stored in folder '/data/sequences/'.

3. Train the RNN model with `train_reg.py`. You can change the training options (e.g. model) by editting this file.

The models are defined in `models.py`. The trained model will get stored in folder '/data/checkpoints/'. If you want to use the pre-trained model, it can be downloaded from http://people.uleth.ca/~luczak/BehavNet/g04-features.hdf5 and copied in '/data/checkpoints/'.

4. To validate the trained model, run `validate.py` on the test set. You can edit this file to validate different trained models.


## Disclaimer
The network and methology presented here has been adapted from [https://github.com/harvitronix/five-video-classification-methods].  

See the accompanying blog post for full details: https://blog.coast.ai/five-video-classification-methods-implemented-in-keras-and-tensorflow-99cad29cc0b5 
