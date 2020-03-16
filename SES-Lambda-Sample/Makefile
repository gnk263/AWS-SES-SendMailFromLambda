BUCKET_NAME := gnk263-sam-bucket

build:
	sam build

deploy:
	sam package \
		--output-template-file packaged.yaml \
		--s3-bucket $(BUCKET_NAME)

	sam deploy \
		--template-file packaged.yaml \
		--stack-name $$(basename `pwd`)-Stack \
		--capabilities CAPABILITY_NAMED_IAM \
		--no-fail-on-empty-changeset
