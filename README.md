# WorkoutGenerator

Deploy to aws with Zapps:

Set up your aws cli:
> pip install awscli

> aws config

Set up your virtual environemnt:
> cd /project/dir

> virtualenv venv

> . venv/Scripts/activate

> pip install -r requirements.txt

Deploy or update the site:
> zappa deploy prod

> zappa update prod

Deploy under your route53 domain and ACM cert (don't forget to update zappa_settings) with:
> zappa certify

Tear it all down with:
> zappa undeploy

The site in action: https://themcilroy.com/
