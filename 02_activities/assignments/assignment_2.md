# Data Visualization

## Assignment 2: Good and Bad Data Visualization

### Requirements:

- Data visualizations are important tools for communication and convincing; we need to be able to evaluate the ways that data are presented in visual form to be critical consumers of information 
- To test your evaluation skills, locate two public data visualizations online, one good and one bad  
    - You can find data visualizations at https://public.tableau.com/app/discover or https://datavizproject.com/, or anywhere else you like! 
- For each visualization (good and bad):  
    - Explain (with reference to material covered up to date, along with readings and other scholarly sources, as needed) why you classified that visualization the way you did.
      ```
      GOOD EXAMPLE: Tableau Public, "Social Media Performance Hub" by Pooja Deshmukh
      Link: https://public.tableau.com/app/profile/pooja.deshmukh5909/viz/SocialMediaPerformanceHub/KPISummary

      I classify Pooja Deshmukh's "Social Media Performance Hub" as a good visualization because it is designed around a clear dashboard purpose: summarizing digital marketing performance through KPIs such as impressions, clicks, and conversion rates. First, the chart is task-oriented. A viewer can quickly scan the most important measures before looking for more detailed platform-level patterns. This follows the course idea that the visualization should match the audience's task. Second, the dashboard uses familiar business encodings such as KPI cards, comparisons, and trend views, which reduce the learning curve for a marketing or management audience. Third, it tells a focused story about effectiveness rather than only displaying raw activity counts. By bringing impressions, clicks, and conversion rates into one view, it helps the viewer move from "how much activity happened?" to "how well did the activity perform?"

      The visualization is also relatively accessible for its intended context because it organizes information into predictable dashboard sections and avoids unusual chart forms. D'Ignazio and Klein (2020) remind us that visualizations are rhetorical objects because design choices shape interpretation; here, the rhetoric supports practical decision-making.

      BAD EXAMPLE: Tableau Public, "Fuel Prices in the UK | #MOM2026 WEEK20" by Tsutomu Ikeda
      Link: https://public.tableau.com/app/profile/ikeda.tsutomu/viz/MOM2026WEEK20FuelPricesintheUK/1

      I classify Tsutomu Ikeda's "Fuel Prices in the UK" as a bad visualization for general communication because the circular line chart makes a time-series pattern harder to read than it needs to be. Tableau Public describes the dashboard as showing UK fuel price trends from 2013 to 2026 and highlighting geopolitical shocks and energy costs. First, a circular line chart is less effective for comparing time values than a standard line chart with a shared horizontal time axis. The viewer has to decode time as rotation, which increases cognitive load. Second, it can make exact trend comparison difficult, especially when prices change gradually or when multiple periods overlap visually. Third, the unusual form may attract attention, but it risks making the design more decorative than explanatory.

      This visualization is not dishonest, and the topic is important, but the form does not best serve the data. Fuel prices are naturally temporal, so a conventional time-series chart would allow viewers to see before-and-after changes around events more directly. From an accessibility perspective, the circular layout may also be harder to describe in text and harder to read on small screens.
      ```
    - How could this data visualization have been improved?  
      ```
      GOOD EXAMPLE IMPROVEMENTS

      One improvement would be to add or emphasize short annotations that explain the most important changes, such as which platform has the strongest conversion rate or where engagement drops. This would make the dashboard's story easier to grasp without requiring the viewer to inspect every KPI.

      A second improvement would be to include a plain-language text summary or alt text for the dashboard. Fossheim (2020) and the course accessibility slides emphasize that the key message should not depend only on visual perception. A summary of the top-performing platform, weakest metric, and main trend would make the visualization more accessible.

      BAD EXAMPLE IMPROVEMENTS

      The main improvement would be to replace the circular line chart with a standard line chart using time on the x-axis and fuel price on the y-axis. This would align with the course principle of choosing encodings that viewers can compare accurately. It would also make the relationship between geopolitical events and price changes easier to see.

      A second improvement would be to add event annotations and a small table of key prices before and after major shocks. This would preserve the narrative goal while making the evidence clearer. If the viewer's task is to understand price change over time, the design should make time, magnitude, and turning points quick to compare.

      References: Tableau Public. (2026). Viz of the Day channel. https://public.tableau.com/app/discover/viz-of-the-day ; Deshmukh, P. (2026). Social Media Performance Hub. https://public.tableau.com/app/profile/pooja.deshmukh5909/viz/SocialMediaPerformanceHub/KPISummary ; Ikeda, T. (2026). Fuel Prices in the UK | #MOM2026 WEEK20. https://public.tableau.com/app/profile/ikeda.tsutomu/viz/MOM2026WEEK20FuelPricesintheUK/1 ; D'Ignazio, C., & Klein, L. (2020). Data Feminism, Chapter 3. https://data-feminism.mitpress.mit.edu/pub/5evfe9yd/release/5 ; Fossheim, S. L. (2020). An intro to designing accessible data visualizations. https://fossheim.io/writing/posts/accessible-dataviz-design/
      ```
- Word count should not exceed (as a maximum) 500 words for each visualization (i.e. 
300 words for your good example and 500 for your bad example)

### Why am I doing this assignment?:

- This assignment ensures active participation in the course, and assesses the learning outcomes
* Apply general design principles to create accessible and equitable data visualizations
* Use data visualization to tell a story

### Rubric:

| Component               | Scoring   | Requirement                                                 |
|-------------------------|-----------|-------------------------------------------------------------|
| Data viz classification and justification | Complete/Incomplete | - Data viz are clearly classified as good or bad<br />- At least three reasons for each classification are provided<br />- Reasoning is supported by course content or scholarly sources |
| Suggested improvements  | Complete/Incomplete | - At least two suggestions for improvement<br />- Suggestions are supported by course content or scholarly sources |

## Submission Information

🚨 **Please review our [Assignment Submission Guide](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md)** 🚨 for detailed instructions on how to format, branch, and submit your work. Following these guidelines is crucial for your submissions to be evaluated correctly.

### Submission Parameters:
* Submission Due Date: `23:59 -  2026-06-09`
* The branch name for your repo should be: `assignment-2`
* What to submit for this assignment:
    * This markdown file (assignment_2.md) should be populated and should be the only change in your pull request.
* What the pull request link should look like for this assignment: `https://github.com/<your_github_username>/visualization/pull/<pr_id>`
    * Open a private window in your browser. Copy and paste the link to your pull request into the address bar. Make sure you can see your pull request properly. This helps the technical facilitator and learning support staff review your submission easily.

Checklist:
- [ ] Create a branch called `assignment-2`.
- [ ] Ensure that the repository is public.
- [ ] Review [the PR description guidelines](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md#guidelines-for-pull-request-descriptions) and adhere to them.
- [ ] Verify that the link is accessible in a private browser window.

If you encounter any difficulties or have questions, please don't hesitate to reach out to our team via our Slack. Our Technical Facilitators and Learning Support staff are here to help you navigate any challenges.
