# Global Superstore Sales & Profit Dashboard

## 1. Dataset and Decision-Maker

### Dataset

This project uses the Global Superstore dataset,
which contains sales, quantity, discount, profit,
shipping cost, and order priority information.

The dataset is used to explore sales performance
and profitability across different order categories.

The dataset source and observation period should be
verified against the original data documentation.

### Decision-Maker

The primary user is a retail sales manager.

The manager needs to understand which order categories
contribute to sales and profit, and whether some
sales patterns require further investigation.

The dashboard focuses on three questions:

1. How much sales revenue and profit are generated?
2. How do sales differ across order priorities?
3. How are discounts associated with profitability?

## 2. Why Build a Dashboard?

A sales manager may otherwise need to inspect spreadsheets
and manually calculate performance indicators.

This makes it difficult to compare categories quickly
and repeatedly.

The dashboard brings the key indicators and visualizations
together in one interface.

It also allows users to filter records by order priority
and discount range.

The dashboard supports sales monitoring and investigation.
It does not automatically determine business policies.

## 3. Dashboard Design Decisions

### Headline Metrics

The dashboard displays three headline metrics:

- Total Sales
- Total Profit
- Total Quantity

These metrics provide a concise overview of performance.

Total Sales measures the sales value of the selected records.

Total Profit measures their combined recorded profit.

Total Quantity measures the total quantity recorded
in the selected records.

All three metrics respond to the dashboard filters.

### Supporting Charts

**Chart 1: Sales by Order Priority**

This chart compares total sales across order priorities.

It helps the manager understand how sales are distributed
across the available priority categories.

Order priority should not be interpreted as a direct
measure of customer value or profitability.

**Chart 2: Sales vs. Profit**

This scatter plot compares sales and profit at the
record level.

It helps identify observations with high sales but
low or negative profit.

These observations may warrant further investigation.

**Chart 3: Average Profit by Discount**

This chart compares average recorded profit across
discount levels.

It helps the manager investigate whether profitability
differs between discount levels.

The chart shows an association rather than proving
that discounts cause changes in profit.

### Interactive Filters

The dashboard includes filters for order priority
and discount range.

These filters allow users to focus on selected
segments and examine how the metrics change.

### What I Chose Not to Show

**1. Every available column in the main dashboard.**

Showing every field would make the dashboard crowded
and reduce attention to the main business questions.

I prioritize sales, profit, quantity, discount,
and order priority because they directly support
the selected analysis.

**2. A separate chart for every variable.**

A large number of charts would increase complexity
without necessarily improving decisions.

I selected a small group of visualizations that
focus on sales performance and profitability.

A detailed data table is available only when the user
chooses to expand it.

### Data Limitations

The current dataset is a static historical snapshot.

It does not necessarily represent current sales activity.

The observation period, currency, definitions of sales
and profit, and meaning of each row should be verified
against the original dataset documentation.

Missing values and duplicate records should be checked.

Results may also be affected by differences in product
mix, customer segments, shipping costs, and other factors.

The observed relationship between discounts and profit
does not establish a causal relationship.

## 4. Data Refresh Plan

### Proposed Refresh Frequency

For a real retail business, I would recommend refreshing
the dashboard weekly as a starting point.

A business with rapidly changing sales activity may
benefit from daily updates.

The appropriate frequency depends on how quickly new
transactions arrive and how often managers need to act.

### Review Frequency

A sales manager could review the dashboard weekly
to monitor sales and profitability.

More frequent reviews may be appropriate during
promotional periods.

### Monitoring Metric

Total Profit and average profit by discount level
are useful metrics to monitor.

For example, a manager could investigate a segment
if its average profit falls below its recent baseline.

The threshold should be established using historical
variation and the business's financial objectives.

### Cost of Stale Data

Outdated data may lead to decisions based on
incomplete sales or profit information.

Weekly updates may be sufficient for routine review,
but daily updates may be preferable during
promotional periods.

### Current Project vs. Production System

The current application uses a static dataset
and does not automatically retrieve new transactions.

The proposed refresh frequency describes a possible
production workflow rather than an existing
automatic update feature.

## 5. Summary

This dashboard helps retail sales managers monitor
sales and profitability and investigate differences
across order priorities and discount levels.

It prioritizes a small number of meaningful indicators
and interactive charts rather than displaying every
available variable.

The main goal is to support clear, evidence-based
business decisions.
