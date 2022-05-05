
#
***
## 0x0F. Load balancer
###

For Holberton School
Cohort 16.

### General
Background Context
You have been given 2 additional servers:

gc-[STUDENT_ID]-web-02-XXXXXXXXXX
gc-[STUDENT_ID]-lb-01-XXXXXXXXXX
Let’s improve our web stack so that there is redundancy for our web servers. This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.

For this project, you will need to write Bash scripts to automate your work. All scripts must be designed to configure a brand new Ubuntu server to match the task requirements.

#### Resources:
Load balancer
Web stack debugging
#### Read or watch:
Introduction to load-balancing and HAproxy
HTTP header
Debian/Ubuntu HAProxy packages

![load balancer](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/275/qfdked8.png)


## Files included

| File                 | Details                                    |
|--------------------- | ------------------------------------------ |
| [0-custom_http_response_header](https://github.com/ruizdani301/holberton-system_engineering-devops/blob/master/0x0F-load_balancer/0-custom_http_response_header) | configure web-02 to be identical to web-01. Fortunately, you built a Bash script during your web server project, and they’ll now come in handy to easily configure web-02. Remember, always try to automate your work!       |
| [1-install_load_balancer](https://github.com/ruizdani301/holberton-system_engineering-devops/blob/master/0x0F-load_balancer/1-install_load_balancer) |	Install and configure HAproxy on your lb-01 server.       |


### Author
***
*Holberton School Student*

Juan Sebastian Posada  - [Github](https://github.com/Juansepo13) - [Twiter](https://twitter.com/@JuanSeb35904130) - [LnK](www.linkedin.com/in/daniel-ruiz-6925aa224)
