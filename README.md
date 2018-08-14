# WorkoutGenerator

## To Do

dynamo local is now working. It's just barely working. Need to test online.

## Deploy to aws with Zappa

[Set up your aws cli](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html):

```bash

pip install awscli
aws config

```

Set up your virtual environemnt:

```bash

pip install pipenv
cd /project/dir
pipenv install

```

Deploy using your own DNS and SSL cert using [Route53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/getting-started.html) and [ACM](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-public.html):

Once you've created your domain and cert, update these lines in zappa_settings.json:

```json

"domain": "themcilroy.com",
"certificate_arn": "arn:aws:acm:us-east-1:824269988929:certificate/a029b88f-a7f8-40a4-bd09-3a49787d4c73"

```

You'll now need to create a secret key for your app.

```bash

python
import secrets
secrets.tocken_hex(16)

```

Take this token and enter it into [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/tutorials_basic.html).

Within the zappa config, enter your secret name, key, and region used when making the key.

```json

"environment_variables": {
    "ENV_SECRET_NAME": "workoutgenerator/secretkey",
    "ENV_SECRET_KEY": "WORKOUT_GEN_KEY",
    "ENV_REGION": "us-east-2"
},

```

Deploy or update the site:

```bash

pipenv shell
zappa deploy prod
zappa update prod

```

Deploy your DNS and cert (this takes awhile to propigate):
> zappa certify prod

Tear it all down with:
> zappa undeploy

The site in action: [The McIlroy](https://themcilroy.com/)