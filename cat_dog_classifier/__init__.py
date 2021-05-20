from tensorflow import keras

def classify(path):
    model = keras.models.load_model("Cat_Dog_Classification.h5")
    load_image = keras.preprocessing.image.load_image(path,target_size=(200,200))
    image_array = keras.preprocessing.image.img_to_array(load_image)
    reshape_array = image_array.reshape(1,200,200,3)
    array_normalize = reshape_array/255
    result = model.predict(array_normalize)
    if result >= 0.5:
        return 1
    else:
        return 0
    