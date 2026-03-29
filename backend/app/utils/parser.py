from datetime import    datetime


def parse_job(row):
    return {
        "title": row.get("title", ""),
        "description": row.get("description", ""),
        "url": row.get("url", ""),
        "location": row.get("location", ""),
        "is_remote": row.get("is_remote", False),
        "posted_at": row.get("posted_at", None),
        "deadline": row.get("deadline", None),
        "source_url": row.get("job_url"),
        "posted_at": None,  # JobSpy sometimes missing
        "deadline": None,
        "tags": None,
        "skills_required": None
    }

def parse_hackathon(row):
    return {
        "title": row.get("title", ""),
        "description": row.get("description", ""),
        "url": row.get("url", ""),
        "location": row.get("location", ""),
        "is_remote": row.get("is_remote", False),
        "posted_at": row.get("posted_at", None),
        "deadline": row.get("deadline", None),
        "source_url": row.get("hackathon_url"),
        "posted_at": None,  # Devpost sometimes missing
        "deadline": None,
        "tags": None,
        "skills_required": None
    }