# Run log — before

- Produced by: `run_eval.py::main`
- Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`
- Corpus: `campus_life` (index variant `default`)
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

Produced by `run_eval.py::check_out_of_scope`, cutoff 0.55. Refused 5 of 5.

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

```
For juniors and seniors, the housing lottery order is determined first by accumulated credit hours, with a random tie-break used only in the case of a tie (admin_housing_lottery.txt).
```

### What determines the housing lottery order for juniors and seniors? — run 2

- Best distance: 0.2035 (passed the gate)
- Sources retrieved: admin_housing_lottery.txt, advising_registration.txt, dining_the_atrium_followup.txt, housing_old_brewhouse.txt, housing_tamsin_court.txt

```
For juniors and seniors, the housing lottery order is determined first by accumulated credit hours, with random tie-breaking used if necessary. 

Source: admin_housing_lottery.txt
```

### What determines the housing lottery order for juniors and seniors? — run 3

- Best distance: 0.2035 (passed the gate)
- Sources retrieved: admin_housing_lottery.txt, advising_registration.txt, dining_the_atrium_followup.txt, housing_old_brewhouse.txt, housing_tamsin_court.txt

```
For juniors and seniors, the housing lottery order is determined by accumulated credit hours first, with random tie-breaking used only when necessary (admin_housing_lottery.txt).
```

### How late can a student drop a course, and what happens if they drop it after week two? — run 1

- Best distance: 0.2917 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_declaring_a_major.txt, admin_grade_appeals.txt, admin_pass_fail_option.txt, admin_withdrawal_deadline.txt

```
A student can drop a course through the end of week six. If they drop a course after week two, it shows as a "W" on their transcript. 

Source: `admin_add_drop_deadline.txt`
```

### How late can a student drop a course, and what happens if they drop it after week two? — run 2

- Best distance: 0.2917 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_declaring_a_major.txt, admin_grade_appeals.txt, admin_pass_fail_option.txt, admin_withdrawal_deadline.txt

```
A student can drop a course through the end of week six. If they drop a course after week two, it shows as a W on their transcript. 

Source: admin_add_drop_deadline.txt
```

### How late can a student drop a course, and what happens if they drop it after week two? — run 3

- Best distance: 0.2917 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_declaring_a_major.txt, admin_grade_appeals.txt, admin_pass_fail_option.txt, admin_withdrawal_deadline.txt

```
A student can drop a course through the end of week six. If they drop a course after week two, it shows as a W on their transcript. 

Source: admin_add_drop_deadline.txt
```

### Do dining dollars roll over from the spring semester to the following fall semester? — run 1

- Best distance: 0.2169 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_dining_dollars.txt, admin_meal_plan_changes.txt, admin_printing_quota.txt, money_jobs.txt

```
No, dining dollars do not roll over from the spring semester to the following autumn semester, and whatever is left in May disappears. 

Source: admin_dining_dollars.txt
```

### Do dining dollars roll over from the spring semester to the following fall semester? — run 2

- Best distance: 0.2169 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_dining_dollars.txt, admin_meal_plan_changes.txt, admin_printing_quota.txt, money_jobs.txt

```
No, dining dollars do not roll over from the spring semester to the following autumn semester, and whatever is left in May disappears. (Source: admin_dining_dollars.txt)
```

### Do dining dollars roll over from the spring semester to the following fall semester? — run 3

- Best distance: 0.2169 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_dining_dollars.txt, admin_meal_plan_changes.txt, admin_printing_quota.txt, money_jobs.txt

```
No, dining dollars do not roll over from the spring semester to the following autumn semester, and whatever is left in May disappears. 

Source: admin_dining_dollars.txt
```

### What is the first step in a grade appeal, and how many days does a student have to raise it? — run 1

- Best distance: 0.2112 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_grade_appeals.txt, admin_pass_fail_option.txt, course_stat_150.txt, course_stat_150_exams.txt

```
The first step in a grade appeal is starting with the instructor, and a student has fifteen days from the grade posting to raise it (admin_grade_appeals.txt).
```

### What is the first step in a grade appeal, and how many days does a student have to raise it? — run 2

- Best distance: 0.2112 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_grade_appeals.txt, admin_pass_fail_option.txt, course_stat_150.txt, course_stat_150_exams.txt

```
The first step in a grade appeal is to start with the instructor, and a student has fifteen days from the grade posting to raise it (admin_grade_appeals.txt).
```

### What is the first step in a grade appeal, and how many days does a student have to raise it? — run 3

- Best distance: 0.2112 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_grade_appeals.txt, admin_pass_fail_option.txt, course_stat_150.txt, course_stat_150_exams.txt

```
The first step in a grade appeal is starting with the instructor, and a student has fifteen days from the grade posting to raise it. (Source: admin_grade_appeals.txt)
```

### How many times can a student change their meal plan tier, and when can they make the change? — run 1

- Best distance: 0.2015 (passed the gate)
- Sources retrieved: admin_dining_dollars.txt, admin_meal_plan_changes.txt, dining_kestrel_commons_followup.txt, dining_verrill_street_grill.txt, money_jobs.txt

```
A student can change their meal plan tier once, and they must make the change in the first ten days of the semester. 

Source: admin_meal_plan_changes.txt
```

### How many times can a student change their meal plan tier, and when can they make the change? — run 2

- Best distance: 0.2015 (passed the gate)
- Sources retrieved: admin_dining_dollars.txt, admin_meal_plan_changes.txt, dining_kestrel_commons_followup.txt, dining_verrill_street_grill.txt, money_jobs.txt

```
A student can change their meal plan tier once, and they must do it in the first ten days of the semester. 

Source: admin_meal_plan_changes.txt
```

### How many times can a student change their meal plan tier, and when can they make the change? — run 3

- Best distance: 0.2015 (passed the gate)
- Sources retrieved: admin_dining_dollars.txt, admin_meal_plan_changes.txt, dining_kestrel_commons_followup.txt, dining_verrill_street_grill.txt, money_jobs.txt

```
A student can change their meal plan tier once, and they must make the change in the first ten days of the semester. 

Source: admin_meal_plan_changes.txt
```
