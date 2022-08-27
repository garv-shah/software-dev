# Usability Testing

Created At: August 27, 2022 3:00 PM  <br>
Created By: Garv  <br>
Description: Documentation of Usability Testing for Maths Club  <br>
Published: August 27, 2022 3:00 PM  <br>
Tags: Programming, Software Development 3&4 <br>

For usability testing, similar to data collection in U3O2, two surveys were conducted. The individuals of the Maths Club
team were interviewed, along with a survey being sent out to the students who frequently attend the CGS Maths Club to
gather their opinions. This encompasses both types of clients: those who are to consume the content (students) and
content creators/admins (the Maths Club team).

The results of the survey are linked [here](https://gshah6110.typeform.com/report/QQU7meAh/8SDZwCirxBvqH80b).

# Survey (Students)

The main takeaways form the survey are that the app overall is quite a good solution that in general is better than
previous solutions and is pretty intuitive to use. The average responses are as follows:

- How useful do you find the app as of now? **(8.2/10)**
- How intuitive do you think the UI was? **(8.6/10)**
- Do you prefer using the app over the website **(Yes)**

Evidently, most users quite like the solution and prefer it over previous solutions. The UI is also quite intuitive, so
usability is good around the board.

When asked what could make the usability better, most users didn't find any changes necessary, besides one user, who
said "the elements are too big and the ratio is a bit broken". Upon further investigation, this user was interviewed and
had a couple usability issues on their device. Namely, their Android device was in an odd aspect ratio where it was
extremely tall, cutting off a lot of the text, and their device had enlarged the app as well, supposedly a zoom feature.
This resulted in a usability issue which influenced their experience with the app.

Such issues most likely can't be fixed on a device to device basis, but steps can be taken to make sure all information
is still accessible. Namely, certain elements can still overflow if the constraints are too small, so this could be
mitigated through code.

Besides that, all responses focused on more features which could be added to the app, including a wider array of
content, a public profile, comment sections, being able to star posts, being able to rate difficulties of posts, and
answer histories. All these can be added in the future, but are outside the scope of the current app.

# Interviews and Observations (Admins)

The interviews revealed a couple usability issues when it came to the Maths Club team. Observations had to be conducted
through a third party, as no direct contributors to the project could be present at the Maths Club sessions in the time
frame of the SAT.

A snippet of the interview with Mr. McCarty (Maths Teacher) can be found [here]().

## Image Issues

There were a couple of issues with images encountered by the team creating the questions. One of these was to do with
CORS, meaning images would essentially fail to load on the website, due to how websites work. This, combined with the
fact that most students could not install the app on their personal devices due to school restrictions, meant that many
students could not see the images added.

On top of this, it was quite hard for admins to add images in the first place. A simple Google Drive link pasted in
seemed not to work, as it was not the raw image. Even upon getting the raw image, links would expire, causing them not
to work, and they had to be in the format `https://drive.google.com/uc?id=XXX` to work properly. Discord images (which
would be the easiest solution) also would not work, since the school blocks images from Discord.

Overall, this makes the user experience surrounding images to be greatly diminished, as they not only can't upload
images from their own device, but they cannot properly copy images from their desired services either. A lack of
displaying errors or uploading images makes this frustrating, and could be remedied by programmatically altering the
URL (such as to the specific format above), or as a last resort, allowing for uploading media.

## Quiz Issues

One interesting usability issue that was found was where one of the Maths Club team members didn't provide a solution
for their question. Instead, they left the solution empty, causing certain quizzes to not work at all. This was a
typical PICNIC problem, but was a thought-provoking case of the app not guiding the user enough. Perhaps the app should
enforce the addition of a solution before submitting a draft to any other section.

# Summary

Overall, the app seems to have usability that is more than satisfactory for the audience and scope of this project. All
clients sampled prefer this solution over prior ones, and most found it intuitive and easy to understand. A couple
issues need to addressed, such as images, quiz issues, and a lack of math typing support, but the general response was
positive!
