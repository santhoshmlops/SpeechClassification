# Speech Classification Pipeline Project

### To run the Project on your local host : 

Clone the repository

    git clone https://github.com/santhoshmlops/SpeechClassification.git
    
Create a conda environment after opening the repository

    conda create -n venv python=3.8 -y
    
 <br/>
    
    conda activate venv
    
    
Install the requirements

    pip install -r requirements.txt
    
    
To run the Web App 
    
    python app.py
    
    
 Click the link to open the Web App
 
    localhost:8080


<img src="https://github.com/santhoshmlops/SpeechClassification/blob/main/hate%20img/gcloud.png" alt="Gcloud">
<img src="https://github.com/santhoshmlops/SpeechClassification/blob/main/hate%20img/fast%201.png" alt="FastAPI">
<img src="https://github.com/santhoshmlops/SpeechClassification/blob/main/hate%20img/train.png" alt="model training">
<img src="https://github.com/santhoshmlops/SpeechClassification/blob/main/hate%20img/model%201.png" alt="model Tuning">
<img src="https://github.com/santhoshmlops/SpeechClassification/blob/main/hate%20img/model%202.png" alt=" model tuning">
<img src="https://github.com/santhoshmlops/SpeechClassification/blob/main/hate%20img/no%20hate.png" alt="No Hate Classification">
<img src="https://github.com/santhoshmlops/SpeechClassification/blob/main/hate%20img/hate.png" alt="Hate Classification">

# To run the Project on Amazon EC2 Instance : 

Require Files :
- .github/workflows/main.yaml
- .dockerignore
- Dockerfile
	
# 1. Login to AWS console :

- Root User  

- Password

# 2. Create IAM user  ( IAM ):

- Add users with the required Permissions policies
	
### Permissions policies

1st - Policy name:

	AmazonEC2ContainerRegistryFullAccess
	
2nd - Policy name : 

	AmazonEC2FullAccess

- Create user

- Open the created IAM User under Security Credentials > Access Key > create Access Key > Command Line Interface(CLI) > Download .CSV

- Download the .CSV Files. It contains Access key ID and Secret Access key it will be used during GitHub Action Runners

# 3. Create Elastic Container Registry ( ECR ) :

- Create ECR with the required Repository Name
- After Created Copy the URI and keep it safe it will be used during GitHub Action Runners
	
# 4. Create Elastic Compute Cloud ( EC2 ) :
	
- Launch Instance > Name > Ubuntu > Create New Key pair > Network Setting ( Allow HTTP and HTTPS ) > Launch Instance
- Open the Created EC2 > Security > Security Groups > Edit Inboud Rules > Add Rule > port range (8080) > ( 0.0.0.0/0) > Save rules
- Click Connect it will open the terminal
- Copy and Paste the below command in Amazon CLI 

Code 1:

	sudo apt-get update -y
Code 2:

	sudo apt-get upgrade
Code 3:

	curl -fsSL https://get.docker.com -o get-docker.sh
Code 4:

	sudo sh get-docker.sh
Code 5:

	sudo usermod -aG docker ubuntu
Code 6:

	newgrp docker
	
# 5. Configure EC2 as self-hosted runner ( GitHub Action ):
- Github Repository > Settings > Actions > Runners > New Self-Hosted Runner > Linus
- Copy the Given code and paste it in EC2 CLI one by one
- Enter the Name of Runner : self-hosted

# 6. Setup github secrets( GitHub Action ):
- Github Repository > Settings > Secrets and variable > Actions > New Repository Secret

1.Name* :
	
	AWS_ACCESS_KEY_ID
1.Secret* :
	Download .CSV > Access key ID
	
2.Name* :
	
    AWS_SECRET_ACCESS_KEY
2.Secret* : 
	Download .CSV > Secret Access key

3.Name* :

    AWS_REGION
3.Secret* :
	Enter >> us-east-1

4.Name* :
	
    AWS_ECR_LOGIN_URI
4.Secret* :
	Copied URI from ECR >> 315865595366.dkr.ecr.us-east-1.amazonaws.com/simple-app << paste Before ( / ) <br/>
	To Paste >> 315865595366.dkr.ecr.us-east-1.amazonaws.com

5.Name* :
	
    ECR_REPOSITORY_NAME
5.Secret* :
	Copied URI from ECR >> 315865595366.dkr.ecr.us-east-1.amazonaws.com/simple-app << paste Afte ( / ) <br/>
	To Paste >> simple-app
	
## Once Code get Commit it CI-CD will Starts Running
