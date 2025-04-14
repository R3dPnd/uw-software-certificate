All right.
Alright. You guys can see my screen. Okay? Or did it go away?
Should see the slides. Okay, perfect.
All right. Let's go ahead and get things kicked off. Welcome to day. One of Tcss. 503. The lengthy named algorithms and problem solving for software developers. This is your second quarter of your graduate certificate in software development and engineering.
I and I'm excited to teach you all about various algorithms.
I'll go through the plan today.
Spend quite a bit of time introducing the course the syllabus I want you to get to know me and my my teaching philosophy, and and how I
how I go about grading and and testing those sorts of things. I I used to teach 5 0 1 in this curriculum, but I've switched to only 1 1 course a year. So this will be your 1st time being introduced to me. So I gotta spend a little bit of time
sharing how I work.
we'll also be talking about the various online resources that you can use for this course, and we should have by the end of the course or sorry end of the lecture today an environment that you should have set up with access to the git repo for this course. And so we'll take a little bit of time to do that. And then the actual content that we're going to be covering today
is a brief review of binary search trees and an alternate
implementation. That is a sequential implementation versus a dynamic which is what you probably did in 501.
Okay, so not a lot of like net. New concepts today. Just a bit.
so it should be pretty pretty painless to get you eased into the ease into the course. Okay.
all right.
So a little bit about me like, why are you listening to to me talk to you about algorithms. So
so my name's Kevin Anderson. You can find me Linkedin with the abbreviation of K. 3 a.
I am a Uw Tacoma grad. I studied computer science in the early 2,010 S. I've got my bachelor's
in 2013, took a year off and then went back to get my master's in the same program.
So I know that this particular certificate program is a
kind of an entry into the mass into any master's computers, masters in computer science program, but also kind of specifically the Uw Tacoma masters, which. So if you haven't, if that's something you're looking into trying out. You have questions about it, you know. Let me know.
When I was preparing the slides for this lecture today, I started realizing how dated that the degree is now 2016. It's been now almost 10 years. So it might be a while since I've been in that program, but I can still talk to you about the concepts and things that we learned, and some of the professors or many of the professors, are still the same.
So I can be a resource there.
so teaching at uw is not my my full time job. I teach once a year or as needed in the in the daytime I I work as the senior manager of the solution architecture team at blue origin, which is Jeff Bezos, rocket, rocket and Human Space
Flight Company.
I've been doing that for about
I've been at Blue for about 8 years, but I've been doing the architecture thing for a couple couple of years. So
my, my day job consists of designing and planning software implementations, either custom build or procuring new software and how they integrate with other things. So do a ton of of work in technology.
I've been working in technology for about 25 years now, various various roles
culminating to, you know, architect level work. I teach various
courses here at here at Uw, most most frequently. Now, I'm teaching just algorithms. But I do have background in data structures, database design and some system science for any of the
system engineers in the room.
And then other relevant experience. I I used to do a lot of analytics. So that'll show up in some of my lectures as well big into big into data.
So that's the last you'll hear about about me in terms of my my background.
Let's talk about something a little bit more interesting. Talk about the course.
So
What are we going to use in this course in terms of of tools.
We're going to be programming in Python. The majority of this course is is all python. This whole certification is mostly python, so it shouldn't be anything new to you. I have 3 10 x listed here on this slide, but honestly, anything, python 3. You'll be fine. I think I might even have an environment that's 3.1 2
like again, we're not going to be doing anything explicit to any versions. So choose any
choose any flavor, any version of python 3 x, and you'll be fine.
The lectures are going to be done using the ide called Jetbrains. Picharm
Jetbrains, the company Pycharm, the specific software. I know that a lot of folks are using Vs code nowadays. It is a really really good Ide. It's free. So a lot of people are using it. I,
coding is personal preference, right? The environment's personal preference. So I prefer pi charm. I've been using it for a long time, so I'll be doing demonstrations in Pycharm if you do choose to use something else like Vs code. That's totally fine. I'll still do my best to support you. I use Vs code in my day job as well, depending on what what I'm doing, so I'm comfortable with it. We'll we'll get you through it.
I will advise that you, as a student, you do get access to a student license for Piecharm professional.
which I recommend doing. So you can learn what that professional ide can do.
You just have to go to jetbrains
and look for student license. Your user, you you can use your Uw email address and
they'll send you a you can log in with your credentials for jetbrains and then activate your license that way
not required for the course. There are 2 things that might be better if you had the professional version. When we get into Jupyter notebooks.
It has a little bit more
full featured functionality for Jupyter notebooks in the professional version than the community version, but
not necessarily required. I'll show you the the roundabout ways to to do things in the community version.
And again, Vs code optional.
We will be using the command line a little bit. We're not going to be doing a ton of scripting or automation, you know. Ci, CD pipelines. That's for your next next course. We're we're just going to be using command line primarily for environment configuration. Get commands and those sorts of things. And I just recommend just getting used to using the command line. I know
I don't know the background of most of you. But this this course typically is for folks that don't have a background, a strong background in programming. They're trying to get into it.
And so I'll advise as a
computer programmer or software developer. The command line is your like, one of your best friends. You're going to find it to be super super useful, so it can sometimes be intimidating to people when they're new to computers, to have to type a command, and understand what the parameters are, and how to pipe things from one command to another like
it can be a little bit intimidating. I do recommend just getting getting used to it as much as possible, because it does make your life easier
last few bits. Zoom, hey? You found your way here. Good job
we'll also be using canvas. So the fact that you got to the Zoom call means you got to canvas to get the zoom link. So
congratulations. I mentioned Jupyter notebooks. That's a new
software library that we're going to be using for some of the lectures. I'll do a demo of it today. And then, lastly, for version control. This is totally optional.
I have a git repo for this course that you can check out from
from Github. I'll walk you through that
Uw! And apologies for for me not getting the latest and greatest uw used to have a student subversion server that you guys can use to like share code back and forth for group projects. That's totally fine. I'm not going to do a ton supporting subversion.
I haven't used it in a really really long time.
If if you guys are still using subversion, great use that to share your stuff. But I do highly recommend practicing with git, because git is just the facto standard. Now, subversion is a little bit dated.
So yeah, those are the the primary tools.
I've been talking for quite a few minutes. I'll take a pause. Any questions or comments so far.
Okay, I'm
here's a slide that just has a couple of good bookmarks included it. Just so you have. When you go to the the canvas site you can download the
slides for this, and then just use these links to bookmark. So this is purely there for for a handy, dandy reference.
And next, we're going to go talk about canvas
and walk through the different aspects like, I'm not going to teach you how to navigate through canvas. I'm assuming that this is your at least your second course in at least your second
quarter in canvas. So you you should know. You know how to log in and and get links and stuff. But I'm going to talk about my specific use of of canvas and what to expect.
So I'll go into canvas here in a second
before I do. I'm just gonna show the final slide again. This is just for reference, so you can download it when you download the slides.
Reading for next week is chapter 3.3 in algorithms version 4
Pdf is on canvas. So you don't have to buy the book which I'll talk about later.
So that'll be for reading. So these are your 8 slides for the week.
not very many. The rest is going to be all kind of interactive. And through canvas.
Okay.
So
when you get to canvas, you'll see my my homepage. I'm going to talk through a few items here on how to be successful in this course and talk a little bit about the office hours, etc, and then we'll go into more specifics about the
assignments and grades and those sorts of things.
Okay, welcome to 5 0, 3.
I'm your instructor. Here is your email address.
One thing to to note, like
students sometimes don't know how to dress their professors. Sometimes they say, Professor Anderson, whatever like. I'm not a professor, I'm not anything fancy. Just call me Kevin. I'm totally fine with that.
hey, Kevin? If you, if you must be, must be formal because of your culture, or what what have you? You can call me, Mr. Anderson? But Kevin is totally fine.
email me at K, 3, a. 2 at Uwedu. I will be monitoring that email throughout the day and get back to you as quickly as I can within 24 h. In most cases.
for additional help. I do offer virtual office hours. So directly after this course, like, say, the course ends like 10 min early, right directly after 1 50 I'll switch over to my to my personal zoom, and then I'll admit students into that for for one on one. Discussions about, you know, if you're struggling through a problem, or just, you know, need any advice or anything at all make myself available for that hour.
it is a gonna 1st come first.st Serve kind of way, so I'll let individuals in and I'll I'll help you, and others will wait in the waiting room. If there does end up getting like. Say, we're struggling to get through a particular problem with one student, and I have a line of 2 or 3, I might say, Hey, let's let's schedule some time, for later in the afternoon, or something to get through it. I've got some other students in the in line.
It's never really been much of a problem just letting you know that, you know, when you do join my office hours you might wait in the waiting room for a few minutes. I'll do my best to get everyone's questions answered in a timely manner, because, you know.
nobody wants to sit waiting in a waiting room.
So that's office hours. If that doesn't work for you.
and you need additional support. I know that previous courses they've had like
mentors, or or, you know, ta support for for some questions I'm assuming. That's still the case here, so use those resources as much as you as you can, or you want. But if you, if you want more of my time. That's totally fine. It just needs to be by appointment
like I mentioned, I have a day job. So you know.
7 to 5. I'm doing architecture work after 5, happy to to join and help you out in in the evenings, or even on Sundays, if if that works best for you. But we have to coordinate with at least 24 h notice, so I can be in the right spot for for those for those help, for those helping sessions.
All right.
What? What do I assume you're going to know? Coming into this course?
You should have already taken data structures.
I originally wrote the course for for this cert. So I know quite a bit of what's what's there. So I have assumptions that you know all the stuff that's in that course, primarily need you to know big O notation.
And
I'm not going to teach you what it is. Or the math behind it right? I'm gonna assume that you've learned that in the last course.
well, so we're not gonna be trying to like.
establish or solve big O, right in this course. But we are going to use it to reference algorithms. And you know why one algorithm is better than the other, because the big O is better. And those sorts of things
also expect you to be able to determine what a what a
time complexity of an algorithm is. We'll talk through some techniques and how to do that like the master's theorem. But we'll also, you know, just need to read code and say, Okay, this has, you know, 2 nested loops. Therefore it's n squared something like that.
Because I'll put requirements on you to implement an algorithm that is linear time or something to that effect.
You also should have a background in your basic data structures, trees, queues, stacks, arrays.
I'm going to be. I'm going to be referencing those in in passing. When we talk about an algorithm, we're gonna say, throw something on a stack. You need to be able to know what the behavior of a stack is to be able to understand why the algorithm works.
As I mentioned before, we will not be
forcing you to buy any texts for this particular course, which is great.
Tuition's already, and high enough. We don't need to have you spend any more more money.
so the books that are available can be checked out at the library if you, if you like the physical copy, or you can.
all the all of the specific chapters that we're going to be assigned are in the
are going to be posted to the, to the modules.
If you are.
if you like, hard copies, the algorithms version 4 from Cedric. Is this this guy here? It's
more approachable I'd say a lot more pretty pictures.
easier, easier. Less. I will say it goes a little bit less into the math. Than this guy here, this intro to algorithms. This is the Stein, Liserson, Corman and rivest
this, if you're if you're wanting to get into algorithm research right? And really want to understand the math behind computer programming like this is where you where you want to go. Super super, dense and highly mathematical. So I'll provide different chapters from different ones, whichever one I feel is the best to explain a particular concept. But most of them are coming out of the the nice easy algorithms book.
James  Godwin
James  Godwin
00:19:49
This tax theaters.
Kevin Anderson
Kevin Anderson
00:19:52
Alright!
A little bit of background noise. So make sure to check your check. Your mute. Just to make sure.
Okay, so that's the the content.
I'll be spoon feeding you most of the content. So I'm not too worried about folks struggling to get through all the reading, the reading expectations here are pretty light. I do expect you to read the chapters, but I'm never assigning more than a dozen pages or so, and anybody can get through that in a week.
Okay, how to prepare?
Well, prepare by showing up starters. You.
I'm I'm sure that you've got this in the the previous lectures or the previous courses. But
my my philosophy, which is pretty common in in teaching programming, is that you have to do
right. You have to practice. There's the the old adage that you can't learn to ride a bike from reading about the physics behind riding a bike right?
You might be able to, you know, be an elite bike rider, if you understand the physics and know how to draft behind trucks, or, you know, like all that stuff to make you elite. You have to know the the science behind it, but you can't become elite just by reading right? You've got to practice.
So I highly encourage anybody who's trying to get into programming, to to practice practice practice.
I I find the best way to do that is to find an a personal project
on your own that will force you to kind of learn and explore new concepts as you as you as you, as you pick them up, or as as you run into them.
So
In an addition to this course, or maybe, after you've completed the this curriculum, go find a find, a little web app that you want to build or an app on a phone that you want to build and just just experiment practice practice practice. That's the that's super important.
but that's the generic generic advice. I have 2 pieces of advice specifically for this course.
Number one is to draw pictures, use props.
There's a lot of abstract concepts here in this course. When you're doing a we'll do an example like sorting. You need to know, hey, that this thing splits into 2, and then this thing splits into 2, and then you have a few things swapping, you know, doing. I'm talking about merge sort, right
hub.
or when we talk about self balancing trees, where you have a dynamic structure of a of a parent, and it's left and right nodes. You have to do some some rotating like. Move the left node to the top of that node, and then push the other one down. So there's a lot of
of cur dot left equals cur dot right cur dot parent equals ker left like there's a lot of these simple lines of code that can really easily get lost. So I recommend using a white using a whiteboard
pencil and and paper, or what some students have done which works really well
is, have a stack of post-its, especially in the graph traversal things, where you have a post-it and represents a node that has a left and a right pointer.
And then you can move those things around. So pictures are going to help you a ton in in an algorithms course.
next is to get really good with the debugger. So at this point, you've been spending plenty of time writing python. You know how to write, build data structures. You know how to write their common methods, and maybe you used the debugger. Maybe you didn't maybe used print statements to figure out when things were going wrong.
this course will make good use of the debugger because you're going to have things that run away that you don't know why they're doing what they're doing. So you need to step through the code
with, and I have one special request or recommendation. Here is when you go through the debugger.
But or even just, you know print statements are fine.
but as you're going through and trying things out with your code, make predictions on each step or on key steps.
why? And make that an intentional thought in your mind. Why is this?
Because it gives your brain. It's it's kind of a neuroscience thing. It gives your brain kind of an opportunity for one of 2 things, one positive reinforcement to say, yes, I understand this because I predicted that the value would be X, and it happened, and you had that intentional moment of Aha! I do understand it.
If you get it wrong.
then you have that opportunity to to reassimilate the knowledge back into your back into your brain like, Oh, I got it wrong. I understand that it did this other thing. And here's why. Now I now I know, so it kind of is. It reinforces a correction to your understanding.
and that intentional thoughts of when stepping through and making predictions is a is a great way to solidify that knowledge that could otherwise be a missed opportunity. So
those are my 2 2 pieces of advice, for this course. Draw pictures and step through code. Use the debugger and make predictions on the outcomes.
Okay, let's talk about the yeah. Is there a comment?
Got it.
Aden Abdulahi
Aden Abdulahi
00:26:02
I don't hear. Is it only me? Or is there a problem in the voice.
Kevin Anderson
Kevin Anderson
00:26:09
Can anybody else hear me.
Weilan Liang
Weilan Liang
00:26:13
Yes.
Kevin Anderson
Kevin Anderson
00:26:14
Yeah, okay.
Sean Warlick
Sean Warlick
00:26:14
You're you're coming through pretty clear over here.
Kevin Anderson
Kevin Anderson
00:26:17
Okay.
Aden Abdulahi
Aden Abdulahi
00:26:19
Okay. Thank you. Very good.
Kevin Anderson
Kevin Anderson
00:26:31
Okay, alrighty. Let's see one second, all right.
So I'll go ahead and keep going. Hopefully. Adam gets gets his audio back. So core structure.
This course will be 10 sessions.
This is week one we'll wrap up at week. 10
consists of 9 learning modules, including this one. There's a little bit of learning in this one. And then the final week of the class is a review.
Basically, I will take all of the key aspects of the course and compress it into 1, 2, and a half hour lecture that you can basically keep the slides for and keep the recording of that will just, you know, highlight, the key things that you needed in this in this course. So
that's the way that the things are structured.
Most of my lectures will be live interactive. Just like just like this one. But there are
times when I get pulled away and need to need to travel. So I have pre-recorded lectures that I'll drop from time to time, and I'll give you the heads up when that when that needs to take place, and then you'll you'll watch the the recordings
and then we'll, you know, you know, discuss the in the following week. If there's any questions.
I will assign
homework. I have 4 assignments for this course, and 4 quizzes. Assignments will be posted with about 10 days before they are
before they're due.
So you have plenty of of time.
None of the assignments in this particular course are particularly excessively challenging. Some of them are,
actually relatively simple compared to how how difficult they could be. But it's really
I'm just trying to get you practiced and reinforced to get some some good habits and programming. So,
that's the the key kind of structure to the course my lectures are going to be. And you'll see this today. The 1st half is typically theory.
Slides, animations, those sorts of of things. And then the second half, or the final quarter of the of the course, I'll switch over to a Jupyter notebook or pie charm explicitly, and then we'll we'll do code
interactively.
So you get kind of
both both sides of the house right. You get the theory, you get the concepts, and then we get to apply those concepts in in
in code.
The syllabus.
We'll talk a little bit about here. It's the high level version. The downloadable version has
more detail.
And let's see, we're doing on time. Okay?
So I'm gonna talk through what we're gonna cover in this course and a few additional.
and we'll say thoughts that I have to prepare you for succeeding in this course, and then and then we'll take a break
in this course. We're gonna cover kind of 5 kind of main classes of of algorithms.
we're we're going to start with a little bit of data structures. We're going to be talking about balanced search trees. And we're going to be looking at some graph implementations and and how those play into
algorithms. So the 1st 2 weeks are going to be a little bit of more data structure than in algorithms.
But after that we're going to talk about greedy algorithms which are your intro to algo kind of concepts
change making. This is super simple algorithm that you've done. Probably, you know, a million times in your life.
You somebody hands you somebody. You're working a cashier. And they you need to make 77 cents and change. How do you choose which coins? Well? You choose the biggest denomination, right? The 25 cent pieces. So you choose 3 of those, and that gives you 75 cents. And then you choose 2 pennies. So we're going to talk about those kind of classes of algorithms where you're taking the most or the least at any given step, and then building up a solution from that.
get your feet wet into into algorithms. We'll take it up a notch and talk about, divide and conquer, which usually leverages some form of recursion and
requires you kind of to solve 2 different problems for for an algorithm, you have to figure out how to break up the problem and solve the problem on smaller pieces. And then you have to solve the problem of putting all of those solutions back into one into one final solution that gives you the proper answer to the question. So divide and conquer is the second class of algorithms.
We're going to study.
We're then going to move on to a technique called backtracking. And if you did the maze traversal, you probably already did a little bit of backtracking
from your in your previous previous courses.
These are for problems that have a really large search space. And what do I mean by search? Space means that there's a lot of different options that, or a lot of different combinations of solutions that that could possibly possibly work, and you have to search through each of those to determine which one is the the most optimal.
So backtracking is a way of traversing through the problem, getting to a spot where
where your condition cannot be met, and you have some sort of constraint. You go. I've met my constraint. I can't go further, you usually using a stack or some sort of like recursive property, you recurse back up and then take another path until you reach the end, or until you've either solved the problem or until you've exhausted your search search space
you will have a an assignment on the Sudoku solving problem.
You also have an assignment on Straussen's matrix multiplication. So those are the 2, the 1st 2 assignments.
Then we're going to take 2 weeks to talk about dynamic programming.
And I love teaching dynamic programming, even though it's it's 1 of the more more tricky subjects, especially for for new programmers, because for me it was the kind of Aha! Moment that
changed me from a kind of a scratch scripter like I knew how to do for loops. I knew I knew how to do. You know, routines subroutines like I knew object oriented programming
when I learned dynamic programming. That's when I felt like I changed from just writing code to actually like writing software,
and the reason for that is that the
use of of these 2D arrays to build up a solution based on prior knowledge of smaller sets of the problem. Like it's, it's unintuitive, it really is.
when you, when you. It's hard to understand how this is really, truly solving the problem.
especially for like a brand new brand new software developer. So once I've learned, hey, this is a technique for solving problems, it really like in my head, changed me from this scratch to to more of a pro. So I spent 2 weeks on it.
And the second week we do a kind of a group exercise where? We have a a problem that I'm not going to spoon. Feed you the answer to right? We'll get into breakout groups and we'll try and figure out, hey, how can we build up the sum of numbers properly? And so it's kind of like more of an interactive group assignment to learn to learn dynamic programming.
And then the last bit of content that we're going to be covering in this course is analytical algorithms.
Like I mentioned before, I come from a data background very much like the the aspect of data analytics as part of the software space. So I do a bit of a do, a lecture on various types of of
algorithms that you would use in analytics
things like clustering that help with recommendation. Engines like you. Go on, Netflix, and you see you would like this, this and this. Well, those are all. Some form of of clustering
similarity between you and other customers that have similar likes. So
we'll talk through a few of those algorithms to kind of give you an appetite for what machine learning and analytics is in in practice.
Okay, couple more items here. I already talked about the lectures.
Learning objectives is fine.
If you struggled to succeed in 501
in terms of like the coding it's gonna continue to build. So make sure that you're getting all the help you can do self assessment tests to make sure that you're you're on par with what you need to be. And if you're below where you're at
ton of resources here, like you're paying us a decent amount of money to learn.
and you make use of of your mentors of me as much as you can, since you know.
that's what you're, it's what you're paying for.
let's see, please read through the details of of this. It's not that long of a of a syllabus.
I'm only gonna touch on the the high points, but I'm gonna like, assume that you're have have read.
Read all of this.
I have a few things on, on grades and assignments. So I'm pretty flexible.
If an assignment is coming due.
and you need a little bit of extra time because you have some sort of of life event, something happening. It could be something fun like I'm not.
I'm not going to evaluate your reasons for needing to shift things around. But if you give me notice right, give me 24 h, 48 h. Notice that you won't be able to to meet a deadline for an assignment.
By all means let me know, and I'll make I'll make exceptions.
If it's every single time. Then we'll have a talk right? Be an adult everything in moderation.
So I'm I'm I'm flexible. There.
Just let me know. I'm not a fan of telling me the day of that. You're not gonna get it done. A few reasons for that one is I schedule when I'm gonna automate my
migrating.
and if you if you haven't deployed anything, then I've got to do things differently. So I like notice. And also I'm also trying to help you get used to what it's like to work in a software development environment. And
you will often have people depending on you like you have to get your code done for someone else to get their code done. So meeting deadlines is is critical and
you gotta let people know. And when you're gonna miss them. So
I'm flexible. But just let me know.
Also, there's 4 assignments.
They make up 75% of your grade. The 4th assignment is worth a little bit more in terms of points than the other 3, because it's kind of the final final assignment that puts all things together.
I have 4 quizzes also, and those quizzes make up 25% of your grade, and the lowest quiz score is dropped.
Specifically the lowest attempted score.
Why do I say attempted? Because if you got 10 out of 10 on the 1st 3 assignment, 1st 3 quizzes, and choose not to even try the 4th quiz. You get a 0
on that quiz. It doesn't drop it. If you didn't try it. So you got to at least participate. Even though you know that that score is either going to be
dropped because everything else is a 10, or you know, what have you so still expect you to do the do. The
do. The quiz
quizzes in this course are used as reinforcement learning, so I don't have any gotchas or trick questions in the quizzes.
I'm not trying to test, to make sure that you understood every single aspect of the reading, and things didn't get commented in lecture, but I have a you know none of that stuff, do I do?
You have 2 attempts to do the quizzes, and it's just reinforcing. What are the key aspects?
one thing that I neglected to to mention.
This is a fairly introductory course in programming.
Right? I know it's a 500 level. But it's it is a kind of an intro to programming level course.
and
I don't expect you to be able to take this knowledge and immediately jump in the deep end and start writing exquisite, exquisite software like, you're not going to be a senior senior engineer after taking this course.
Sorry, but what it will prepare you for is
being able to have the base knowledge to be conversant with senior engineers. So you can learn the more advanced techniques. When you go and get a job somewhere or in, as you continue in your in your education, right? I'm very big on vocabulary and conceptual information like you need to be able to understand concepts so you can reason with it and have conversations with others to try to solve problems.
So that's what my quizzes are about, making sure you understand the vocabulary
and making sure you have a basic understanding of the of the concepts.
that that, you know. Make up the course.
Couple more things if you do. Bomb happens. Bomb bomb a quiz.
bama, an assignment. There's not a lot. There's 8 8 different assigned items in this course.
So if you bomb something, let me know that you need to make up those points. It's something that you know. Grades are important to people.
and if you want to to make up that bombed assignment, I'm I'm here for it right? I have
a soft spot for people that work hard.
and if you are willing to put in the extra time and effort to to do things, then I'm willing to reward that with with an extra credit assignment to get those points back.
It's not designed for, hey? You got 9 out of 10, and you need to get that 1 point back like I.
That's fine. We can work. We can talk about it, but it's really a valve for those that have really bombed because it's extra work for me to to assign the the homework extra work for you, and I got to grade it. So you know, I'm only, gonna you know, offer it in. In.
you know, cases where the grade is really going to be impacted. Not for like one z 2 z point kind of things.
so there is a late assignments policy here. I'm only going to do this if I if absolutely necessary.
most of the time. If you let me know I'm not gonna penal penalize you for getting things in late. You just gotta let me know. Okay.
and yeah.
So I've talked again for quite a while. I'll take another pause.
Any comments, questions, concerns.
Okay.
I've got one more.
One more thing to talk through. The kind of one of the elephants in the room when we talk about software development these days, and that is use of generative AI
Llms to write your code for you.
You'll actually, you're actually gonna see
in my ide that it has baked in AI which offers more intelligent like autocomplete like, hey? You're! I think you're trying to do this. I'll I'll write some code for you. That's fine.
But I highly encourage you to not leverage that during this course.
The autocomplete is is totally fine, but, like, make sure you understand it. What I'm more concerned about in this course is the use of
Gpt or similar to generate your code.
I'll tell you that I am not going to spend any any time trying to determine whether or not. Your code is something that was generated for you, or something that you wrote.
Okay.
so if you use something like that and submit the assignment, I'm not going to pay attention to whether or not you wrote it or not, and like I'm not going to run it through any sort of tools.
I'm just going to to grade it and make sure it works.
That is, selling yourself short because you aren't actually learning how to solve the problems.
Will you have this wonderful tool when you get a job somewhere, absolutely will your bosses and colleagues expect you to use those kind of tools to accelerate your work absolutely.
But it is a a hindrance to your ability to actually learn and solve the problems.
So I I guess, like I said before, it's on you.
you some if you use those to solve your problems in this course. Fine.
But you're here because you want to be good developers. You're here because you want to learn how to use the how. You want to learn this new, this new skill, this new way of thinking, this new way of solving problems.
And you're not going to learn those core ideas nearly as well. If you're letting something else do your work for you. Okay?
So it's the last I'll say on the subject, it's an honor system.
It's so tempting to to use rather than think through the problem, because you're all everyone's busy. We want a fast solution. But
education is not the time to cut corners and sell yourself short.
You get 10 weeks of your life to learn this specific with, you know, with experts in the in the field, helping you out. If you're not spending the time like you're, you're you're wasting your time and energy and money. So I'll get off my soapbox on the Gpt stuff.
Again, honor system up to you. Highly discourage the the use of those things in solving your problems.
Okay?
Oh, sorry. One more thing about about grades and assignments.
So when I provide you with code for the assignments, I'm gonna give you like sample code, like
signatures for the
for the classes and methods and those sorts of things. And maybe I'll throw a few tests in.
I want to acknowledge that I am, or I want you to know that I am not going to provide you with every single unit test that I'm going to use to grade your grade. Your stuff?
Couple reasons for that.
One is that it would be super easy for people to gain the system. And just, you know, write code that directly responds true or correctly to the the test that I provide. So you wouldn't have to do a proper implementation.
And B, it's a training situation where you're not going to be given all of the unit tests for your for your work.
You're going to have to write your own. You have to understand the edge cases. So I'm going to give you maybe one or 2 tests. But just because your code passes those tests that I give you in in the sample code that doesn't guarantee you a hundred percent on your assignment.
Things are going to grade you on.
does it return the proper proper values? So I'm going to give you things in the description, in the, in the text of the of the assignment that says, you know.
if empty, return none otherwise return the value of the node or something something very explicit.
and if you don't respond in that way, it's going to be docked points because you're going to be given interfaces that you need to adhere to, and you need to understand how to interpret them and and provide results.
If you want eyes on your assignments ahead of time, like, Hey, am I in the right direction? Use use office hours, and I'll happy to go through your code with you to make sure that you're setting yourself up for success.
It's a lot of info introducing the course. But you all should know exactly what to expect from me.
reach out to me on email or or on canvas.
actually, let me ask you a quick question, as I haven't actually seen any updates from from the course this year
previous years we were using discord or slack. Do you guys have a discord or slack channel for for this cohort?
Or is that something that we've stopped doing? Yes, you do.
Okay, great. I will reach out to whomever is running that and get
get added to the server.
Cause I'll do a discord for 5 0, 3 as well.
because that's a nice easy way to keep
to keep in constant contact. I respond to discord a little bit more frequently than I do email during the day. But most of the time I'm in meetings or heads down working so working hours. I'm still a little bit slow, but faster on discord.
All right. Let's see, let's go ahead and take.
Let's take a 12 min. Break come back at 1035, and then we'll start talking about the programming environment, the github, and then we'll go through a Jupyter notebook and then I'll let you guys go.
Let me set a timer.
and all right.
We'll be back in just a few minutes.
Resume that recording.
Okay, let's go back to canvas
and talk through a couple more items here. Just because I have some expectations.
Okay, so everything you're gonna need in the course is gonna be found in the modules section. Okay,
this 1st module. This is just the boilerplate that is, for every course. If you've read it from other courses, you don't need to worry about it, but it's just reference stuff that is there for for your review.
other items prior to week. One right? We got this module 0, which has a couple of links right? It's got
link to the git repo. Obviously, I'm making sure that that's available in many different spots, so you can gain access to it.
for those that might need a little bit more of a review on Big O, I've got
web article that covers big O in a pretty decent way.
Nice Easter egg at the end. If you have read it all the way through, where there, where? He says, Oh, Big O doesn't actually matter, and provides some examples of of why it doesn't. But it's it's still a fun fun article, anyway. I recommend giving it a read probably a 1520 min. Read
also, I've provided some
some instructions for how to install Python and Pycharm, how to get git hub and secure shell set up so that you don't have to authenticate. Every time you do a git, push or get pull
configuring the course repo, etcetera. So I've got
some instructions that I'll talk through maybe some of them today. But I'll tell you this.
I didn't go through and read these instructions and verify that they are still, you know, character per character accurate. So if you end up going through one of these and a step fails, or something. Just let me know. I'll get it updated, and I'm sure they'll be fine. These aren't things that change very often. You know, they didn't have any issues last year. But if anything has changed just just surface it to me, I'll get fixed as soon as possible.
Okay, all right. So that covers module 0. I need to.
Actually add something. So there is in the
I'll add this. So you get a link to it. But in the discussions.
Tab, there is a week 0 discussion
that I've posted to have folks reply to.
I want to know what your background is like. Am I teaching a class where everybody is like Brand, Brand, new, with no experience? Or am I teaching a class with most of you that have been, you know writing software in your day job, and they're just looking for a certificate. I like to know what the what the level is.
so I can tailor things accordingly.
I also like to know more about you like, why are you going after this course? Why do you want to get this certificate? And now that we've gone over all of the specific items that we're going to learn in this course, tell me what what's most exciting to you.
That will help me, you know, really focus my time on the the things that are most most interesting to students. So please post your responses here and maybe
respond to others. If you have common interests, right? We're trying to build a little bit of community here.
As as well, because these people will be your cohorts that maybe when you get a job you might coordinate with with them on questions and experiences, etc. So
that's week 0 discussion, and that should
I'm gonna cover the big, the big items
slides are always gonna be posted before core the before the
before the class. You can download them. I don't post the modules too far ahead of time, because I do make edits as we go right, because I'm always constantly improving and tweaking. So you'll see module 2 be posted usually around like Tuesday, Wednesday. Sometimes as late as Friday. If I'm really really really busy. But you'll get Module 2 posted here soon, which will have links to the slides and code, etc.
Okay, so let's get into content for for today.
1st things first, st I want to show you the git repository so you can get familiar with that. So
if you follow the links in the module.
you'll get to the the code repo for the the course.
I keep things updated like looks. I was updating some notebooks as of 13 h ago. Sample code and assignment code gets updated each each quarter with refinements and improvements.
So you'll want to clone this repo and keep up to date.
It's broken up into 3 main folders. It's pretty simple assignment code. This is code that is going to be associated with any of the assignments that are
any of the assignments that are coming for the course. So yes, you can take a sneak, peek, and see what the assignments are going to look like.
but please don't do them
because A, you won't know what I'm expecting. Just by the code. And BI reserve the right to change things like the matrix multiplying starter code. I might change that assignment entirely this year, because, I've got some ideas on how to improve it right? So
while you might be able to look ahead. I don't encourage you
expecting to be able to get too far ahead in the course just in general.
if you do, if you are the type of student that like really needs to get ahead because I don't know. Maybe you've got an upcoming wedding or something that you need to get ahead of the course, you know, work with me, and we can talk through it. But, generally speaking, I want everybody to kind of stay at the same pace.
So outside of assignment code, all of the slides that have code in them for the course that code will be in a python file broken out by week. So week one you'll see code for binary search tree for week 2. We're going to do binary search trees and red black search, binary search trees.
And so all of that code is going to be here for your review as well.
And then, finally, the most interactive are the the Jupyter notebooks. I have 5 total for the course. I'll probably create a few more to to for like weeks 4 and 5.
But this we're going to be talking through Jupiter today, and we'll be going through the trees one. But this is where you would go. Get those code, the that code, or.
if you prefer to not deal with, get all of the course code is going to be available for download in the modules. I will do my, I do my best to. If I do make a change in the git repo to, then make those changes reflected in
canvas. But it's a manual upload. I don't have the. I don't have that stuff automated on push maybe that's good good
project for me to work on this quarter.
but when I do push code into the repo. I have to manually save it here, but they stay pretty much up to up to date.
Yes, you submit this question in the chat. Do we submit homework assignments through canvas? Yes, I will provide you with the file names and
requirements and rubric for for submitting the python file to canvas upload.
Good question.
Okay, so how do we get this
this code available in your in, in your environment?
Alright, let's talk through it. So
you want to get the URL
from from the code base. I prefer secure shell over https, but you can do either.
You just want to copy the the URL for for the repo.
and then I'm going to open up pie charm.
Vs code is pretty similar. Right? You just open from version control.
Same same idea.
We're going to create a new repository
on our local machines. That's synced up to the the Github Repository.
So I'm going to click clone Repo.
and it already, you know, assumes that I want to use git. I'm going to paste the URL,
and I'm going to give it a new
a new folder name, because I already have Tcss. 5 0, 3 there, so I don't want it to warn me.
Defaults are are fine, so I'm gonna hit clone
because my secure shells already set up. I don't have to authenticate it already knows who I am if you want to. Follow the instructions that I've provided
to get your your Ssh key set up, you can go ahead and do so.
okay.
second.
So
in. Now that I have it clone, I can start looking at and executing executing code. So
let me talk through a few of the nuances here. So
it's not your 1st project for python, so you should already have a decent understanding of of
which interpreter to use right? This is which version of Python are you installing specific packages for this environment? I know you haven't talked. You haven't learned a ton about managing packages and those sorts of things that'll come a little bit later. But it's good to get a little bit of exposure
today.
So in the folder or in the in the repo. I've put some hard requirements right? These are all the libraries that are needed for for the code base. Well, you need to install those requirements. In order to get this to to function
and you need to kind of know where to install these these requirements to. So that's where environments come in.
you can choose to have, you know, just your native python environment. That's totally fine. I prefer to use what's called conda, which is a package manager. So I can create environments that are specific to specific projects. So when I install Jupyter, 1.0 for one project, it doesn't cause problems with another project that might be using Jupyter. 1.2.
Okay, so I'll show you a little bit of of how to use Conda. It's not
It's not expected, but just gives you a little bit of a say, an intro to how package management works.
So I
it's assuming I want the python 3.9 5 0 3 environment. I'm going to change that. So how do I change the environment? I will go to file settings.
I think on the windows it's like
files project settings here. It's under pie charm settings.
and we want to go to the project sidebar and choose the interpreter.
Oh, it's yelling at me, saying that this is an invalid interpreter. That's great. That's fine. I'm totally okay with that I'm going to add a new interpreter.
I'm not going to run anything online which you you can have this execute out on the cloud somewhere. I'm just going to add a local interpreter.
and I don't use python virtual environments. I use Conda.
So I'm going to create a new environment. I'm going to make it python 3 dot 10,
just just because I'll show you that you can select different python versions. And I'm going to call this, you know my
Tcss. 503 environment.
And once I've selected it, it's going to create this new kind of core environment without anything else installed into it except for the base base items that we've that I've predetermined. Okay.
so now, I have this project associated to this specific environment for python. Okay.
so now, if I want to install these requirements? Your your ide sometimes will be like, hey? Would you like to? Would you like to install it and give you little helpful click button clicky things that will help you do things quickly. But this is an education class. So I'm going to show you some other ways of doing things. So
I'm I'm going to open up terminal again. This is the Command line stuff that I talked about before.
your terminal may not look like mine. I use software called Oh, my gosh.
that gives me a little bit more decoration in my, in my terminal like, I can see what conda environment I'm in. I see what branch I'm in in my git repo. I see the the full color coded path of where I'm at, so it may look different for you. If you want to learn more about
making your terminal more friendly, just let me know. But I'm going to assume that you just got a kind of a basic basic view.
So what I'm going to do here is Pip Install.
So Pip, is the package manager for python. Right? So I'm going to do a pip install. And instead of typing
Jupiter pandas requests, I'm just going to say, install the requirements. File requirements dot text.
and when I hit enter it is going to install all of the
All of the requirements for this project
explicitly at the version number that I've that I've said
most of these are fairly fairly small
pandas and psychic learner a little bit big.
but they should install pretty quickly. And so now I should be able to execute all the necessary code.
Okay, okay, that's your environment.
couple more pieces of advice. So anytime you come in here.
You're going to
because this is my repo that I'm going to be making updates to. If you come into your command line and do like a get status.
You might see that, hey? You're behind commits from origin. So just for awareness, origin is the remote version of the repo. It's the one that's out there on Github com.
right? So that's when you have references to origin. That is the the repo that exists on the Internet.
Okay? So this shows that I'm up to date with with origin. Main.
I just have a habit of
being, we'll say, oh, overly exhaustive when it comes to keeping my code up to date. So I'll often just come in and just do a get poll just to get the latest information from from what's there online?
Now there are going to be times where you might have accidentally changed some code right? Hello, world.
You've changed code.
If I'm in here and I type get status
I'm going to see. Hey? There's there's change to that code, and maybe I'm being
being wild and like trying to do things that
I don't. You're not thinking clearly, or you're experimenting, and I don't know. Sometimes you might accidentally do something, and let's just say we have added this code to a commit. So that means, Hey, I actually know that I've changed this file, and I want to save those changes. So I'm going to do a git. Add, which adds that file into into what would be committed code to the repository.
And now, if I do a get status, it'll show. Hey? I've got these changes that are going to be committed and committing code is basically pushing new code into the repository. And then it basically sets a new snapshot of hey? This is what the code was at this exact moment in time. Here's who submitted it. Here's the version number, or the sha.
the hash of that code like you can always revert back to it.
So, we're going to get commit.
And this means actually, these changes I care about. I want to save. So my new changes.
So if you were to do this on the course repo you might
be, you know, have the habit of okay. Now I want to push my code. So this code is changed locally on your machine, like, if you were to open up this file on your hard drive. It has this this gobbledygook.
And if you were coding with a team
you might want to have that code available to somebody else to start using. So you might do what's called a push. So that's when you push your your code to the, to the remote, to the remote repository for sharing
if you tried that with this
shared repo you would get denied right. If I type get push. It would accept it. I don't want to, because I don't want that code. So you might get into a situation where you've committed code to the repo.
because, for whatever, for whatever reason, or you know you might have just made changes unbeknownst to you. That happens with Jupyter notebooks. We'll talk about that later.
But you always want to get the latest and greatest from from me.
Well,
When that happens and you have code committed, you have to resolve the merge requests, or any collisions, and you know what in in this particular case, like you don't any of your code that you've made any changes that you've made to the repo you should. You should really just want to wipe out because they are not done purposefully. You want my code to be pristine.
So in this particular case, you'll do something that's like a git reset that will basically wipe out any changes that you've made, and then sync it up directly to what's the latest and greatest in the in the
in the repo that's on Github. So to do that you have to make sure you have all of the changes from the previous. Get sorry you get all the changes from from origin. Make sure you have the latest and greatest from from my environment. So you do a get fetch origin, and that will give oops. Get fetch origin.
That will give you all the latest code from from origin, and then we do a get reset!
Oh, reset hard to origin and main oops.
Think I've got that command right?
Yep.
So now it has basically gotten rid of those changes. And now, if we do a git status.
we're clean. Okay?
So if you ever find yourself out of out of whack with the
with the online repo, just remember these 2 commands, write them down, go to this recording.
get fetch origin to make sure you have the latest and greatest, and then locally to you, and then do a git reset hard. It's going to wipe out anything that you've done and make it exactly what the main branch is in the git repo.
Okay.
very good.
All right. Let's talk through Jupiter.
So it's nice to be able to look at someone else's code and kind of step through. You know. You can use a debugger and step through the code, and that's all. That's all fine and dandy. But what I find it more useful in teaching is to give somebody kind of this like interspersed notes first, st and then some code, and then some more notes, and then some more code, and explaining how this code works. And Yada Yada Yada, right?
And Jupyter notebooks is a great great tool for for doing that. So I'm going to introduce you to that a little bit
and you'll you'll get used to it throughout the throughout the course, because I'll use it
like for 5 at least 5 different lectures, maybe more this quarter.
Okay?
So in order to start a Jupyter notebook, there's a few different ways.
once you've once you've installed Jupyter. So if you've done the requirements and install Jupyter. This should work. If not, you can just do a pip, install Jupyter.
and it should automatically install the necessary libraries to make this work. Okay.
if you're using Picharm pro, and you open up any one of the workbooks, you should have a little play, icon
here, and what this will do is it will start a Jupyter notebook server.
which is basically a web server that runs on your local host. And then you interact with these things in a web browser.
So you can just open up the file here and then click, run, and it should
give you. Let's see. Why is it not
alrighty? They've changed the behavior slightly since last time I used this previous version.
you want to be able to get to the Jupyter notebook server. And so the easiest way to do that, assuming how this isn't functioning, the way I would expect it to is to just come in here to your command line and just type Jupyter
hyphen notebook.
And what that will do is kick off the Jupyter notebook code and launch the Jupyter notebook.
environment in in your web, Browser, I'm
unsure. Why, it's not giving me
the actual results here. This worked perfectly yesterday.
Let's try.
Sorry for having to fix this in production. So let's to kill this.
we'll bring up a new one.
Okay.
Don't know why. It's probably because I clicked play. Something was colliding anyway.
So once you have Jupyter notebook launched from your local machine?
then we can start interacting with it here in in a web web browser.
So we're gonna click on Jupiter notebooks. Double click on it. And we're gonna open up. Hello, world! This is just a notebook that's going to show you kind of the basics of of
how Jupyter notebooks work with work with Python and Markdown.
So a a notebook consists of cells, one or more cells, and those cells have either raw text in them which I never actually ever use.
It has code of whatever language. In this particular case we're using python.
But this works for other languages as well.
or it has a markup language called Markdown, which is a way of formatting formatting text. You might be familiar with this, you might not. I'll go through kind of some high, level Markdown syntax, so you can become familiar with this as a tool super popular in
in get, because your readmes are usually marked down. So it's good to get familiar with this kind of notation.
and Jupiter uses it as well. So I'll spend a few minutes talking through it.
Okay, so this is a sample notebook, and you'll see that they have little play buttons to execute the code in each of the each of the cells. So
we see that it's nice and pretty right. It's got a nice big title. We got some bold we've got a hyperlink here. If I double click on this cell you'll see that it's nothing more than actual. Just just raw Ascii. Right? It's just. It's just text.
the single pound sign is the largest heading indicator.
You've got
asterisk asteris to indicate that something is bold underscores to indicate that something should be emphasized or italics
you've got a square brackets, followed by parentheses to indicate that there's a hyperlink.
and so you can make this whatever format you want, and then, when the cell is executed, you can execute, either by pressing the play button, or most of you will get used to the keyboard shortcut of shift enter.
It might be different on a PC. But it's it shows in the little tool tip here.
So this particular notebook, I've just given you some some basic examples, right? Like
big pound sign for header, 1, 2 pound signs for
for level 2, and it gets smaller and smaller and smaller.
you can get to a level 6, and it makes the header really, really teeny. Tiny
can't go any further than 6 at least. On whatever is rendering my markdown.
You have other options like hyphens or underscores to create. Page breaks
bullets, and lists are also easy to to format. I'll show you what those look like.
there's like. It's just an asterisk space item, asterisk space item. If you want to indent. You use 2 2 spaces. You can use bullets or dashes.
You can mix them if you if you want, and it changes the behavior slightly
if you want a numbered list.
you can just do 1, 1, 1, 1 that indicates that it's going to be numbered. You can choose to do 1, 2, 3, 4, if you want, but that means that if you do reorder things, you have to change all of those numbers. So I just prefer to just do ones, and then let the rendering take care of the numbering for me
and it's also good for making checklists. If you create a
It's like square bracket, close bracket. You can show that things are checked. There's a lot of different formatting you can do. This is just kind of scratching the surface. If you find yourself being really interested in creating these kind of notebooks, you can. You can find cheat sheets online as well.
Another fun thing. I'm a math guy. My bachelor's came with a math minor. I believe math solves most problems. But I'll keep the math a little bit light in this particular course, but it is something I'm a big fan of
I. So Markdown is cool to me because it also offers plugins for a another type of markup language called Latex
Latex, was built on Tech, invented by Donald Dalek. Nuth just a
way of of expressing documents right and similar to Markdown, but far more complex.
But Latex has a mathematical markup language that that allows you to do really fancy things. So if you wrap
your tech your latex with
your markdown if you if you
group your markdown with dollar signs that tells it to do a latex math formula, so you can do, do fancy things and have it render pretty math
like the quadratic equation, or this integral so
which can be useful when you know, trying to solve. Some
make make an elegant view of of a of a math problem that you're solving with with code.
So that's the Markdown side of things like, how do you make it? How to make the font pretty? But that's just one aspect, right. The real, true power. Here is the ability to execute code. So we're going to have a cell here that we've called a code cell.
And we're just going to type python directly into it. So setting X to 0 to demonstrate some state management. So let's talk about that. If I execute X equals 0.
So I'm just hitting shift enter to to run the run. The code.
this next code, this next line of code, is waiting to be executed if I run it now.
what do you think will happen when it prints.
What do you think this is going to say after I run this?
It's kind of giving it away a little bit right.
but I predict that it's going to say you have executed this block one time. Let's try it.
There it goes it! It returned that text.
Now, what if I do it again?
Is it going to say you've executed this block one time?
No, it's going to say
2 times and 3 times and 4 times. So each time you run this code, it's just like you're executing it within the python interactive interpreter. Right? It's maintaining the state between runs. Even if I run this this Markdown code, it's still going to remember. 4, 5, 6.
But if I come here and I run this line of code again and shift enter.
Is this going to say I've executed this block 7 times, or 6, or is it going to go back to one?
One could probably think either could be possible. But the way that it works is
it goes back to one because it's all sharing the same state.
The state between these cells is shared amongst all this, all of the cells. So I've set it to 0. And then when I run this again, X is back to 0.
Okay? So again, state is global for anything that's executed within within the notebook
in the order in which it was executed in okay, okay.
when dealing with python. You often have to import libraries.
It's just common. It's not just with
not just with python, but code in general. Usually you're importing other libraries, and to do that in Jupyter notebook, all you need to do
is
I don't know why it keeps hiding is run import statements, and once you've run those import statements, because it's a shared state, you now have access to those libraries anywhere in your notebook, even if I were to scroll up like if I did something weird right? And I did like requests. Get Hello!
some URL, right? If I if I ran this code
before running this code, I would get an error right?
So. But if I run this, and then I run this, then I do get a
execution of this particular requests. Not sure.
Oh, it's an invalid, URL that's expected. So
I do this example to show. Hey? You can execute things in any order. But typically you're going to want to write them top to bottom
for the most, for the most part.
Okay.
So other other behavior.
Sean Warlick
Sean Warlick
01:28:52
1, 1 little quirk I like to point out about imports and Jupyter notebooks. If you're working with a library that you're developing.
You have to like. Re, you have to restart the kernel to get it to import your updates. There's there's some cell magic
that can do that, but I always have to look it up, and I don't remember what it is, so.
Kevin Anderson
Kevin Anderson
01:29:11
Oh, yeah, that's
Yeah, it's a good point. I actually have a
when I when I get to my next notebook. I have a little bit of a workaround for for demonstrating functions of a class that I'm like
building building up from scratch to kind of get around that that particular issue.
Not good for programming practices, right? But good for demonstration, anyway.
Thanks, Sean.
I think that was Sean. Right.
Sean Warlick
Sean Warlick
01:29:43
Yeah.
Kevin Anderson
Kevin Anderson
01:29:44
Okay, good. Good. I'll I'll get to get to know voices here over the, you know. Probably by week 10.
I'll have it down.
Okay.
So what we're gonna do is just show some basic basic basic interaction with
with various objects. So I'm going to write a simple get request. So I know this isn't a course on web development.
but I'm or writing web services, or anything like that. I know this is a kind of out of scope of what you guys know, so don't necessarily get too wrapped up that you might not understand exactly what this code is doing. I'll walk you through it.
Basically, I have this Internet address that
is going to respond back with some data.
Right? This is a a page, page, one of
of of some fake user data, right? It's just used for testing.
If the response is good, then print the
print the response in a nice, pretty way. That's basically taking this kind of
kind of raw interpretation, right? Saves it as a Json and then prints it in a nice, pretty, indented state. If it fails
like the web, the service is down, or I've typoed the the URL. Then just say the connection failed and return the status code, and the reason. So let's try a forced failure.
The connection failed with a 4 0 4, which means the the URL. The the resource was not found.
So I'm going to go here and make this good again. And now I'm going to return the code.
So I'm going to return the response in a nice kind of pretty version of Json, and notice how the Jupyter notebook has been nice and kind to me, and has not
made me scroll all the way down. It made a nice little window that I can scroll up and down in if I want to expand. There are options to to do that depending on your on your version. You can expand and contract this way. There are ways to expand it hovering over the left side.
But again, those change with version. So
the idea here is that it will render the results in a way that is somewhat somewhat pleasing.
so far, anything we've printed or anything we've displayed on the screen. We've done a print statement right to return a string that gets displayed. But you don't always have to do that I like working with pandas. Like I said before, data guy, use pandas a lot
and re creating.
Or you can, you can print things out to the screen in a more pretty way. And I'll kind of demonstrate that here in a moment.
Okay, so here I have a pandas import that's going to take this financial data that I found online somewhere. And I'm gonna create a data frame.
I think you guys might still study data frames a little bit in 501 at least. I originally had a lecture on them.
So hopefully you you don't think I'm talking complete nonsense when I talk about data frames, the brief explanation, right? It's just a rectangular data set of of
of various types, right text numbers, etc.
So we're going to create this rectangular piece of data from this URL.
And then we're going to show how big it is which is just using the shape, the shape attribute, which is the tuple of the number of rows and number of columns. And then we're going to print out what it looks like. So
we're going to execute this code. It's going to take
2 seconds to download the data. And here we have
a thousand, 30 or 1,800 rows and 14 columns.
now, I want to make sure I understand what that code looks or what that data look like. So I'm going to do this head method which just returns all columns and
the 1st N records. So if I wanted the 1st 10 records I could do head 10, it'll give me 10
by default. I think it's only 5
and you can see it gives me a pretty table that has some
some formatting right banded rows and a little bit of a highlight. There's no interactivity like you can't like download this as data or anything like that, but it's at least a little bit prettier.
Then, if you were to try to actually print this data frame, it's going to look like, well, it's going to look like garbage. Maybe this is what you want, but most of the time you want a more pretty, pretty view. So this is just to demonstrate that.
The demonstration!
Sorry, just to show that, hey? You don't always have to print something.
Jupyter notebook will try to intuit a with common objects. This is the way it wants to be rendered.
Okay.
And lastly, you can do plots which is really handy, especially if you're trying to do analysis. I don't know if anybody does data, analysis or
impact analysis or anything like that during during your day job. But I recommend using Jupyter as the backbone for for doing those analyses because you can write the code
on the data.
do a plot, do a transform? Do a plot do a transform each each step of the way, writing explanations of why and your interpretation of the of the plots, etc.
And then, when you're done, you can export the notebook to someone else, especially this works super well in the scientific community. I know not. Everybody on this call are like researchers, but you have a Jupyter notebook that shows the data like, now, anybody can recreate your your results. They don't have to trust that you've made the plot right? Right? They've got. They have the source code and can can recreate your your work. So
recommend that for doing analysis.
I also have. I used to have a data engineer that worked for me a while back
she was amazing. She used Jupiter for 2 2 primary purposes. One was to
build data pipelines, or at least prototype data pipelines. So she would know. Here's my source. Here's my transform. Here's my target. Here's my second target. Here's my next transform and go through step by step
to get to this new shape the new shape of the data, and could walk through with a customer. Hey, this is the source. This is what it looks like. This is the end, step by step by step, and now she has a pipeline that she can then put into a production environment.
Also used it for troubleshooting. So hey, I am working on some data, and my
system is not up and up and running. Your database goes down or whatnot. You can use Jupyter notebook to make it, to write code and execute commands, and then you kind of get a running tally of all of the things you did to try and solve the problem, and when you're done you can export it as HTML. Save it in your in your incident log to say, Hey, this is how we fixed it last time you can recreate it again. So super powerful tool
lots and lots of of reasons for it.
Okay.
so so far I've talked to you about the tools and general content about the class. Let's actually start talking about some some data structures and algorithms. Shall we?
Okay, let me close this out
notes. We'll close this all right.
Trees.
She'd know about binary search trees by now. Right? This is just going to be somewhat of a
of a review, because it's going to be important for us to understand binary search trees for our next lecture, which will be on self balancing binary search trees and the algorithms that are employed to keep things balanced.
But before then, let's talk through binary search trees. So just as a reminder.
A bst is a special type of tree where the it's a it's a
a tree that each parent only has 2 nodes at most, 2 nodes, a left and a right, oh.
2 children, a left and a right, and those nodes hold values.
and those values must be sortable or comparable. Right. You have to be able to say that one is greater than another.
You wouldn't have like red is greater than green unless you were doing it in alphabetical order, right? You need to have something that's comparable.
and all of the nodes in a tree
or in the in that node's left subtree are less than the value of the node that's at the root of that subtree.
So everything to the left is smaller, and everything to the right is bigger.
And so, as a reminder that left and right rule is just arbitrary implementation detail, you could, you could make it
the other way around, right, where everything on the left is bigger than everything on the right.
It's it just has to be consistently implemented. The actual left to right is is irrelevant. It's just a matter of of principle or
So
just want to make sure that that's clear. The left or right is not not that big of a deal.
Okay? Because we have this kind of property of the of the tree structure.
as long as that tree remains balanced
we get this big O of log n, search capacity or search time complexity, which is incredibly incredibly fast. Log n algorithms are, are you should aspire to get as things as close to log, n, as you can.
Because if you imagine, if you have 4 4 billion
elements in a list, 4 billion is a lot, by the way of things to search through with log of N, you can get through it in 32 steps.
right? You have to look at most 32 times which is super fast when we're looking at things that are in the trillions, you know. Think about searching the entire Internet right? If things are stored in a B tree. You can search through trillions with only like 50 hops. Right? So login is super super efficient. So I'm a big fan of binary search
for this particular data structure, you've got some common
common methods or functions. These are named, either put or insert, which is when you're adding to the structure. Get or search is when you're trying to find data in the structure. And then, lastly, remove and delete, which are when you're taking something out of the structure.
This again, I'll review. This is what might actually be somewhat new, depending on your last course.
There's different representations in code or in in programming of of a tree.
Binary search trees. Yes, but also just generically.
you can implement a tree structure in 2 different ways
at least 2 different ways. One is dynamic, which is what you've learned before, which is your node based representation right where you've got a node, and then it has pointers in memory to its left and right children, and then those are nodes themselves, and have pointers to the left and right, and so it kind of visually looks a little bit more like this where you've got a node and dot left and dot right? Children. Okay.
an alternative is to represent these data. These data structures in a in an array.
Typically, this is used when the data structure, when the tree is going to be very dense, right heaps are a good example of being implemented as an array, because they're always going to grow from kind of left to right. They don't have really long branches. They get. They stay really well balanced, and we'll talk about why, that is a problem.
Why? Why? Imbalance is a problem for array. Based trees.
But we will. But
well, so we'll we'll talk through.
Okay?
So we look at
this representation of this is the root node right? And then this is the root dot left. This is root dot right.
and then this is root dot left dot left.
So there's that structure.
We represent this in an array by using kind of an indexed based accounting method. So the root is 0,
and the next row starts 1, 2,
and then the next row is index 3, 4,
and then this one doesn't exist right. There's no dot left underneath this 11. So in an array that's contiguous memory, right? So you still have an index 5. You just put null. You just don't store anything in that.
And then finally 6.
And then, if you were to add another row right, you'd have index 7, 8, 9, 1011, 1213, 14.
So each time we add another another level to the tree.
we add a bit more to our array to represent the next N. Number of of values, and it always doubles each time. So the 1st row you add
one. The next row is 2. The next row is 4, 6. I'm sorry.
4, 8, 1632. You get the get the picture. So the every layer layer. You're adding that many more
that many more lines.
Okay, so we're gonna talk through
just a refresher on the algorithms for adding and removing or sorry adding and searching. And then we're going to show what that looks like in a array based structure.
Okay.
so a couple things to note here, I'm creating a class called Binary search tree dynamic, and it has a subclass of tree node.
Right? This tree node belongs to this class. And it has the basic data of
the data that's being stored
the parent of of the node. So if we want to traverse upwards, we have that, and we have a dot left and a dot right super simple.
and we have a of a constructor that, just
to be honest, I actually don't remember why I put Max children equals 2. So we're going to ignore that and it would just initiate with a self. Dot root equals none. So we initiated an empty tree.
Yes, this is super simple. You learned last quarter that of course, we would do a you know, self, Doc. Size
right and set that to 0. But I'm just trying to keep the code simple for explenative
purposes. So we'll leave it out.
But again, toy example, right? Super super basic.
So we're going to create this new blank, binary search tree. So now I have a variable called Vst, that is, of this structure, right? It's got tree node as a as a subclass. It's instantiated with a dot root like we're we're good.
And what you would typically see right?
What you've done before in object oriented programming is you would want to have a bst dot insert X, right?
We'll say, insert tent where this function is a property of this
class. So you would write it like this? Right? You do def
insert, and then you would pass the self, and then the value right
so self, meaning the instantiated version of the object.
So this is how you would write it in, you know, object-oriented based programming.
Well, because I'm dealing with Jupyter notebook, and I want to execute just blocks of code on its own.
And I've created this class, and I don't want to have to reinstantiate the class every time I modify it. I'm going to do a slightly different technique that is pretty easy to to grasp once you've seen it. But it might be confusing without any explanation. So allow me to explain. Just really, really, briefly.
So, I'm creating this insert statement, this insert function. That's just kind of standalone. It's part of my main main program. I just have defined this helper function called insert
instead of self.
I'm actually accepting as input a binary search, siri. I'm
I'm passing it a
an instantiated binary search tree. So I know the structure of it because it's a bst. It's 1 of these guys, but it's not operating on itself.
So this would be the exact same thing as me doing this, calling itself.
Obviously it would indent these, and then I could do bst dot insert.
But instead of doing that, I'm just
taking the code and passing bst into it.
So the function becomes more of a insert.
and then the code, then the the object that I'm inserting. And then the data I'm inserting into it.
So just a slightly different ordering of things. But it allows me to build the
the functions up of a binary search tree in separate segments without having to understand. Run the class all at once.
Okay,
as as Shawn mentioned like, there's ways around doing this with forcing the the restart of the module and a bunch of stuff which is a little bit more overhead.
I choose this because A, it's easier. And B, there's actually a lesson here in object-oriented programming
in languages that don't explicitly call out objects.
C.
If you ever have the the pleasure of of coding in C, you'll you'll learn that it doesn't do as much fun stuff for you like garbage collection and memory management and all those fun things.
it doesn't have objects by nature. It has this concept called a struct, which is basically the data associated to a piece of of memory. But it doesn't have any code, no methods. So you do the same kind of thing when you do when you do object-oriented programming in C, even though C isn't a quote object-oriented language, you still write code that handles structs
as an As input and then that becomes object oriented because you're still building code on a particular struct
so good to learn that this is a way of doing object-oriented programming, just not in the native sense.
Okay, good on time.
All right.
So
just as a reminder on how insert works. Right? You look to see if it's the very 1st object in in the tree.
either by saying, is size 0, or is the root none. If the root is none, then set the root to be the this new node and then return.
Otherwise you need to traverse left and right right.
He checked the value of the of the current node.
Right? You start at the root, and you say.
is my value less than this one?
If it. If it is less, then look to see if there's an open spot to the left, so is my is my
current node childless on the left hand side. If it is, then
we know that that is where the new data needs to go. So we
you update the brand newest nodes parent to the node that you're currently at, right. So we can traverse back up if we need to, and then the node that we're at, we set its left child to be that new, that new node that we created and then return.
Same happens if it's the right side by the way, and if we do
find that there is a node where it needs to go. So
we, we've inserted the node. Say, we're inserting 3, and we find that 3 is less than 10. Okay? Is the left? Does the left child have a child. Okay, yes, it does. So we just continue to traverse down to the left
and checking each time, do we go left and right? Okay?
So again. Review from last last quarter.
Let's test to make sure that this thing works right?
So we're going to insert nodes in the following order, 1520, 2515.
So let's think about how that's going to end up working right? So the 1st
10 gets put in at the very, very top. So the root is number 10.
And then if we insert 5, we're going to say is 5 bigger or less than 10, it's less than so it's going to go to the left, child. Oh, there's an open spot, so we're going to insert 5 there.
Then we're going to insert 20.
Same thing is 20, bigger or less than 10. It's bigger. Is there a child to the right? Nope, so we're going to insert 20 there
next is 25. We're going to look, start at the root again
is 25, bigger or less than 10. It's bigger.
Go right.
Is it bigger or less than 20? Yes, go right.
Is there an open spot? Yes, insert the data.
and then do the same thing for 15 where you go right and then left.
and then to validate the data I'm going to introduce a little concept. That I refer to as dot walking
dot walking, and that just indicate it's a way of representing that you have this object dot value, dot value dot value. And as they're linking to different places in memory, you can just separate them by dots, and then you end up getting all the way to the data that you want.
So in this particular case, we would say that bst, which is the
which is the whole object itself. Right
has an object called root oops, oops.
and then root dot data is 10, right? Because the object that's in memory
at the location where root is has a
pointer to an object, to another.
a memory location. That is data.
So if we if we say Bst dot root dot data, we get the value at root.
If we say Bst, dot root, dot left dot data that's going to be the data from the left node, but we can continue to to build on this and say, Bst, dot root dot right dot right dot data
is the root. Then the right node, then the right node. And then the data of the of the right node. Right? So when you're doing some validation, and you have a structure that you like know? You want it to be very precise. All the way down. You can do these kinds of of dot walking type tests.
And why, oh, did not execute the code to establish the
the function. So that's why that failed.
Okay, so we see, yep, we expected 1520, 2515. And
here we here, we got it.
In these Jupyter notebooks.
You're gonna see some green text sometimes with student example.
These are gonna be places for you to make edits and remember what I said, like.
you're gonna make edits to these that you may not like want to commit to the repo like you're gonna make some changes to this and get you're gonna get out of line with the
with the git repo. So unless you've made a copy of it elsewhere you're gonna get that collision issue. So solve the problem. And then.
you know, when you're ready to get the latest, then get fetch and then Re,
get reset, and you'll you'll lose the stuff. But you know these are just there for for you to practice specific
specific little problems.
So in these they won't execute typically on their own. Sometimes I have like unit tests that say, Hey, if you've done it right, then this line will will work correctly. But in this particular case, like it's on you to
choose some number of inputs right? And then practice
understanding. If it's dot left dot right dot left dot right? Where does the data live? Again
make predictions on what you think it's going to be, and then have it output the results to make sure you're you're getting it right.
One last thing on the student examples is, I will have
boilerplate for you. That is usually called out with just pound signs. That of the pound sign is where what code you need to change
right? So you need to change the the pound signs to like dot left, or something like that.
So again it won't compile, or it won't run, it'll air out saying, Why do you have all these pound signs, but because that's what you should be doing to change. So this is for your practice on your own time. No grades on these just your own practice. Okay.
okay, searching.
Searching is about the same
as insert right? We have to look to see if we found the value. And if if the value that we're at is not what we're looking for, check to see if I need to go left or right, so we start our traversal by setting our current node to the root.
and then until we until we fall out.
If current equals none, which means we've found a child, or we've traversed the end of wherever we're at. Either that be an empty tree, or, you know, 2 or 3 children down.
If that's the case, then we return none, because we don't want to, because we haven't found it.
If the data does match, then return the data, otherwise
do a comparison. And if your data is
if the data that's in the record that I'm at is bigger than the data I'm searching for, then tell the searcher to go to the left, otherwise tell it to go to the right, and then it just keeps on looping, looping, looping. Yeah.
So again, also review.
And
here's a little test I wrote. So I'm going to insert 1525, 15. And now I'm going to do a query for (101) 515-2021.
I'm expecting it to respond with the number 10, the number 15, the number 15, the number 20.
But when I search for 21 I'm expecting none.
Alright. So I just wrote this little test that says for every query and expectation. So it's gonna iterate through these things at the same time, one by one.
Search for it. And did I get the results I wanted? Then say, I passed, okay,
So the student example is for you to to practice with creating a new binary search tree.
inserting some data into it, making a loop to do that insert of the data you've you've classified here.
and then do a search. Make sure that you've got the the things validated that your predictions are going correctly.
Okay, removal in the dynamic sense, or in the dynamic structure. It's the more difficult
more difficult algorithm. In that it has 3 different, 3 different special cases.
One is if you're removing a node that has no children, that's 1's easy. You just delete the node right? You find out what its parent is, and sever the the node from
from the tree and let garbage collection do the rest.
If there is one child, either the
either dot, left or dot right, it doesn't matter.
All you need to do is delete the node that you have intended to delete, and then make whichever one of its children, it only has one by definition, right? Whichever children is now in the position of the tree that that
child was in, or where where the parent was in when it got deleted.
This is easy in a dynamic mode, right? Because even if that
say it's the left child, even if that left child itself has left and right, children, and a whole subtree underneath that.
just by moving the pointers, you've moved all that data all up at once without having to move stuff. Move stuff around right? So nice and easy to to move that structure up.
If there are 2 children that's a little bit less intuitive, but still somewhat easy to explain. Right? Say, you're removing a node. Let's go find a tree here. Let's say we're removing 20. Well, in order to make sure that we have kind of not have to restructure a whole bunch of stuff. Basically, we want in the subtree under 20. We want to find
the very next.
Largest
integer or value in that subtree. Okay? Because if it's the very next one it's going to remain. It's going to maintain the shape because anything that is
smaller, then it will still be to the left of it, and anything bigger is going to be to the right. So it's still, it's still going to maintain the proper proper shape if we have. The very next number moved up into it. So.
in order to find the the the next smallest number
we need to traverse 1st to the left, because that's gonna give us everything that's smaller than it, right?
And then we need the biggest biggest value from that list.
and in order to get the biggest value from a subtree, you just keep traversing to the right. So what we do with this algorithm? Is we?
If possible, we do one step to the to the left.
Sorry we go one step to the one step to the right, and then all the way down to the left, and that will give us the the number that we're seeking.
Oh, gosh! I'm so sorry you go one step to the left to get the smaller number, and then all bunch of steps to the right to get the biggest, and then you swap the values and remove that child.
Okay?
The code for doing that.
This is a little little bit more lengthy, obviously, than what we shown above.
you should have this already in your head. I don't have any animations for it for this slide, but if you want animations that show how this is working. We'll talk through it.
But this is, you know, sample working code that does the does the delete from a dynamic sense.
Okay.
I've got some test code for removal. If you if you want to to try it out. It shows. Hey? You're removing
10. We want 15 to be in its in its place. So this is proving that that ends up working.
So that's the dynamic version.
Let's talk about the array
or sequential based representation. So we don't have these dot lefts, and we don't have these dot rights right? We have to know where in that array each of these things live. And it turns out to be
these trees. These structures have a nice mathematical property that allows us to traverse up and down, using using some basic basic arithmetic to figure out the parent and child nodes
ids of their their location in the array.
Excuse me. So here's what a tree would look like dynamically right. And here are the indexes of those values. So 0 1, 2,
3, 4, 5, 6, 7, 8, 9, 1011, 1213, 14. Right?
Those are the the values of the indexes, and
take my word for it, or you can do the do the math yourself. If we want to find the left node of of.
If we want to find the index of a left child
of a particular value, all we need to do is multiply that index by 2 to give us the next row, and then offset it by one.
To get the left child or 2 to get the right child.
Okay, how does this work?
And let's just let's just do some experiments
0 times 2 is 0 plus one is one.
So that gives me my left child.
plus 2 is my right, child.
Say, we're at Number 5, and we want to get to the left child of 5. Well, 5 times 2 is 10,
plus one gives me 11 plus 2 gives me 12.
So this happens anywhere in the tree
index times 2 plus one for the left child, plus 2 for the right child.
If we want to get to the parent, it's it's basically the reverse. But we have to know
which do we subtract? Do we subtract 2, or do we subtract one?
Well, here's another fun. Property.
If it's the right child, it's always going to be even right.
Root is the special case. But if I'm the right child of 2, I'm 6, if I'm the right child of 5, I'm 12. If I'm the right child of 4, I'm 10. So the right child is always an even
even value. And you can intuit this right. The 1st value is even because it's 0, and then you always have 2 children.
So 1, 2. So it goes odd even. And then the next row is going to be
for every parent in the previous row. You're going to have 2 children. So it's going to be odd, even odd, even odd, even odd, even right? So it's kind of easy to intuit that always the right child is going to be. Even
so we use that to our advantage.
And we say we're going to offset by one. If it is odd.
So this is the modulo operator. Right? Index. MoD. 2 equals one. That means it's odd. So only offset one otherwise offset by 2,
and then we just do the reverse of what we did before. So we take the
index, and instead of multiplying by 2 and adding one, we subtract one or 2 depending on.
If it's odd or even, and then divide it by 2 instead of multiplying it by 2. And that will give us a parent.
Okay?
So now, when we want to go dot left or dot right, we can't just use the memory pointer. We have to use an index of the array. So we have these little helper functions
that I thought I had updated. Sorry
the the functions are get index of the left, which is, you know, 2 times index, plus one get index of the right
2 times the index plus 2, or get the index of the parent.
Now.
there's 1 thing I haven't covered yet, which is, how do you? Because, you remember, arrays? You have to allocate the memory because it's contiguous like you need it all at the same time. So in a tree, in a representation like this, you have to make sure that you're growing the tree to be able to store all of the data that you need. So what I have done in this particular example is, I've set the initial tree size to 64. So it's going to have 64 total nodes that it can, that it can store.
And when it gets to be too big.
so say we've inserted 64 values, or rather have in the case of an imbalanced tree. We've gone all the way to the right and have
grow outgrown our tree size. We have to do an expansion, and what I do here is I just copy all of the data from the previous array into a new array, but then add a whole bunch of nuns at the end of the new array, and basically double the size of the array every single time.
So the heuristic of doubling in size limits the
It's the amount of overhead that you have to do
because you don't want to have to do this every single time you insert right, you want to have it to be like
logarithmically executed, as the
basically as you add more and more and more records, the less and less often you want to have to do it. So doubling, it is a good way of doing that.
Okay, so insertion
exact same as before, except instead of using dot left and dot right, we have to use indexes. So we don't have our dot root.
Our root is data 0, right? It's the zeroth element of the array.
If it's none. That means it's empty. So therefore.
set the data and move on.
Otherwise
you're going to be instead of iterating through pointers like using the current current pointer. We're going to be using an index, which is the current pointer. Right? So we're going to start at root index equals 0.
And then we're going to check to see if it if it's none.
Which means, you know, if it, if it is none. That means we found an empty an empty
location in the tree, and that's where we should be pushing the data.
We then instead of
So we do the we. We have shown that it's not none. So we have something to to evaluate against. Right. So now we're going to say at the Index, the data at the index that I have, that I'm searching. Is it bigger or less than the data that I'm inserting.
If it if it is, then if it's less than then, we need to traverse left right.
So previously, how we would do bst dot write
we or Dot left. We just use this function
to get the index of the left
of the the left node. Set that to the index, and now, when we move to the next loop. We're now looking at a different object in the in the tree.
Okay?
This is also the special case, right? When we need to expand. So
if we ever find the case where the index is beyond where it should be. So remember the the child is going to be 2 times the index of the parent, plus one or 2. Right? Well, let's just say my array is only 14 sized. Well, if the parent is
to the right of this. It's going to be number 28, plus 2. So it's gonna be 30 right?
That's outside of the range of the array, and we need to expand it. So
I just created a the, you know, the expand function here that's going to allow us to copy all the data into a new, bigger, bigger array.
And
okay, I've got
something going live here that I gotta fix directly after class so I'll push new code.
I'm not quite sure why, that's not running, but I don't have time to fix it in lecture today.
I want to talk about one last thing of the problems within a sequential array.
This happens to the same problem with a with a binary search tree that isn't balanced is that you say you just insert things 0 1, 2, 3, 4, 5, 6, 7, 8, 9, 10.
Well, in a binary search tree you lose that logarithmic time complexity if it's not balanced, because now you have to search dot right dot right dot right dot right dot right right. So all the way to the to the last number.
It's even worse in in array, based, because every time you're growing to the right, you are needing to extend the index of your array right the size of your array. So even after inserting
20 numbers, your array is now 4 million long, and if you're using a you know classic array that is, that is like contiguous memory. You've now
locked up that much memory, that much memory to store 20 values. So it needs to be balanced is what I'm trying to trying to say. If you have a tree structure that is very, very imbalanced, you're going to have even in your
in your array version. It's going to be using way too much memory. And in your binary search tree, in the dynamic sense, it's now you also have loss of logarithmic structure or logarithmic time complexity for your for your searches.
Okay, searching is the same. Instead of dot left you're using. Get index.
Removal is even far more complicated in in the array, in the sequential versions. Because.
you know what I said. You can just pluck a node out and then raise it up. Well, you can't do that in an array. You have to like. Shift all of the values over one.
So there's a bit of troversial to clean that up which I'm not going to cover in this in this demo, but just know that the dynamic version, or sorry the sequential version does have a lot more overhead when having to restructure, which is why the sequential version is usually used in something like a heap where you're not having to restructure over and over again. You're really typically just bubbling specific cells up and down.
Okay.
alright, we're right at time. I didn't get you out early like I promised. Thank you all. I will switch over to office hours to address any questions you guys might have. Otherwise read the
read the assigned reading on balanced search trees, and next week we will go through learning how to create some new structures called 2, 3 trees and red black trees.
So thank you. All appreciate the time.
Talk soon.
