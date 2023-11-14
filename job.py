"""Fetch Basin & wxm data to set up a job for Bacalhau compute."""

import subprocess
import re


def get_basin_deals(namespace, relation):
    try:
        # Run the basin command
        result = subprocess.run(
            ['bash', '-c',
                f'basin publication deals --publication {namespace}.{relation}'],
            capture_output=True, text=True, check=True
        )

        stdout = result.stdout
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)

        # Regular expression to extract CID and deal ID from table format
        regex = r'\|\s*(\d+)\s*\|\s*[^|]+\|\s*(bafy[a-z0-9]+)\s*\|'
        deals = []

        # Find all matches and extract the groups
        for match in re.finditer(regex, stdout):
            deals.append({'deal_id': match.group(1), 'cid': match.group(2)})

        return deals

    except subprocess.CalledProcessError as e:
        print(f"Error finding basin deals: {e.stderr}")
        raise


# Get basin deals for wxm
namespace = "wxm2"
relation = "date_2023_10_18"
print(f"Getting deals for {namespace}.{relation}...")
deals = get_basin_deals(namespace, relation)
print(deals)
