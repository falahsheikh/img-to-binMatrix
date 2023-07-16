import cv2
import numpy as np

img = cv2.imread("org.jpeg") #replace the image file you want to process
WIDTH, HEIGHT, _ = img.shape

cell_width, cell_height = 5, 5  
new_width, new_height = int(WIDTH / cell_width), int(HEIGHT / cell_height)

img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_NEAREST)

new_img = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)

font_path = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.3  
font_thickness = 1

for i in range(new_height):
    for j in range(new_width):
        r, g, b = img[i, j]
        k = int((float(r) + float(g) + float(b)) / 3)
        if k < 128:
            text = "1"
        else:
            text = "0"
        text_size, _ = cv2.getTextSize(text, font_path, font_scale, font_thickness)
        text_origin = (j * cell_width, (i + 1) * cell_height - 2)
        cv2.putText(new_img, text, text_origin, font_path, font_scale, (0, int(g), 0), font_thickness, cv2.LINE_AA)

# Save the image using OpenCV
cv2.imwrite("matrix.png", new_img) #the processed file will output as 'matrix.png'
