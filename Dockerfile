  FROM tensorflow/serving
   # Copy the model to the TensorFlow Serving default model directory
   COPY model /models/my_model
   ENV MODEL_NAME=my_model
