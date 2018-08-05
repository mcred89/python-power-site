# WorkoutGenerator

Deploy to aws with Zappa:

[Set up your aws cli](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html):
> pip install awscli
> aws config

Set up your virtual environemnt:
> pip install pipenv
> cd /project/dir
> pipenv install

Deploy or update the site:
> pipenv shell
> zappa deploy prod
> zappa update prod

Deploy under your [Route53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/getting-started.html) domain and [ACM](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-public.html) cert:

Update these lines in zappa_settings.json:
> "domain": "themcilroy.com",
> "certificate_arn": "arn:aws:acm:us-east-1:824269988929:certificate/a029b88f-a7f8-40a4-bd09-3a49787d4c73"

Deploy your DNS and cert (this takes awhile to propigate):
> zappa certify prod

Tear it all down with:
> zappa undeploy

The site in action: [The McIlroy](https://themcilroy.com/)