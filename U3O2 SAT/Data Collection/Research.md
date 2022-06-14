# Research

Created: May 15, 2022 10:09 AM
Tags: Data Collection, SAT

# Observations

Through my research, I took some time to observe the environment of maths club as it stands now, taking down some notes
while the club ran around me. I noticed that a lot of the time, the club hosts people that don’t necessarily care too
much for the questions, but would rather work on their own maths or get help on classwork. I quite like this aspect of
the club as well, and would like to encourage it in the future to make the club’s demographic more open and not just
catered to people who are competition focused as it is now. Some of the students in the club were also not even doing
maths, but rather had just come in because it was cold outside. I’m hoping that in the future, a more accessible process
could encourage these people to at least try the problems out, and a range of difficulties would cater or a wider
audience. I’ve also noticed a lot of paper just kind of left there after the club, and we’ll definitely want to reduce
that, which the app should help with.

# Other Projects/Viability

I was researching into other possible projects that I could use in mine, namely for specific functions such as the post
editing or quiz system. As I wanted the system to be as easy to use, it would probably be better for me to grab a few
existing GUIs that have had a lot of time and effort spent on them and refactor them to work in my system. I was looking
for an easy text editor that I could integrate with LATEX. I ended up
finding [AppFlowy](https://github.com/AppFlowy-IO/AppFlowy), a notion alternative made in Flutter. Coming from Notion,
where I feel like the document editing and control is extremely intuitive, it would be nice to have something similar in
my system. Behind the scenes, AppFlowy uses a package called [Quill](https://github.com/singerdmx/flutter-quill) that
enables the rich text editing. In my project, I could either fork AppFlowy and integrate LATEX support, or I could use a
rich text editor like Quill to integrate my LATEX support.

An alternative rich text editor I also found was [Super Editor](https://github.com/superlistapp/super_editor), which I
may like to use instead. There’s a demo [here](https://editor.superlist.com) which looks quite nice, and it’s backed by
a relatively big company, which means support should be good.

In terms of actually editing the maths, I’ve yet to find a really good editor that feels natural like Desmos or
Symbolab. The one package I have found that looks good is [Flutter Tex](https://pub.dev/packages/flutter_tex), but that
just seems to render the typed out LATEX, which isn’t the most convenient. I’d much prefer to have an editor, but for
now, we might need to jut manually type in the LATEX and have it render while you type. Not ideal, but it works.

> ## Revision:
> Actually, I was looking into this issue a bit more at the time of writing this, and I found a few new really nice
plugins that seem to solve my issue. The same people that made Catex before made
this [Math Keyboard](https://github.com/simpleclub/math_keyboard) for flutter, which I think will be perfect. I also
found this project called [MathCanvas](https://github.com/gongbj0113/MathCanvas) that seems to have promise, but it’s in
its very early stages, so probably not yet.

In terms of the backend and the login system, I plan to use Firebase for my login system. Firebase works great for user
management and auth, so it should be a great way to build up the app with a platform I have experience with.

For the blog posts, I looked at a variety of systems, including Jekyll, Hugo and ButterCMS, but they all didn’t feel
very native to Flutter, and (not including the former) all have their own proprietary CMSs they use, which would end up
costing a lot in the long run. I considered using Firebase as the whole CMS, with all blogs stored in our own format,
and though that would definitely work, I’m worried about the sheer number of images and documents we’re going to have to
put on the app, and the size limit is very much a problem. As such, I feel like it would be a good idea to use a
combination of Notion and Firebase, where Firebase outlines the document structure, and Notion handles all the files and
possibly text. I had a very good experience with it when creating my own blog with Next.js, and it seems like the only
backend I can find that fixes our problem with file limits. It will be a roundabout solution for sure, but hopefully it
can provide the speed and flexibility I’m looking for, while also perhaps providing a document structure that can be
edited with the Notion app itself!