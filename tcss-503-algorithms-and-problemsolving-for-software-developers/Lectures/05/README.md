So welcome to Week 5. After the lecture today
we will be precisely halfway through the course.
and you will be precisely halfway through your certificate.
And so congratulations for those that have made it this far hope. You guys are
enjoying the the courses and and really leveling up your your programming. And that's the goal.
So it's also kind of fitting that we mark this midway
with, divide and conquer, because well, as you will, as we'll learn, divide, and conquer is about splitting your problems into smaller problems, typically in in by a factor of 2.
Okay.
so today, I'm going to review assignment one. And I know I extended the the due date to
to today at midnight. So
for those of you that haven't haven't done it yet. You're gonna kind of get the full full solution. But I feel it's better for me to
show you all the the solution today than to to wait for another another week. So
a little bit out of out of order because of the the extension on the assignment. But.
I don't. I don't feel there's an issue there.
We're going to be covering the divide and conquer as an algorithm style, and we'll introduce and
an analytical method for determining the big O of divide and conquer. And we'll be applying that method to a couple of algorithms, Karatsuba's fast multiplication, which is a little bit math heavy. So I'll I'll go slow on it, and then we'll cover matrix multiplication.
which is also somewhat math, heavy, but a little bit less less so. And then we'll follow up with another practical algorithm that's used a lot which is the closest pair of points, the ability to be given an arbitrary set of
of points on a graph or on a chart. Rather.
you know, a Cartesian plane, and then find the 2 points given all those points which 2 are the closest together.
So quite a bit to to cover today.
Last lecture, we covered greedy algorithms which, as you recall, are the simple simplest of the algorithm types where you're just taking the most or least, or some, you know, some simple rule. At each step we talked about the difference between locally and globally optimal results.
And then we covered change, making both in the greedy sense and introducing dynamic programming. Just a little bit. We covered minimum spanning trees and and Dijkstra's shortest path.
Any questions or go backs from last lecture.
All right, okay, let's talk about assignment number number one
like I had mentioned before, and why we did the the extension. There was a little bit of of of struggle across the across the board.
So clearly I had not emphasized a few, a few key points.
One of the biggest points that was a was a concern was,
the implementation of a classical red, black tree. So if you were doing your own research and looked up red, black, you probably found classical, which is slightly different than left leaning so
to the left leaning has very specific properties, and that you that you needed to to implement so
and make sure to make that even more more clear for the for the next time.
So the the ultimate solution for the student was to take the
recursive version of the algorithm and translate it into an iterative approach. So you were kind of given the the logic for overall how to balance the tree you just needed to to convert it into
into a way that you don't have to use recursion and
to do that. There's kind of 2 main, 2 main changes. One is in your
insertion and rotation. You have to make sure you're covering parents.
There's alternatives right? You can
use a stack or something to deal with. Deal with your path. That's an that's an alternative of of solution. But using parents is a little bit more
more straightforward for where you're at.
So let's talk about the the recursive method that was that was provided to you. Right?
fairly fairly simple. Only a few lines of of code where you are taking the node
setting node right to its parent, and the kind of rotating it, notate rotating it around.
To do this and manage the the parents effectively. You have a few few more pieces of logic, a couple of like special cases when dealing with the root, when it doesn't have a parent. So that's another common mistake is
forgetting that the root doesn't have a parent. So if you're going, you know, node dot parent dot right, or something like that, that can cause an error because there is no parent. So there is no dot right for the parent.
And
so let's step through a proper implementation, or we'll say 1 1 option for for implementing the the rotation.
so we'll we'll step through it.
I'll also emphasize again that these kinds of of node and link based algorithms. It does get tricky to, you know, mentally picture node dot write node dot write dot parent, and all those things. So again, I'm going to encourage you to use post-it notes or a whiteboard, or any sort of diagramming tool
to draw these out because it does, it does really help. So we're going to start by passing in the node that we want to rotate. So this is the picture. You've got node here, and it's got a right leaning edge a right leaning red edge. So we need to rotate. X. Put it up here. Put Node down here and correct all of the child links appropriately.
So we're going to start by getting a pointer to node dot, right? So we can reference it easier. So we have X
captured here.
We then are going to store the pointer to node dot parent, because later on in the algorithm. We are going to change node dot parents pointer to point to X.
So we still need to know what its original parent was, so that we can do some reassignment of of that note as well.
So I just capture the the pointer in this variable original parent.
The 1st step is to set node dot write
to X's left, child. So it's the same as as this one right? Same same process.
So we're going to move this pointer down here. So we now have node dot right is what is pointed to this cloud. I have this line still drawn here, because X dot parent at this point is still pointing to node, and it needs to be adjusted.
Now, we also need to, because we moved Node Dot right from being a child of X to now, being a child of node, we need to update update that parent.
However, we're not guaranteed that X is going to have a child.
So x dot left may not exist.
So we have to check to see if
if this exists, then do something about it. If it doesn't exist, then you don't have to set its parent.
So that's where, if Node dot write is not none, then we set Node, Dot, writes Parent to the node.
We then have to, you know, to move X up in the tree. We have to update its its child. So we set X dot left equal to node. So now Node is referred to as both Node and X dot left.
And here's where we update nodes, nodes parent to be to be X,
because it's I didn't draw it here, but there's still a pointer upwards right to a note, dot parent.
So we're going to set X dot left dot parent to X, and then
we have to make sure that we're copying the color of of node because this edge here.
the one that's pointing down toward it could be red. It could be black, you don't know. So you're just going to take whatever the color is, and and and move it over to to X.
After that we know that
X is connected by a red edge, because that's the reason that we're rotating because you rotate left when you have a right leaning node. So we just set the the color of node to red
to ensure that we now have that left leaning edge.
We have to update
X's parent because X was previously pointing to to node as its parent. So we have to give it its new parent to the original parent.
and after that we have a couple of special cases.
So at node could be the root of the tree.
You could be rotating around the very, very top. And if you have that situation, original parent is equal to none. So we could check this a few different ways. I'm just
checking to see if self dot root is node. So this is just saying, Hey, if I'm the parent, if if Node the node I'm rotating around is the is the root.
Then. I have to update. I don't have to. I don't have to.
I don't have to do anything special about the assignment of the of the parent.
because if original parent is none, then this just gets set as none. No problem.
But I do have to update the root pointer in the class.
Because, remember, you're always going to start at root, and if you don't update the route, then you're going to be traversing the tree starting from the wrong spot.
So we 1st checked that.
And if that's the the case, then original parent was was none, and it doesn't have a left or a right child. So you don't have to worry about that. So if you fall into this part of the branch, you'll exit out after that. Otherwise you have to check
to see if original parents, left or right child is is pointing, was previously pointing down to to node.
Now I've drawn this for simplicity's sake. It's kind of a straight line, but in reality it looks more like this right where you've got the original parent has a right or a left side. So you have to check to see if
Node was originally pointing to, or originally pointed to from original parent, either on the right side or the left side.
So I do that just by checking. If original parent dot left is equal, is is the node. If it is, then assign original parent left to X, otherwise do it to the right side.
So in this case it's on the right side.
So we we update original parent dot right to X. So then we have a proper, a proper flow.
and then, if you review the recursive code and and recall that we we need to be able to continue traversing from the new the new root of that subtree.
So we return the value or return the pointer to X, so that later on in the algorithm, we can use that
use that new pointer as our as our current node for the traversal.
So after it's been rotated, it should look more like more like this.
And now we are at a spot where we have a nice left leaning, left-leaning node
in. In the case where Node Dot left is a red link which is which is possible right. If node dot left is red, then the next step in the algorithm which we'll show later is to do a rotate right? Because whenever there's 2 left children that are red, that represents a 4 node, so we have to get rid of that. So that's that that second rule
that we check.
So
I didn't show rotate right on this, because it's basically the exact same thing except all of the right links are changed to left links, and vice versa. With the exception of
of this, this this section here.
so you would be no dot left.
X dot right equals no dot left. So it's basically a mirror image.
So after you have your your rotations correct, let's talk about how we do the the insert.
We have the the special case where?
where, if you are inserting into an empty tree.
so it's the very 1st insert into your red black tree. The root is none. So if that's the case, then just insert the node@self.root, set it to black, because the root always has to be black and return. Return from the insert because you don't have to do any rotations. Your trees balanced. There's nothing to do. So that's your kind of 1st few lines of code in the insert.
If you are not in this special case, meaning you do have something in the tree. You do have to check the check the balance afterwards. So we're going to find 1st traversing downward. Where do we insert the
where do we insert the node? And this step, remember, is exactly the same as inserting into a binary search tree. You just traverse left or right until you find the bottom of the tree, and then insert that node at that at that spot.
So if you do this correctly, and then don't do any balancing, you have yourself a structured binary search tree. But you don't get that. You don't get that balance unless you do the recursive bit backup.
So let's let's talk about how we traverse down the tree multiple ways to do this. I'm I'm doing it with a while. Loop
you start with current and you start at the very, very, very top of the tree, you start with the root.
and then until you reach any of these exiting values we continue to traverse. So we're going to say
Oh! And let me talk about this one here real quick. So in the
in the key value kind of of tree
we might be inserting into a node that already exists. So the keys match. But the value might be changing. So if we find that any of the values are equal to what I'm trying to insert. Then just update the value. And because we're not changing the structure, we're not inserting any nodes. All we're going to do is
set the value of the current node into to be the the value of what I'm trying to to insert
and then just return because I don't have to do any restructuring. I don't have to do any rebalancing. It's just it's it's just updating the values.
Now, in in most cases, right? You're we're inserting something something brand new. So we have to check to see. Where do I insert it? If the value of the key is less than the value of the if. The value of the key that I'm inserting is less than the value of the node that I'm at.
then I know that I need to traverse left.
So what I do here is
I check to see if cur dot left is none, so if Ker left is none. That means I've reached the bottom of the tree. In this case Ker left does exist. So I'm just going to update the current pointer to current left. And now Ker is here.
I will go to the next iteration of the loop.
I'll find that I have to go left again.
and now I have to go right because I've I'm inserting I so I is bigger than E,
and then we get to H,
where we're going to find. Oh, I need to go to the right.
Well, cur, Dot, write is none. It doesn't exist. I'm at the bottom of the tree, so I'm going to insert the node that's already been created as a red as a red pointer.
and I'm going to insert it here to the right.
I'm going to set the current dot right, parent. The insert node. Insert nodes parent to be
current, which is, you know, I'm inserting it here. I've pointed it downward. Now I have to point it back up
once I get to here. I know I'm at the bottom of the tree. I've inserted my node so I can break out.
Break just means exit the the while loop.
So at this point of the algorithm.
I have a a red link pointing to I, and it's pointing back up to H accurately, and notice that current is still pointing to H,
and and that's that's desirable. You could
have Kerr pointing to I at this point. But remember the 3 rules, it all has to do with children.
So if you have a right leaning edge, or if you have 2 left leaning edges, or if you have 2 red children. Well, we know that I has no children, so there's never going to be any rotations or activities that we need to do for that new node. So we just leave the current pointer at H, because that's where there's the potential for a rotation to occur.
So once we've broken out of this while loop. We then have to do the balancing. So this, this is the traversal back up the tree.
So we're going to do another while loop, but using the the existence of cur as the as the as the condition.
So
at this point we just need to do those 3 checks. These are the same 3 checks that we did in the recursive call
check to see if it's left. If it's right leaning.
if it's right leaning, then do the rotation left.
and if we do, the rotation left.
we're going to end up with H. Being moved down to the left child of I and Ker is being captured as the new root of that subtree. So Ker stays where it's at.
If H. Had anything over here like another red, another red link. Then we would have to do another rotation of I to put put it back down. But that's not the case in in this example.
So.
but we still have to check. So we check to see if it has the 2 2 left children. If it does, then we rotate it right.
and then also again capture the current.
The final check is if it has 2 red children, and if it does flip the colors.
So after we've done that, we have completed all the rotations for this local local area. And now we need to check
cur, we need to check its parent. So we need to continue to reverse up the tree. So we just set cur equal to cur dot parent. So now current is pointing to E,
and we keep going until we reach the reach, the the route.
When we reach the route we'll go through the the 3 checks and but
do whatever we need to have, and then it will set
cur equal ker dot parent, which will happen to be
none at the very end. Right so once you've reached this point and you're at the root.
You set current to the value of none, and you'll fall out of the while, loop because it's going to only go while current is not none.
The last step, as always, is to set the root false. And there we go.
So that's your
That's the that's the solution to to homework one
so as a reminder dude night.
I've given you the the full test suite. So run that test suite and you'll see what the final final score is going to be on your submission
any questions or go backs.
Okay?
So let's move on to some of the
some of the new content. So divide and conquer. Dnc, this
is as kind of mentioned before an algorithm class, where we take the
the input and then we split it or divide it into smaller problems. So splitting the array into 2 sides. Remind me, you guys cover merge sort in a previous course in a bit of detail. Right? So if I refer to merge sort you, you know what I'm talking about.
Sean Warlick
Sean Warlick
00:25:00
Yeah.
Kevin Anderson
Kevin Anderson
00:25:01
Okay, cool. Just wanna make sure I I could totally go go into it if you if it wasn't covered. But it is expected that you at least know the the basics of.
Sean Warlick
Sean Warlick
00:25:10
I don't think I I could write from scratch, but I know what it's doing.
Kevin Anderson
Kevin Anderson
00:25:13
Yeah, that's fair. That's fair.
So
that so merge sort is a divide and conquer algorithm. You're taking the the large array, splitting it into 2,
and then doing something else when you're putting those 2 back together. That's it's
almost always done recursively. So you you call your algorithm to split it into 2. And then you you call that algorithm on both the left side and the right side, and then you go down until you reach your base case, which is usually a size of one or a size of 2 elements. Do the trivial activity, and then return those back up the tree.
so you break the most. Commonly you break it into 2 sizes, solve those 2 sizes recursively, and then, when you are putting them back together, it's usually in either constant or linear time.
And the result of that is is, if you have a, you're often doing this for for N squared
algorithms. If you take if you're able to do this recursive problem and then put it back together, recursive problem by splitting it up into 2 sides and then putting them back together. In linear time, you end up with an N log N algorithm, which is significantly better than than N squared.
So let's let's look at why this, this occurs kind of with a from a math perspective.
So let's
let's take an algorithm algorithm, A that accepts N, and it processes the records in N squared time.
if and and then let's take another algorithm that takes that same input and can take
can split a into 2 pieces and then put them back in, put them back together in linear time.
So again, think merge sort is. The is the the best simple example of this.
So if we're just looking at the number of calculations.
N, so a of N is going to result in N squared processes where B of N can be written as
splitting
the input into 2. So you have size of of N divided by 2 being fed in to to both sides of A, and then you have
N number of steps to put them back together.
So you end up with
doing doing the math. We can substitute N squared in here, and we end up with the number of steps is N squared, divided by 2 plus n, which is about half of N, and we'll put some actual numbers to this. So you don't have to picture those those numbers
in your in your head.
So let's say we have a list of a thousand.
If you have a list of a thousand and it has to process that list in N squared time, you're gonna do about a million.
You're gonna do about a million
activities, a million, a million computations.
Conversely, if you take that same 1,000 number divided by 2 and pass it into a twice.
you get af af 500 plus a of 500
plus a thousand for that linear time. Step to put them back together. You end up with
500 squared is 250,000, plus 250,000 plus one. So you're ending up with with 501,000, which is almost half.
Okay.
Let's let's see
if if we can split it into halves. What happens if we split it into into thirds like, do the do you know, split the array into a left, a center, and a right.
When we do the math, we would say that
we would have a of 333. I just made the number a little bit more round, so we split it into 333 different chunks. Those are all n squared, and then you're adding 999. So you end up with
110,000, plus a hundred 10,000, plus a hundred 10,000 plus oops.
Let me fix that typo.
and you end up with
333,666, which is just over a 3.rd
So if you were
thinking about this you might say, well, why wouldn't we split it to fourths, to fifths, to 5th sixths, and to get that number
all the way all the way down.
That's a good intuition. But what I've shown here is a bit of a simplification of the process. There's a little bit of overhead that that takes place
so the overhead ends up being, you know.
you have us. You have a a constant for every single time you split it, and then you have to run the the putting it together that many times. So you the closer you get to splitting it by N, you, you get to n squared overall. So imagine if you were to do merge sort, and you were splitting it into arrays of of one right off the bat. Then
you have to put those things together at, you know, end times. So you end up
not getting optimal results by splitting it up to too much because of all of the additional overhead. So you balance the overhead, usually by 2 or 3.
is is sufficient to get you the the desired results.
So I'm going to take. I'll take a pause. Any any questions about the theory behind divide and conquer being
being faster than a than a naive like N squared algorithm.
So because these divide and conquer algorithms can be a little bit more complex checking
big O of recursive algorithms can also be kind of daunting.
So there is a a theorem
for analyzing the big O of a divide and conquer algorithm to determine what the what the big O is, just by looking at a few key parameters of the of the algorithm itself.
So
I know this again, this is pretty mathy. But it it's it's it's less intimidating. Once we go through a few examples.
So
we take this this function, we're gonna we're T of N is going to be the the big O right? And
because the divide and conquer algorithm usually has the steps of breaking it up into problems of a smaller size, and then recursively calling the algorithm a few times on those smaller sizes and then putting them back together with a kind of a you know a collector algorithm, if you will, that ends up being, you know, this this
last bit, and that can sometimes be linear time. It can sometimes be constant time, and it can be you know.
and cubed in in some cases, and so the the value of D,
the the power of of that
putting together part of the algorithm, that's that's what gets set as D,
this only works. If you're splitting it
into more than more than one sub problem
at a size that's that's smaller than the original. So B can't be 0. And then you know your D needs to be greater than or equal to 0. So this can be a constant time. If D is 0, then this becomes big o of one which is constant time. If d is one, then this is big O of N. If it's d is 2, then it's big O of N squared.
So we we figure out what the values of A, B and D are.
and then we can use this to calculate our our big. O, if it follows one of one of 3 different different cases.
So if d, which is the power of the of the
latter part of the equation. If it's bigger than log B of A, then that becomes the the dominant force. So it, even if this was in constant time or actually no, let me take it back, even if this is
and if this is
n squared time. But to put it back together, it's n cubed that n cubed is the dominant is the dominant expression
or the dominant term. So you end up with just using that as your big O,
if the cases are the exact same. So if
if d is equal to log B of A, then you end up with something that's multiplicative. So you have
this and and to the d
expression times the log of N, so the number of times you're having to to do the recursion.
Otherwise, if D is smaller, then you end up with this log base B of A as your complexity. So
to this, to the this point in the course we've been talking mostly about nice round numbers for the powers, so n of one or sorry big O of N to the one big O of n squared big O. Of n cubed. But what we're going to see is that even if we get, you know
big O of N to the one half that's significantly better than big O of n squared.
So having decimals, you know. More complex numbers in the
in the big O is, is, you know, a different class.
n to the 2 is a different class. So yeah, n, squared is a different class than N to the 2.5
to to help solidify this. Let's look at an example.
So in merge sort, remember, we're splitting the array into size of N divided by 2.
So we're splitting it into 2 subproblems.
We then recursively call both sides.
So the recursive call is happening 2 times. So so A and B both equal 2.
So you're splitting it in half and then doing recursion on both sides, and then
the linear aspect or so when you're putting them back together, it's a linear time. So the the latter part of the equation is big. O of N, so d equals one.
So in merge sort we have. B is 2, A is 2, and d is one.
So let's figure out what is log B of a well log base, 2 of 2 equals one.
So we check.
What is DD is one
log base log base, 2 of 2 is one. So we're in this in. So we're in this condition here.
which means that it becomes the the computational complexity of merge sort is N log, n.
and this works for even more more complicated algorithms that have different ways of of
different ways of splitting and different ways of doing the recursion.
So, you know, take a pause.
Let you absorb a little bit.
I know the the math is is tricky, but it becomes kind of algorithmic for you. You do you identify how many you know? What's the size of the subproblem? How many recursive calls? And what's the complexity of putting it back together? Plug those into this into this formula, and you get the big O without having to read every line of code, and understand what the what the sizes of each of the recursive calls, etc. So it gets
so it. This is a an easier way of determining the the complexity
on a relatively complicated complicated algorithm.
Sean Warlick
Sean Warlick
00:39:49
What help me understand what the the sub problem represents here in the recursion? Is it the number of times that you had the depth of the recursion, or is it the steps within the recursion.
Kevin Anderson
Kevin Anderson
00:40:03
It is.
It's not the depth of the of the recursion. It's the
number of of times you call the recursion.
So even if you're doing something within that
thank. It matters less about what's happening within the recursion, and it's more more about the number of times you. You make that recursive call.
I don't know if that answered your question directly. Let me know.
Sean Warlick
Sean Warlick
00:40:40
I don't know. It's still hard to wrap my head around recursion in some ways. But it I'd have to kind of, I think, work through it. Yeah.
Kevin Anderson
Kevin Anderson
00:40:48
Well, let's let's look at a a less
symmetric problem, and and maybe that will help split it out.
If not, let me know. And I can. I can take another stab.
So we're gonna invent an algorithm that that is is magical. We we don't. I don't actually have a
you know, a tangible, you know. Example. But this one is is is explanatory, anyway. So we're going to take an algorithm that breaks the input into sizes of 4. So we're going to have an algorithm that says, it's a 16
it's a 16 element array. We're going to split it into 4 arrays of of 4, or maybe making the the math different. Let's say it's
a element. There's 20 elements. So we're going to have 4
arrays of of 5 elements each.
and we're going to. Then take only the 1st 3
of of those arrays, and then recursively call the
recursively call the algorithm on just those 1st 3,
dropping the the 4th one on the floor for a moment, and then, when we
have the results of all of those recursive calls. We're going to put those
3, those we're going to put that array back together in a in a step that takes n squared time.
So some kind of fake code here.
We split it into fourths.
We we create 3 arrays of of of
the the you know, the 1st 4th of the elements, then the the second quarter, and then the 3rd quarter, and then the 4th quarter is just getting getting dropped on the floor because this is magic.
We then call the recursion 3 times
to create these little, these, these 3 sub problems, the the results of these 3 sub problems. And then we have. We're gonna put them all back together into into a new array. And then
that new array gets, you know, a nested loop. So an N squared thing to then ultimately return.
In this particular case the values of A, B and D are going to be different. So
we're 1st gonna tackle B, which is
each subproblem is being solved on a quarter of the original size.
So it's N divided by 4. So B equals 4.
We then call the recursion 3 times.
So a gets set to 3, because again, we're we're solving
the the we're solving only 3 of those sub problems.
And then.
after we've solved those 3 subproblems, the part to put it back together is n squared. So d equals 2.
If we then take a look at what is
log B of a so log base, 4 of 3 ends up being about point 7 9 2
with beat with
log base, 4 of 3 being only 0 point 7 and log and D equals 2. We find ourselves in the 1st row of the of the solution. So this algorithm ends up being big. O of N squared.
Because again, it's that putting it back together in in quadratic time is what the what what dominates the the algorithm. So we end up with
big O of N squared, if that if this last piece
was linear, so let's just say we didn't have this nested loop, and we just returned everything in I
then we would have d equals, one
d equals one. It would actually
It would actually be in the it would still be in the same. Oh, let's pretend that it's constant time. So let's just say we just return. R. So there's no processing here. So n equals 0 sorry d equals 0.
Then with d equals, 0
log 4, 3 is going to be bigger than D, so we're going to put it would end up being big. O of
of log base base, 4 of 3.
So it would be a much faster algorithm if you didn't have this.
So
for each of the algorithms, we're going to be talking about Kuratsuba's and matrix multiplication. Specifically, we're going to talk about the the breaking of we're going to do the master's theorem for each of those those 3 to to help solidify it a little bit more.
Okay.
okay?
So Karatsuba's fast multiplication algorithm.
This was an algorithm that was originally originally proposed by Anatoly Karatsuba, who's a Russian
Russian computer scientists in the sixties
he published this in 1962. I believe.
The problem is relatively simple.
Given 2 n digit numbers calculate the product of N. Times y.
Of the of those 2 of those 2 integers.
before we explore what Karatsuba is doing. Let's look at how we, as as humans, are kind of taught how to do how to do multiplication.
Because there is, there is an algorithm right? That we that we all all use and have used since since grade school. Right.
We'll take the
the 2 numbers. We put them on top of each other, and then we multiply the ones
the ones value
by each of the the smaller smaller items, because remember the multiplication tables, for you know, 2 times, 2, 2 times one. That's kind of constant time you have that memorized. So you don't have to
go go back and try to remember. How do you do? 9 times 9? That's just. It's a constant time thing.
So you do all of those simple, simple calculations
you add a 0. Because then now you're now you're multiplying each of these by basically
by 10 times the this number, and that makes it easy. You just add a 0 to to make that happen so 2 times, 2, 2 times, 1, 2 times 3,
and then you do it again
one times, 2, 1 times, 1, 1 times 3. And you create this, this
this algorithm, you you end up with adding up
N number of of numbers together.
If you had, you know, if this was 4,
and if you had, you know, 4 digit number here. You'd have another row if you had a 5 number here. If you had something that was like 10,000, you'd have 5 numbers here.
So you're doing quite a few multiplications. And then you're putting it all back together in
in linear time. So the math of this algorithm ends up calculating out to to N squared because you're having to do all of these
all of these calculations, one for every you know, one for every pairwise value.
And then you have a linear time at the end to put to to put it together.
So this is the grade school multiplication algorithm and
computers are really really fast and doing this on, you know, a thousand times a thousand or
even 10,000 times 10,005 digit numbers pretty pretty easy, but in really complex computation, astronomical calculations, or
I don't know. Particle accelerators have really, really big numbers. So
anytime, you have really, really, really big numbers having to spend big O of N squared time to multiply them is is really really time consuming. So Kurtsuba was trying to figure out a way to have the computer do do the calculations faster than than this kind of naive approach.
So kind of putting the cart before the horse a little bit. But
we'll we'll do the analysis to kind of prove out why Karatsuba's algorithm is is so much faster. It ends up being log base, 2 of N to the log base 2 of 3, which is N to the 1.5 8,
and just to
make the math solid for you. So you can see it that 1.5 8 is much faster than N squared. Let's just put some values into it. So N squared of a thousand is a million. But N to the 1.2 8 or 1.5 8 of a thousand is only 54,000. So
even though the the number difference between these 2 powers is not very much
in in practice. That actually is a, it's, it's far less computation.
So anytime you can get your algorithm to be
even a few decimal points smaller than N squared. You're going to get significant improvements.
So let's see how how he, how he came up with this, or rather, what is the result of his, of his work?
We're gonna have to go back to high school algebra.
I'll I'll step through it and try to go as slow as possible, so I don't stumble, stumble over the numbers.
but it starts with this kind of basic premise that any number
can be written as the sum of 2 other numbers in a very specific way. Where you have
some some number times a base to a power
plus some other number. So, for example, if
if the base is, we're gonna stick with base 10, we're not going to go into binary yet.
but let's just consider a base 10 system, and we could write a hundred 27 as
one times 10 to the 2, which is a hundred, plus 27,
2,504 can be written as
2 times a thousand, plus 504.
So in these cases, x, 1 would be one.
The base is 10
M. Which is the power of the of the split is 2, and then the final number is 27.
So we just have this property that we can split the numbers, and they are still equal.
After we've after we've broken them up.
So if if you are convinced that we can write the numbers this way.
Then, if we have 2 numbers x times y, we can write them as that expression.
the x, 1 times B to the M. Plus x naught times
y 1 times B to the m plus y naught.
And then, if you remember your your high school algebra. You can do foil on
on this set of multiplications, and you end up with this relatively funky, funky result.
But you've got the the 1st 2 1, st 2 terms here x, 1 bm, times, y, 1 bm, that becomes
x, 1 times y, 1 times B to the 2 times M.
So if this was, you know, B to the one it would be B squared. If this was B to the 2 it would be, you know, B to the 4.th
So you end up with these terms, and
using Karatsuba's brain, we do some some additional factoring.
So we take this longer expression, and we do some some combinations and
end up with this expression. Okay, notice that there are.
When we're talking about XY, there are 4 different multiplications that are taking place.
There's the XY. Multiplication here.
the XX 1, y. One
x, 1, y naught, y 1 x naught, and then y naught. X naught.
So 4 different multiplications that need to take place. We're ignoring this multiplied by a base, because this is a trivial task. If you have any number.
we're talking base 10 systems right?
If you have any any number.
12,402, and you want to multiply it by by a power of of the base, so multiply it by 10. You're just adding a 0 at the end. If you want to multiply it by a hundred, right? You're adding 2 zeros at the end, so so
multiplying any number by by
a power of the base, you end up with a trivial just adding 0. So you don't actually need to do this multiplication. You just have that that nice, easy trick of adding, adding zeros to the end.
I just realized that you guys might not have dealt with numbers in different bases? Much?
So you know, a base 10
system is what we all know and love in in mathematics. We, we typically use base 10, you know, 10 different digits, 0 through 9 computers.
or use a base 2, right? They use binary. So they only have 2 digit digits, 0 and one.
there are other base numbers. There's there's other base systems.
There's there's hexadecimal, which has 16 digits, you know, 0 through F, so it's it's
understanding basis is like, kind of beyond the scope of of this course. But
but it's something to kind of realize that we're talking about this in base 10. But when it gets implemented in in computers, it's it's base 2. But so that's why we have kind of
generalized this to say, any base you can do this on Base 8, you can do it on base 16.
so that's the the whole reason that we have this base base factor here.
Maddy
Maddy
00:57:55
I do have a question about.
I guess the exponent in front of the base when you're multiplying the 2 numbers together.
For both numbers. The exponent is M.
Why are we assuming, I guess, that, like these numbers are on like the same order of magnitude, like.
I don't know if you're multiplying
10 and a hundred M. Would not be the same.
Kevin Anderson
Kevin Anderson
00:58:23
Hmm, we're both curves.
Yeah. So because we've set it to M.
Whatever M is is guaranteed to be the same. So we're going to split it, to be both a hundred or both a thousand.
so you could arbitrarily choose that you want it to be
10 to the 6, th and it would be 10 to the 6th on both sides. You wouldn't split one to be 10 to the 6, th and the other to be 10 to the 10 to the 5.
Maddy
Maddy
00:58:54
Okay.
Kevin Anderson
Kevin Anderson
00:58:56
When we when we see this being being recursed, we're gonna see, hey, we we pick a value. Let's just say the the number is a thousand digits long. We're going to set the split at at
to say a thousand long. Then we'll put the split at 500. So we're gonna split both of the numbers the
the same way.
Maddy
Maddy
00:59:24
Okay, I see. Thank you.
Kevin Anderson
Kevin Anderson
00:59:25
Yep, yeah. Good. Good question
it. It definitely shows you're you're following along and thinking about it. So thanks for the question.
okay, so we're gonna take that that expression here.
right? We've done all the algebra. So now we have a new form of of the mathematical
equation here, and we're going to simplify it further.
We're gonna take
the x 1, y. One, instead of having to say x, 1, y. One or XYX, 1 y, one y, 1 x 0. We're going to refer to those going forward as Z to the 2 or z 2 z. 1 and z 0.
So z 2 is x, 1, y. One z. 1 is x 1. y. Naught.
You can see the color coding right?
So when we split it out in this way we still see
that we're still doing 4 multiplications, this one here.
this one here, this one here and this one so 4.
What Karatsuba's contribution was with his brilliance provided us was that we could write z 1 as
as as this here x 1 plus x naught times y 1 plus y naught minus
z 2 minus z 0. So I don't
need you to go through the algebra to figure out that this is the case. We can just trust that that this is the case. And
when we, when we see it this way, we've we've kind of simplified
one of the multiplications. So in this, in in practice, multiplication is a more more expensive act than than addition.
because, you know, when you are adding 2 numbers, you don't ever have to, you know, expand it out the way that we do with multiplication. Right? So the addition is trivial, the multiplication is hard, so
the the less multiplication we can do the the better.
So this now allows us to do
all of these these calculations. Instead of doing 4 multiplications, we get to do 3.
And let's let's do some math to prove that out.
So I just chose some, you know, arbitrary numbers.
And because this is 5 digits, we're just gonna select the split to be to be 3.
So that gives us X is going to equal 14 times times 10 to the 3, rd
plus 1 99.
So so that gives us x, 1 is 14 and x 0 is 1 99
for YY, 1 is going to equal 8, and y 0 is going to be
675.
When we want to plug those into the into the Z equations, we end up with
Z 2 equals 112 Z. Naught equals 134,000
z. 1 ends up. After you do all this, all this math you end up with z. 1 equals
11,042.
So it's not called out in the slides, but
to help PIN this to like the recursive nature of these things is that
if these numbers, let's say that these numbers were really, really, really big, and M was also big. So let's take the 1,000 digit number. Example, you'd have
2 500 digit numbers.
So those 2 500 digit numbers would then be re. So this multiplication here the x, 1 times y, 1
would be a 500 digit number times a 500 digit number. You would recursively call
the the algorithm on the left and the right you would recursively call Karatsuba for
the 2 500 digit numbers, and then those would be split into 250 digit numbers, and so on and so forth, until you get to really small numbers that you can multiply quickly. So
the reason that we're getting an advantage from doing all this extra overhead is that we only have to recursively call
the the algorithm 3 times instead of instead of 4.
Sean Warlick
Sean Warlick
01:04:49
Maybe it's just rusty in algebra, but in the 1st line, where we've got z 1 equals.
But this is, are we just? We have assigned.
Oh, did you just multiply by? Oh, you multiplied by minus one there?
Because, wasn't it?
v 1 plus or x 1 plus. Okay, yeah, never mind. That's.
Kevin Anderson
Kevin Anderson
01:05:19
Yeah, the arithmetic is the is the tricky thing to read.
Sean Warlick
Sean Warlick
01:05:25
Yeah, okay, that's just multiply that minus one from where we just described it earlier. Okay.
Kevin Anderson
Kevin Anderson
01:05:32
No problem.
So when we we've calculated the 3, the 3 values for Z, we end up putting it back into.
put it back into the equation.
So we have Z 2 times B, 2 m.
so that's a hundred 12 times a million
plus this center term, which is 11,000 times a hundred. So that gives you 11 million, plus 134, which is z naught, and you end up with the the proper value.
If we were to do this using kind of grade school math, we would
do it this way, and we show that we've got the the same result.
So a lot of a lot of math, right?
A lot of algebra here.
I'm not trying to teach you algebra. What I'm trying to, you know, teach you is this particular algorithm that uses algebra in order to to reduce the complexity of of multiplication.
or, say, increasing the complexity of the problem, but reducing the time complexity to to execute it.
So what is the
you know? We've actually, we already said what the the big O of this particular algorithm is. But let's use the master's theorem to to calculate it. So
how many, how many sub problems are we are we calling? Yep.
you got it right, Janine, we're splitting it. Or we're we're calling the recursive aspect 3 times because we're doing that multiplication only 3 times. So a equals 3
the size of the subproblems. We took the 1,000 digit number, and we've reduced it to 500
at each step. So B equals 2 yep.
and the work outside of of the recurrence which is doing all of the addition and putting things back together is is d of one.
Yep.
So when we shove this into the master's theorem.
We see that
d is less than log base, 2 of 3, because log base 2 of 3 is
1.5, or what? 1.5 8.
So we end up with this being the the result.
which is again much faster than than N squared.
So it helps solidify these things to see it in code.
So this is what the code would look like for something like this. So
it's a recursive function. So you have to start with your base case. So our base case is if either number is
less than less than 10. So it's you know, a single digit number. Then we're going to use the the trivial constant time multiplication of X times Y for these small numbers.
If we're not in this case where we have small numbers. We're going to do the recursive call.
So to get M. We're just going to say, Hey, which is the
But
what's the halfway mark of the number of digits. So we're using some pythonic magic here to take the the decimal value of X
represented as a string. Right? It's a thousand string character.
And then get the length of that string.
whichever one is. The Max then
divided by 2 using integer division.
we then can use some
some additional arithmetic to to get the x 1 x 0 y. One, and y, 0 values. So this is.
you know, dividing it by the the base of your dividing, you know. 20,000
20, let's say the number is 20,500. We're going to divide it by
it's divided by 10,000, so you'd end up with
with the integer math. Here it becomes 2,
and then this is modulo. Right? So you're we're dividing it by that same 1,000. And we're gonna get that, the left, the the remaining values.
So this is just the the math to split it into the
into these 4 items. And then we call the the algorithm algorithm recursively again with, you using
this math over here, right? So we're going to multiply X 0 times y, 0.
And then we're gonna mult, we're going to calculate
Z of one which is the sum of these 2 right multiplied by each other, and then
XX, 1, y. One.
And then, after we've, you know, gone through the recursive calls, and they've all returned their values. The the final result is is
that is this one here
where it's z 2 times we're using base 10. So 10 times 2 of the m plus this
plus this. So this is this line here is representing representing this.
So this is the code for it.
If I've I've been asked by students to kind of baseline this and prove that it's faster.
And and here's where it gets gets tricky is that in your modern programming language
and your current computer architectures. This
or or a similar version of Karatsuba, is already implemented at the at the core.
So when you multiply 2 really big numbers in python. It's already doing the optimization and doing these faster algorithms. So if you were to run a speed test where you multiplied 2 really really big numbers in python using just x times. Y.
It's actually going to perform faster
than having written your own high level version because of the overhead that is applied to to the math
right? So this is already being in. You can think of it as being applied already on the processor itself.
So this is more of an illustrative example of a divide and conquer algorithm that you could use. But because this algorithm has already been implemented in the under workings of your machine.
You don't have to. You don't have to do this.
If you were writing in assembly.
I hope you never have to do that in a career. Unless you're into that kind of thing, you would do something like this because you you're you're dealing with really, really low, level code in assembly like you're writing to the registers on the processor, and it's it's very tedious.
But so I mentioned that because
if you try to do this in python. You're going to go, hey, Kevin? This is way slower! Why is it slower? You said it was faster. Well, it's because the optimization is already taken care of for you.
Awesome.
Okay?
let's see, I think it's a good time for a break. Let's take 10 min before we start talking about matrix multiplication.
Google changed oops. That's because I didn't do 10. There we go! There we go alright. We'll be back
all right.
So we're not quite done with with math. This, this this lecture, but this is less algebra. So
This one should be a little bit easier to to consume for the for the folks that aren't as in love with with mathematics.
So matrix multiplication is a very common but
very common algorithm that is used in computer science. It's used in graphics in 3D rendering used to solve solve equations. So it is is super common. And as you can imagine, like computers are all about crunching numbers, right? So numbers are often laid out in matrices, and you sometimes need to do multiplication on those matrices. So it's it's
very core to to a lot of of algorithms. So it's important for us to have a
an effective way of of doing it.
So I'm not going to go into this, assuming that you know how to do matrix multiplication. So we're going to do a quick review of what matrix multiplication is and and how how it's performed, because there are very specific rules on how you multiply matrices.
So a matrix is a multi dimensional structure.
We're just going to call that, you know, a two-dimensional structure with rows and columns, and if you want to multiply 2 of these matrices together, the rule for multiplying them is, you take the sum of the products of a given row and its corresponding column.
So
there's here's the the summation written in Sigma notation, but I'll but I'll walk you through it if you, if you can't interpret this easily. Basically, this means for every cell. Ij.
you are taking the Ith value and the K I-th value of A and the Jaith
value of B. So this is the the row of A and the column of of B, and you multiply those numbers together
and then add, add them up.
So using this super simple, 2 by 2 example we'll we'll walk through it.
So when doing matrix multiplication. I like to set it up in in this way, where I put the 1st matrix on the left, and then the second matrix on the top.
And then the resulting matrix is kind of in this in this intersection. So this helps me remember that it's the row of the 1st one times the column of the second. So in this example that I've illustrated here we have
the upper right value of the resulting matrix. So c. 12 is going to equal
a 1 1 times B 12 plus a 1, 2
times B, 2. So you take that the the sum of the the products of the the corresponding row and column.
and then you do that for for each each value in order to get the result.
So because of this kind of row to column pairing. The matrices have to be in a very specific shape.
So
you have to basically the number of of rows in the 1st matrix has to match the number of columns in the second matrix. So you can multiply a 3 by 3 by a 2 by 3
to in order to get the get the result.
So we say, A is an NA is an m, by N matrix, m rows, N columns B is a N times, PN. By P. Matrix, which is N. Rows and P. Columns. The result is going to be an array, a matrix that is.
rows by P columns. So it does have a slightly different different shape given given the inputs,
so this is is this just a a rule that
that takes place. Now I neglected to mention this at the start. It's not really necessary for the for the assignment, but
if you're multiplying 2 matrices a times B. That doesn't mean that a times B equals B. Times a.
Because there is an order of of things. So in regular arithmetic, right? A times B is equal to B. Times A, you've got that property
that does not apply for matrices. So order does matter.
So let's step through an example here. So we've got one matrix, 1, 2, 3, 4 times, another matrix, 5, 6, 7, 8. And we want to get the the result. So we're going to say.
the we're going to multiply the 1st row by the 1st column in order to get the the 1st value. So we're going to say.
C 11 is equal to one times 5
plus 2 times 17. So this one gets the value of 19
in order to do C of 1, 2. We then multiply the 1st row by the second column.
So we end up with one times 6
plus 2 times 8 to get 22.
So on and so forth, until we get all of the results.
Okay, so
there's a lot of arithmetic that takes place. And while this is a trivial example, right to 2 by 2
these matrices can be very, very large.
if you think about multiplying 2 2 matrices together that have
a huge a huge set of of attributes.
By the way, like this is used in
large language models a lot. There is matrix multiplication and matrix transformation that occurs in in those. And you read online. Oh, there's billions of parameters. Well, these have huge vector spaces like, we're talking millions, if not hundreds of millions of values. So that's a lot of a lot of calculation that takes place in order to to deal with these very, very large large data sets.
And if we do this using just brute force, naive implementation. We're saying
that for every row in M, or sorry for every row in the 1st column in the 1st matrix
times, every column in the second matrix go through
the the end number of additions and and sum those sum those up.
So this ends up becoming a an M. Times, P. Times, n
algorithm, which simplifies to to n cubed, which N cubed
is a very slow algorithm. If you ever have a algorithm, that's
end of the 3, rd you better be dealing with some pretty small small inputs
because even just a hundred by 100, matrix is gonna
become a million operations and a thousand by a thousand is going to be, you know, a much, much bigger, much much bigger number. So N. Cubed
is a is a time complexity to avoid.
So because this is a divide and conquer lecture, you're probably thinking, okay, well, what's the divide and conquer method for for doing this. So let's let's evaluate it.
we're going to simplify the inputs, just to make the the lecture easier to get through. So we're going to take 2 matrices that are N. By N. So 2 square matrices. And
and we're also going to simplify and make these kind of perfect perfect squares so powers of 2, so that when we split it in half we get a nice nice round number. So we're going to take these square matrices powers of 2, and then we're going to recursively divide them until we have
matrices that are 2 by 2 each. Right? So we're going to start with an 8 by 8. Make it a make it 4 4 by fours, and then each of those 4 by fours are going to be split into another 4 sets of 2 by 2 matrices.
and then we're going to put those results back together to get the final N by N matrix. And the reason that we can do this is that we have this beautiful property of of matrices in multiplication, in that the
the result of each corresponding matrix can be expressed as
the matrix multiplication of those smaller matrices matrices. What do I mean by that?
Let's take these 2, these original 4 by 4 matrices
and split them into 4 matrixes. Right?
And we're going to call those 4 sub matrices a 0, a, 1, a, 2, a, 3,
and b 0 b, 1 b, 2 b, 3.
Well, remember when we're doing this kind of element wise, we're multiplying each row by its corresponding column.
That applies, even when we generalize it to a submatrix. So it becomes
the resulting matrix C can be expressed as the property, the the product of a naught. Times B, naught
plus a 1 times. B, 2. So you're you do this row, wise pairwise multiplication of matrixes matrices.
Okay?
So because we have this same property, we just keep on
recursing down until we're treating the the final step as kind of a 1 by one matrix.
So because we have this wonderful property, we're able to do this, divide and conquer algorithm without without a whole lot of of additional additional work.
So this is a pseudocode kind of algorithm just to to show you what it looks like, if you
so we're gonna take the the original 2 matrix matrices. And
the value of NN is the size of the the matrix.
Remember, we're dealing with just square matrices right now. So keep it simple. So if the size is less than or equal to 2, then we're just going to do the classic easy matrix multiplication as normal, right? That little. It's that's an N cubed algorithm. But because N is really really small, it doesn't.
It doesn't impact us.
So
if it is bigger than 2. So we're not at our base case, we're going to divide M by 2 and then call the matrix multiplication recursively on each of the sub problems. So
remember, we have matrix a times, matrix b
plus matrix a plus matrix B, so we're calling. So we have to multiply. 1, 2, 3, 4, 5, 6, 7, 8.
So we end up with 8 recursive calls.
Okay, so
one thing to to note, I'll just have to have you trust me on is the
The addition, like putting this all back together is is quadratic time, because the addition is is row and column wise, so easier than matrix multiplication, but still not the you know, the most efficient, efficient algorithm. That's what we're left with.
So when we use the Master's theorem. On this we have 8 subproblems, because we're calling the recursion 8 times
the size of the subproblems is is half of the original
is half of the original size. So
if the original matrix is 16 by 16, the result is 8 by 8.
When we split it by 2. We make it 8 by 8, and then 4 by 4, and then 2 by 2. So our size of our subproblems is 2,
and as I've given you the answer. The work being done outside of the recurrence is, is
is quadratic.
So when we use the master's theorem, we end up with
log of B of A, which is log base, 2 of 8, which is 3
and d equals 2. So because D is smaller than 2,
I'm sorry because D is smaller than 3. We end up with the big O of this theorem of this
algorithm as big O of log base
log base 2 of 8, which equals N cubed.
So we showed that the naive version was N cubed. And now we have this divide and conquer algorithm. That is also n cubed.
and this is no better
from a from a big O perspective any better than the naive. And as a matter of fact, it's probably in practice worse, because we're doing a lot more work. We're breaking it up. We're storing all of these sub matrices in memory because we're using this call stack, right? So we're recursively calling deeper and deeper and deeper. So you have all of this overhead
so you wouldn't just
you wouldn't decide to do, divide and conquer on this, because your your result is is n cubed
So that's another good reason why we have this. This master's theorem, so that before we even start solving a problem in like, before we start writing the code, we can
assess the the approach. How many subproblems we're going to do, and then those sorts of things and get the the.
the expected the expected time complexity. And we can decide. Oh.
the divide and conquer algorithm isn't any better than the brute force one.
So
I wouldn't be teaching you this if there wasn't a better way, right? So we're going to introduce a new method for matrix multiplication
that was published by by a computer scientist. Last name of Straussen.
And it uses the exact same
premise, right? That you can multiply the matrices together.
in these kind of subcomponents, but he's
done some some magical math. I'll say it that way. It's outside of the scope of the course to teach you how he came up with with these. The Wiki Wikipedia article is
pretty pretty
It's pretty, Mathy. So if you are interested, I recommend you giving it a read. It's pretty dense. Would take, you know, probably a 2 h lecture, just to just to talk it through. But so, for the purposes of this lecture, we're just going to trust on trust. His math.
So what he figured out was, instead of doing these kind of
a not b naught a 1 b 2. He's gonna simplify.
I won't say simplified. He's done some cleverness to say that C. Naught can be calculated using
this short form, p plus s minus t plus. V.
Okay, not expecting you to memorize this. Don't worry.
But he's he's got these like different expressions.
or these these different values. For for each of these submatrices and those get put together, using simple addition in order to to construct the the result.
Now I want you to look through this.
This is addition. This is addition.
You know. You can ignore all of the
all of the additions and focus just on what's going to be the recursive call, which is the multiplication. And see how many multiplications we do. We do have. We have 1, 2, 3, 4, 5, 6, 7.
Remember how many we had in the naive case. We had 1, 2, 3, 4, 5, 6, 7, 8.
So he's reducing the number of of multiplications that you need to do by one
right from 8 to 7 and doing the the master's theorem. On this.
All we're changing is the number of subproblems.
And what we end up getting
is a big O of N log base, 2 of 7,
which is 2.8 1,
the the naive divide and conquer, which was just splitting them in half and doing doing this math that was n cubed. Well, this is N to the 2.8 1,
and that ends up being
asymptotically faster than than the basic divide and conquer. What do I mean by that? Meaning that for a sufficiently large value of
of N, then this ends up becoming becoming a faster method, and
repeating what I've said before on that, even though this is only
tiny bit better than N. Cubed, it ultimately ends up with significantly less calculations. If we look at a hundred by a hundred matrix.
we would calculate a million calculations right? But 10 to the 2.8 1 is only 416,000. So even though we've reduced the the power just a little bit like 0 point 1 9.
We are seeing at a at a value of of only a hundred
by of N equals a hundred. We we're seeing, you know.
of the calculations. Now imagine if this was a thousand by a thousand, you're going to see an even bigger.
an even bigger improvement. Right?
So before I move on, I'm gonna
talk briefly about the assignment. The assignment for next
for assignment 2 is implementing Straussen's matrix multiplication.
After I get done with closest pair of points, I'll go through and show you how to do the how to do the tests and how to use the starter code. But your your assignment is to take the naive
matrix multiplication algorithm that I've given you and convert it into Straussen's. And the way that you do that is, instead of having the. So I have recursive calls for all 8 of these. You just need to implement what's on this slide?
To to to do the matrix multiplication.
using only 7 recursive calls instead of instead of 8.
It's a. It's designed to be a much, much less code writing than assignment one.
So you're really, if you get too deep.
pull up and and and rethink because you're really just changing the the recursive recursive calls.
So it's due next Saturday.
but I expect you to be able to to get that done, reach out if you have any pro any questions.
So
and like I said, I'll show you the code here. Once I get through closest pair of points, because that's the
the you know the content. I gotta get through today.
I don't want to be rushed through this
As I mentioned at the front of lecture. It's very common in computer science to try and find the
closest pair of values. Given a given a data set.
And by data set. I'm going to be referring to right in the basic form Xy coordinates. And
you are often given, you know, a huge huge set of points. And you need to know, hey, which 2 are the closest. A couple of of tangible use cases here.
recommendation engines and clustering in out in analytics often are comparing millions of millions of rows of data. And you want to know,
who is this person most like. So here's an example.
A Netflix recommendation.
I am Kevin, and I have.
A really, really really wide array of all of the movies that I've liked or disliked, so
it can be a million.
a million values, this movie, this movie, this movie, this movie, 1 0 1 0 1 0. Or it can even be my rating 0 through 5. And
Netflix wants to recommend another
another movie to you. So what it will do. And this is an oversimplification. But it'll look at all of the people's recommendations, and try and find another person
that has a very similar
similar set of of choices. Right? They're they're close. If you were to plot all of those choices on a, you know, multi dimensional graph. You would see that hey, person A and person B are close. This other person is the closest, closest together.
Take any recommendations that are
that the second person has liked, and provide it as a recommendation to the other person. If they haven't haven't watched that before. So you're you're taking huge data sets and trying to find similarities. And that's computationally complex. So we have algorithms that make that make that easier.
Another example is, you're playing a video game, and you're walking around a room. And the
the object that is closest to you highlights.
Well, you're scanning for all of the objects in the room around you in like real time. Right? So you need to be able to say, hey? Which is the closest thing to highlight. And you use an algorithm similar to this to to make that to make that work.
So we're gonna simplify. This does generalize to be multi-dimensional. But we're gonna simplify it to be just
just an XY coordinate. So it's 2 points on a plane.
We're going to be given a set of N number of these points, and we need to identify the 2 points that are closest together.
So in order to do that we have to establish like, what does it mean to be close together? And we're just going to keep it simple. And for now, and talk about Euclidean distance, which is just the you know.
the
hypotenuse of the right triangle that is formed by these 2 points. Right? If you remember from from high school. You've got your distance formula, which is delta x squared plus delta y squared.
And then you take the square root of that
one pro tip. Here is that
for calculating the distance, you don't actually need to take the to calculate relative distances. So the distance of these 2 points, compared to the distance of these 2 points which one's bigger, you don't have to take the square root.
The square root is actually a pretty expensive operation compared to compared to addition and subtraction and multiplication. As a matter of fact, I don't think any of you maybe
have calculated a square root before.
Right? It's it's computationally intensive.
it's computers still do it pretty fast, but it is an expensive operation, especially if you're having to do it millions and millions of times, so you can get away with not having to do the the square root operation. Now, if you needed to know. Okay, you found the closest pair of points. What's their distance? Then you can do the square root on just that one pair, but when doing the comparison, the square root is is unnecessary.
so how would we do this? Using a kind of a brute force method method.
we would take the current minimum, set it to infinity.
I initialize the closest points. And then for
I and J, so we're going for every single point
in in the input compared to every other point in the input and do the distance formula, and if the distance between those is smaller than the current minimum, then set the current minimum to D and capture those 2 points as your closest points.
Well, that is n squared.
We can do better. The intuitive reason for how we can do better is
when we have these things plotted. And we're checking brute force every point by every point. You're comparing this point to this point and this point and this point, even though there's points that are way closer to it. So like, why would you even bother evaluating the calculating the distance between this and all the other points?
Let's make this more locally focused. So you can reduce the the search space for each point. You only have to look at the points around it.
So this is super clever. I really love this one. So the idea is to divide the points in half. So we create some sort of vertical line, and then you compute the closest pair on each half.
So you're only looking at things that are close to it. Because obviously, if you have a point that's over here, it's going to be further away than points that are on the other side of the line.
Hmm!
The the cleverness, though, lies in dealing with the situation where
you've got a line. Well, if you're not comparing this point here to this point here, this one could be closest.
because you're cause it's just barely on the other side of the line. So you have to have kind of a special case for dealing with this boundary
and using some some geometry and some logic, we can make that fast.
Okay, so let's walk through what this looks like.
So when we choose the split.
we want the points to be fairly, equally sized. So you start by sorting the values of along the X-axis. So your array is going to be this point, then this point, then this point, then this point, then this point you know, so on and so forth, and then you take the median of of
of that set.
So it's the the midpoint, so it could be all the way over here. It could be all the way over here. You don't know.
You just know that, hey? We've got equal equal number of points on both on both sides.
You then
given those 2 sets you call you, you calculate the shortest, the smallest distance on both sides of the split, and these are going to be marked as as d. 1 and d. 2.
So
given the 2 2 sides, the closest pair of points on both sides is d. 2 on the on the right side, and d 1 on the left.
and
So I kind of mentioned this a couple of minutes ago.
We have the the we have the the pair that is the smallest distance on either side, but we have the situation that this pair could be closer
than either than either one of these.
So
so we're going to have a kind of additional step in this algorithm to to do that comparison?
To to do that, we take the the minimum distance between d, 1 and D 2. What's the min between these? And we can do that easily, because yep, it's the the min of of d 1 and d 2. That's correct, Janine, because
if d 1 is smaller than d. 2. Then we know that d 2 isn't the closest pair, so we just throw it away. So we we are in the next step we know.
Given what we know of the points that we've evaluated. The shortest distance is d 1.
And so now we can look at just the boundary
around Xq, which is our midpoint. And look
only at at values that are a distance of D away from from that line.
because if there was ever a point that was further away than D.
It can't be closer than D to any point on the other side, right? This is just geometry values over here. You can't. It's it's it's even if it was a straight line, right? It would be exactly equal, in which case it would be D,
and we would have already identified that as the as the closest pair. Right if there was a point
on this
on the left side. That was, if 2 points on the left side were closer together than D.
Well, then, we would have done it wrong, because it's the minimum
The minimum distance on the left side is going to be D, so we know that no 2 points on the left are going to be closer
than than D, so we're only having to compare the left side to the right side.
Okay, is that is that clear?
Okay, perfect.
So we have another couple of of of properties. So
I've drawn this as a as a grid. Very specifically. So, we know that, given this grid
that no box can contain more than 1 point.
because if 2 2 dots were in the same same box they would be smaller than D, because the furthest distance in each box right is, you know.
you know, one plus one or one squared plus one squared.
a squared plus b squared equals C squared. So this distance becomes the square root of 2, which is 0 point 7. So if there are ever 2 points in this box, they would be smaller. They would be closer together than D,
and therefore
therefore it's impossible, because if they were smaller than D, then D would have been smaller in the 1st place. So they would be smaller boxes. Okay?
So we know that that
each box can only contain one, and we also know that, given the most extreme case.
there can only be a comp a dot compared across the line within this bounding box.
right within within 15
within 15 values. So we know it can. Only it can be at most one per box.
Okay? And we know that it can only be at at
most this far away because of of geometry, right? If they were. If it was up here, then the hypotenuse would be be larger than D.
So we're given this nice property that for any given point we only need to look at at most.
a constant time set of numbers. And that set of numbers is 15.
Okay?
So this means that when we are doing a comparison like there could be millions and millions of dots here, but for each dot we only have to look at at 15. So that is a a constant number of lookups per
per point.
So that's that's that's fairly fairly quick. Right?
And so in the algorithm, we end up
so so we do a resort. So we sort these by the value of Y because we're kind of going to start at the bottom and keep working up, and we're just going to look at the next 15 values.
Now, in this very sparse graph, right? The 15 might exist up here like we're not guaranteed to have one.in each box, but we're guaranteed that at most we have to compare as 15, so we could be comparing one to here, one to here, one to here, one to here, but we're only going to compare 15 and then move on.
So we have to kind of summarize, split it into 2.
Get the minimum on both sides, then compare the then given. Given given that new new
the new bounding box of xq plus or minus d.
Compare every point to the next 15, and if you ever find a pair of points in that 15
that is smaller, then you know that that one is is smaller than D, and so, therefore that is the the new minimum.
So you do this recursively. I'm showing you, hey, this is the one step, but you end up
in practice. You compare the left side and the right side
you split, then that left and right side into smaller chunks and smaller chunks
until you get, you know, only a few points around each bounding box, and then those bounding boxes grow.
and then ultimately you find yourself with the smallest pair of points.
I love this algorithm. It's super super clever. I love the the aspect that you can say, well, we're guaranteed only one per box. So therefore we can just look at 15, and it simplifies the logic because you don't need to check to see you know where these are on the Xy plane. You just say, what's the next? 15?
Okay.
the the pseudocode for? For this is a little bit cryptic, but we'll walk through it.
So we are are going to keep life simple for us and kind of control the inputs, we're going to say that the Inputs inputs are, too.
2 arrays, one array representing the X values and one array
including the the the Y values. Yeah.
typically, right? You'd see these as Tuples X comma y. But we're keeping making life easy for us, and just saying an array of X and array of y.
If the size of
the number of points that are provided to this algorithm is less than 3. This is the base case we're just going to brute force. You're going to compare. There's 3 nodes, ABC, you're going to say which is closest A, B BC or Cb. And return the the shortest distance between those 2.
If we have more than 3. Then we're going to run the closest pair algorithm again on the left side or the 1st half
and the second half. So I've got this little like
function here, that is saying, split px and py into the 1st half, and then split px and y as the second half.
We then take
the minimum, so this will keep on recursing until it gets down to the brute force, and it'll it'll bubble back up once it bubbles back up, you get D,
and once you get d
you know, or you get d 1 and d 2, those are the 2 minimum distances that's these guys here. Right?
So when you have those you find D,
and then you create a a new set of of points where the but
where their X value is within one
one unit D from from the line.
And then for that set of points. So that's the all of the points that are within this bounding box.
Those points are said to be said to be said to be sorted by Y,
and so we're just going to go for every every single point. Just look to see if
you know, just look to see a few forward, if it's if it's less
actually, I think I need to change that. Yeah, I'll update the this, the slide to make it more aligned with the specific number 15 here. But
for for every point in SY.
Check the next few, and then, if the distance between those
is greater than d, then then break otherwise. sorry.
It's been a while since I've talked to the slide. Okay? So
if the distances in the X is greater than D, so
that means that they're they're farther away from each other just horizontally. So just break out. Otherwise do that distance, form distance formula between the 2 and and return it.
So this is a little bit of the abstract version of this. Let's let's talk through what the actual code looks like, because this will perhaps be be a bit more clear. So here's the the brute force method, right for every X and y, compare every everything to everyone. So this is your your N squared algorithm
where I'm returning the minimum distance and the minimum points. So this is the X and the Y. This is the the value of their distance, much shorter code.
Somebody might like this better. But, as we pointed out, it's
It's it's better to do it in the in the closest pair.
I'm realizing now that I don't have a slide, for the master's theorem on this one, so I'll include that as well to give you the exact big O notation.
But here's here's what the what the code looks like. We are using python. So we are taking P as a as a set of of Tuples.
Okay, so
Tuples of XX and y, so we're going to take the midpoint of of X and y, this is, hey? How do we split it into 2 2 equal 2 equal parts.
we're a and we're making the assumption that that list of Tuples is already sorted.
Correct. Yep, yep, yep, great! Call out.
I should probably put that in the slide here that says, Give an assorted list. P.
So we take the midpoint, and then we do the the left call and the right call, and
if the left side is smaller than the than the right side, then we capture those points, and we set the minimum point to be
this is the the value of the
the x, the the x values. Otherwise
do it on the right side.
Take the midpoint, and then for every every point in in that new set
append the points that are close. You know I need to go re
reread this one because my brain is falling out of my head. Let me take
like 20 min later today, and walk. Walk through this to give you a much more precise desk description of what this is doing, because I have
veered off from the original algorithm to do some some magic here. So I'm going to rather than fumble through this. I'm going to take a pause, because I do need to talk about the the assignment, anyway. So expect a recording later today that just walks through this specific algorithm.
Is that fair?
Sorry for not having it completely completely memorized?
These things can be tricky.
Okay, so let's talk through the assignment. Let me get into like this.
Okay, actually, let's do
oops that one.
Okay.
So this assignment. It's worth 50
key key things to to talk through. You got to have the file name be Straussens dot pi. You're going to implement a, A,
a function called Straussen's. It's going to take 2 2 matrices implemented as numpy arrays. I
I don't know if you guys have covered numpy. It's relatively easy to to learn if you need help with it, you know. Just reach out, but it's
pretty pretty trivial.
And then you're going to return the product of A and B, using Straussen's
way of breaking down the the matrices.
I've given you
2 functions out of the box. One is the recursive matrix multiplication. This works on on perfect squares. It divides the the stuff by 2 and then puts it back together in that NN cubed algorithm. I've also given you a basic smoke test, so that if you run the starter code just by itself, it will.
It will test your Straussens in kind of a quick, quick way. But I also have added, for for this cohort a new new set of tests.
and I've done it slightly differently than than the tests that I included in red, black. So in red, black I had all the tests in the same file, which becomes a bit unwieldy. It's very kind of disruptive to your, you know, focusing on on just your your class. So I have
Let me show you the Straussen's tester. So I've included this file in
in the test suite. Sorry in in the assignment. You've got a Straussen's test tester dot pi. This
function will import the Straussen's method from the Straussen's file in the same directory. Okay? So
when you're doing your testing, put, drop the Strauss. Your your implementation of Straussen's in the same folder as as Straussen's tester. And this will import your specific implementation of Straussen's. Okay.
the. And then when you run this file, it's going to create the new testing class, using your function, and then it will run the tests for for your function. So this is the starter code. It has
no Straussen's implemented. But if I come here and I run the tester.
it's going to say I failed because all 5 of the tests came back incorrect.
Okay, so this does have some decently large matrices to to calculate.
So so it for some, you know.
let you know less powerful computers. It might take a little bit longer. So I have given you this like super simple smoke test, which is only a 4 by 4.
so you can just run this file
and and get your tests done.
But when you're ready to submit, run the run, the Strauss and Tester, and that will give you your your full results.
So in the remaining time I'll talk through the details of the recursive matrix multiplication so that you see what's happening and give you some ideas on how to do this with Straussen's. Some of the notation is a little bit cryptic, so I will talk through that as well.
So we are are taking the Inputs A and B
and just forcing them into a numpy array. This is an additional step. If somebody were to have implemented A and B as a two-dimensional list, or something like that. So we're forcing them to numpy arrays. And then, if the size of a
the length of A is one meaning. It's a 1 by one. Then just return the that cell times the other cell a times B,
otherwise we're going to do the recursive call. So
we're taking the shape of N and dividing it by 2. So if you put in an 8 by 8, it's going to create a 4 by 4. And this is just saying, a 0 is the values up to n, so you know, 0 through 4, and then
0 through 4 for the upper left, and then this is the upper upper right quadrant or yeah
lower left, and then lower right. So this is the split up of a
this is the split up of B
upper left. So this is just that that that index notation. From python.
And then
we are going to be calculating the C, 1, 2, 3, and 4, or sorry. 0 1, 2 and 3. And if you look at the slides right, if we go back to the
to the slides.
Where's that? It's probably like in like.
there we go.
So C is put together with the upper left
times, the upper upper left times, the upper left plus the upper right times, the bottom left.
So
C ends up getting put together in this way. And so that's what my code looks like here, right? We're multiplying B naught times a naught. Times, B, naught. And then a 1 times B, 2. So this corresponds like almost directly right.
So
after we get all 4 of those responses of C. 0 all the way through C. 3, we then this is again Pythonic magic where we're using numpy just to to stack them together. So we're putting c 1 and C 2, horizontally together, and then we're putting C 2 and C 3 horizontally together, and then we're vertically stacking the top and bottom and returning that. So that's the
that's the syntax, using the using numpy arrays to to break apart and put back together these things. So your assignment is to basically take the, you know. Break them down.
However, you, however you want, but they do break down the same way.
and then put the recursion back together, using calls to Straussen for the recursive calls and the specific
matrices that need to be multiplied together, using using using this.
and then you put them back together the additions and stuff
here. So calculate these matrices and then put them together, using this the
addition. So if you have a numpy array plus a numpy array
it, you can just use the plus operator. So BP, plus s
is matrix plus matrix. So that works. So you don't have to implement a matrix addition that's already done for you.
So any any questions about the about the assignment?
Alrighty?
Very good. All right. That wraps us up for for today.
Remember, you've got a quiz due and
the this assignment is posted. It's due next Saturday. Reach out. If you have any, have any problems, I'm gonna take a 10 min break and then I will jump on office hours just shortly after shortly after 12. So if you join at 12, and I don't let you in right away, just, you know. Give me a few minutes. I gotta go take care of something.
Very good, awesome. Thank you all.