# Acceptance criteria — The Unofficial Guide

Five criteria that say what "working" means for this system, written in unit 1
**before** any results existed.

An acceptance criterion names a target: a number, a count, a rate, or something
a person could plainly observe. *"Retrieval works"* is an opinion. *"For at
least 4 of my 5 test questions, the top results include a chunk containing the
answer"* is a criterion.

Under each one, write a sentence or two on **why that target** and not a
stricter or looser one. A reason that says something about your corpus or your
pipeline earns credit; *"80% seemed reasonable"* does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## 1. Retrieved chunks contain the answer

For at least 4 of my 5 test questions, the retrieved chunks include one that
contains the answer.

**Why this target:**

My five test questions cover specific topics in the Campus Life corpus, and each question has a corresponding document containing the needed information. I chose 4 of 5 because retrieval should succeed on most questions while allowing one question to be missed due to differences in wording or similarity between documents.

---

## 2. Every answer names a source

Every answer the system produces names at least one source document.

**Why this target:**

The system is designed to answer questions using retrieved documents, so every answer should be traceable to a source rather than appearing as unsupported information. I chose all five because the source name is generated from the retrieved document metadata, making attribution an expected part of every in-corpus answer.

---

## 3. The relevance gate stops out-of-corpus questions

When I ask a question my documents clearly don't cover, the relevance gate
stops it and the system returns "I don't have enough information about that" —
in at least 4 of 5 tries.

<!-- The five questions are the ones in `OUT_OF_SCOPE` at the bottom of
     `questions.py`, and `run_eval.py` puts them through the gate and writes
     what happened into your run log. Swap them for your own if you'd rather —
     just keep five of them, or the "4 of 5" above has nothing to be 4 of. -->

**Why this target:**

The Campus Life corpus covers specific campus information rather than general world knowledge, so questions about topics such as sports, medicine, and programming should be clearly outside the corpus. I chose 4 of 5 because the gate should reject most clearly unrelated questions, while allowing for the possibility that one question may have a misleadingly similar embedding.

---

## 4. Chunks are self-contained

For at least 4 of my 5 test questions, the retrieved chunk that contains the answer can be understood without needing text from another chunk of the same document.

**Why this target:**

The Campus Life documents are mostly short, focused posts, and the chunks I inspected already contain complete thoughts about one topic. I chose 4 of 5 because keeping the relevant information together should make most answers understandable from a single retrieved chunk, while allowing for a question whose answer may depend on information spread across a longer document.

---

## 5. Source attribution is correct

For at least 4 of my 5 test questions, the source document named in the answer is the document that contains the information used to answer the question.

**Why this target:**

The Campus Life corpus contains many separate documents covering specific administrative and campus topics, so an answer could name a real document without that document actually supporting the answer. Requiring 4 of 5 correct source attributions tests whether the system is connecting its answer to the retrieved evidence rather than merely displaying a source name.

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 2 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath it, like this:

         ## 1. Retrieved chunks contain the answer

         For at least 4 of my 5 test questions, the retrieved chunks include
         one that contains the answer.

         **Why this target:** ...

         > **Revised in unit 2:** For at least 4 of 5 questions, the top three
         > results contain the answer.
         >
         > **Why revised:** I couldn't judge "the chunks include one that
         > contains the answer" the same way twice — I scored two questions
         > differently on Monday than on Wednesday. The new version is
         > something I can actually check.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "I said 4 of 5 but got 2 of 5, so 2 of 5 is more realistic."

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.

     The whole reason the originals stay visible is so someone can see what you
     said before you knew the answer.
     ───────────────────────────────────────────────────────────────────────── -->
