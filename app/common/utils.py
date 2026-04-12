from datetime import datetime, UTC
import uuid


def generate_uuid() -> str:
    return str(uuid.uuid4())


def utc_now_iso() -> str:
    return datetime.now(UTC).isoformat()