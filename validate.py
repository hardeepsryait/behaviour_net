"""
Validate our RNN. Basically just runs a validation generator on
about the same number of videos as we have in our test set.
"""
from keras.callbacks import TensorBoard, ModelCheckpoint, CSVLogger
from models import ResearchModels
from data import DataSet
import os
import csv
import pandas as pd
data2_file = []

def validate(data_type, model, seq_length=125, saved_model=None,
             concat=False, class_limit=None, image_shape=None):
    batch_size = 1

    # Get the data and process it.
    if image_shape is None:
        data = DataSet(
            seq_length=seq_length,
            class_limit=class_limit
        )
    else:
        data = DataSet(
            seq_length=seq_length,
            class_limit=class_limit,
            image_shape=image_shape
        )

    val_generator = data.frame_generator(batch_size, 'test', data_type, concat)

    # Get the model.
    rm = ResearchModels(len(data.classes), model, seq_length, saved_model)

    # Evaluate!
    prediction = rm.model.predict_generator(
        generator=val_generator,
        val_samples=29) #put the value as the number of test files 
    prediction = prediction.tolist()
    print(prediction)
    print("===========================")
    prediction1 = pd.DataFrame(prediction).to_csv('prediction.csv')
   

        
def main():
    model = 'lstm'
    saved_model = os.getcwd()+'\\data\\checkpoints\\g04-features.hdf5'
    data_type = 'features'
    image_shape = None
    concat = False

    validate(data_type, model, saved_model=saved_model,
             concat=concat, image_shape=image_shape)

if __name__ == '__main__':
    main()
