import requests
import sys
import re
from datetime import datetime

if __name__ == "__main__":
    assert(len(sys.argv) == 5)
    repository = sys.argv[1]
    token = sys.argv[2]
    readme_path = sys.argv[3]
    file_name = sys.argv[4]  # The filename is now passed dynamically

    # Get the current date
    today = datetime.today()
    day_of_month = today.strftime("%d")  # Get current day of the month (e.g., 06)
    month = today.strftime("%b")  # Get current month (e.g., Nov)

    # Prepare the solution URL for today (dynamically from the file_name)
    solution_url = f"https://github.com/{repository}/blob/main/November%202024%20GFG%20SOLUTION/{file_name}"

    # Prepare the badge URL and commit link to update README
    badge_url = "https://img.shields.io/badge/GeeksforGeeks-Solution%20of%20the%20Day-blue"
    badge_link = f"[![Today's POTD Solution]({badge_url})]({solution_url})"  # This makes the badge link to the solution for today

    # Read the README file and update the sections for commit and badge
    with open(readme_path, "r") as readme:
        content = readme.read()

    # Update badge link
    content = re.sub(
        r"(?<=<!--START_SECTION:potd-badge-->).*?(?=<!--END_SECTION:potd-badge-->)", 
        f"\n{badge_link}\n", 
        content, 
        flags=re.DOTALL
    )

    # Write the updated content back to the README
    with open(readme_path, "w") as readme:
        readme.write(content)