# Estimation: Office Hours Queue

Week 4, Agile Software Development. Members are listed in `README.md`.

## How we did it

We read the stories together once, then estimated them one by one on a Fibonacci scale: 1, 2, 3, 5, 8, 13. Points are about size and uncertainty compared with the other stories, not about hours. We did not convert anything to hours because we have not built anything together yet and any hour number would be a guess.

What the numbers meant to us:

- 1 or 2: small and clear, we already know how to build it.
- 3: a normal feature with a few states or checks.
- 5: needs some thinking, usually more than one edge case.
- 8: several rules interacting, or something we are still unsure about.
- 13: too big for one story, split it first.

## Points

| ID | User story | Points | Why |
|---|---|---:|---|
| US01 | Open Office Hours Session | 3 | Creating the session, saving it and switching it to Open. Not hard, but it touches storage and the student view. |
| US02 | Close Office Hours Session | 2 | The same session record as US01. Only the state changes and joining has to stop. |
| US03 | View Session Status | 2 | Read the current state and show it. Almost no logic. |
| US04 | Join Queue with Topic | 5 | A form, a required topic, a new entry, a position to calculate, and the entry has to show up for the instructor too. |
| US05 | Prevent Duplicate Queue Entries | 3 | One check before the insert, but we still have to agree what counts as active and write the error message. |
| US06 | View Queue Position | 3 | Position comes from queue order, so it has to be recalculated and refreshed when someone ahead is removed. |
| US07 | View Estimated Waiting Time | 5 | Average service time is an assumption. We need to store it, handle a queue where nothing has finished yet, and decide when the number refreshes. |
| US08 | View Waiting Students and Topics | 3 | List the waiting entries in order with their topics. Mostly UI work. |
| US09 | Call Next Student | 3 | Move the first waiting entry to Called and make sure the same student cannot be called twice. |
| US10 | Mark Student as Done | 3 | Mark Called as Done and shift the remaining positions. Small, but it overlaps with US06. |
| US11 | View Queue Entry Status | 2 | Showing Waiting, Called or Done. Display only. |
| US12 | View Session History | 3 | Filter finished entries for one session and list them. One query and one screen. |
| US13 | Cancel Own Queue Entry | 3 | Cancelling removes the entry, so positions and estimates have to update again. |
| US14 | Tag Common Questions | 5 | Tags need their own data, a way to attach them to an entry, and a place to show repeated ones. |
| US15 | Anonymous Queue Display | 5 | Hiding names touches every screen that shows the queue, and the instructor view still has to show them. |

## Where we disagreed

- US04 started at 3 ("it's just a form") and went to 5 once we counted the position calculation and the instructor side.
- US07 started at 3 and moved to 5 when we realised the average service time has to come from somewhere and the first session has no history to average.
- US13 was 2 or 3. We took 3 because it touches positions again, the same code as US10.
- US14 split us between 5 and 8. We kept 5 and will split it if tags end up needing filtering or a report.

## Totals

MVP stories (US01 to US12): 37 points. Stretch stories (US13 to US15): 13 points. Whole backlog: 50.

Only the MVP is committed for now. The stretch stories are there if we have room.

## Notes

- These are our first numbers. Planning Poker before Sprint Planning may change them, and that is fine.
- US07 and US15 are the two we are least sure about. If either grows while we refine it, we split it instead of pushing the points up.
- Points can move if we learn something, but they are not hours and not a delivery promise.
