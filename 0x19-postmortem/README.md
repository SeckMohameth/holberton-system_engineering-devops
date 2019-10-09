# 0x19. Postmortem

![Alt Text](https://media.giphy.com/media/nrXif9YExO9EI/giphy.gif)


## Summary
On October 8th from 2:10pm EST to 3:23pm EST, EC2 instances on AWS stopped responding to request along with difficulties of users publishing content. All users on the beta version of the Vers platform were affected during this time. About 60% of iOS users and 25% of visitors on the web app were affected.



## Timeline:
* **2:10pm EST** - First reports of users not being able to publish videos and access the companion web app.
* **2:30pm EST** - Team looks into the issue trying to see if this is something involving Amazon Web Service (AWS).
* **3:00PM EST** - The team (Me) begins to freak out after finding out that AWS is having a service disruption involving the S3 and EC2 services in the Northern Virginia (US-EAST-1) Region. Nothing I can do until Amazon resolves the issue on their end.
*


## Cause:
The cause was a service disruption in the Northen Virginia (US-EAST-1) Region that caused users not being able to upload their videos and some having trouble with the web app.
The problem was


## Resolution

![Alt Text](https://media.giphy.com/media/3ofT5WIy61ORed2bPW/giphy.gif)



## Future Measures:


## Author
Mohameth Seck - [Twitter](https://twitter.com/seck_mohameth)

**Role**: CEO, CTO, CMO, Frontend engineer, Backend engineer, UI/UX designer, iOS developer, Web Developer, and basically everything else. 
In other words I am the team.