# Visualization 2: Recent KSI Collision Events by Neighbourhood

**Dataset:** City of Toronto Open Data, [Motor Vehicle Collisions Involving Killed or Seriously Injured Persons](https://open.toronto.ca/dataset/motor-vehicle-collisions-involving-killed-or-seriously-injured-persons/)

**Software used:** I made this visualization with Plotly. I kept the data cleaning in Python and exported both an interactive HTML file and a static PNG so it is easy to review.

**Intended audience:** This chart is for people who want to compare where recent severe collisions are happening in Toronto. I was thinking of community members, local councillors, planners, and road-safety advocates.

**Message:** The main message is that KSI collisions are not spread evenly across the city. From 2021 to 2025, some neighbourhoods had much higher counts than others, including West Humber-Clairville, St Lawrence-East Bayfront-The Islands, and South Riverdale. I also wanted to show that many of these collisions involved pedestrians, cyclists, motorcyclists, or micromobility users, not only people inside cars.

**Design choices:** I used a horizontal bar chart because the neighbourhood names are long, and they are much easier to read this way. I sorted the bars by total collisions so the highest areas stand out quickly. I split each bar into two parts to show whether a vulnerable road user was involved. The interactive version lets the viewer hover for values, while the PNG works as a simple static version.

**Reproducibility:** The same Python script downloads the public CSV and recreates the chart. It groups the data by collision ID, makes a vulnerable-road-user flag from the pedestrian, cyclist, motorcyclist, and micromobility columns, filters to 2021-2025, and keeps the top 12 neighbourhoods by count.

**Accessibility:** I used a horizontal layout, readable labels, and colours that should be easier to distinguish than a red/green pair. The legend explains what each colour means, and the static PNG means the main point can still be understood without using the interactive HTML.

**Impacted people and communities:** This kind of neighbourhood comparison can affect where people think road-safety problems are most urgent. It matters for residents, commuters, vulnerable road users, local businesses, and communities that may already be dealing with unsafe streets.

**Feature choices:** I included neighbourhood, year, collision ID, and the columns showing whether pedestrians, cyclists, motorcyclists, or micromobility users were involved. I did not use exact coordinates because I was not making a hotspot map, and I excluded 2026 because it is incomplete.

**Underwater labour:** A lot of the work was behind the scenes: figuring out how to count one collision instead of multiple people, dealing with missing values, choosing a fair time period, deciding that 12 neighbourhoods was readable, and exporting both the HTML and PNG versions.
