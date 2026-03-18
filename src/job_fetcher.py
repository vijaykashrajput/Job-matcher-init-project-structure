import requests

def fetch_jobs(keyword="developer"):

    url = "https://remotive.com/api/remote-jobs"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        jobs = []

        keywords = keyword.lower().split()  # 

        for job in data.get("jobs", []):

            title = job.get("title", "").lower()

            # match ANY keyword word
            if any(word in title for word in keywords):

                jobs.append({
                    "title": job.get("title"),
                    "company": job.get("company_name"),
                    "description": job.get("description", "")
                })

            if len(jobs) >= 10:
                break

        return jobs

    except Exception as e:
        print("Error:", e)
        return []