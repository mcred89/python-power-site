# WorkoutGenerator

This is a demo site that uses python, flask, and zappa to create a serverless web application. The site utilizes DynamoDB, Lambda, API Gateway, Route53, AWS Certificate Manager, and Secrets Manager.

This site costs ~$0.50/mo in Route53 hosting, but otherwise stays within the AWS free tier.

## Walkthrough

If you want to download and use the site on your own (or just gut the site proper and use the skeleton as your own), you need to set up DynamoDB local, a few things in AWS, and Zappa.

## DynamoDB local

You don't have to complete this step for the site to run. It's also easy enough to fully deploy the dev site that you may determine that this isn't worth it. I find it convient to run the site locally while testing and most of the local setup is automated within the app.

[You can download DynamoDB local here](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html)

To run it you just need extract the contents of the zip, navigate into that directory, and run `java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb`. You'll need to run that command every time you want to restart the DB. The DB is persistent across runs.

I've already configured the app (in run.py) to create DB named 'LOCAL' and use it when running the site locally.

## Set up AWS

1. [Create an AWS account](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/)

2. You'll now need to create a secret key for your app.

```bash
python
import secrets
secrets.tocken_hex(16)
```

- Take this token and enter it into [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/tutorials_basic.html).
- Within the zappa_settings.json, enter your secret name, key, and region used when making the key for both dev and prod.

```json
"environment_variables": {
    "ENV_SECRET_NAME": "workoutgenerator/secretkey",
    "ENV_SECRET_KEY": "WORKOUT_GEN_KEY",
    "ENV_REGION": "us-east-2"
}
```

- Note that you'll want to make sure that this key is stored in the region you plan to use for the site, table, etc.

3. Deploy your dev and prod DynamoDB tables using the [CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-using-console.html) teample in `cloudformation/user_db.yaml`.

- You'll have to specify the max read and write capcity for autoscaling and the table name prefix
- At this point you need to update zappa_settings.json for both dev and prod. Update these variables in the config:

```json
        "environment_variables": {
            "USER_TABLE": "dev-WorkoutGenerator-Users"
```

- **Important Note On The USER_TABLE Name** Your chosen table profix will added to this name: "-WorkoutGenerator-Users". For example, I used 'dev' as my CloudFormation parameter for dev and my tablename is "dev-WorkoutGenerator-Users" (just like the code block above).

4. You can deploy using your own DNS and SSL cert using [Route53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/getting-started.html) and [ACM](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-public.html):

- Once you've created your domain and cert, update these lines in zappa_settings.json:

```json
"domain": "themcilroy.com",
"certificate_arn": "arn:aws:acm:us-east-1:824269988929:certificate/a029b88f-a7f8-40a4-bd09-3a49787d4c73"
```

5. [Set up your aws cli](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html):

```bash
pip install awscli
aws config
```

## Local Env Setup

1. Set up your virtual environemnt

```bash
pip install pipenv
cd /project/dir
pipenv install
```

## Deploy to aws with Zappa

1. How to deploy or update the site:

```bash
cd /project/dir
pipenv shell
zappa deploy dev
zappa update dev
```

- Note that the `dev` arguemnt in the commands is referencing the top level enrionment names in zappa_settings.json:

2. Deploy your DNS and cert (this takes awhile to propigate):
> zappa certify dev

Tear it all down with:
> zappa undeploy dev

## Local Development

- Assuming your DynamoDB local table is already running:

```bash
cd /project/dir
pipenv shell
python ./run.py
```

- Navigate to `http://127.0.0.1:5000/` in your browser

## The site in action

[The McIlroy](https://themcilroy.com/)