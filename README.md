# 🎨Image Colourizer🖌️ [![Project Status: Active](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active) [![](https://img.shields.io/badge/Prateek-Ralhan-brightgreen.svg?colorB=ff0000)](https://prateekralhan.github.io/)


A Flask based Web-app to colourize black and white images built using openCV and Caffe deeplearning framework.

## Installation:
***pip install -r requirements.txt*** will install all the necessary dependencies.

## Usage:
1. Simply run the command ***python app.py*** and it will run the web application in your local machine.
2. Navigate to http://192.168.29.175:5000/ in your favourite web-browser.

<kbd>
<img src="https://user-images.githubusercontent.com/29462447/135691618-d211c8ac-9033-40e4-ae4a-7a304e23c54e.png" data-canonical-src="https://user-images.githubusercontent.com/29462447/135691618-d211c8ac-9033-40e4-ae4a-7a304e23c54e.png"/> 
</kbd>

3. Your web-app will be loadup and now it is ready to use!

<kbd>
<img src="https://user-images.githubusercontent.com/29462447/135691647-484fb2a7-8b2b-4370-8813-7faa077fcad3.png" data-canonical-src="https://user-images.githubusercontent.com/29462447/135691647-484fb2a7-8b2b-4370-8813-7faa077fcad3.png"/> 
</kbd>

4. Simply browse your black and white images which the web-app will process and automatically download the colourized images in your system.

## Results:

| **Original Image**  | **Colourized Image**  |
|---------------------|-----------------------|
| ![pic1](https://user-images.githubusercontent.com/29462447/135691846-e1ea276e-4008-4add-b431-3566c3f9ed08.jpg)  | ![pic1](https://user-images.githubusercontent.com/29462447/135691857-515e42a8-bae4-4a1c-99c8-9aab6e8b624d.jpg)  |
| ![pic2](https://user-images.githubusercontent.com/29462447/135691911-0f44e193-3ff8-472d-aeca-f88fbeb103d7.jpg)  | ![pic2](https://user-images.githubusercontent.com/29462447/135691906-7cdf2e98-38d1-406a-9a8e-0e93885e2aac.jpg)  |
| ![pic3](https://user-images.githubusercontent.com/29462447/135691944-0edc5c55-2a74-48bf-8842-2dc541787e23.jpg)  | ![pic3](https://user-images.githubusercontent.com/29462447/135691952-f444fe19-26b9-482b-83d3-277276407729.jpg)  |
| ![pic6](https://user-images.githubusercontent.com/29462447/135691994-ea18b7e6-dda4-47c5-9959-5d975cd7b8f0.jpg) | ![pic6](https://user-images.githubusercontent.com/29462447/135691988-3bee4fd2-38fd-487b-9d57-cd563af1b768.jpg)|
| ![pic5](https://user-images.githubusercontent.com/29462447/135692044-e087507c-3fa4-4e27-8e3a-c5d9c5799573.jpg)| ![pic5](https://user-images.githubusercontent.com/29462447/135692048-b2d0dfa3-d4aa-496a-804a-ac8419905e13.jpg)|
| ![pic4](https://user-images.githubusercontent.com/29462447/135692086-56ed3cab-c7e3-45e1-ae3f-bd025f42c237.jpg)| ![pic4](https://user-images.githubusercontent.com/29462447/135692079-982fe45b-92e4-4e49-b1b0-f60afd6b717d.jpg)|

------------
## COPYRIGHTS FOR ALL THE IMAGES (RANDOMLY REFERENCED FROM GOOGLE) BELONG TO THEIR RESPECTIVE OWNERS.
------------


### Running the Dockerized App
1. Ensure you have Docker Installed and Setup in your OS (Windows/Mac/Linux). For detailed Instructions, please refer [this.](https://docs.docker.com/engine/install/)
2. Navigate to the folder where you have cloned this repository ( where the ***Dockerfile*** is present ).
3. Build the Docker Image (don't forget the dot!! :smile: ): 
```
docker build --tag image_colourizer_app .
```
4. Run the docker:
```
docker run --publish 8000:8080 --detach --name bb image_colourizer_app
```

This will launch the dockerized app. Navigate to ***localhost:8000*** in your browser to have a look at your application. You can check the status of your all available running dockers by:
```
docker ps
```








