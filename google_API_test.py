import io
import os
from google.cloud import vision
import time

client = vision.ImageAnnotatorClient()

start = time.time()
file_name = os.path.abspath('test images\\runners_bib_1.jpg')
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = vision.types.Image(content=content)

response = client.text_detection(image=image)
texts = response.text_annotations

print('Texts:')
for text in texts:
    print('\n"{}"'.format(text.description))
    vertices = (['({},{})'.format(vertex.x, vertex.y)
                for vertex in text.bounding_poly.vertices])
    print('bounds: {}'.format(','.join(vertices)))

print('\n\nDone in', time.time() - start, 'seconds.')
