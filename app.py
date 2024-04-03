# # import streamlit as st
# # import requests
# # from PIL import Image
# # from io import BytesIO
# # import numpy as np
# # import tensorflow.keras as keras

# # # Function to load images from the provided URLs
# # def load_images():
# #     title1_url = 'https://github.com/hvamsiprakash/Simpson-Character-Classification-using-Keras-and-CNN/raw/main/images/title1.png'    
# #     title2_url = 'https://github.com/hvamsiprakash/Simpson-Character-Classification-using-Keras-and-CNN/raw/main/images/title2.png'
# #     title1_image = Image.open(BytesIO(requests.get(title1_url).content))
# #     title2_image = Image.open(BytesIO(requests.get(title2_url).content))
# #     return title1_image, title2_image

# # # Load and display images as titles
# # title1_image, title2_image = load_images()

# # # Set page background color to black
# # st.markdown("""
# #     <style>
# #         body {
# #             background-color: black;
# #             color: white;
# #         }
# #     </style>
# # """, unsafe_allow_html=True)

# # # Display title images in the main interface
# # st.image(title1_image, use_column_width=True)
# # st.image(title2_image, use_column_width=True)

# # # Function to preprocess image
# # def preprocess_image(image):
# #     img = image.resize((64, 64))
# #     img = np.array(img)
# #     img = img.astype("float32") / 255.0
# #     return img

# # # Load the model
# # @st.cache(allow_output_mutation=True, suppress_st_warning=True)
# # def load_model():
# #     try:
# #         model_url='https://github.com/hvamsiprakash/Simpson-Character-Classification-using-Keras-and-CNN/raw/main/models/model.h5'
# #         response = requests.get(model_url)
# #         response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
# #         model_path = 'model (1).h5'
# #         with open(model_path, 'wb') as f:
# #             f.write(response.content)
# #         model = keras.models.load_model(model_path)
# #         return model
# #     except Exception as e:
# #         st.error(f"Error loading model: {str(e)}")
# #         return None

# # model = load_model()

# # # Function to predict
# # def predict(image, model):
# #     processed_image = preprocess_image(image)
# #     prediction = model.predict(np.expand_dims(processed_image, axis=0))
# #     predicted_class = np.argmax(prediction)
# #     return predicted_class

# # # Map class indices to character names
# # map_characters = {
# #     0: 'abraham_grampa_simpson',
# #     1: 'apu_nahasapeemapetilon',
# #     2: 'bart_simpson',
# #     3: 'charles_montgomery_burns',
# #     4: 'chief_wiggum',
# #     5: 'comic_book_guy',
# #     6: 'edna_krabappel',
# #     7: 'homer_simpson',
# #     8: 'kent_brockman',
# #     9: 'krusty_the_clown',
# #     10: 'lisa_simpson',
# #     11: 'marge_simpson',
# #     12: 'milhouse_van_houten',
# #     13: 'moe_szyslak',
# #     14: 'ned_flanders',
# #     15: 'nelson_muntz',
# #     16: 'principal_skinner',
# #     17: 'sideshow_bob'
# # }

# # # Streamlit UI
# # st.sidebar.title("Project Description")
# # st.sidebar.markdown("""
# # This is a Simpson Character Classifier. 
# # It takes an image of a Simpsons character as input and predicts which character it is. 
# # The model used for prediction is a convolutional neural network (CNN) trained on a dataset of Simpsons characters.
# # """)

# # st.sidebar.title("Classes Predicted")
# # # Display the 17 classes the model can predict
# # for character_name in map_characters.values():
# #     st.sidebar.write(character_name)

# # st.title("Simpson Character Classifier")

# # # Uploaded file for prediction
# # uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# # if uploaded_file is not None and model is not None:
# #     image = Image.open(uploaded_file)
# #     # Resize the uploaded image
# #     image = image.resize((200, 200))
# #     st.image(image, caption='Uploaded Image', use_column_width=True)
# #     prediction = predict(image, model)
# #     predicted_character = map_characters.get(prediction, "Unknown")
    
# #     # Check for mismatches
# #     st.write(f"Predicted Character: {predicted_character}")



# # import streamlit as st
# # import requests
# # from PIL import Image
# # from io import BytesIO
# # import numpy as np
# # import tensorflow as tf

# # # Function to load images from the provided URLs
# # def load_images():
# #     title1_url = 'https://github.com/hvamsiprakash/Simpson-Character-Classification-using-Keras-and-CNN/raw/main/images/title1.png'    
# #     title2_url = 'https://github.com/hvamsiprakash/Simpson-Character-Classification-using-Keras-and-CNN/raw/main/images/title2.png'
# #     title1_image = Image.open(BytesIO(requests.get(title1_url).content))
# #     title2_image = Image.open(BytesIO(requests.get(title2_url).content))
# #     return title1_image, title2_image

# # # Load and display images as titles
# # title1_image, title2_image = load_images()

# # # Set page background color to black
# # st.markdown("""
# #     <style>
# #         body {
# #             background-color: black;
# #             color: white;
# #         }
# #     </style>
# # """, unsafe_allow_html=True)

# # # Display title images in the main interface
# # st.image(title1_image, use_column_width=True)
# # st.image(title2_image, use_column_width=True)

# # # Function to preprocess image
# # def preprocess_image(image):
# #     img = image.resize((64, 64))
# #     img = np.array(img)
# #     img = img.astype("float32") / 255.0
# #     return img

# # # Load the model
# # @st.cache(allow_output_mutation=True)
# # def load_model():
# #     model=tf.keras.models.load_model('models/model.h5')
# #     return model 

# # model = load_model()

# # # Map class indices to character names
# # map_characters = {
# #     0: 'abraham_grampa_simpson',
# #     1: 'apu_nahasapeemapetilon',
# #     2: 'bart_simpson',
# #     3: 'charles_montgomery_burns',
# #     4: 'chief_wiggum',
# #     5: 'comic_book_guy',
# #     6: 'edna_krabappel',
# #     7: 'homer_simpson',
# #     8: 'kent_brockman',
# #     9: 'krusty_the_clown',
# #     10: 'lisa_simpson',
# #     11: 'marge_simpson',
# #     12: 'milhouse_van_houten',
# #     13: 'moe_szyslak',
# #     14: 'ned_flanders',
# #     15: 'nelson_muntz',
# #     16: 'principal_skinner',
# #     17: 'sideshow_bob'
# # }

# # # Streamlit UI
# # st.sidebar.title("Project Description")
# # st.sidebar.markdown("""
# # This is a Simpson Character Classifier. 
# # It takes an image of a Simpsons character as input and predicts which character it is. 
# # The model used for prediction is a convolutional neural network (CNN) trained on a dataset of Simpsons characters.
# # """)

# # st.sidebar.title("Classes Predicted")
# # # Display the 17 classes the model can predict
# # for character_name in map_characters.values():
# #     st.sidebar.write(character_name)

# # st.title("Simpson Character Classifier")

# # # Uploaded file for prediction
# # uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# # if uploaded_file is not None and model is not None:
# #     image = Image.open(uploaded_file)
# #     # Resize the uploaded image
# #     image = image.resize((64, 64))
# #     st.image(image, caption='Uploaded Image', use_column_width=True)
    
# #     # Preprocess image and predict character
# #     processed_image = preprocess_image(image)
# #     prediction = model.predict(np.expand_dims(processed_image, axis=0))
# #     predicted_class_index = np.argmax(prediction)
# #     predicted_character = map_characters.get(predicted_class_index, "Unknown")
    
# #     # Display predicted character
# #     st.write(f"Predicted Character: {predicted_character}")


# # import streamlit as st
# # from PIL import Image
# # import numpy as np
# # import tensorflow as tf
# # from io import BytesIO
# # import requests


# # @st.cache(allow_output_mutation=True)
# # def load_model_and_labels():
# #     # Load the trained model from the specified directory.
# #     model = tf.keras.models.load_model('models/model.h5')
# #     class_names = {}
    
# #     # Open and read the labels file.
# #     with open('models/labels.txt', 'r') as f:
# #         for line in f:
# #             # Split each line at the first space to separate the index from the class name.
# #             parts = line.strip().split(' ', 1)
# #             if len(parts) == 2:  # Ensure there are exactly two parts.
# #                 key, val = parts
# #                 class_names[int(key)] = val
# #             else:
# #                 print(f"Skipping invalid line in labels file: '{line}'")
# #     return model, class_names

# # model, class_names = load_model_and_labels()


# # # Function to preprocess image
# # def preprocess_image(image):
# #     img = image.resize((64, 64))
# #     img = np.array(img)
# #     img = img.astype("float32") / 255.0
# #     img = np.expand_dims(img, axis=0) # Model expects a batch
# #     return img

# # st.title("Simpson Character Classifier")

# # # Uploaded file for prediction
# # uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# # if uploaded_file is not None:
# #     image = Image.open(uploaded_file)
# #     st.image(image, caption='Uploaded Image', use_column_width=True)
    
# #     # Preprocess and predict
# #     processed_image = preprocess_image(image)
# #     predictions = model.predict(processed_image)
# #     predicted_class_index = np.argmax(predictions)
# #     predicted_character = class_names.get(predicted_class_index, "Unknown")

# #     # Display predicted character
# #     st.write(f"Predicted Character: {predicted_character}")


# # import streamlit as st
# # from PIL import Image
# # import numpy as np
# # import tensorflow as tf

# # # Function to load the model and class names
# # @st.cache(allow_output_mutation=True)
# # def load_model_and_labels():
# #     model = tf.keras.models.load_model('models/model.h5')
# #     class_names = {}
# #     with open('models/labels.txt', 'r') as f:
# #         for line in f:
# #             key, val = line.strip().split(' ', 1)
# #             class_names[int(key)] = val.replace("_", " ")  # Replacing underscores with spaces
# #     return model, class_names

# # # Function to preprocess image
# # def preprocess_image(image):
# #     # Convert the image to RGB if it's not already
# #     if image.mode != 'RGB':
# #         image = image.convert('RGB')
    
# #     # Resize the image
# #     img = image.resize((64, 64))
    
# #     # Convert image to numpy array
# #     img = np.array(img)
    
# #     # Normalize image
# #     img = img.astype("float32") / 255.0
    
# #     # Add batch dimension
# #     img = np.expand_dims(img, axis=0)
    
# #     return img

# # # Load model and class names
# # model, class_names = load_model_and_labels()

# # # Streamlit UI
# # st.title("Simpson Character Classifier")

# # # Uploaded file for prediction
# # uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# # if uploaded_file is not None:
# #     image = Image.open(uploaded_file)
# #     st.image(image, caption='Uploaded Image', use_column_width=True)
    
# #     # Preprocess and predict
# #     processed_image = preprocess_image(image)
# #     predictions = model.predict(processed_image)
# #     predicted_class_index = np.argmax(predictions)
# #     predicted_character = class_names.get(predicted_class_index, "Unknown")

# #     # Display predicted character
# #     st.write(f"Predicted Character: {predicted_character}")

# import streamlit as st
# from PIL import Image
# import numpy as np
# from keras.preprocessing import image as kp_image
# from keras.models import load_model as keras_load_model

# # New dictionary
# map_characters = {0: 'abraham_grampa_simpson', 1: 'apu_nahasapeemapetilon', 2: 'bart_simpson', 
#         3: 'charles_montgomery_burns', 4: 'chief_wiggum', 5: 'comic_book_guy', 6: 'edna_krabappel', 
#         7: 'homer_simpson', 8: 'kent_brockman', 9: 'krusty_the_clown', 10: 'lisa_simpson', 
#         11: 'marge_simpson', 12: 'milhouse_van_houten', 13: 'moe_szyslak', 
#         14: 'ned_flanders', 15: 'nelson_muntz', 16: 'principal_skinner', 17: 'sideshow_bob'}

# # New functions
# def center_crop(img, dim):
#     """Returns center cropped image
#     Args:
#     img: image to be center cropped
#     dim: dimensions (width, height) to be cropped
#     """
#     width, height = img.shape[1], img.shape[0]

#     # process crop width and height for max available dimension
#     crop_width = dim[0] if dim[0]<img.shape[1] else img.shape[1]
#     crop_height = dim[1] if dim[1]<img.shape[0] else img.shape[0] 
#     mid_x, mid_y = int(width/2), int(height/2)
#     cw2, ch2 = int(crop_width/2), int(crop_height/2) 
#     crop_img = img[mid_y-ch2:mid_y+ch2, mid_x-cw2:mid_x+cw2]
#     return crop_img

# # New pre-processing function
# def preprocess_img(request):
#     #f = request.files['file']
#     file_path = get_file_path_and_save(request)  # Assuming get_file_path_and_save is defined somewhere
#     image = cv2.imread(file_path)  # Assuming cv2 is imported somewhere
#     cropped_img = center_crop(image, image.shape)
#     pic = cv2.resize(cropped_img, (64,64))
#     img_reshape = pic.reshape(1, 64, 64, 3)
#     return img_reshape

# # Function to load and preprocess the image
# def preprocess_image(image):
#     img = image.resize((64, 64))
#     img = kp_image.img_to_array(img)
#     img = np.expand_dims(img, axis=0)
#     img /= 255.0  # Normalize the image
#     return img

# # Load the model
# @st.cache(allow_output_mutation=True)
# def load_custom_model():
#     return keras_load_model('models/model.h5')

# # Compile the model with metrics
# def compile_model(model):
#     model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# # Main function to run the Streamlit app
# def main():
#     st.title("Simpson Character Classifier")

#     # Load the model
#     model = load_custom_model()

#     # Compile the model
#     compile_model(model)

#     # Upload image through Streamlit file uploader
#     uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

#     if uploaded_file is not None:
#         # Read the image
#         image = Image.open(uploaded_file)
#         st.image(image, caption='Uploaded Image', use_column_width=True)

#         # Preprocess the image
#         img = preprocess_image(image)

#         # Make predictions
#         class_names = list(map_characters.values())

#         # Prediction
#         prediction = model.predict(img)
#         predicted_class = np.argmax(prediction)
#         st.write("Predicted Character:", class_names[predicted_class])

# # Run the app
# if __name__ == "__main__":
#     main()


# Importing required libraries
import streamlit as st
from tensorflow.keras.models import load_model
import numpy as np
import cv2
from werkzeug.utils import secure_filename

# Load the pre-trained model
model = load_model('models/model.h5')

# Define character mapping
map_characters = {0: 'abraham_grampa_simpson', 1: 'apu_nahasapeemapetilon', 2: 'bart_simpson', 
        3: 'charles_montgomery_burns', 4: 'chief_wiggum', 5: 'comic_book_guy', 6: 'edna_krabappel', 
        7: 'homer_simpson', 8: 'kent_brockman', 9: 'krusty_the_clown', 10: 'lisa_simpson', 
        11: 'marge_simpson', 12: 'milhouse_van_houten', 13: 'moe_szyslak', 
        14: 'ned_flanders', 15: 'nelson_muntz', 16: 'principal_skinner', 17: 'sideshow_bob'}

# Function to center crop an image
def center_crop(img, dim):
    width, height = img.shape[1], img.shape[0]
    crop_width = dim[0] if dim[0] < img.shape[1] else img.shape[1]
    crop_height = dim[1] if dim[1] < img.shape[0] else img.shape[0]
    mid_x, mid_y = int(width/2), int(height/2)
    cw2, ch2 = int(crop_width/2), int(crop_height/2)
    crop_img = img[mid_y-ch2:mid_y+ch2, mid_x-cw2:mid_x+cw2]
    return crop_img

# Function to preprocess the uploaded image
def preprocess_img(uploaded_file):
    image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1)
    cropped_img = center_crop(image, image.shape)
    pic = cv2.resize(cropped_img, (64,64))
    img_reshape = pic.reshape(1, 64, 64, 3)
    return img_reshape

# Function to predict the uploaded image
def predict_result(predict):
    pred = model.predict(predict)
    return map_characters[np.argmax(pred[0])].replace('_',' ').title()

def main():
    st.title("Simpsons Character Classifier")

    # Upload image
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)

        # Preprocess and predict
        if st.button('Predict'):
            try:
                img = preprocess_img(uploaded_file)
                pred = predict_result(img)
                st.success(f"The predicted character is: {pred}")
            except:
                st.error("File cannot be processed.")

if __name__ == "__main__":
    main()

