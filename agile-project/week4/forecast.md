# Sprint forecast: Office Hours Queue

Week 4, Agile Software Development. Team details are in `README.md`.

## What we assumed

- 5 people: one Product Owner, one Scrum Master, three developers.
- One week sprint, as the course brief says.
- We have not finished a sprint as a team, so there is no velocity to use. The number below is a guess at capacity, not a measurement.
- Everyone is available except for exam days. We will confirm this in Sprint Planning; if two people are out for most of the week, we drop US08 and keep the rest.

## Sprint 1 goal

One thin slice end to end: the instructor opens a session, the student sees that it is open and joins with a topic, and the instructor sees that entry in the waiting list. Someone outside the team should be able to follow that path at the review.

## What we would take

| ID | Story | Points | Why this one |
|---|---|---:|---|
| US01 | Open Office Hours Session | 3 | Nothing else works before a session exists. |
| US03 | View Session Status | 2 | The student needs to find out that a session is open. |
| US04 | Join Queue with Topic | 5 | This is the main student path. |
| US08 | View Waiting Students and Topics | 3 | Without it the instructor cannot see what was submitted. |
| Total | | 13 | |

If US01 and US03 go faster than expected, US02 is the next one in, because closing reuses the same session code.

## Why only 13

It is our first sprint, and the goal is a working path rather than a feature count. 13 is about a third of the MVP, which leaves room for the setup we know we still need: the Jira project, the backlog import, and agreeing on where the queue is stored.

If we run late, we stop at what the PO accepts instead of carrying three half-finished stories into Sprint 2.

## Not in this sprint

US02, US05, US06, US07, US09, US10, US11, US12, and US13 to US15.

This is not a priority order. It just shows what the first slice needs and what it can do without.

## Risks we can see

- The Jira project and the import can take an evening if the fields do not match the CSV.
- Queue storage is new to us, so US04 is the story most likely to slip.
- "Estimated wait" depends on a number we do not have yet, which is why US07 is not in this sprint.

## How we will forecast next time

After the sprint, the number that matters is the accepted points, not the planned ones. We compare the two in the retrospective, say where the difference came from, and start the next forecast from the accepted figure.
