import json
import summarize

test_bio = """* B. Childhood Memories and Early Interests
* 1. Wartime Sydney (Cremorne, Manly Beach, rock pools, ferries, oil slicks)
* 2. Tasmanian Interludes (10 Carnarvon Street, making mud, dog Sidi)
* 3. Early Scientific Curiosity (Steam engines, father's light box, fascination with how things work)
* 4. Development of Myopia
* 5. Early Encounters with Music (Beethoven symphonies on 78rpm, father's oscilloscope, Miss Budden's school piano)
* 6. Learning to Read (Angus and the Cat, Pretzel, "eureka moment")
* 7. Fascination with Language ("Between the bars" incident)
* 8. Father's Influence (Model aeroplanes, explaining the stars)
* C. Early Schooling
* 1. Kindergarten in Sydney (Miss Budden's)
"""

resp = summarize.generate_summaries(1,test_bio)
# pretty print the response.text json
print(json.dumps(resp, indent=2))