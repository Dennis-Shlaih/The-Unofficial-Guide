from rapidfuzz import fuzz
import re


MATCH_THRESHOLD = 80
SOURCE_PATTERN = re.compile(r"(?i)\b[\w.-]+\.txt\b")


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
    return SOURCE_PATTERN.sub("", answer).strip()


def _supports_answer(answer, chunk):
    answer_text = _answer_text(answer)
    if not answer_text or not chunk.strip():
        return False
    return fuzz.token_set_ratio(answer_text.casefold(), chunk.casefold()) >= MATCH_THRESHOLD


def _result_value(result, name, default=""):
    if isinstance(result, dict):
        return result.get(name, default)
    return getattr(result, name, default)


def judge_self_contained(question, expects, answer, results) -> bool:
    """Check whether one retrieved chunk independently supports the answer.

    This lexical check is a repeatable proxy for human judgment of whether a
    chunk is understandable on its own; it requires the answer to match one
    chunk rather than evidence assembled across several chunks.
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