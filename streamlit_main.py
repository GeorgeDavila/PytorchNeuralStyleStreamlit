#Build Stramlit App
import streamlit as st
from PIL import Image
import os
#from neural_style import neural_style
#from neural_style import * #check_paths, train, stylize, stylize_onnx_caffe2, main

st.title("Pytorch Neural Style Transfer On Streamlit")

#st.write('Available Style Images:')

candy_image = Image.open('images/style-images/candy.jpg')
mosaic_image = Image.open('images/style-images/mosaic.jpg')
rain_princess_image = Image.open('images/style-images/rain-princess.jpg')
udnie_image = Image.open('images/style-images/udnie.jpg')

#display the reference images
st.write('Style Reference Images:')
col1, col2, col3, col4 = st.beta_columns(4)
with col1:
    st.header("Candy")
    st.image(candy_image, use_column_width=True)
with col2:
    st.header("Mosaic")
    st.image(mosaic_image, use_column_width=True)
with col3:
    st.header("Rain Princess")
    st.image(rain_princess_image, use_column_width=True)
with col4:
    st.header("Udnie")
    st.image(udnie_image, use_column_width=True)

#st.image(candy_image, caption='Candy Style Source Image', use_column_width=True)

#pick model
styleOption = st.selectbox( 'Pick your model style', ('Candy', 'Mosaic', 'Rain_Princess', 'Udnie'))
st.write('You selected:', styleOption)

upload_img = st.file_uploader("Upload your image here (png or jpg)", type=['png', 'jpg'])

if upload_img is not None:
    input_image = Image.open( upload_img )
    #input_image = Image.open(user_image.read(), encoding="utf-8")

    #Want to replace input image so as not to take up space with each new one 
    input_image.save("images/content-images/userinput.png")
    st.image(input_image, caption='Your Image', use_column_width=True)

    #st.write( 'image name: ', user_image.name)
    #print(user_image.name)

    #input_img_name = str(user_image.name).replace(' ', '-')
    #rename file to that of input_img_name: 
    #os.system('mv images/content-images/' + str(user_image.name) + ' images/content-images/' + input_img_name )

    #print(input_img_name)

    model_path = 'saved_models/' + str(styleOption) + '.pth'
    #save one unique image per styleOption, doesn't clog up too much but also doesn't erase some recents
    output_image_path = 'images/output-images/output-userimage-' + str(styleOption) + '.png'

    os_cmd = "python neural_style/neural_style.py eval --content-image  images/content-images/userinput.png --model " + model_path + " --output-image " + output_image_path + " --cuda 0"

    if st.button('Create Style Transfer Image'):
        os.system(os_cmd)
        st.image(output_image_path, caption='Output', use_column_width=True)
    else:
        st.write('click button to run model')

#accept_multiple_files=True -> something could be added #restrict file type to png and jpg. On fully deployed webapp dont want a user uploading erroneous or malicious files, hence this restriction

#run once file is downloaded 
#if uploaded_file is not None:
