import tensorflow as tf
classifier = tf.estimator.LinearClassifier()
classifier.train(input_fn=train_input_fn, steps=2000)
predictions = classifier.predict(input_fn=predict_input_fn)