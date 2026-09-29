# The Unofficial Guide

Dennis Shlaih - Campus_Life

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

The Unofficial Guide is a retrieval-augmented question-answering system using built using the campus_life corpus. It answers questions about campus life, including course information, housing, dining, academic policies, and other student resources. The system retrieves relevant chunks from the corpus and uses those chunks as the basis for its answers, while identifying the source document. It is designed to provide answers grounded in the information contained in the Campus Life documents rather than relying on unrelated information.

## Chunking Strategy

**Chunk size:** 800 characters maximum
**Overlap:** 0 characters

The campus_life corpus contains 88 short, focused documents, and the starter chunker produced 88 chunks because almost none of the documents reached the 800-character limit. After inspecting the documents and the starter output, I decided that most posts should remain as one chunk because each post generally focuses on one topic and already forms a complete thought. For documents that are long enough to require splitting, my chunker uses paragraph boundaries rather than cutting at an arbitrary character position, which helps keep related information together and avoids splitting sentences or paragraphs. I used no overlap because the documents are short and focused, so repeating text between chunks would add unnecessary duplication rather than preserving needed context.

## Sample Chunks


**Chunk 1** — source: `admin_add_drop_deadline.txt#0` — produced by: ` chunker.py::split_documents`

```
On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows as a W on your transcript. Nothing anywhere on the registrar's site says this plainly, and students find out from each other.

```

**Chunk 2** — source: `course_biol_160.txt#0` — produced by: `chunker.py::split_documents`

```
BIOL 160 Cell Biology

I lived here my sophomore year. Format is lecture three times a week with a weekly lab. Assessment: four unit tests and a cumulative final. Not curved.

Expect 9 to 11 hours a week, the heaviest first-year course by reputation.

The one piece of advice: the unit tests come fast, roughly every three weeks; falling behind once is very hard to recover from.
```

**Chunk 3** — source: `course_hist_118_workload.txt#0` — produced by: `chunker.py::split_documents`

```
Workload for HIST 118 Modern World History

People keep asking so: a lot of reading, about 120 pages a week, but no problem sets. That's real time, not optimistic time.

It's front-loaded — the first month is heavier than the rest, partly because you're learning the format.
```

**Chunk 4** — source: `dining_pellew_dining_hall_followup.txt#0` — produced by: `chunker.py::split_documents`

```
Re: Pellew Dining Hall

Adding to what people have said about Pellew Dining Hall. The wait figure of 12 to 18 minutes at peak matches what I've seen. If you're trying to eat between classes, go before 11:45 and it's a different building entirely.

Also worth saying: the furthest hall from anywhere, next to the athletics centre. Nobody tells you this at orientation.
```

**Chunk 5** — source: `housing_innisfree_hall.txt#0` — produced by: `chunker.py::split_documents`

```
Innisfree Hall — what it's actually like

Transferred in last year, so take this with a grain of salt. Built 1991, renovated 2022. Rooms are doubles arranged as pairs sharing one bathroom between two rooms.

The good: the shared-bathroom-between-two-rooms arrangement is the best compromise on campus.
```

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:**
What is the first step in a grade appeal, and how many days does a student have to raise it?
**Answer:**

```
The first step in a grade appeal is with the instructor, and a student has fifteen days from the grade posting to raise it (admin_grade_appeals.txt).

Sources retrieved: admin_add_drop_deadline.txt, admin_grade_appeals.txt, admin_pass_fail_option.txt, course_stat_150.txt, course_stat_150_exams.txt
```

**My relevance cutoff:** 0.55

Question | In corpus? | Best distance
What determines the housing lottery order for juniors and seniors?  |	Yes | 0.2035
How late can a student drop a course, and what happens if they drop it after week two?  |	Yes | 0.2917
Do dining dollars roll over from the spring semester to the following fall semester? | Yes | 0.2169
What is the first step in a grade appeal, and how many days does a student have to raise it? |	Yes | 0.2112
How many times can a student change their meal plan tier, and when can they make the change? |	Yes | 0.2015
What is the capital of Mongolia? |	No |	0.8246
How do I change the oil in a diesel engine? | No |	0.9340
Who won the 1994 World Cup? |	No |	0.8859
What is the recommended dosage of ibuprofen for a headache? | No |0.8442 
How do I write a for loop in Rust? | No | 0.8960

## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1.** I used CoPilot to write the code for the split_documents function in chunker.py. I kept the 800-character maximum and used zero overlap because the corpus is mostly short, focused posts. After running python app.py chunks, I checked the resulting chunks and confirmed that the sample chunks were complete and understandable.

**2.** I used CoPilot to help interpret the retrieval distances from my five in-corpus and five out-of-scope questions. It helped me identify the gap between the hardest in-corpus match (0.2917) and the closest out-of-scope match (0.8246). Based on those actual results, I chose 0.55 as my relevance cutoff rather than simply keeping the starter value. I then used the cutoff in my configuration and verified that the five in-corpus questions passed while the five out-of-scope questions were rejected.

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET  |
| 2. Every answer names a source | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 4. Chunks are self-contained | 4 of 5 | 2 of 5 | 2 of 5 | 2 of 5 | MISSED |
| 5. | 4 of 5 | 2 of 5 | 2 of 5 | 2 of 5 | MISSED |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunk contains the answer | MET | All 5 questions had the answer in their retrieved chunks across all 3 runs, meeting the 4-of-5 target. |
| 2 | Every answer names a source | MET  | The scorer found that 5 of 5 of the questions includes a source in the answer in each one of the 3 runs. |
| 3 | Gate stops out-of-corpus questions | MET | The scorer found that 5 of 5 of the out-of-corpus questions are stopped by the gate. |
| 4 | Chunks are self-contained | MISSED | The scorer found one retrieved chunk that independently supported the answer for 2 of 5 questions in each of the three runs, below the 4-of-5 target. This is a lexical proxy for whether the chunk is understandable on its own. |
| 5 | Source attribution is correct | MISSED | The cited-source check found a retrieved chunk from the named source supporting the answer for 2 of 5 questions in each of the three runs, below the 4-of-5 target. |

## Diagnoses

4. Chunks are self-contained: MISSED by the automated check. For the housing-lottery question, `admin_housing_lottery.txt` has the credit-hours rule and random tie-break together in one chunk. For the add/drop question, `admin_add_drop_deadline.txt` has both the week-six deadline and the W-after-week-two rule together. For the grade-appeal question, `admin_grade_appeals.txt` has the instructor-first step and fifteen-day limit together. These are short documents, so `chunker.py::split_documents` keeps each as one chunk, and retrieval returns those chunks. The failure happens after generation in `scorer.py`: it compares the entire answer against one chunk using token-set similarity with a threshold of 80. The generated paraphrases fall below that lexical threshold, although each chunk contains the complete answer. Thus these results do not show a chunking or retrieval failure; they show that the automated proxy can mistake different wording for missing context.

5. Source attribution is correct: MISSED by the automated check. In those same three answers, generation names the matching source file, and that file is among the retrieved results: `admin_housing_lottery.txt`, `admin_add_drop_deadline.txt`, or `admin_grade_appeals.txt`. The matching source chunks contain the facts used in the answers. `scorer.py::judge_source_attribution` finds the cited filename, but then requires the whole generated answer to pass the same token-set similarity threshold against that chunk. Because the paraphrases fail this check, the scorer marks the correct citations unsupported. Loading, chunking, embedding, and retrieval supplied the right evidence; generation cited its source; the false negative is in the scorer after generation, outside the five pipeline stages.


## The Improvement

**What I changed:**

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
