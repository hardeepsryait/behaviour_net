# Behavior_net 

Artificial neural network to predict motor deficits in video recordings of rodents.

Extracts features from each frame with a ConvNet, passing the sequence to an RNN, in a separate network

This code has been used to produce the results in the preprint: [Ryait et al, 2019](https://www.biorxiv.org/)

## Requirements
The code was developed for python 3.5 (tested on Linux and Windows)

- tensorflow ???
- Keras>=2.0.2
- numpy>=1.12.1
- pandas>=0.19.2
- tqdm>=4.11.2
- matplotlib>=2.0.0

You can install all the modules using 'pip install <module>'

## Steps to follow:

1. Download the datasets in '/test/Reach/' and '/train/Reach/' folder respectively into a data folder. 
	In this data folder, put the `data_file.csv` file. This file will reference all the files (format must be kept same).
	
2. To extract the features from the images using the CNN, run `extract_features.py`. 
	These features will get stored in folder '/data/sequences/'.

3. Train the RNN model with `train_reg.py`. You can change the training options (e.g. model) by editting this file.

The models are defined in `models.py`. The trained model will get stored in folder '/data/checkpoints/'

4. To validate the trained model, run `validate.py` on the test set. You can edit this file to validate different trained models.


## Disclaimer
All the file in this repository has been taken from [https://github.com/harvitronix/five-video-classification-methods] with slight modifications.  

See the accompanying blog post for full details: https://blog.coast.ai/five-video-classification-methods-implemented-in-keras-and-tensorflow-99cad29cc0b5 
