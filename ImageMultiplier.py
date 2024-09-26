from PIL import Image
import glob

# This function is used to create images for the neural network. It takes one image and turns it into 24. This is not
# used within the actual system and only exists on the side for this one purpose.


def split(img, num):
    width, height = img.size
    div = width//2
    img_crop_left = img.crop((0, 0, div, height))
    img_crop_right = img.crop((div, 0, width, height))
    img_crop_left.save('IMG-End/imgSplitLeft-' + num + '.jpeg')
    img_crop_right.save('IMG-End/imgsplitLight-' + num + '.jpeg')


j = 0
i = 0
for filename in glob.glob('IMG-Start/*.jpeg'):
    image = Image.open(filename)

    split(image, str(j))
    j += 1

    image_flip_left = image.transpose(method=Image.Transpose.FLIP_LEFT_RIGHT)
    image_flip_left.save('IMG-End/imgFL1-' + str(i) + '.jpeg')

    split(image_flip_left, str(j))
    j += 1

    image_flip_top = image.transpose(method=Image.Transpose.FLIP_TOP_BOTTOM)
    image_flip_top.save('IMG-End/imgFT1-' + str(i) + '.jpeg')

    split(image_flip_top, str(j))
    j += 1

    image_rotate = image.rotate(90, expand=True)
    image_rotate.save('IMG-End/img90-' + str(i) + '.jpeg')

    split(image_rotate, str(j))
    j += 1

    image_flip_left = image_rotate.transpose(method=Image.Transpose.FLIP_LEFT_RIGHT)
    image_flip_left.save('IMG-End/imgFL2-' + str(i) + '.jpeg')

    split(image_flip_left, str(j))
    j += 1

    image_flip_top = image_rotate.transpose(method=Image.Transpose.FLIP_TOP_BOTTOM)
    image_flip_top.save('IMG-End/imgFT2-' + str(i) + '.jpeg')

    split(image_flip_top, str(j))
    j += 1

    image.rotate(90, expand=True)
    image_rotate.save('IMG-End/img180-' + str(i) + '.jpeg')

    split(image_rotate, str(j))
    j += 1

    image_flip_left = image_rotate.transpose(method=Image.Transpose.FLIP_LEFT_RIGHT)
    image_flip_left.save('IMG-End/imgFL3-' + str(i) + '.jpeg')

    split(image_flip_left, str(j))
    j += 1

    image_flip_top = image_rotate.transpose(method=Image.Transpose.FLIP_TOP_BOTTOM)
    image_flip_top.save('IMG-End/imgFT3-' + str(i) + '.jpeg')

    split(image_flip_top, str(j))
    j += 1

    image.rotate(90, expand=True)
    image_rotate.save('IMG-End/img270-' + str(i) + '.jpeg')

    split(image_rotate, str(j))
    j += 1

    image_flip_left = image_rotate.transpose(method=Image.Transpose.FLIP_LEFT_RIGHT)
    image_flip_left.save('IMG-End/imgFL4-' + str(i) + '.jpeg')

    split(image_flip_left, str(j))
    j += 1

    image_flip_top = image_rotate.transpose(method=Image.Transpose.FLIP_TOP_BOTTOM)
    image_flip_top.save('IMG-End/imgFT4-' + str(i) + '.jpeg')

    split(image_flip_top, str(j))
    j += 1

    i += 1
