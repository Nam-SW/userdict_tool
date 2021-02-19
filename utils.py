from typing import List


def str_to_list(text: str) -> List[str]:
    """
    str(List[str]) 형태의 문자열을 리스트로 바꿔줍니다.

    Args:
        text[str]: str(List[str]) 형태의 문자열
                   ex) "['문', '자', '열']"

    Returns:
        List[str]: 리스트 형태로 전환된 text
    """
    text = text[1:-1].replace('"', "").replace("'", "")
    return text.split(", ")
