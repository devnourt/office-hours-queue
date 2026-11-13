# User stories: Office Hours Queue

Week 4, Agile Software Development. Team details and the submission checklist are in `README.md`.

## Why we picked this problem

Office hours get crowded when a group of students shows up at the same time. One student is being helped and the rest are standing outside with no idea when their turn is. Some leave, some ask again later, and the instructor has no list to work from.

The queue is small on purpose. A student writes a short topic, joins, and can see their place. The instructor works down the list in order. That is the whole product for this sprint.

## Roles

- Student: joins the queue and follows their own entry.
- Instructor or TA: opens the session, calls students, closes it.
- System: applies the queue rules and calculates the estimates.

## Scope

US01 to US12 are the MVP. US13 to US15 are stretch stories. We will only take them if the MVP is accepted with time left.

## US01. Open Office Hours Session

Instructor. MVP. 3 points.

As an instructor I want to open an office-hours session, so students can start joining the queue.

Acceptance criteria:

- With no session open, the instructor can open one and it becomes Open.
- Once it is Open, students can see it and join.

## US02. Close Office Hours Session

Instructor. MVP. 2 points.

As an instructor I want to close the session when my office hours end, so nobody new joins after I stop.

Acceptance criteria:

- Closing an open session sets its status to Closed.
- Joining is refused while the session is Closed.

## US03. View Session Status

Student. MVP. 2 points.

As a student I want to check whether office hours are open, so I don't walk over for nothing.

Acceptance criteria:

- The app shows the current status, Open or Closed, and it matches what the instructor last set.

## US04. Join Queue with Topic

Student. MVP. 5 points.

As a student I want to join the queue with a short topic, so the instructor knows what I need before calling me.

Acceptance criteria:

- I can join only while the session is Open and I have no active entry.
- The topic is required, and the field is kept short.
- After I join, one entry is created and my position is shown.

## US05. Prevent Duplicate Queue Entries

System. MVP. 3 points.

As the system I want to block a second active entry for the same student, so nobody holds two places in the queue.

Acceptance criteria:

- If I already have an active entry in the open queue, a new join attempt is rejected and my original entry and position stay as they were.

## US06. View Queue Position

Student. MVP. 3 points.

As a student I want to see my position in the queue, so I know when my turn is coming up.

Acceptance criteria:

- While my entry is active, my position is shown as a number.
- When the queue order changes, for example someone ahead of me leaves, my position updates.

Depends on US04.

## US07. View Estimated Waiting Time

Student. MVP. 5 points.

As a student I want an estimated wait, so I can decide whether to stay or come back later.

Acceptance criteria:

- The estimate is my queue position multiplied by the average service time.
- If there is no average yet, the app says the wait is unknown instead of showing zero.

The average is the part we are least sure about. In a first session nothing has finished, so there is no number to average, and we don't want to make one up.

## US08. View Waiting Students and Topics

Instructor. MVP. 3 points.

As an instructor I want the waiting students and their topics in front of me, so I can prepare for each one before calling them.

Acceptance criteria:

- Waiting entries appear in queue order, not alphabetically.
- Each row shows the student and the topic they wrote.

## US09. Call Next Student

Instructor. MVP. 3 points.

As an instructor I want to call the next student, so the queue moves forward in order.

Acceptance criteria:

- With at least one student waiting, Call Next marks the first waiting entry as Called.
- A student who is already Called cannot be called again as the next waiting entry.

We read "next" as the first waiting entry. Calling someone out of order is not in this story.

## US10. Mark Student as Done

Instructor. MVP. 3 points.

As an instructor I want to mark the student I just helped as Done, so the queue can move on.

Acceptance criteria:

- A Called entry can be marked Done.
- After that, the positions of the remaining entries are recalculated.

## US11. View Queue Entry Status

Student. MVP. 2 points.

As a student I want to see whether I am Waiting, Called or Done, so I know what is happening with my request.

Acceptance criteria:

- My current status is shown on my entry and changes when the instructor calls me or marks me Done.

## US12. View Session History

Instructor. MVP. 3 points.

As an instructor I want the list of students I already served in a session, so I can check who I saw and what they asked about.

Acceptance criteria:

- Completed entries for the session are listed, oldest first.
- Each entry shows the student and the topic.

History is per session. Showing every session together is not part of this story.

## US13. Cancel Own Queue Entry

Student. Stretch. 3 points.

As a student I want to leave the queue before my turn, so I don't hold a place I am not going to use.

Acceptance criteria:

- While I am Waiting, I can cancel and my entry leaves the active queue.
- The students behind me get their positions updated.

## US14. Tag Common Questions

Instructor. Stretch. 5 points.

As an instructor I want to tag topics, so I can spot the questions that keep coming back.

Acceptance criteria:

- A tag can be attached to a queue entry and is saved with it.
- The same tag can be reused on other entries.

## US15. Anonymous Queue Display

Student. Stretch. 5 points.

As a student I want other students' names hidden on the public display, so the queue doesn't expose personal information.

Acceptance criteria:

- Students see the queue without other students' names.
- The instructor view still shows the names.

We argued about this one. Hiding names everywhere would make the instructor's job harder, so the hiding is only on the student side.

## Decisions we made while refining

- "Active" means Waiting or Called. Done entries do not block a new join.
- The topic is required. We have not fixed a character limit yet, only that it stays short.
- Positions are recalculated when an entry leaves the queue, not on a timer.
- Right now every queue screen shows names. US15 is what changes the student-facing one.

## Questions still open

- US02: what happens to students already waiting when the session closes? For now we assume they stay and can still be served, but nobody new joins.
- US07: where does the average service time come from in the first session?
- US09: if the called student does not show up, is there a way to skip them? Not in the current stories.
- US12: how long is history kept? We have not decided, and it may not matter for the MVP.

## Rules the stories depend on

- One active place per student in an open queue.
- Estimated wait = queue position x average service time.
- When an entry is completed or cancelled, the positions behind it are recalculated.
- Joining only works while the session is Open.
