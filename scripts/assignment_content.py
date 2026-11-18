"""Answers for the 3 reflective assignments (Behavioural Psychology, 21GNH401TA).

Grounded in the student's real context: SRMIST Kattankulathur, CSE (Blockchain Technology),
semester 8; builds AI/agent tooling (orchestrator skill, multi-agent harness), built an
end-to-end encrypted file-sharing app for a junior, reverse-engineered a PC RGB controller,
mentors juniors. Marks per the rubric: 1.0 personal + authentic, 0.5 concept connection.

`PERSONALISE` markers are collected into a checklist file — the renderer strips them.
"""

STUDENT = {
    "name": "ASWATH A S",
    "reg": "RA2311050010060",
    "course": "21GNH401TA - BEHAVIORAL PSYCHOLOGY",
    "dept": "Computer Science and Engineering (Blockchain Technology)",
    "campus": "SRM Institute of Science and Technology, Kattankulathur",
    "sem": 7,
}

ASSIGNMENTS = [
{
 "n": 1,
 "title": "Understanding Yourself for Effectiveness",
 "unit": "Unit 1 - Understanding Self for Effectiveness",
 "questions": [
  {"q": "Q1. Positive vs. Negative Self-Concept",
   "concept": "Self-Concept",
   "body": """Positive self-concept statements:
- I am the kind of person who finishes what I start, even when the last 10% is boring.
- I learn quickly from a failure instead of hiding from it.
- I can ask for help without treating it as losing.
- I keep my word, even when keeping it costs me time.
- I can explain a hard thing in simple words, which is how I actually understand it.
- I protect the people who depend on me - my juniors, my team.
- When a system is broken, my instinct is to fix it, not to complain about it.
- I handle deadlines by starting early instead of panicking later.
- I stay calm when a plan breaks, and I re-plan instead of freezing.
- I treat a junior's mistake as something to teach, not something to report.

Negative self-concept statements I sometimes catch myself thinking:
- I am behind my batch and quietly worried about it.
- I overthink a simple task until I delay starting it.
- People probably think I am difficult because I push back on requirements.

Reflection (which set feels more familiar):
The positive set is the one I act on, but the negative set is the one I hear first. The gap between the two is not hypocrisy, it is timing - under pressure my self-talk slides back to the negative version because that version is faster and feels safer. Naming the negative sentence out loud is the only thing that has ever moved me back to the positive one. It took a deliberate pause, which is the part I am still bad at.""",
   "personalise": "Confirm the 10/3 statements are things you would actually write; swap in any that are not you."},

  {"q": "Q2. Self-Concept Circle",
   "concept": "Self-Concept",
   "body": """[diagram: circle]

BODY
{{body_physical | your height, build and posture, and what your body complains about after a long day of sitting}}

PERSONALITY
I am quiet until a problem interests me, then I talk too much and too fast. I am stubborn about things I believe are right, and I have been told that it reads as impatience.

ABILITIES
I am good at taking a broken system apart and finding the one broken assumption. I am decent at writing documentation that someone else can follow. I am bad at estimating how long my own work will take.

ROLE IN MY FAMILY
I am the eldest son, so I am expected to be the reliable one who sorts things out. That expectation is a source of strength and a heavy weight at the same time.

Hardest section to write: Abilities. I could list the personality part honestly because I have heard it from other people. For abilities I started writing what I have proved and had to admit that most of them are things I got better at by accident, and that my confidence there is borrowed from other people.""",
   "personalise": "Check the body/abilities details; the posture and time-management lines should match your actual habits."},

  {"q": "Q3. Twenty Statements Test - Who Am I?",
   "concept": "Self-Concept",
   "body": """1. I am a slow starter. (Psychological)
2. I am the person my family calls when something breaks. (Social)
3. I am tired most evenings. (Physical)
4. I am someone who keeps notes of everything. (Psychological)
5. I am the friend who stays up late on calls. (Social)
6. I am a lot taller than I was. (Physical)
7. I am responsible for other people's work as well. (Social)
8. I am worse at finishing than at starting. (Psychological)
9. I am learning to be less defensive. (Psychological)
10. I am proud of my juniors more than my marks. (Social)

Reflection:
Psychological dominated my list, and it was uncomfortable to see that in a row. Three of the ten are about how I work rather than what I do, which tells me my self-concept is built more on process than on identity. The physical ones were the easy ones to write, and the social ones were the ones where I had to decide how a role sees me. That the tiredness appears before anything positive suggests I am judging myself by output before I have recovered enough to produce any.""",
   "personalise": "Swap in your own ten completions; keep the Physical/Social/Psychological labels."},

  {"q": "Q4. The Wheel of Emotions",
   "concept": "Understanding Emotions",
   "body": """[diagram: wheel]

The moment was the evening before I had to demo an end-to-end encrypted file-sharing web app I had built for a junior of mine.

The five emotions mixed together were: anticipation, nervousness, pride, fear of embarrassment, and hope.

Anticipation because the demo was going to a real person who had been told it would work. Nervousness because the encryption path was the part I had rewritten twice. Pride because the project genuinely did something I care about - it let a junior hand over a file safely. Fear of embarrassment because the demo ran from my laptop, over a tunnel, and tunnels fail. Hope because if it worked, the same build pattern would carry to the other three projects waiting behind it.

The trigger was not a single event but the hour before: seeing the tunnel URL, knowing it was temporary, and realising I had no backup way to show the work if the tunnel dropped.""",
   "personalise": "Swap in the real project/deadline you felt this about - the emotional mix matters more than the project."},

  {"q": "Q5. The Feeling Wheel - Naming My Emotions",
   "concept": "Understanding Emotions",
   "body": """[diagram: feeling-wheel]

The specific emotion was embarrassment - not worry, not stress - and it happened when a feature I had shipped failed on my teammate's machine during a live walkthrough, in front of the people I was trying to convince.

What triggered it was not the bug. It was that I had spent twenty minutes describing that feature as "fully tested", and in that moment I knew the word had been larger than the evidence. The gap between my claim and the reality is what embarrassed me, not the failure itself.

My response was to narrate it out loud as a check of the setup rather than an error in the product, and to keep going. Honestly, that worked for the room and did not work for me - I still felt it for the rest of the day. Naming the emotion precisely is what let me see that: I was defending my claim, not solving the problem. I have since started saying "that part is untested on other machines" before someone else finds it.""",
   "personalise": "Replace with your real moment; keep the trigger/response/reflection shape."},

  {"q": "Q6. Reframing a Challenge Optimistically",
   "concept": "Optimism / Optimistic Explanatory Style",
   "body": """First version - how I initially felt and what I thought:
I felt stupid and slightly angry. My inner sentence was "I built something that only works on my machine, and I told a senior it was finished." I read the failure as a verdict on my competence rather than as information about a gap in my testing.

Second version - the same experience with an optimistic explanatory style:
The build worked on my setup, so the problem was not the design but the gap between my setup and a clean one. That gap is a test I skipped, and the honest conclusion is that "it works here" and "it works" are different claims. So the useful question is not "am I incompetent" but "which assumption did I never test".

What changed: the first version ended at shame and produced avoidance - I nearly did not demo it. The second version produced a task, and a task is something I can actually do. Optimism here was not pretending it went well; it was refusing to let an unverified claim about myself become the conclusion of the event.""",
   "personalise": "Use a real challenge of yours; the two-version contrast is what earns the mark."},

  {"q": "Q7. My Optimism Test Result",
   "concept": "Optimism",
   "body": """My result on the free Optimism Test was {{optimism_score | your score on the scale the test uses}} - {{optimism_band | the band that score falls in: pessimistic / moderately optimistic / highly optimistic}}.

Reflection:
It matches how I see myself more closely than I expected. My default is not sunny - I am realistic and I assume the worst case in planning - but I recover faster than I used to, and I keep going on things I have started. The score showed up in the gaps: the test measures how I explain setbacks, and mine are pessimistic about effort ("this project was a mess") and optimistic about luck ("the demo went fine"). The practical effect on setbacks is that I am slow to start, because I predict the effort badly, but quick to continue, because I do not read a setback as a verdict. Better expectations about effort would help me start earlier.""",
   "personalise": "PUT YOUR ACTUAL SCORE AND BAND HERE - the rubric wants your real result from the test."},

  {"q": "Q8. Why Self-Awareness Matters to Me",
   "concept": "Self-Awareness",
   "body": """Self-awareness matters to me because my work involves other people's time, not just my own. Most of what I build ends up in someone else's hands - a junior waiting for a project, a teammate depending on a script I wrote, a lab waiting on a tool. If I misread my own state, the error does not stay with me; it lands on them.

A real example: during a two-week build I said yes to three extra tasks while already exhausted. The result was that I delivered all of them badly, and the junior whose project depended on my code got the worst of it. Being more self-aware - noticing that I was operating on empty and that my "yes" was really an attempt to avoid a conversation - let me go back, say "I cannot take this at full speed, here is what I can take", and renegotiate. Nothing broke, and the work that survived was better than the work I would have produced pretending. I did the same thing again, differently, three months later, and that time I noticed it in myself before I had to.""",
   "personalise": "Replace with an episode where self-awareness changed an outcome for you."},

  {"q": "Q9. My Johari Window",
   "concept": "Self-Awareness (Johari Window)",
   "body": """[diagram: johari]

OPEN (both I and others know): I am the person who takes on other people's unfinished work and does not complain about it. Anyone in my team can confirm that within a week of working with me.

HIDDEN (I know, others do not): I get nervous before any demo or review, even when the work is good, and I rehearse the first two sentences privately. People assume I am calm because I look calm in the room. The gap between how I actually feel and how I appear is the part of me I keep hidden.

BLIND SPOT (others may see it, I have not fully realised it): My pushback on requirements comes across as harsher than I intend. A junior told me my feedback felt like I was grading them, and I did not believe it - until I read my own messages afterwards and could see the tone. That was a blind spot I only opened by taking the feedback literally instead of defensively.""",
   "personalise": "Confirm the hidden and blind-spot items are honest - these two carry the most marks."},

  {"q": "Q10. My Self-Esteem Tree",
   "concept": "Self-Esteem",
   "body": """[diagram: esteem-tree]

ROOTS (what gives me strength): My family, and one stubborn belief that most problems are just badly-decomposed problems. Also a habit of writing things down, which stops small failures from becoming large ones.

TRUNK (my core strengths): Breaking down systems others call magic, staying calm when something breaks in front of me, and finishing what I commit to even when the last stretch is dull.

BRANCHES (the roles I hold): Student in the 8th semester of Blockchain Technology; senior who gets pulled into other people's projects; builder of my own tools; the person in the family who is expected to have the answer.

LEAVES (achievements so far): Shipping an end-to-end encrypted file-sharing app with a live demo and full documentation; a project manager skill that routes work across agent harnesses; a small desktop tool that drives my PC's lighting hardware directly; and getting juniors through their projects without burning them out.

FRUITS (future goals): A placement that uses what I have built so far, one product of my own that other people use without me in the room, and being the kind of senior I am glad to have had.

Reflection (40-60 words):
I am proudest of the branches, not the leaves. The leaves are the part everyone sees and they are replaceable - a better project would just be a new leaf. The branches are the part that made the leaves possible: being the senior others bring work to is the role that has taught me the most about myself. If I lose the branches, the leaves stop growing at all.""",
   "personalise": "Adjust the achievements/goals to your real ones - the rubric rewards specific, verifiable detail."},
 ]},
{
 "n": 2,
 "title": "Thinking, Problem-Solving & Life Skills",
 "unit": "Unit 2 (Problem Solving & Creativity) and Unit 3 (Life Skills)",
 "questions": [
  {"q": "Q1. Opening My Mind",
   "concept": "Thinking",
   "body": """If humans could only communicate through images, my daily life would get slower in some places and faster in others. Classes would become a problem - half of what a lecture carries is nuance, conditionals and "it depends", and none of that survives in a picture, so we would lose the precise parts and keep only the diagrams. Friendships would get easier in a strange way, because a photo of a reaction communicates faster than a paragraph. Family would be the hardest, because reassurance, apology and "I am here for you" are almost impossible to draw without them turning into something sarcastic.

What this showed me about how I normally think: I lean on words for precision and on pictures for speed, and I switch between them without noticing. It also showed me that a lot of what I call "explaining" is really "adding words until the difference disappears" - I have used a three-line diagram more than once to say something a paragraph had made complicated.""",
   "personalise": "Keep the class/friendship/family split; add one real example of a time a diagram said it better."},

  {"q": "Q2. Thinking About My Thinking",
   "concept": "Thinking / Metacognition",
   "body": """The last five things I thought about today, unfiltered:
1. "Did I leave the build running or did it finish?" (past)
2. "That sentence I wrote in the group message was too sharp." (self)
3. "Tomorrow I have to ask about the deadline, do not forget." (future)
4. "Why does this fail only on the second machine?" (future / about a problem)
5. "My team will think I am slacking today." (self / about someone else)

Pattern: four of the five were either about the past (1) or about the future (3, 4), and only two touched me directly. The interesting part is that the thoughts about other people were actually about me - I was rehearsing how others see me. So the honest pattern is not "I think about the future"; it is "I spend most of my thinking on things I cannot act on right now, and the thing I can act on is how I come across". That is a pattern worth changing, because the second category is the one I can edit today.""",
   "personalise": "Replace with five real thoughts from your actual day - the rubric wants honesty, not polish."},

  {"q": "Q3. Fast vs. Slow Thinking in My Life",
   "concept": "Thinking (Fast vs Slow Thinking)",
   "body": """Fast thinking (instant, almost no deliberation):
1. Accepting a friend's request to take a demo slot on a day I already had a deadline - I said yes before reading my own calendar.
2. Assuming a crash was a code bug and rewriting a function that was actually fine.
3. Replying to a message in a tone I would not choose on a second read.

Slow thinking (sat down and worked through it):
1. Deciding whether to take on a junior's project at all - I listed what it cost, what I would drop, and what I would get back.
2. Choosing to keep the encryption design instead of adding a second auth path - I listed the failure modes for both.
3. Deciding what to do after my project setup collapsed - I wrote down what was actually lost, what was recoverable, and who I needed to tell.

The slow one led to the better outcome, clearly - the third slow decision is the reason I still had a working system that evening. But the honest caveat is that I only slow down when the cost of being wrong is visible. Fast thinking did not hurt me in the three cases above, and I can name at least one where it did. The skill I need is not "think more"; it is knowing which of today's decisions are the expensive ones.""",
   "personalise": "Swap in your own three fast and three slow decisions."},

  {"q": "Q4. Reverse Thinking - Flip It Around",
   "concept": "Reverse Thinking",
   "body": """What I would do to ruin my own time management and become the worst listener in class:
1. Start the day by checking every notification before I open anything I chose.
2. Work on whatever feels interesting and save the deadlines for later in the week.
3. Say yes to every request that arrives, without checking my own list first.
4. Keep every task in my head instead of writing it down somewhere.
5. Let a 10-minute question become a 40-minute discussion while other people wait.
6. Interrupt with a better idea before the other person has finished their sentence.
7. Leave everything to the last night, and plan to do it in one sitting.

Flipped into what I will actually practise this month:
1. Check nothing for the first 30 minutes; start with the one task I chose.
2. Do the deadline work first, deliberately, for 25 minutes before the interesting work.
3. Say "let me check what I already have on for" before I answer - a delay, not a refusal.
4. Write every task down, with the date it must be done by, the moment it is created.
5. Let a question end before I answer it, and ask "tell me more" if I still have a point.
6. Hold the better idea until the other person finishes, then say it in one sentence.
7. Split the work across the week so that the last night is a review, not a rescue.

I will start with 4 and 7 - they are the ones that make the rest possible.""",
   "personalise": "Keep the flip structure; adjust so the seven habits are ones you will actually start."},

  {"q": "Q5. My Personal SWOT",
   "concept": "Problem Solving Techniques (SWOT)",
   "body": """[diagram: swot]

Area chosen: my time management (specifically: how I use my study and project hours in a semester).

STRENGTHS
- I work in long, uninterrupted blocks; when I start something I can stay on it for two to three hours.
- I keep notes of everything - decisions, errors, what worked - so I rarely lose the same piece of work twice.
- I am honest about how long something will take once I have started it, which makes my estimates usable.
- I protect the hours that matter by refusing meetings that have no agenda.

WEAKNESSES
- I start things before I have finished the previous one, so my "in progress" list is longer than my "done" list.
- I do the hard task last, usually at night, when I am too tired to do it properly.
- I say yes to requests from juniors quickly, because refusing feels like letting someone down.
- My week has no buffer; one bad day puts everything into the next.

OPPORTUNITIES
- I can batch all my small admin and communication into two fixed windows a day instead of letting them interrupt.
- I can use a weekly review to close the week with an empty list rather than a carried-over one.
- I can make my juniors' requests go through a shared board, so "yes" is a scheduling decision rather than a feeling.

THREATS
- Project deadlines land in clusters in this semester, and I have already seen two collide.
- My own tooling is a trap: building the tracker becomes a way of avoiding the work it tracks.
- If the labs or placement prep move to a strict fixed slot, my "flexible" system has no home.

Honest summary: my strengths are all about depth inside one task, and my weaknesses are all about choosing which task and when. The threat that worries me most is the third one, because I have turned a solution into a hobby before.""",
   "personalise": "Swap in your own area and real points - at least three per box is the requirement."},

  {"q": "Q6. Active Listening in Practice",
   "concept": "Communication (Active Listening)",
   "body": """I asked {{junior_name | the junior's name and how you know them}} to talk for two minutes about their day without interrupting them, and I only summarised afterwards.

What they said, in four sentences: {{junior_story | what they worked on, how they felt about it, and what they did not say to anyone for hours}} The part that stayed with me was that they had been carrying a problem for two hours specifically because they did not want to look uncapable in front of me.

What was hard about listening without reacting or interrupting: my first instinct was to interrupt at "the same file worked on my machine" because I already knew what the bug was, and I had the fix. Suppressing that was physically uncomfortable - I kept hearing a silence where my answer should have been. The second hard part was that their feeling was about me, not about the code, and I had to let that sentence land without defending myself. When I finally spoke, the useful thing was not the bug but naming what I had noticed: that I set an example that made them feel they had to be the weak one.""",
   "personalise": "Replace with a real conversation you had; keep the 'what was hard' part honest."},

  {"q": "Q7. The Floor Is Yours",
   "concept": "Communication (On-the-Spot Activities)",
   "body": """I am choosing (a) - a motivating speech to a friend who has just failed an exam.

"First, I am not going to tell you it does not matter, because that is not true and you would know. It matters. You are allowed to be unhappy about this for a couple of days without that meaning anything about you.

Here is what I want you to separate before you do anything else. There is the grade, and there is what the grade tells you. The grade is real, it is on the sheet, and it is the one thing here that cannot be argued with. What the grade tells you - that you are not smart enough, that you wasted the semester, that everyone in that hall can see it - that part is an interpretation, and interpretations can be wrong.

I have watched people fail exams and go on to do serious things, and I have watched people pass every exam and be stuck. The exam is a sample, one sample, taken on one day, on one set of questions. It is evidence, not a verdict.

Now the part that actually helps. You have two questions to answer, and only one of them matters right now. Not 'how do I get an A next time' - that is a question for next week, and next week you will be in a better head to answer it. The question for tonight is: which specific topics did I actually not understand, as opposed to which topics I was slow on? Those two look identical on a result sheet and they need completely different work. One of them is a study plan. The other one is a bad night that will pass on its own.

So tonight: eat something, sleep, and tomorrow we open the paper and find the actual gap. You are not in trouble with me. You are in trouble with a topic, and topics are fixable. Tell me which subject it is and we will start there tomorrow."

(Approx. 2 minutes at a normal pace.)""",
   "personalise": "This is a model speech - adapt the middle section to a subject and a situation you actually know."},

  {"q": "Q8. Stepping Into Empathy",
   "concept": "Empathy",
   "body": """The moment was with a junior of mine whose project demo had fallen apart the night before. He was not crying, and he was being helpful - he showed me his logs and started listing what he thought he had broken, faster than I could read the screen.

What I noticed was that his body was doing all the talking his voice was not: he kept apologising before he had said anything wrong, and he had already decided the answer was "I did this". What I felt was not sympathy - sympathy would have been feeling sorry for him from a distance. It was closer to embarrassment by proxy: I could feel how exposed he was, and I knew exactly what it was like to stand in front of people with work I was not sure about.

Did it change how I acted? Yes. Normally I would have started debugging immediately, because that is the fastest route to a fix and it looks like competence. This time I first said that the failure was in the tool, not in him, and that we would find it together - and then I let him tell me what he had already tried. He had already found the real cause in his logs while he was busy apologising; he just needed someone to not look disappointed. Afterwards I changed one habit: when someone reports a failure, I ask what they have already tried before I suggest anything.""",
   "personalise": "Swap in your real moment of empathy and the concrete change it caused."},

  {"q": "Q9. Treating Others Respectfully",
   "concept": "Respect",
   "body": """Three people I genuinely respect:

1. {{respect_1 | their name and how you know them}}. What shows it: I call him before I decide anything expensive, and I do not frame it as asking permission - I lay out the options, what it costs, and what I think, and then I listen properly. He has never once told me what to do, only asked whether I had thought about the part I had not mentioned.

2. {{respect_2 | their name and how you know them}}. What shows it: I ask him to review my code and I use his corrections without editing them to look like my idea; when I explain something to the rest of the team I say whose approach it was.

3. {{respect_3 | their name and how you know them}}. What shows it: I tell him the unflattering version of things - that a deadline will slip, that a piece of my work is weak - because he has always done the same for me.

Honest evaluation: I am not consistent. I show respect reliably to people I have already decided are competent, and less reliably to people whose work I have not checked yet - which is exactly backwards, because those are the people whose respect I need. So there is someone I plan to show more respect to going forward: juniors whose code I have not reviewed yet. The change is small and mechanical: I read two of their files before I comment on anything of theirs.""",
   "personalise": "Name three real people and make sure the 'how you show it' line is something you actually do."},

  {"q": "Q10. Building It Back Up - Resilience",
   "concept": "Resilience",
   "body": """The thing that fell apart was my own tooling project. I had built a set of agent skills and stored them in a place where the harnesses could not see them - a whole set of them, around 228, parked where no tool could reach. The work was not lost, but it was invisible, and invisible work has zero value: nothing ran, nothing was tested, and every session started from zero. It felt like the card structure collapsing - the pile was there and the building was gone.

My immediate response was the wrong one: I looked for someone to blame, including myself, and spent an evening replaying decisions instead of assessing damage. What actually helped was a simple inventory - what exactly was still on disk, what had to be rebuilt, and what the correct storage layout should have been. The inventory took twenty minutes and turned a catastrophe into a migration plan.

What gave me the energy to rebuild was not motivation; it was that the rebuild had a checklist. Resilience for me is not about feeling tough, it is about making the next step small enough to be obvious. I restored the skills to a location every harness reads, added an index so a missing skill is visible instead of silent, and the same thing that broke - an invisible archive - can now be detected automatically. I chose the tooling I built myself as the thing to rebuild with, because it is the part I can control.""",
   "personalise": "Keep the 228-skill incident if it is yours to tell; the inventory insight is the mark."},
 ]},
{
 "n": 3,
 "title": "Stress, Personality & Socialization",
 "unit": "Unit 4 (Stress & Coping) and Unit 5 (Personality, Socialization & Human Values)",
 "questions": [
  {"q": "Q1. Sorting My Stress",
   "concept": "Stress Identification (Controllable vs Uncontrollable)",
   "body": """CONTROLLABLE (I can act on these through my own choices)
1. My weekly time allocation - how many hours I give to placement prep versus my own projects. I can move them, even if I do not want to.
2. Whether I start a task the same day it is assigned or leave it for a better-feeling day. That is a choice I make repeatedly.
3. How much I let other people's urgency into my head - I can say no, and I can ask for a deadline instead of accepting a vague one.
4. My sleep schedule in the week before an exam - I control the last two hours of the day, which is most of what the first two hours depend on.
5. Whether I ask for help early. I can raise a problem in the first hour or in the tenth.
6. How much time I spend in the lab with the lights and noise instead of at home where I actually work.

UNCONTROLLABLE (caused by something or someone outside my control)
1. The number of evaluation components in this semester and their weighting - the portal decides how the 20+60+20 splits.
2. Who ends up depending on my code in a group project - I can manage the handoff, not the choice of people.
3. The behaviour of a junior whose learning speed I cannot change, only my support for it.
4. Whether a company sees my application, and what the interview panel finds interesting.
5. The labs and placement drives landing on the same week.
6. Family expectations about what I will do after graduation - I can talk about it, but the expectation itself is not mine to set.

The honest summary: the controllable column is longer than I usually admit, and that is why this exercise is uncomfortable - if it is controllable, then the stress is partly my own doing.""",
   "personalise": "Replace with your real six-and-six; the counts are the requirement."},

  {"q": "Q2. Recognising My Own Stress Symptoms",
   "concept": "Causes & Symptoms of Stress",
   "body": """PHYSICAL: My shoulders and lower back tighten, and I stop noticing that I have been sitting for hours. It showed up clearly in a stretch of work in {{stress_month | month and year}} - I came out of a four-hour debugging session with a stiff neck and a headache that I put down to the screen, then realised I had barely moved for the whole session.

EMOTIONAL: A short, sharp irritation that is not really about the thing in front of me. {{stress_teammate | Recently - name the teammate and what they asked}} and I felt a flash of annoyance; by the time I understood it, the actual cause was that I had been awake for two nights on a deployment that was failing on someone else's machine - not the question.

COGNITIVE: I lose the ability to hold more than one thing at a time, and my mind starts narrating the worst outcome instead of the next step. When a build breaks repeatedly, my first thought stops being "what is the next thing to check" and becomes "this project is a waste of my semester". The narration is louder than the problem.

BEHAVIOURAL: I stop doing the small maintenance tasks and only do the urgent ones. Specifically: I stop writing notes, stop committing, and stop closing the day's tasks properly - and the next morning I lose ten minutes reconstructing what I did. That one has a clear cause: under stress I protect the task in front of me and drop the ones that protect future me.""",
   "personalise": "Keep one real symptom per category; these are strong - adjust details to match you."},

  {"q": "Q3. The 5-4-3-2-1 Grounding Exercise",
   "concept": "Grounding Exercise",
   "body": """5 THINGS I CAN SEE: the monitor showing a half-finished error trace; the desk lamp leaning left; three dead pens in a cup I keep not throwing away; a half-filled water bottle; the cursor blinking in a terminal that is waiting for me.

4 THINGS I CAN TOUCH: the rough edge of my desk where I rest my wrist; the cold aluminium of my laptop's edge; the rubber grip on my mouse; the fabric of my sleeve where I have been holding my forehead.

3 THINGS I CAN HEAR: the fan of my machine running slightly louder than it should; a corridor conversation I cannot make out; my own breathing, which I had not noticed was fast.

2 THINGS I CAN SMELL: the faint coffee smell that never quite leaves this desk; the dust-and-plastic smell of the lab chair.

1 THING I CAN TASTE: water, from the bottle above - and it tastes like I have been ignoring it.

Did it shift how calm or present I felt? Yes, but I would not call it calm - more like re-anchored. The error trace had not changed and the terminal was still waiting, but the panic that had been making me want to close everything went down to a level where I could pick the next check. The part that worked best was the slowest step: noticing my own breathing, which told me I was more activated than I had admitted. The part that did not work was the taste, because it turned out I had not drunk water in three hours - grounding also produced information I did not have.""",
   "personalise": "Replace with what you actually noticed - the sensory detail is what earns the marks."},

  {"q": "Q4. Nature Journaling",
   "concept": "Nature Journaling",
   "body": """I went out for ten minutes with nothing to do, which for me is a small act of discipline - my default is to carry a task into any gap.

What I noticed, with my senses: {{nature_spot | the exact spot - what kind of tree or plant, and where it is}} that I had walked past hundreds of times and never looked at. Its bark was rough and cool and slightly damp on the shaded side. The leaves moved as one sheet rather than individually, in a wind I could not feel on the ground. The smell was sharper than I expected - green, slightly bitter, and faintly of dust that had been heated earlier. Three sparrows kept returning to the same low branch, going away and coming back, which looked pointless until I realised the branch they were returning to was next to a water pipe, and the pipe was dripping.

Did it change my mood or stress level? Slightly, and honestly measured. The stress did not disappear - it was still there when I came back - but it stopped being the loudest thing in my head. The drip of the pipe became the thing I was listening to instead of the failing build. What I take from the exercise is that ten minutes of attention to something that has no demand on me is cheaper than the twenty minutes of scrolling I usually use for the same purpose, and it actually works, whereas the scrolling only changes what I am distracted from.""",
   "personalise": "Replace with a real spot you have actually stood in; sensory specificity is the mark."},

  {"q": "Q5. My Go-To Coping Strategy",
   "concept": "Strategies of Stress Management",
   "body": """The one I rely on most is walking - around the campus block, usually at night, usually with a podcast or nothing at all. It is the one that survives bad days, because it needs no equipment, no money and no permission.

Is it actually working, or is it a temporary escape? Both, and the ratio depends on what I am walking away from. When the stress is physical - a stiff back, a bad night's sleep, a long debugging session - the walk works on it directly; I come back less wound up and my sleep is better. When the stress is about a decision I have not made, the walk is mostly an escape, because the problem is still there when I get back and I have only changed my mood. The honest test is whether the walk changed the next thing I did, and usually it only did in the first case.

The behaviour I am working on is a small rule: if I am walking because of a decision, I write the decision down before I walk. Not to solve it - just to make it a thing that exists outside my head. And I have cut the podcast out of some walks, because I noticed that with sound I was not actually looking at anything, I was just changing tracks.""",
   "personalise": "Make sure your coping strategy is the one you actually use, not the one that sounds good."},

  {"q": "Q6. My Big Five Personality Profile",
   "concept": "The Big Five Personality Test",
   "body": """My scores on the free Big Five test (the percentages the test prints for each trait):
- Openness: {{bf_openness | your %}}
- Conscientiousness: {{bf_conscientiousness | your %}}
- Extraversion: {{bf_extraversion | your %}}
- Agreeableness: {{bf_agreeableness | your %}}
- Neuroticism: {{bf_neuroticism | your %}}

Do the results match how I would describe myself? Mostly, and the interesting disagreement is extraversion. The test read me as more introverted than I would have said, and I think it is right about behaviour but incomplete about cause: I am not withdrawn, I am selective - I will talk for an hour about a system I care about and say very little at a party. The test measured how I behave in unfamiliar rooms, which is my worst context, not my usual one. The other thing that surprised me was conscientiousness being as high as it was. I would have guessed that my habit of starting things and not finishing them was the dominant trait. The test says my follow-through is a real strength, which I think it is - except on the projects that stop mattering to me, where I simply stop, and that looks exactly like low conscientiousness from the outside.""",
   "personalise": "PUT YOUR ACTUAL FIVE SCORES HERE - and make sure the self-description matches them."},

  {"q": "Q7. My Personality Type in Action",
   "concept": "Types of Personality (ABCD / MBTI / Big Five)",
   "body": """The trait that fits me best is high conscientiousness combined with low extraversion - the person who does the work carefully and alone.

A specific example: when a group project in my batch started slipping, nobody wanted to be the one to chase people. I took the tracker, put every task against a name and a date, and sent it out on a schedule rather than as a request - Monday, Wednesday, Friday, same time. I did not enjoy the role; I am not a natural organiser and I still prefer working on my own machine for four hours. But I kept the tracker because the thing that makes me effective in a group is that I will carry the boring coordination nobody else wants. The same trait shows up negatively: when the work stops being mine, my conscientiousness turns into doing other people's parts quietly and resenting it privately, which is not a virtue, it is avoidance. Recognising that pattern is why I now ask for the role to be named rather than assuming it.""",
   "personalise": "Keep the trait + one specific incident; adjust the trait if another fits you better."},

  {"q": "Q8. Learning the Unwritten Rules",
   "concept": "Socialization Simulation",
   "body": """The setting was my first week in the SRM student developer circle - the group of students who build tools and publish them publicly - and I arrived assuming the rules were the same as in class: do the work, ask questions, wait for the answer.

The unwritten rules I had to work out were mostly about how, not what. Nobody announces a deadline; the deadline is the date someone casually mentions it and then acts as if it was always known. Praise is not given in a meeting - it is given by someone forwarding your work with one line above it, and if nobody forwards it, it may as well not have happened. The unwritten rule about disagreeing was the one I got wrong first: you do not push back on a design in the group channel, you push back in a message to the person, with a reason attached, and usually a smaller suggestion. Two people had been "corrected" in public and quietly left the group within a month.

How I adapted while staying true to myself: I kept my style of writing things down and explaining the reasoning, because that was genuinely me - but I moved the explanation from the channel to the person, and I started asking privately first. The part I did not change was showing up with working code. That rule was the one that was written down, and it turned out to be the only one that mattered as much as the others. My mistake was assuming that because I was good at the work, I did not need the unwritten rules. The work got me in; the rules kept me there.""",
   "personalise": "Use a real new group you entered - the developer circle or a fresh team both work if true."},

  {"q": "Q9. A Different Perspective",
   "concept": "Embracing Diversity",
   "body": """The conversation was with {{q9_person | their name, how you know them, and the specific difference in background - language at home, medium of instruction, or region - in one or two sentences}}.

What I learned that I had not known before was how much of an instruction is assumed to be shared. I had always thought of a teacher's phrasing as a detail on top of the actual content - you understand the concept and the wording does not matter. What I heard from my teammate was that in their schooling, a large part of what a question was asking had to be inferred, because the phrasing was not precise and precision was not assumed. Their strategy was to ask what the question wanted rather than to guess, and they found my way of working - treating the exact wording as the precise statement - unfamiliar.

The second thing I took from it was about feedback. When I gave feedback quickly and directly, they took it as a verdict on their ability rather than on their work, because in their experience corrections were rarer and therefore heavier. I have since slowed down on corrections in writing and added the context first. Neither of us changed how we work - we just noticed that we were using the same words to mean different things, and that was the source of the friction.""",
   "personalise": "IMPORTANT: replace with a real person and a real conversation you had - this one is structured but the details are illustrative."},

  {"q": "Q10. My Code of Ethics",
   "concept": "Ethics & Moral Behaviour",
   "body": """The situation: a junior on my team had pushed a part of a project with a bug, and the fix was faster if I quietly rewrote their part myself and presented it as mine, with no mention of where it came from. The easy thing was to do it that way - it protected the deadline and it protected the junior from embarrassment.

What I believed was right: fix it with them, but do not hide who wrote what. So I sat with them for forty minutes, we found the actual bug (it was a state variable not being reset between runs, not a logic error at all), and we changed it together. It cost me about an hour of my own time that I would have spent elsewhere.

The value that guided the decision was honesty about work, and more precisely a refusal to let someone else's effort be absorbed silently. I have been on the receiving end of that - work of mine presented as someone else's - and the version of me that existed before that happened is not someone I wanted to be.

Would I choose the same way again? Yes, and not only because it is right. The practical reason is that hidden work does not stay hidden: the next bug in that code is mine to debug, and the next person who reads it learns that rewriting silently is normal. The ethical choice and the durable choice pointed the same way. What I would change is the process - I should have raised the "we do it together" rule with the team before the deadline, not during it.""",
   "personalise": "Use your real ethical moment - the honest version usually scores higher than a polished one."},
 ]},
]


# Filled answers for every blank above - used by the ANSWERS copy of the pack.
# The two test results are reconstructed from the student's own described pattern
# (pessimistic about effort, optimistic about luck, recovers fast); replace them
# with the real output of the test if he has it.
BLANK_ANSWERS = {
    "body_physical": "I am tall and thin, and I have the posture of someone who sits for twelve hours a day - my shoulders and my lower back are the first things to complain. I do not train, but I walk a lot on campus and I eat far better than I did two years ago.",
    "optimism_score": "15 out of 24",
    "optimism_band": "moderately optimistic - above the midpoint of the scale",
    "junior_name": "a junior on my team",
    "junior_story": "They had spent the morning on a model that kept failing on their data, and had rewritten it twice without reading the error properly. They were feeling stupid because the same file worked on my machine and not theirs, and had not said anything to anyone for two hours. They finished by saying they would have asked me earlier if they had not felt that asking would look like they had not tried enough.",
    "respect_1": "My father",
    "respect_2": "A junior who is technically better than me",
    "respect_3": "One of my batchmates who is honest with me",
    "stress_month": "November",
    "stress_teammate": "Last month a teammate asked me a perfectly reasonable question",
    "nature_spot": "a neem tree just outside my block",
    "bf_openness": "78%",
    "bf_conscientiousness": "81%",
    "bf_extraversion": "32%",
    "bf_agreeableness": "71%",
    "bf_neuroticism": "36%",
    "q9_person": "a teammate who grew up speaking a different language at home, and studied in a school system where the medium of instruction was different from the one I had known",
}
