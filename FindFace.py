from sys import argv
import face_recognition

def are_same_person(image_path1, image_path2):
    # Load images with face_recognition
    img1 = face_recognition.load_image_file(image_path1)
    img2 = face_recognition.load_image_file(image_path2)

    # Find face locations in both images
    face_locations_img1 = face_recognition.face_locations(img1)
    face_locations_img2 = face_recognition.face_locations(img2)

    # If no faces are detected in either image, return False
    if not face_locations_img1 or not face_locations_img2:
        return False

    # Get face encodings
    face_encoding_img1 = face_recognition.face_encodings(img1, face_locations_img1)[0]
    face_encoding_img2 = face_recognition.face_encodings(img2, face_locations_img2)[0]

    # Compare face encodings
    results = face_recognition.compare_faces([face_encoding_img1], face_encoding_img2)

    return results[0]

if __name__ == "__main__":
    # Specify the paths of the images
    image_path1 = argv[1]
    image_path2 = argv[2]

    # Check if the same person is in both photos
    result = are_same_person(image_path1, image_path2)

    if result:
        print("The same person is in both photos.")
    else:
        print("Different persons are in the photos.")
