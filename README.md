* Behavior_net *

All the file in this repository has been taken from [https://github.com/harvitronix/five-video-classification-methods] with slight modifications.  

Model used : Extract features from each frame with a ConvNet, passing the sequence to an RNN, in a separate network



See the accompanying blog post for full details: https://blog.coast.ai/five-video-classification-methods-implemented-in-keras-and-tensorflow-99cad29cc0b5 

Requirements

: Please see the `requirements.txt` file. 

Steps to follow:

1. Download the dataset in '/test/Reach' and '/train/Reach' folder respectively.

In the data folder put the "data_file" CSV file. This will be the reference file for rest of the codes.(format must be kept same)

2.To extract features from the images with the CNN. This is done by running "extract_features.py".These features will get stored in folder '/data/sequences'.

3. Train the RNN model from "train_reg.py". There are configuration options you can set in that file to choose which model you want to run.

The models are all defined in `models.py`. The trained model will get stored in folder '/data/checkpoints'

4. Using this trained model validate using "validate.py" on about the same number of videos as we have in our test set.
