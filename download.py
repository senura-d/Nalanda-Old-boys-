import urllib.request
import os

downloads = [
    ("Charity - ONASA (Updated)", "https://lh3.googleusercontent.com/aida/AP1WRLvCP0DWgPHg_9GhUIlDmxOw_eVI1ZQ00Vi9QB77o6YOaHqUliQF46zuICCpBFkaumi5dVCErzVt63x20ns68c2Zjw2Q4tf2rl8gi8XNjZx-Ozrc3qgZH6-QofNWvfYBChCBJud2KjIdZyEfl2r03Kf3e50dtJkdFy0ZY904e3m9y-RR2umCWpPz2lrkJRXg3Qip-qnZvJkhLMKAF_zoHYmUgwPYfOWv0w3957rRhb__-DNMUjOJDFC6i2I", "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzg5NTc2ZTlmMzMwNDQ3MTA5NDJjZDE1MDE5ZjNhNThhEgsSBxC_ssOk0gsYAZIBIwoKcHJvamVjdF9pZBIVQhM1MTM5NjQwNzMwNjU3MDI0NjE0&filename=&opi=89354086"),
    ("Gallery - ONASA (Updated Style)", "https://lh3.googleusercontent.com/aida/AP1WRLvG4iN0LQ0r_RVzbSCLfR5f5av8g6HHwP6AdwGuZTaMCkvOdLLjm0Ktk073R5yrfVxSehVdMndG00Iiuf2cn_rR0w95_UohNB7z4nIUZiw85Ujf5sTjZ6uTIuA3aupOOVaxSa1uCFvzWnCZsTbRYvS0F1OS4_T40-wonc8dr9eZ8T5mvEcWdU1H6sxJz7yCFNr11KoEFM6BaNtI-toZwewSXOS9LlyPoHM_Gr8cLmBRRxrVoMlzLw5yvO4", "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzk3YTIyYWY5YzU5ZDQ1ZWY4ZDY5NDU4OTAzYTQ0ZTliEgsSBxC_ssOk0gsYAZIBIwoKcHJvamVjdF9pZBIVQhM1MTM5NjQwNzMwNjU3MDI0NjE0&filename=&opi=89354086"),
    ("Privacy Policy - ONASA", "https://lh3.googleusercontent.com/aida/AP1WRLuEF4I1iyRuylVIOGRfRoSkFbsFQQKp4xHVwQTJuhZbfE6vtCMFMbR4FdALdU0wy7kzHEkud8Dk8gJ1MqOcMewSGYkUWv7ss3pxAa-_ATNQnsq8DWsk5qX-PYdf5oLRcJcINmjoLzrDRxxXglvq5oxn4F7EMHcANuVhYIc_Epz-ZqqisTJ2GJHI0VRBh7riopFsuF9EXQZdW5qetAI66NakEMG24whWHgaJ4-9vS6y8k36GpJMuS4jIS70", "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzAwMDY1NGRiYjIyMmNhOWYwN2M0ZGUzZTY4MGZiNjRkEgsSBxC_ssOk0gsYAZIBIwoKcHJvamVjdF9pZBIVQhM1MTM5NjQwNzMwNjU3MDI0NjE0&filename=&opi=89354086"),
    ("Terms & Conditions - ONASA", "https://lh3.googleusercontent.com/aida/AP1WRLv2TamgUyEQT5LjIdULVaOhG-j7cuUHeadNjofKkcdANIFQi5a0rvHea4JAVRjGZ7FOkDjKeUqKWZBi7fHZVINSpKnxmWVzf-mi3tpby496H9Yp4MXoxa9VxLkHHrhZrGUVPtjiTla2HpAoxLcrVK8FmsJqPK2F7NRb1omvYWEVVWgMDWxbbJxc4Nx0SiE2GxEmYu-eLSvKNjbNgFBm0XfyohXycMQSmVx9qb1qJU6gEe2KhsnqFMAqYg", "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzAwMDY1NGRiYjIxNTcwY2EwNGVhYTZkYmRlMjAxNmY4EgsSBxC_ssOk0gsYAZIBIwoKcHJvamVjdF9pZBIVQhM1MTM5NjQwNzMwNjU3MDI0NjE0&filename=&opi=89354086"),
    ("Membership - ONASA (Redesign)", "https://lh3.googleusercontent.com/aida/AP1WRLsCPh6rc9_BWZNXhCf317RQwsYh_zcdYR_9mxm8KXLsBoREeF4Q-zOLItl_HMcTwqTwSNw8wLETml56KTvYBGlI0-p0Pbz2Q4xZ7G1XvVJCrA_gy303UHCw9sz0qQ1F_PSmAKCO8SWaPllCzwed9OIc6wHYp670Afelk9EMHtjJSnocQhn7b7vsBt5W_KV2ayEUZg24QZHTuSoG2rxjM4Ee6fV4vTTC1Pmd9jXdaswkaOUr_SQ5rlTYlCU", "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzAwMDY1NGRiYjFlOGI2YzIwMWE2MjgwYTI1MzM4MmE1EgsSBxC_ssOk0gsYAZIBIwoKcHJvamVjdF9pZBIVQhM1MTM5NjQwNzMwNjU3MDI0NjE0&filename=&opi=89354086"),
    ("About Us - ONASA (Redesign)", "https://lh3.googleusercontent.com/aida/AP1WRLu0zGr20ANrctBfzdHzBY-BqrIByDPRwisXco5nBWfr3MD4apB59e6guBH7t2ukDTlCK3dv02uybFpCqip1jH8fciPlg6vZc4j1EuNnDLm6uZtxgUqkQ36I9oWe-nkNjV4m_bvkdMJkPhB9RftQhTGIYhrlaPVC9KXtpNsy96kILqtUmMNRK6dTVTJeZn8FVmlalVQZaZLxUgOUjfB7mVNpV5wXawg2wNh0JdhAeBUKj3xDOuxQTQAeJA", "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzAwMDY1NGRiYjFmODI3NzMwMWE2MGJkYTVjMzdkYzY5EgsSBxC_ssOk0gsYAZIBIwoKcHJvamVjdF9pZBIVQhM1MTM5NjQwNzMwNjU3MDI0NjE0&filename=&opi=89354086"),
    ("Events - ONASA (Redesign)", "https://lh3.googleusercontent.com/aida/AP1WRLvnAIfuqo7QaIzL7RHVxYV8DSdFPlqvt87itzqMnFUwi-05PzJwsYJUGJ1jSsEZxT7pyWKG6Uf7csz8g0dwfGd7PfHgSZ-5iPYCOKYNx-7rlTyqHVvYly-Jz8smYd2nu7oxw8o4HLhIVjfDchEFg7mPsA3cvntyijKqc2xqsIph0n3ydzeER2IMYVXdpDpXdeSJM74syoJ7tYqPgtskDRuJ4np4BRGo1Iy-Is1rFOFA4-3XQon2CXZPE6A", "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzAwMDY1NGRiYjIwNTMxNjcwMzgzOWM4ZjI2MzJiYmZlEgsSBxC_ssOk0gsYAZIBIwoKcHJvamVjdF9pZBIVQhM1MTM5NjQwNzMwNjU3MDI0NjE0&filename=&opi=89354086"),
    ("Home - ONASA (Redesign)", "https://lh3.googleusercontent.com/aida/AP1WRLutJgNxdLiOnX65XlgTsa6usTmMjTFWLIfpCCPDqgv-a2tv809-Z8oxaPRON2gTT-yr2lQDTb7TR-YeBOMXmnt4h8V6leUrjG7HLNYZWjbv6UAEmBvjhcyyDe3eFD6HL566-NACH6qmbC2gpIq5KkVfsTbFSp5rCO9kE05SiVNB-fnGOyuOdHdWvwYx6F2D0deXuSIHnp5SaU8YGy_AvM3OJnKsYQk-kr44pOd59KAJu9auuThhAORep7A", "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzAwMDY1NGRiOWRiMzM1ZGMwMjBjYzA3NzkzMDMyMTNjEgsSBxC_ssOk0gsYAZIBIwoKcHJvamVjdF9pZBIVQhM1MTM5NjQwNzMwNjU3MDI0NjE0&filename=&opi=89354086"),
    ("Login & Registration - ONASA", "https://lh3.googleusercontent.com/aida/AP1WRLufrjIDcCamWGa9AN3jRNPvE7-HeXZ8SnkvLk4Npp8KYC2ixLZUxLRYMuYS4ogpptRzO-UaJGC2il6iWGZ6USDp3oBDueBm2gyGgOaQbxZlOI64-IxH7QutWWoLt_PL7euGzSdhNhWSwoMX29z65DMxlYCBdLzS6LHrlE1_BjHdIXju9hpQOs4yucrVnjylFjA9G3TxhHtwiLSKT1e_gjyYaMo4fWAkQN__RPvMlTS9cW96cGR6g9feukY", "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzAwMDY1NGRiYjJiZGI0OWYwMmE5YjYyMzI1MDc2NmEzEgsSBxC_ssOk0gsYAZIBIwoKcHJvamVjdF9pZBIVQhM1MTM5NjQwNzMwNjU3MDI0NjE0&filename=&opi=89354086")
]

os.makedirs('screens', exist_ok=True)

for name, img_url, html_url in downloads:
    safe_name = name.replace(' & ', '_').replace(' - ', '_').replace(' ', '_').replace('(', '').replace(')', '').lower()
    
    print(f"Downloading {name}...")
    
    img_path = os.path.join('screens', f"{safe_name}.png")
    try:
        urllib.request.urlretrieve(img_url, img_path)
    except Exception as e:
        print(f"Failed to download image for {name}: {e}")
        
    html_path = os.path.join('screens', f"{safe_name}.html")
    try:
        urllib.request.urlretrieve(html_url, html_path)
    except Exception as e:
        print(f"Failed to download HTML for {name}: {e}")

print("Done.")
