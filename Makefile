build:
	pip install -r ftx_auto_compound/requirements.txt && sam build --use-container

test:
	sam local invoke

deploy:
	sam deploy --stack-name ftx-auto-compound-zlz --s3-bucket tingyao-sam-apps --capabilities CAPABILITY_IAM

cleanup:
	aws cloudformation delete-stack --stack-name ftx-auto-compound
