# Sprint Review

Created: July 26, 2022 01:40 PM <br>
Tags: Sprint Planning, SAT <br>

## Progress!

In this sprint, the planned progress was achieved regarding the Login System, Adaptive Theming, and the frontend UI.

A successful login system was created which is linked to Firebase, allowing for three sign in methods: email, Google and
Apple (Face/Touch ID). Theming was also achieved, with a successful dark and light mode that responsively adapts to the
state of the system light and dark modes, allowing for a cohesive user experience.

Finally, a majority of the sprint was spent on the creating the UI, where every screen besides the admin screen was
built up panel and the post view. The admin panel was due to a lack of time, but the post view was intentional due to a
change in the design of how posts are generated. Previously the idea was to read the Quill page and create a map to
Flutter widgets, getting them to create widgets dynamically based on the contents on Firebase. Now that it seems like
Quill has built-in JSON serialisation, this might not be needed, which will be beneficial for the project, as the design
from Figma can be enforced through multiple Quill widgets inside normal Flutter widgets.

Fastlane integration was something that wasn't achieved during this sprint and has been scrapped from the project
entirely, due to the amount of time it was taking and the impracticality of having an elaborate CI/CD system for a
project so short. The decision was made that it was more logical to spent time on the app itself in such a short
timeframe rather than the deployment system, which wasn't even necessary for the SAT.

> A meeting has been conducted with Ms. Cotugno to discuss the progress throughout this sprint and gain feedback for the
> future.

## Blog:

For more information on the progress throughout the sprint and a review of what was and was not completed, please view
the blog of the project [here](https://garv-shah.vercel.app)
