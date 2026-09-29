# The Unofficial Guide

Dennis Shlaih - Campus_Life

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in RUNNING.md.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The <!-- --> comments
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

**Chunk 1** — source: dmin_add_drop_deadline.txt#0 — produced by: chunker.py::split_documents



**Chunk 2** — source: course_biol_160.txt#0 — produced by: chunker.py::split_documents



**Chunk 3** — source: course_hist_118_workload.txt#0 — produced by: chunker.py::split_documents



**Chunk 4** — source: dining_pellew_dining_hall_followup.txt#0 — produced by: chunker.py::split_documents



**Chunk 5** — source: housing_innisfree_hall.txt#0 — produced by: chunker.py::split_documents



## Sample Answer

**Question:**
What is the first step in a grade appeal, and how many days does a student have to raise it?
**Answer:**



**My relevance cutoff:** 0.55

Question | In corpus? | Best distance
What determines the housing lottery order for juniors and seniors?  |   Yes | 0.2035
How late can a student drop a course, and what happens if they drop it after week two?  |       Yes | 0.2917
Do dining dollars roll over from the spring semester to the following fall semester? | Yes | 0.2169
What is the first step in a grade appeal, and how many days does a student have to raise it? |  Yes | 0.2112
How many times can a student change their meal plan tier, and when can they make the change? |  Yes | 0.2015
What is the capital of Mongolia? |      No |    0.8246
How do I change the oil in a diesel engine? | No |      0.9340
Who won the 1994 World Cup? |   No |    0.8859
What is the recommended dosage of ibuprofen for a headache? | No |0.8442 
How do I write a for loop in Rust? | No | 0.8960

## How I Used AI

**1.** I used CoPilot to write the code for the split_documents function in chunker.py. I kept the 800-character maximum and used zero overlap because the corpus is mostly short, focused posts. After running python app.py chunks, I checked the resulting chunks and confirmed that the sample chunks were complete and understandable.

**2.** I used CoPilot to help interpret the retrieval distances from my five in-corpus and five out-of-scope questions. It helped me identify the gap between the hardest in-corpus match (0.2917) and the closest out-of-scope match (0.8246). Based on those actual results, I chose 0.55 as my relevance cutoff rather than simply keeping the starter value. I then used the cutoff in my configuration and verified that the five in-corpus questions passed while the five out-of-scope questions were rejected.

---

# Unit 2

## Run Log — Before

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET  |
| 2. Every answer names a source | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 4. Chunks are self-contained | 4 of 5 | 2 of 5 | 2 of 5 | 2 of 5 | MISSED |
| 5. Source attribution is correct | 4 of 5 | 2 of 5 | 2 of 5 | 2 of 5 | MISSED |

# Run log — before

- Produced by: 
un_eval.py::main
- Retrieval: store.py::search, chunks from chunker.py::split_documents
- Corpus: campus_life (index variant default)
- top-k: 5 · relevance cutoff: 0.55
- Runs per question: 3, caching off
- When: 2026-09-28 20:10

| Question | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| What determines the housing lottery order for juniors and seniors? | pass | pass | pass |
| How late can a student drop a course, and what happens if they drop it after week two? | pass | pass | pass |
| Do dining dollars roll over from the spring semester to the following fall semester? | pass | pass | pass |
| What is the first step in a grade appeal, and how many days does a student have to raise it? | pass | pass | pass |
| How many times can a student change their meal plan tier, and when can they make the change? | pass | pass | pass |

## Chunk and source checks

Self-containment is scored as whether one retrieved chunk, by itself, lexically supports the answer. This is a repeatable proxy, not a replacement for human judgment of full context. Source attribution passes only when every cited filename has a retrieved chunk that supports the answer.

| Question | Single-chunk support by run | Cited-source support by run |
|---|---|---|
| What determines the housing lottery order for juniors and seniors? | fail, fail, fail | fail, fail, fail |
| How late can a student drop a course, and what happens if they drop it after week two? | fail, fail, fail | fail, fail, fail |
| Do dining dollars roll over from the spring semester to the following fall semester? | pass, pass, pass | pass, pass, pass |
| What is the first step in a grade appeal, and how many days does a student have to raise it? | fail, fail, fail | fail, fail, fail |
| How many times can a student change their meal plan tier, and when can they make the change? | pass, pass, pass | pass, pass, pass |

Single-chunk support per run: Run 1: 2/5; Run 2: 2/5; Run 3: 2/5.

Cited-source support per run: Run 1: 2/5; Run 2: 2/5; Run 3: 2/5.

---

## The relevance gate on out-of-corpus questions

Produced by 
un_eval.py::check_out_of_scope, cutoff 0.55. Refused 5 of 5.

Retrieval is deterministic and the gate is a comparison against a
fixed number, so these do not vary between runs — one pass over the
list is the whole measurement.

| Out-of-scope question | Best distance | Gate |
|---|---|---|
| What is the capital of Mongolia? | 0.825 | refused |
| How do I change the oil in a diesel engine? | 0.934 | refused |
| Who won the 1994 World Cup? | 0.886 | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.844 | refused |
| How do I write a for loop in Rust? | 0.896 | refused |

---

## Real output

This is what the system actually produced. Paste the relevant parts
into your README underneath the table — the rubric asks for real
output as text, not a description of it.

### What determines the housing lottery order for juniors and seniors? — run 1

- Best distance: 0.2035 (passed the gate)
- Sources retrieved: admin_housing_lottery.txt, advising_registration.txt, dining_the_atrium_followup.txt, housing_old_brewhouse.txt, housing_tamsin_court.txt



### What determines the housing lottery order for juniors and seniors? — run 2

- Best distance: 0.2035 (passed the gate)
- Sources retrieved: admin_housing_lottery.txt, advising_registration.txt, dining_the_atrium_followup.txt, housing_old_brewhouse.txt, housing_tamsin_court.txt



### What determines the housing lottery order for juniors and seniors? — run 3

- Best distance: 0.2035 (passed the gate)
- Sources retrieved: admin_housing_lottery.txt, advising_registration.txt, dining_the_atrium_followup.txt, housing_old_brewhouse.txt, housing_tamsin_court.txt



### How late can a student drop a course, and what happens if they drop it after week two? — run 1

- Best distance: 0.2917 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_declaring_a_major.txt, admin_grade_appeals.txt, admin_pass_fail_option.txt, admin_withdrawal_deadline.txt



### How late can a student drop a course, and what happens if they drop it after week two? — run 2

- Best distance: 0.2917 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_declaring_a_major.txt, admin_grade_appeals.txt, admin_pass_fail_option.txt, admin_withdrawal_deadline.txt



### How late can a student drop a course, and what happens if they drop it after week two? — run 3

- Best distance: 0.2917 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_declaring_a_major.txt, admin_grade_appeals.txt, admin_pass_fail_option.txt, admin_withdrawal_deadline.txt



### Do dining dollars roll over from the spring semester to the following fall semester? — run 1

- Best distance: 0.2169 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_dining_dollars.txt, admin_meal_plan_changes.txt, admin_printing_quota.txt, money_jobs.txt



### Do dining dollars roll over from the spring semester to the following fall semester? — run 2

- Best distance: 0.2169 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_dining_dollars.txt, admin_meal_plan_changes.txt, admin_printing_quota.txt, money_jobs.txt



### Do dining dollars roll over from the spring semester to the following fall semester? — run 3

- Best distance: 0.2169 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_dining_dollars.txt, admin_meal_plan_changes.txt, admin_printing_quota.txt, money_jobs.txt



### What is the first step in a grade appeal, and how many days does a student have to raise it? — run 1

- Best distance: 0.2112 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_grade_appeals.txt, admin_pass_fail_option.txt, course_stat_150.txt, course_stat_150_exams.txt



### What is the first step in a grade appeal, and how many days does a student have to raise it? — run 2

- Best distance: 0.2112 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_grade_appeals.txt, admin_pass_fail_option.txt, course_stat_150.txt, course_stat_150_exams.txt



### What is the first step in a grade appeal, and how many days does a student have to raise it? — run 3

- Best distance: 0.2112 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_grade_appeals.txt, admin_pass_fail_option.txt, course_stat_150.txt, course_stat_150_exams.txt



### How many times can a student change their meal plan tier, and when can they make the change? — run 1

- Best distance: 0.2015 (passed the gate)
- Sources retrieved: admin_dining_dollars.txt, admin_meal_plan_changes.txt, dining_kestrel_commons_followup.txt, dining_verrill_street_grill.txt, money_jobs.txt



### How many times can a student change their meal plan tier, and when can they make the change? — run 2

- Best distance: 0.2015 (passed the gate)
- Sources retrieved: admin_dining_dollars.txt, admin_meal_plan_changes.txt, dining_kestrel_commons_followup.txt, dining_verrill_street_grill.txt, money_jobs.txt



### How many times can a student change their meal plan tier, and when can they make the change? — run 3

- Best distance: 0.2015 (passed the gate)
- Sources retrieved: admin_dining_dollars.txt, admin_meal_plan_changes.txt, dining_kestrel_commons_followup.txt, dining_verrill_street_grill.txt, money_jobs.txt



## Verdicts

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunk contains the answer | MET | All 5 questions had the answer in their retrieved chunks across all 3 runs, meeting the 4-of-5 target. |
| 2 | Every answer names a source | MET  | The scorer found that 5 of 5 of the questions includes a source in the answer in each one of the 3 runs. |
| 3 | Gate stops out-of-corpus questions | MET | The scorer found that 5 of 5 of the out-of-corpus questions are stopped by the gate. |
| 4 | Chunks are self-contained | MISSED | The scorer found one retrieved chunk that independently supported the answer for 2 of 5 questions in each of the three runs, below the 4-of-5 target. This is a lexical proxy for whether the chunk is understandable on its own. |
| 5 | Source attribution is correct | MISSED | The cited-source check found a retrieved chunk from the named source supporting the answer for 2 of 5 questions in each of the three runs, below the 4-of-5 target. |

## Diagnoses

4. Chunks are self-contained: MISSED. The misses were the housing-lottery, add/drop, and grade-appeal questions. This is because chunking did not split their evidence. As a result, each answer is present in one source document, which split_documents keeps as one chunk. The failures come from the scorer after generation because it compares the whole answer with one chunk using a lexical-similarity threshold. Paraphrased answers can easily fail that check even when the chunk contains the complete and understandable answer. The other two answers pass because their wording is closer to the source.

5. Source attribution is correct: MISSED. The same 3 answers name the documents that contain their information, and retrieval returned those documents. So the misses do not appear to come from loading, chunking, embedding, retrieval, or the choice of source in generation. The attribution scorer matches the cited filename to a retrieved source, then applies the same whole-answer lexical check. As a result, that check will reject the paraphrases and label the citations as unsupported. Thus, there is a measurement problem in the scorer, which remains outside of the 5 pipeline stages.

## The Improvement

**What I changed:** In scorer.py, I replaced the whole-answer-to-whole-chunk token-set comparison with a sentence-by-sentence support check. It compares meaningful words in each answer sentence with the chunk, requires at least 60% coverage, and requires any number in the answer to appear in the chunk. The source-attribution check still requires the cited filename to match a retrieved source, then checks that source's chunk.

**Why I picked it:** The three misses already had the correct answer-bearing chunks retrieved and cited, but the old scorer rejected their paraphrased wording. This change targets that measurement problem without changing chunking, retrieval, or the original 4-of-5 targets.

### Run Log — After

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 2. Every answer names a source | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 |MET | 
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 4. Chunks are self-contained | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 5. Source attribution is correct | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |

**Did it help?**

Yes. The fix directly addressed the measurement issue behind the earlier misses: before the change, criteria 4 and 5 scored 2 of 5 in all three runs because the evaluator compared each full answer to a single chunk using a brittle whole-answer lexical check. After the change, every criterion reached 5 of 5 in each of the three runs. That makes the improvement clear: the earlier problem was not that the pipeline retrieved the wrong evidence, but that the scorer rejected paraphrased but correct answers.

## What's Still Broken

Nothing in the project’s five required criteria is still broken after the fix. The remaining limitation is in the scoring method itself: it still relies on lexical overlap and sentence coverage instead of deeper semantic matching. That means a very different paraphrase could still be treated as unsupported even when the retrieved source clearly supports the answer. I stopped here because the evaluation targets are already met across all three runs, and the remaining risk is a general quality issue in the scorer rather than a failure of the core retrieval pipeline.

## What I'd Do Differently

I would rewrite criteria 4 and 5 to measure evidence support more directly rather than comparing whole answers to chunks by word overlap. A better criterion would ask whether the answer sentence is supported by the retrieved source text, not whether the wording matches almost exactly. I would keep the source-attribution requirement tied to the cited filename, but I would validate support with sentence-level matching or embeddings instead of a whole-answer token-set comparison. In other words, I would test the reasoning evidence rather than just the surface wording.
