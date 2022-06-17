# Research

Created: May 15, 2022 10:09 AM
Tags: Data Collection, SAT

# Observations

Through research, some time was taken to observe the Maths Club environment as it stands now, taking down some notes
while the club ran. It was noticed that a lot of the time, the club hosts people that do not necessarily care too much
for the questions, but would rather work on their own maths or get help on classwork. It seemed that many quite like
this aspect of the club as well, and it would be nice to encourage it in the future to make the club’s demographic more
open and not just catered to people who are competition focused as it is now. Some students in the club were also not
even doing maths, but rather had just come in because it was cold outside. It is a hope that in the future, a more
accessible process could encourage these people to at least try the problems out, and a range of difficulties would
cater for a wider audience. It has also been noticed that a lot of paper was left there after the club, and it will
definitely be a goal to reduce that, which the app should help with.

# Other Projects/Viability

Research was done into other possible projects that could be used in this one, namely for specific functions such as the
post editing or quiz system. As the system should be easy to use, it would probably be better to grab a few existing
GUIs that have had a lot of time and effort spent on them and refactor them to work in this system. One needed element
is an easy text editor that could be integrated with LATEX.
Eventually [AppFlowy](https://github.com/AppFlowy-IO/AppFlowy) was found, a Notion alternative made in Flutter. From
experience, Notion document editing and control is extremely intuitive, and it would be nice to have something similar
in this system. Behind the scenes, AppFlowy uses a package called [Quill](https://github.com/singerdmx/flutter-quill)
that enables the rich text editing. In this project, either fork of AppFlowy could be used, which requires manual LATEX
integration, or a rich text editor like Quill could be used to integrate LATEX support.

An alternative rich text editor that was also found was [Super Editor](https://github.com/superlistapp/super_editor),
which could be used instead. There is a demo [here](https://editor.superlist.com) which looks quite nice, and it is
backed by a relatively big company, which means support should be good.

In terms of actually editing the maths, a near perfect editor that feels natural like Desmos or
Symbolab is yet to be found. The one package that has been found that looks good
is [Flutter Tex](https://pub.dev/packages/flutter_tex), but that simply seems to render the typed out LATEX, which is
not the most convenient. It would be much preferred to have an editor, but for now, content creators might need to just
manually type in the LATEX and have it render while they type. Not ideal, but it works.

> ## Revision:
> Actually, this issue was being looked into a bit more at the time of writing this, and a few new really nice
> plugins have been found that seem to solve numerous issues. The same people that made Catex before made
> this [Math Keyboard](https://github.com/simpleclub/math_keyboard) for Flutter, which could be perfect. Not only does
> it allow Math typing, it also supposedly can calculate equality based on LATEX strings. A project
> called [MathCanvas](https://github.com/gongbj0113/MathCanvas) was also found that seems to have promise, but it is in
> its very early stages, so it may not be usable yet.

In terms of the backend and the login system, the plan is to use Firebase for the login system. Firebase works great for
user management and auth, so it should be a great way to build up the app with a platform the developer has experience
with.

For the blog posts, a variety of systems were looked into, including Jekyll, Hugo and ButterCMS, but they all did not
feel very native to Flutter, and (not including the former) all have their own proprietary CMSs they use, which would
end up costing a lot in the long run. Using Firebase as the whole CMS was considered, with all blogs stored in their own
format, and though that would definitely work, the sheer number of images and documents being put on the app may cause
size limits to become a problem. As such, it may be a good idea to use a combination of Notion and Firebase, where
Firebase outlines the document structure, and Notion handles all the files and possibly text. The developer has had a
good experience with Notion's APIs when creating their own blog with Next.js, and it seems like the only backend that
can be found that fixes the issues with file limits. It will be a roundabout solution for sure, but hopefully it can
provide the speed and flexibility the system requires, while also perhaps providing a document structure that can be
edited with the Notion app itself!