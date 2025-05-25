import json
import summarize

test_bio = """* Childhood Memories and Early Interests
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

. Personal Life, Philosophy, and Reflections
* A. Music as a Lifelong Passion
* 1. Performance (Violin, piano, chamber music, David Crighton memorial concert)
* 2. Theoretical interest in acoustics
* 3. Connection between music and mathematics (unconscious power of abstraction, organic change)
* B. Family and Home Life
* 1. Marriage to Ruth Hecht (Pianist, artist, culinary expert)
* 2. Three stepchildren (Peter, Jonathan, Miriam) and their interests
* 3. Work-life balance and evolution of family engagement
* 4. Home in De Freville Avenue and Windsor Road (studies, home improvements, solar panels)
* C. Hobbies and Other Interests
* 1. Gliding (Inspired by Philip Wills' "Flight without Power", Aviator simulator, Cambridge Gliding Club, solo in 1990)
* 2. Interest in perception psychology (Richard Gregory's "The Intelligent Eye")
* D. Intellectual Development and Philosophy
* 1. Lucidity in Science (Importance of clear communication, proofreading Batchelor, Adams-Airy affair, teaching undergraduates)
* 2. Nature of Scientific Understanding (Feynman's approach, multiple perspectives, role of simple models, thought experiments)
* 3. "Reverent Agnostic" (Views on religion, Dawkins, Martin Rees)
* 4. On Climate Change (Palaeoclimate record, CO2 as non-condensing greenhouse gas, Earth system as amplifier, criticism of disinformers, IPCC process)
* 5. Politics and Society (Trust, journalism, democracy, IPCC involvement – or lack thereof)
* E. Reflections on Career and Colleagues
* 1. Royal Society Fellowship (Honour, responsibilities, supporting others)
* 2. Mentors and collaborators (Batchelor, Bretherton, Charney, Phillips, Gough, Spiegel, Crighton, Hoskins, Palmer etc.)
* 3. Experience of being interviewed for National Life Stories
"""

if __name__ == "__main__":
    # summarize.DEMO_MODE = True
    resp = summarize.generate_summaries(1, test_bio)
    # pretty print the response.text json
    print(json.dumps(resp, indent=2))

    # save the response to a file
    # with open('response.json', 'w') as f:
    #     json.dump(resp, f, indent=2)