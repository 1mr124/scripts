from sys import argv
from skimage import color, io, transform
from skimage.metrics import structural_similarity as ssim

def resize_image(image, target_shape):
    return transform.resize(image, target_shape, mode='constant', anti_aliasing=True)

def calculate_ssim(image_path1, image_path2):
    # Read images
    img1 = io.imread(image_path1)
    img2 = io.imread(image_path2)

    # Convert images to grayscale
    gray_img1 = color.rgb2gray(img1)
    gray_img2 = color.rgb2gray(img2)

    # Resize images to have the same dimensions
    min_shape = (min(gray_img1.shape[0], gray_img2.shape[0]), min(gray_img1.shape[1], gray_img2.shape[1]))
    gray_img1_resized = resize_image(gray_img1, min_shape)
    gray_img2_resized = resize_image(gray_img2, min_shape)

    # Compute Structural Similarity Index (SSI)
    similarity_index, _ = ssim(gray_img1_resized, gray_img2_resized, full=True,data_range=1.0)

    return similarity_index

if __name__ == "__main__":
    # Specify the paths of the images
    image_path1 = argv[1]
    image_path2 = argv[2]

    # Calculate similarity index
    similarity_index = calculate_ssim(image_path1, image_path2)
    print(f"Similarity Index: {similarity_index}")

    # You can set a threshold based on the similarity index to determine similarity
    threshold = 0.5  # Adjust the threshold as needed

    if similarity_index > threshold:
        print("The images are similar.")
    else:
        print("The images are not similar.")
