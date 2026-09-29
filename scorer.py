from rapidfuzz import fuzz
import re


MATCH_THRESHOLD = 80
SUPPORT_COVERAGE_THRESHOLD = 0.60
SOURCE_PATTERN = re.compile(r"(?i)\b[\w.-]+\.txt\b")
STOP_WORDS = set(
    "a an the and or but if then than when while of at by for from in into "
    "on onto to as is are was were be been being has have had do does did "
    "that this these those it its their they he she we i you your my our "
    "me him her them can could should would will shall may might must first"
    .split()
)
NUMBER_WORDS = {
    "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
    "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9",
    "ten": "10", "eleven": "11", "twelve": "12", "thirteen": "13",
    "fourteen": "14", "fifteen": "15", "sixteen": "16", "seventeen": "17",
    "eighteen": "18", "nineteen": "19", "twenty": "20",
    "thirty": "30", "forty": "40", "fifty": "50", "sixty": "60",
    "seventy": "70", "eighty": "80", "ninety": "90", "hundred": "100",
    "second": "2", "third": "3", "fourth": "4", "fifth": "5",
    "sixth": "6", "once": "1",
}


def judge(question, expects, answer, result) -> bool:
    """Return whether the answer contains a sufficiently close expected phrase."""
    if not all(isinstance(value, str) for value in (question, expects, answer)):
        return False

    expected = expects.strip()
    response = answer.strip()
    if not expected or not response:
        return False

    return fuzz.partial_ratio(expected.casefold(), response.casefold()) >= MATCH_THRESHOLD


def _answer_text(answer):
    """Remove cited filenames so source labels do not count as answer evidence."""
    text = SOURCE_PATTERN.sub("", answer)
    text = re.sub(r"(?i)\(?\s*sources?\s*:\s*\)?", "", text)
    return text.strip()


def _normalise_token(token):
    if token in NUMBER_WORDS:
        return NUMBER_WORDS[token]
    if token.isdigit():
        return str(int(token))
    if len(token) > 4 and token.endswith("s") and not token.endswith("ss"):
        return token[:-1]
    return token


def _content_tokens(text):
    return {
        _normalise_token(token)
        for token in re.findall(r"[a-z0-9]+", text.casefold())
        if token not in STOP_WORDS
    }


def _supports_answer(answer, chunk):
    answer_text = _answer_text(answer)
    if not answer_text or not chunk.strip():
        return False

    chunk_tokens = _content_tokens(chunk)
    sentences = [
        sentence.strip()
        for sentence in re.split(r"(?<=[.!?])\s+", answer_text)
        if sentence.strip()
    ]
    for sentence in sentences:
        answer_tokens = _content_tokens(sentence)
        if not answer_tokens:
            return False
        numeric_tokens = {
            _normalise_token(token)
            for token in re.findall(r"[a-z0-9]+", sentence.casefold())
            if token.isdigit() or token in NUMBER_WORDS
        }
        if not numeric_tokens.issubset(chunk_tokens):
            return False
        matched = answer_tokens & chunk_tokens
        if len(matched) / len(answer_tokens) < SUPPORT_COVERAGE_THRESHOLD:
            return False

    return bool(sentences)


def _result_value(result, name, default=""):
    if isinstance(result, dict):
        return result.get(name, default)
    return getattr(result, name, default)


def judge_self_contained(question, expects, answer, results) -> bool:
    """Check whether one retrieved chunk independently supports the answer.

    Each answer sentence must have enough meaningful wording in the same chunk,
    including any numbers. This remains a lexical proxy for human judgment.
    """
    if not isinstance(answer, str) or not answer.strip():
        return False
    return any(
        _supports_answer(answer, str(_result_value(result, "text")))
        for result in results
    )


def judge_source_attribution(question, expects, answer, results) -> bool:
    """Check that every filename cited by the answer has a supporting chunk."""
    if not isinstance(answer, str) or not answer.strip():
        return False

    cited_sources = {source.casefold() for source in SOURCE_PATTERN.findall(answer)}
    if not cited_sources:
        return False

    for source in cited_sources:
        matching_chunks = [
            result
            for result in results
            if str(_result_value(result, "source")).casefold() == source
        ]
        if not matching_chunks or not any(
            _supports_answer(answer, str(_result_value(result, "text")))
            for result in matching_chunks
        ):
            return False
    return True