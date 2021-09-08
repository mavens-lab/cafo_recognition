import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import helperFunctions

directory = r'C:\ML Research Materials\Image Set'

(training_data, training_labels), (testing_data, testing_labels) = helperFunctions.load_data()

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(400, 400)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(2)
])

training_data = training_data / 255.0
testing_data = testing_data / 255.0

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# model.fit(training_data, training_labels, epochs=5)
#
# test_loss, test_acc = model.evaluate(testing_data,  testing_labels, verbose=2)
#
# print('\nTest accuracy:', test_acc)

# model.save('beta_model')

probability_model = tf.keras.models.load_model('beta_model')

probability_model = tf.keras.Sequential([probability_model, tf.keras.layers.Softmax()])

predictions = probability_model.predict(testing_data)

print(f'[Non-Dairy   Diary] prediction as follows \n {predictions[55:65]}')


'''---------------------------Visual Representation of the predictions with a graph---------------------------'''

name_list = ['Non-Dairy', 'Dairy']


def plot_image(j, predictions_array, true_label, img):
    true_label, img = int(true_label[j]), img[j]

    plt.grid(False)
    plt.xticks([])
    plt.yticks([])

    color_map = plt.cm.get_cmap('binary')

    plt.imshow(img, cmap=color_map)

    predicted_label = np.argmax(predictions_array)
    if true_label == predicted_label:
        color = 'blue'
    else:
        color = 'red'

    plt.xlabel("{} {:2.0f}% ({})".format(name_list[predicted_label],
                                         100 * np.max(predictions_array),
                                         name_list[true_label]),
               color=color)


def plot_value_array(k, predictions_array, true_label):
    true_label = int(true_label[k])
    plt.grid(False)
    plt.xticks(range(2))
    plt.yticks([])
    this_plot = plt.bar(range(2), predictions_array, color="#777777")
    plt.ylim([0, 1])
    predicted_label = np.argmax(predictions_array)

    this_plot[predicted_label].set_color('red')
    this_plot[true_label].set_color('blue')


num_rows = 5
num_cols = 3
num_images = num_rows * num_cols
plt.figure(figsize=(2 * 2 * num_cols, 2 * num_rows))
for i in range(num_images):
    plt.subplot(num_rows, 2 * num_cols, 2 * i + 1)
    plot_image(i, predictions[i], testing_labels, testing_data)
    plt.subplot(num_rows, 2 * num_cols, 2 * i + 2)
    plot_value_array(i, predictions[i], testing_labels)
plt.tight_layout()
plt.show()
