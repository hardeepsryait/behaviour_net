# Behavior_net 

Artificial neural network to predict motor deficits in video recordings of rodents.

Extracts features from each frame with a ConvNet, passing the sequence to an RNN, in a separate network

This code has been used to produce the results in the preprint: [Ryait et al, 2019](https://www.biorxiv.org/)

## Requirements

- tensorflow ???
- Keras>=2.0.2
- numpy>=1.12.1
- pandas>=0.19.2
- tqdm>=4.11.2
- matplotlib>=2.0.0


## Steps to follow:

1. Download the dataset in '/test/Reach' and '/train/Reach' folder respectively. 
	In the data folder put the "data_file" CSV file. This will be the reference file for rest of the code (format must be kept same).

2. To extract features from the images with the CNN. This is done by running "extract_features.py". 
	These features will get stored in folder '/data/sequences'.

3. Train the RNN model with '''
 "train_reg.py"
'''
 There are configuration options you can set in that file to choose which model you want to run.

The models are all defined in `models.py`. The trained model will get stored in folder '/data/checkpoints'

4. Using this trained model validate using "validate.py" on about the same number of videos as we have in our test set.


## Disclaimer
All the file in this repository has been taken from [https://github.com/harvitronix/five-video-classification-methods] with slight modifications.  

See the accompanying blog post for full details: https://blog.coast.ai/five-video-classification-methods-implemented-in-keras-and-tensorflow-99cad29cc0b5 
