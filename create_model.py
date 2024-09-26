   import tensorflow as tf

   # Create a simple model
   model = tf.keras.Sequential([
       tf.keras.layers.Dense(10, activation='relu', input_shape=(4,)),
       tf.keras.layers.Dense(3, activation='softmax')
   ])

   # Save the model
   model.save('model')
