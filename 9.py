from pydantic import BaseModel
import wikipediaapi

class Info(BaseModel):
    name: str
    founder: str
    founded: str
    branches: str
    employees: str
    summary: str

def get_line(text, keyword):
    return next((line for line in text.split('\n') if keyword in line.lower()), "Not available")

def fetch(name):
    wiki = wikipediaapi.Wikipedia(
        language='en',
        headers={"User-Agent": "MySimpleFetcher/1.0 (contact@example.com)"}
    )
    page = wiki.page(name)
    if not page.exists():
        raise ValueError(f"No page found for '{name}'")

    txt = page.text
    return Info(
        name=name,
        founder=get_line(txt, "founder"),
        founded=get_line(txt, "founded") or get_line(txt, "established"),
        branches=get_line(txt, "branch"),
        employees=get_line(txt, "employee"),
        summary="\n".join(txt.split('\n')[:3])
    )

# Run it
print(fetch("VTU").model_dump_json(indent=2))
