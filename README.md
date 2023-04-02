# VCP
### Author: Team Z, COMP 523

## Title
This project will build the public-facing interface to a computer vision volumetric capture project being built by the Reese Innovation Lab. VCP, standing for Volumetric Capture Processor, is an app created by the Resse Innovation lab that produces volumetric 3D models from multiple video and data sources.

Volumetric capture is a capturing process that captures people and turn them into 3D models. VCP produces volumetric 3D models from multiple video and data sources. This project will build the public-facing interface to a computer vision volumetric capture project being built by the Reese Innovation Lab.

We are going to present the VCP app created by the Reese Innovation Lab to the public using websites. Our website will allow authorized members to modify the data, publish new projects, scenes (within the projects) and captures (within the scenes) and download after the upload process is done.

## Getting started

- Prerequisites: Latest Docker, Macbook with macOS 11.5.2 on x86
- Installing:
  - In your terminal run `git clone git@github.com:teamz-comp523/vcp_project.git` to clone the repository
  - Open vcp_project folder
  - Run `docker compose up` in terminal which will automatically install all dependencies into the containers
- Running locally:
  - For the backend
    - Run `docker compose up` in terminal
    - Open `localhost:8000` for backend
  - For the frontend, go to VCPFrontend folder
    - change the TESTHOST url to localhost:8000 in the src/backend/backendAPI.js
    - run `docker compose up` to start the frontend container
    - open `localhost:3000` for frontend
- Warranty: 11/14/2021 were this instruction last tested and verified to work by Team Z from COMP 523 UNC on macOS 11.5.2 on x86 with Docker 20.10.8

## Testing

- How to test the project:
  - Backend Test
    - Open the vcp_project folder in terminal
    - Run `python manage.py test vcp_backend/tests/*Test.py`
  - Frontend Test
    - Open vcp_project/VCPFrontend in terminal
    - Run `npm test`

## Deployment
- The project is deployed on AWS Elastic Beanstalk
- The docker images are stored on AWS ECR
- The database is deployed on AWS RDS
1. Clone the up-to-date repo
2. Retrieve an authentication token and authenticate your Docker client to your registry.
   Use the AWS CLI:
    `aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 686487091234.dkr.ecr.us-east-1.amazonaws.com`
3. Build your Docker image using the following command: 
   `docker build -t cv-reconstruction-django .`
4. After the build completes, tag your image so you can push the image to this repository: 
    `docker tag cv-reconstruction-django:latest 686487091234.dkr.ecr.us-east-1.amazonaws.com/cv-reconstruction-django:latest`
5. Run the following command to push this image to your newly created AWS repository:
   `docker push 686487091234.dkr.ecr.us-east-1.amazonaws.com/cv-reconstruction-django:latest`
6. Upload the Dockerrun.aws.json file in deploy/ to the Elastic Beanstalk to deploy


## Technologies used
Python/Django hosted on AWS for managing and processing multiple camera data files HTML, CSS, JavaScript template/views Code managed in Github

ADRs are [here](https://teamz-comp523.github.io/vcp/app_arch.html)


## Contributing
1. To get into the repo, email the main account [comp523vcp@gmail.com](comp523vcp@gmail.com)
2. Make sure StandardJS is installed in your IDE for frontend development
3. Project website is [here](https://teamz-comp523.github.io/vcp/)

## Authors

- Xingda Li: AWS deployment, Docker containerization, Frontend Design, Database Design, Testing
- Yuanzheng Zhao: Frontend Design, Testing, Optimization 
- Yufan Liu: Backend development, user registration/verification, Docker containerization, Tesing

## License

- MIT open source

## Acknowledgements

- We'd like to thank Vraj Patel as the mentor for our project and for guiding us and providing helpful feedback throughout the semester.

## Backend API Doc
- Go to this [link](https://lush-sweatshirt-df6.notion.site/VCP-Backend-API-Doc-524438de6e484506bbcfada6f9832eba)

## Usage
1. clone this directory
2. `docker compose up` to start local dev environment
3. if web service does not start successfully, go to Docker Dashboard and restart the web container specifically.
4. go to `localhost:8000` and you will see Django REST framework API ready.

## Troubleshooting
1. If you cannot connect to the db on aws, try the 2nd answer [here](https://stackoverflow.com/questions/52324170/aws-rds-for-postgresql-cannot-be-connected-after-several-hours) 

