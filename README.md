npm install -g serverless

serverless create --template aws-python3 --name datadistribution

pip freeze > requirements.txt

serverless deploy --aws-profile default

https://serverless.com/blog/serverless-python-packaging/