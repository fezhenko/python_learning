import cv2
import random


def return_picture_name_from_the_list_according_to_input(list, user_input, path):
    while True:
        if user_input in range(len(list)):
            i = str(list[user_input])
            new_path = path + i
            print(f'This image has been chosen: "{new_path}"')
            return new_path
        else:
            x = len(list)
            user_input = int(input(f'Repeat please\nInput correct number in range {x}\n'))


pictures_list = ['galaxy.jpg', 'kangaroos.jpg', 'Lighthouse.jpg', 'Moon sinking, sun rising.jpg']
path = '/sample_images/'
x = len(pictures_list)
what_picture = int(input(f'Choose a number from in range of {x}\n'))


img = cv2.imread(return_picture_name_from_the_list_according_to_input(pictures_list, what_picture, path))
rezised_image = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)), cv2.INTER_NEAREST)
new_image_name = f"resized_img_{random.randint(1, 100)}.png"
print(f"This is resized picture name: {new_image_name}")
cv2.imshow(new_image_name, rezised_image)
cv2.waitKey(2000)
cv2.imwrite(new_image_name, rezised_image)