from dataclasses import dataclass


@dataclass
class CrowdIndicator:
    """
    Serializer and Deserializer for the response from BW
    Example:
        {
            "level": 0,
            "flevel": 42,
            "isqueue": false,
            "queue": 0,
            "percent": 0,
            "pstr": "",
            "pstrm": "calc(0 - 0px)",
            "success": true
        }
    """

    level: int
    flevel: int
    isqueue: bool
    queue: int
    percent: int
    pstr: str
    pstrm: str
    success: bool
