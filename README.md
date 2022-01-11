# Github Report
<div id="top"></div>
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>

  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

An Oncology, AI platform


### Built With


* [python](https://www.python.org)
* [docker](https://www.docker.com/)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running please follow these simple example steps.

### Prerequisites

A list things you need to install to use the software.

  ```sh
    docker v1.10 or above
    docker-compose v1.6.0 or above   
  ```
  
### Installation


1.build the containers
   ```sh
   docker-compose up
   ```


<!-- USAGE EXAMPLES -->
## Usage

1.You could access the application at http://localhost:5000/

The application accept image types in - png, jpg or jpeg
  
## Alternative architecture

    AWS API GATEWAY -> AWS LAMBDA ->SNS -> SQS -> AWS EC2 / Sagemaker  -> S3 
                            

1) All the api would be handle by API gateway and perform certain task such as IP whitelisting.
2) Image would be processed by AWS LAMBDA function (serveless) and save the input image into s3.
3) Send the event to SNS as it is able to fanout the event data to multiple SQS. (able to scale horizontally)
4) SQS allowing parallel asynchronous processing and presist the data.
5) EC2 or Sagemaker to run the inference.
6) Save the  output image in S3.
7) user can access the image with s3 url 
8) optional: point cloudfare to s3 to enable faster image access across different region.
9) DynamoDB to record data such as user id, datetime, metadata and so on. (NoSQL for better scalability)


    
<p align="right">(<a href="#top">back to top</a>)</p>