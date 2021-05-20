# cat_dog_classifier
It is a cat and dog classifire.

## Installation
```python
pip install cat_dog_classifier
```

## How to use it
It take the image path and classify, if it is cat then answer is 0 else 1 for dog.
 ```python 
import cat_dog_classifier

image_path = "C:\Users\xvinay28x\Desktop\dog.jpg"
result = cat_dog_classifier.cat_dog(image_path)
if result ==  1:
    print("It is Dog")
else:
    print("It is Cat")
```

## License

© 2021 Vinay Garg