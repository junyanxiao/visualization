# Visualization 1: Toronto KSI Collision Events Over Time

**Dataset:** City of Toronto Open Data, [Motor Vehicle Collisions Involving Killed or Seriously Injured Persons](https://open.toronto.ca/dataset/motor-vehicle-collisions-involving-killed-or-seriously-injured-persons/)

**Software used:** I made this chart in Python. I used pandas to clean and group the data, and Matplotlib to make the final PNG.

**Intended audience:** My main audience is people in Toronto who want a quick picture of road safety over time. This could include residents, road-safety advocates, or City staff.

**Message:** The main thing I wanted to show is that KSI collision events are lower than they were in 2006, but the pattern is not a simple steady decline. There are still years where the numbers go back up, especially around 2022 and 2023. I left out 2026 because it is only a partial year in the dataset, so comparing it to full years would be misleading.

**Design choices:** I chose a stacked bar chart because I wanted the total number of KSI collisions to be easy to compare by year, while still showing how many involved a fatality. I used bar length as the main visual cue because it is easier to read than something like pie slices. I also added two annotations, one for the peak year and one for 2025, so the reader does not have to search for those points. I kept the colours simple and avoided extra decoration because the topic is serious.

**Reproducibility:** The code downloads the CSV from Toronto Open Data, cleans it, groups the person-level rows into unique collision events, removes the incomplete 2026 year, and saves the chart. If someone reruns the script, they should get the same chart unless the City updates or corrects the dataset.

**Accessibility:** I used a large title, readable axis labels, a legend, and high-contrast colours. The chart is not only understandable through colour because the legend explains the stacked sections and the y-axis shows the actual count scale.

**Impacted people and communities:** This data is about people who were killed or seriously injured, so the chart affects more than just transportation planning. It connects to victims, families, pedestrians, cyclists, drivers, neighbourhood residents, emergency responders, and people making road-design decisions.

**Feature choices:** I used the date, year, collision ID, and severity fields. I did not include details like age, driver action, or safety equipment because this chart is about the overall trend, not the circumstances of each collision.

**Underwater labour:** The less visible work was finding a useful dataset, reading the notes and limitations, realizing that each row was a person rather than one collision, deciding to count unique collision IDs, and checking that the fatal/non-fatal categories were being handled correctly.
