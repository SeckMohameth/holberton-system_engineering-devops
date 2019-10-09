# 0x19. Postmortem

## Vers App Goes Down 😨

![Alt Text](https://media.giphy.com/media/nrXif9YExO9EI/giphy.gif)


## Summary
On October 8th from 2:10pm EST to 3:23pm EST, EC2 instances on AWS stopped responding to request along with difficulties of users publishing content. All users on the beta version of the Vers platform were affected during this time. About 60% of iOS users and 25% of visitors on the web app were affected.



## Timeline:
* **2:10pm EST** - First reports of users not being able to publish videos and access the companion web app.
* **2:30pm EST** - Team looks into the issue trying to see if this is something involving Amazon Web Service (AWS).
* **2:53PM EST** - I get off the phone with Jeff Bezos to address the issue.
* **3:00PM EST** - The team (Me) begins to freak out after finding out that AWS is having a service disruption involving the S3 and EC2 services in the Northern Virginia (US-EAST-1) Region. Nothing I can do until Amazon resolves the issue on their end.
* **3:17PM EST** - Users are calling and emailing about the issue. I send out a message assuring them the problem would be resolved shortly.
* **3:23pm EST** - AWS is up and I was able to get the Vers app back on. 


## Cause:
The cause was a service disruption in the Northen Virginia (US-EAST-1) Region that caused users not being able to upload their videos and some having trouble with the web app.
The problem was someone at AWS was in the middle of recording their Vers video and accidentally hit the big red button that says do not touch.


## Resolution

![Alt Text](https://media.giphy.com/media/3ofT5WIy61ORed2bPW/giphy.gif)

I got my friend Jeff Bezos on the phone and was like "dawg what's up? Something going on with AWS and messing with my app!"

Jeff: "Don't sweat it bro. My people are on it. I actually was in the middle of using the your awesome, dope, great, amazing, extravagant, one of a kind mobile app Vers."

Me: "ight that's good to hear. My people will be on stand by waiting to get it back up."

Jeff: "Your people? Ain't it just you Mo?"

Me: "Bye Jeff"


## Future Measures:

I can't control what goes on at Amazon, but maybe I'll set up a few more EC2 instances and S3 buckets at other regions. My boi Jeff will give me a discount so all is good. If all else fails I'll just go to Google Cloud Platform (GCP).

## Author
Mohameth Seck - [Twitter](https://twitter.com/seck_mohameth)

**Role**: CEO, CTO, CMO, Frontend engineer, Backend engineer, UI/UX designer, iOS developer, Web Developer, and basically everything else. 
In other words I am the team.