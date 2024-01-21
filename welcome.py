import streamlit as st
import time


def welcome_animation():
    welcome_container = st.empty()
    
    image_urls = [
        "https://www.softseotools.com/uploads/image-to-text.png",
        "https://www.reviewsxp.com/blog/wp-content/uploads/2020/10/Image-To-Text-Converter-Tools.png",
        "https://i0.wp.com/www.nepalitrends.com/wp-content/uploads/2020/12/Image-to-text-converter.jpg?resize=880%2C528&ssl=1"
    ]

    # st.balloons()
    
    for i in range(3):
        col1, space, col2 = welcome_container.columns([1, 0.3, 1])
        with col1:
            st.markdown(
                f"""
                 
                    <h1 style="font-size: 2.5em; text-align: center; text-align: justify;">🌟 Welcome to ImageText 🌟</h1>
                    <br/>
                    <h2 style="font-size: 1.5em; text-align: center; text-align: justify;"> Your Gateway to Effortless Image-to-Text Conversion!</h2>
                    <br/>
                    <p style="font-size: 1.1em; font-family: Arial; text-align: center; text-align: justify;">ImageText is a tool that simplifies text extraction from images, making information more accessible. It effortlessly transforms images into editable and shareable text for students, professionals, and creative enthusiasts.</p>
                    <p style="font-size: 1.5em;">Developed by team DarkCoder 🕶️🕶️</p>
                
                """,
                unsafe_allow_html=True
            )
        with col2:
            st.markdown(
                f"""
                <style>
                    img {{
                        border-radius: 15px;
                        width: 100%;
                        height: auto;
                        max-width: 500px;  /* Set maximum width for the image */
                    }}
                </style>
                """,
                unsafe_allow_html=True
            )
            col2.image(
                image_urls[i],
                use_column_width=True,
                # caption=f"Image {i + 1}",
                output_format="png",
                width=500,
                clamp=True,
                channels="RGB",
            )
        time.sleep(1.5)

    welcome_container.empty()








