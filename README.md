# WorkoutGenerator

**NOTE**
I started trying to push what I could do with zappa and flask on this site. User auth, while possible to manage, is impractical with this site model. Even without the user auth, this site is leveraging API Gateway in an odd way by serving HTML. You can see what type of progress I made on the develop branch of this repo.

I've been wanting to learn JS; AWS Amplify and the serverless framework in particular.
I will be converting this site to JS and keeping this repo around as an archive.

If you'd like to see the type of (neat, although simple) site that this repo is capable of producing, continue on.
[The site in action](https://pypower.themcilroy.com/)

## Deploy to aws with Zappa

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

Deploy your cert (this takes awhile to propigate):
> zappa certify

Tear it all down with:
> zappa undeploy