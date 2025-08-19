---
title: Funding Forest Businesses
subject: Funding
subtitle: An Analysis of CAL FIRE's Business and Workforce Development Grants
short_title: 8. Funding Analysis
authors:
  - name: Vance Russell
    affiliations:
      - 3point.xyz
    email: vance@3point.xyz
license: CC-BY-4.0
keywords: funding, forest business, gaps, geospatial
abstract: |
  To better understand the geographic distribution, success rates, and funding gaps/needs, the Forest Business Alliance undertook a preliminary study examining CAL FIRE's Business and Workforce Development Grants from the first quarter of 2022 through the first quarter of 2025. More funding is needed for the Business and Workforce Development Program Grants—application requests far outstrip the available funding. The top grant receiving counties are Tuolumne, Shasta, Humboldt, Plumas, and Tulare. However, the most successful applications (proportion funded/requested) are from Stanislaus, Sutter, Solano, Alpine, and Siskiyou counties. The largest amount of grants awarded went to the Sierra Cascade (61.6%) and North Coast (31.6%) regions. The applicants' project locations need to be more precise to increase the accuracy of the analysis. Accurate location data for applicants and grantees would also help identify counties and regions with the most need, such as disadvantaged communities.
kernelspec:
  name: python3
  display_name: Python 3
exports:
  - format: pdf
    template: curvenote
    output: exports/8-funding.pdf
    article_type: Report
---

*Chapter updated to include 2025q1 grant awards, 8/20/25*

# Findings
To better understand the geographic distribution, success rates, and funding gaps/needs, the Forest Business Alliance examined CAL FIRE's Business and Workforce Development Grants from the first quarter of 2022 through the first quarter of 2025.[^new]. The analysis of CAL FIRE's Business and Workforce Development Grants Program found the following:

- 💸 **Program Funding**. Funding requests far outstrip the grant funds awarded.[^mn] A steady linear increase in funds requested from 2022-2025 has been counterbalanced by a steep decline in grants funded. For Q1 2025, approximately \$85.7 million in requests from more than 100 proposed projects were made, with \$5 million awarded. To date, the total program requests since 2022 are just north of $457 million, with \$105.7 million funded.
- 🏆 **Top 10 Counties**. The top 10 grant-receiving counties in order were Tuolumne, Shasta, Humboldt, Plumas, Tulare, Yolo, Placer, Siskiyou, Fresno, and Sonoma Counties.
- 🚫 **No Funding**. The counties that have not yet received funds are Colusa, Del Norte, Imperial, Inyo, Kern, Kings, Merced, and Santa Barbara. Imperial is the sole county not making a funding request and is unlikely to do so given its landscape dominated by desert and agriculture.
- 📊 **Regions**. As of March 2024, the largest portion of grants were awarded to the Sierra Cascade (61.6%) and North Coast (31.6%) regions. The Central Coast (5.2%) and Southern California (1.6%) were far behind, although both regions' requests have increased substantially during the last two grant solicitations.
- 🥇 **Success Rates**. The counties with the highest grant success rate (proportion awarded/requested) were Stanislaus, Sutter, Solano, Alpine, Siskiyou, Lake, Modoc, Mariposa, Santa Cruz, and San Benito counties. However, a bivariate analysis simultaneously examining requested and awarded amounts showed that the most successful counties (high amount awarded with the low amount requested) were Alpine, San Francisco, Sacramento, San Joaquin, Sutter, and Ventura Counties.
- 📍 **Analysis & Location**. The applicants' project locations need to be more precise to increase the accuracy of the analysis. Accurate location data for applicants and grantees would also help identify counties and regions with the most need, such as disadvantaged communities.

[^new]: New data and analysis will be added during subsequent grant rounds.
[^mn]: Forest product infrastructure development is a state priority for wildfire mitigation. Sustainable infrastructure to process wood biomass in California and workforce development are critical elements of the <a href="https://wildfiretaskforce.org/wp-content/uploads/2022/04/roadmap-to-million-acres_2022.pdf" target="_blank">Roadmap to a Million Acres</a>.

# Background
Prior to European settlement, fires were commonly utilized throughout California by Tribal communities as a tool for managing food, game, disease, and community safety. Approximately 4.4 million acres burned annually in California before 1800 ([Stephens et al. 2007](https://doi.org/10.1016/j.foreco.2007.06.005)). This acreage is far more than in recent years but likely differs in the total acres burned at high severity. Fast forward—fire suppression, severe drought, and climate change have created forest ecosystems well outside their natural conditions, making them prone to severe wildfires and negatively affecting habitats and communities.

```{figure} ../figures/fund/health.png
:name: health
Simplified forest health theory of change.
```

This century's increase in large fires has underscored the urgent need for forest health projects. These projects aim to thin unhealthy forest stands and reintroduce fire into forested ecosystems ({numref}`health`). However, they have also created a new challenge—excess wood and biomass that pose additional wildfire risks. California is in dire need of more infrastructure and workforce capacity to manage this situation effectively. The USDA Forest Service's Wood Innovations Grant Program encourages development of wood products and processing at local to regional scales. At the state level, CAL FIRE created the Wood Products and Bioenergy Program with the first grants awarded in 2022. Both programs aim to fund projects that process woody biomass and build capacity for work in the woods.

# Methods
The funding analysis examined awards by county from 2022-2025 ({numref}`awarded_ca`). The funding data is available on CAL FIRE's Wood Products & Bioenergy website. We extracted the requested and awarded data from the website and added them to an Excel file. We added a sub-categorization of projects by type. 

To conduct the analysis, we excluded statewide grants since they could not be geographically assigned. For projects covering multiple counties, we averaged the total requests and awards across each county identified for the project. The data was compiled in Excel and then joined to a county spatial layer (California Tiger Census) and a vegetation layer (Calveg) to create the spatial database. 

The spatial analysis was completed using ArcGIS Pro. See [Local Bivariate Relationship](https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-statistics/learnmore-localbivariaterelationships.htm) for an explanation of the bivariate analysis tool. 

Graphs were produced within Excel using power pivot and pivot charts.

# Analysis

## Awarded
Total amounts awarded by county are shown in {numref}`awarded_ca`. The darker green counties indicate a higher amount awarded whereas purples and blues indicate lower amounts. 

```{figure} ../figures/fund/awarded_ca.png
:name: awarded_ca
Awarded grants by California County from 2022-25. Numbers in thousands $USD.
```
### Norcal
Not surprisingly, the highest number of grant requests for the Business and Workforce Development Grant Program is in the northern part of the state, with most from the Sierra Nevada ({numref}`norcal-fig`). Surprisingly, some agriculturally dominant counties rank highly, e.g., Yolo County, partly because large bioenergy projects were funded there.

```{figure} ../figures/fund/norcal.png
:name: norcal-fig
Business & Workforce Development grant funding in Northern California.
```

### Socal
Before 2024, only two counties in Southern California had projects with funding: San Luis Obispo and Ventura. However, this changed substantively in the 2024 first quarter grant round when all but Santa Barbara, Kern, and Imperial Counties had received funding ({numref}`socal-fig`) and increased significantly for requests in the last grant round of 2025. 

Much of Southern California is characterized by chaparral and desert landscapes, and fire mitigation in this region focuses on preventing ignition sources rather than thinning forests or processing wood products. As a result, there are fewer proposals, and many of the requests are focused on workforce development. 

```{figure} ../figures/fund/socal.png
:name: socal-fig
Grant funding in Southern California.
```

## Bivariate
A bivariate analysis, which queries the data by total requests and awards, paints a slightly different picture than the awards analysis ({numref}`biv`). Where the success rate is the relationship between funded and requested grants, the lightest shades tend to indicate low success rates, whereas the light blue to dark purple indicates counties with high grant success rates.

```{figure} ../figures/fund/biv.png
:name: biv
Bivariate analysis comparing amounts of requested to awarded grants.
```

{numref}`biv` reveals some Southern California counties have requested grants but not been successful (e.g., San Luis Obispo, Kern, Orange, Riverside). Ventura County has a high success rate (high awarded to requested, shown in light blue). In the rest of the state, Sacramento, San Francisco, Sutter, and Alpine Counties show similar high success rates. In contrast, counties such as Tulare, Plumas, and Shasta have received a large amount of funding but have also made many requests.

## Gaps
The total funding requests and awards by county reveal the divide between the northern and southern portions of the state (Figure {numref}`chart`). The largest number of grants requested and awarded were in the Sierra Cascade Region. Nevertheless, the totals do not fully explain the project quality in the region. For instance, Inyo, Kings, and Merced have not funded any projects. The Forest Business Alliance addresses the lack of capacity in each entity's ability to apply for grants to strengthen sustainable forest businesses and process more wood, ultimately increasing forest health across the state.

```{figure} ../figures/fund/chart.png
:name: chart
:height: 400px
Stacked bar chart of requested and awarded grants by Wildfire Task Force Region and county.
```

<span style="font-size:12px !important; font-weight:normal !important; color:#444 !important; text-decoration:none !important;">
  <a href="../figures/fund/chart.png" target="_blank" style="font-size:12px !important; font-weight:normal !important; color:#444 !important; text-decoration:none !important;">Click to zoom figure</a>
</span> <br>

Funding by project type showed the most funding for workforce development training, biomass, transportation, and equipment projects ({numref}`type`). Business development, marketing, and thinning projects were the least funded project types.

```{figure} ../figures/fund/type.png
:name: type
:height: 300px
Awarded grants by project type.
```

The number of unfunded projects by county reveals interesting patterns ({numref}`nofund`). Some counties with the most unsuccessful applications are in the Sierra Cascade Region, e.g., Tuolumne, Shasta, and Plumas. Counties with low success rates submitted fewer proposals, e.g., Inyo, Kings, and Alpine.

```{figure} ../figures/fund/nofund.png
:name: nofund
:height: 400px
Unfunded requests by California County.
```

<span style="font-size:12px !important; font-weight:normal !important; color:#444 !important; text-decoration:none !important;">
  <a href="../figures/fund/nofund.png" target="_blank" style="font-size:12px !important; font-weight:normal !important; color:#444 !important; text-decoration:none !important;">Click to zoom figure</a>
</span> <br>

## Temporal
The Business and Workforce Development Program funding changed substantially from 2022, when it started. {numref}`temp` shows the requested and awarded grants by year and region, with larger amounts requested from the Sierra and Central Coast. However, the Central Coast and Southern California have started to catch up in requests. Socal has not caught up in successful grants, however.

```{figure} ../figures/fund/temp.png
:name: temp
:height: 300px
Requested and awarded grants by year and region.
```

<span style="font-size:12px !important; font-weight:normal !important; color:#444 !important; text-decoration:none !important;">
  <a href="../figures/fund/temp.png" target="_blank" style="font-size:12px !important; font-weight:normal !important; color:#444 !important; text-decoration:none !important;">Click to zoom figure</a>
</span> <br>

# Next
The Forest Business Alliance will continue to add new projects to the Business and Workforce Development funding analysis database in response to new grant solicitations. We recommend the following:

- **Location**. More accurate project locations, e.g., latitude/longitude points, should be added to reflect where the funding is directed and to examine the relationship between forest health and wood products businesses. We will include new analyses, such as with new projects that are funded through subsequent grant rounds, how do the funding success rates change geographically and temporally?
- More analysis is needed to determine the reasons for the county and regional differences. Is it organizational and business capacity? Is it related to the capabilities to create strong projects and proposals? Could it be something more pervasive, such as regional economic differences or the availability of institutional support for potential applicants?
- Given the need for wildfire mitigation in the state, the bottleneck of processing biomass in a sustainable manner, and the mismatch in requested vs. funded businesses, we highly recommend the state consider increasing funding for this valuable program.

# Funding
Funding for the Forest Business Alliance is provided by the CAL FIRE Business and Workforce Development Grant Program and Yuba Water Agency. [CAL FIRE's Wood Products and Bioenergy Program](https://www.fire.ca.gov/what-we-do/natural-resource-management/climate-and-energy-program/wood-products-and-bioenergy) manages the BWD grants and works to maintain and enhance California's wood products infrastructure to support healthy, resilient forests and the people and ecosystems that depend on them.

[The Forest Business Alliance](https://www.forestbusinessalliance.org) provides technical assistance, workshops, and a peer-learning network to increase local and regional capacity for California wood products and forest health. Funding for this project is provided by CAL FIRE's [Business and Workforce Development Grants](https://www.youtube.com/watch?v=ycVSe4K3EZQ). Don't hesitate to contact us at forestbusinessalliance@gmail.com for any questions or feedback.

```{image} ../calfire.png
:height: 200px
:name: calfire
```
