# ADF Watermark Pipeline

![Initial Watermark Process](../assets/images/projects/adf-watermark-pipeline/fig-1.png)

## Overview

Designed and built an Azure Data Factory (ADF) watermark pipeline that automates incremental data extraction from multiple SQL Server tables into Snowflake using watermark-based change tracking. This solution replaced dozens of individual pipelines with a single reusable pattern, reducing operational complexity and enabling near-real-time data synchronization.

## Project Background

AMNT's data estate includes multiple SQL Server databases containing operational data that needed to be consolidated into Snowflake for analytics. Traditionally, each source table required its own ADF pipeline for incremental loading — creating a **proliferation of pipelines** that were:

- **Hard to manage** — dozens of pipelines to monitor, update, and troubleshoot
- **Error-prone** — each pipeline had its own logic, making consistency difficult
- **Not scalable** — adding a new source table meant building an entirely new pipeline

The solution was a **watermark-based pipeline pattern** that could dynamically handle multiple tables through a single, reusable architecture.

## Solution Architecture

### Data Flow

```
SQL Server (On-Prem)
        ↓
Azure Data Factory (Watermark Pipeline)
        ↓
For Each Loop → Lookup → If Condition → Copy Activity
        ↓
Snowflake (via Copy Activity Sink)
```

### How the Watermark Process Works

![Inside For Each Loop Activities](../assets/images/projects/adf-watermark-pipeline/fig-2.png)

The watermark pipeline operates in a **For Each Loop** that iterates over each watermark reference table stored in the `WTMARK_DB` schema. For each reference table:

1. **Lookup Activity** — Reads the last watermark value (e.g., last `ModifiedDate`) from the reference table
2. **If Condition Activity** — Checks if any records in the source table have a watermark value greater than the stored value
3. **Copy Activity** — Executes only when new records are detected; copies new rows and updates the watermark value

This approach ensures **only changed data is copied**, minimizing load on source systems and Snowflake.

## Key Responsibilities

1. **Architecture Design** — Designed the watermark-based pipeline pattern for ADF, selecting the For Each Loop + Lookup + If Condition + Copy activity flow
2. **Watermark Schema Design** — Created and maintained the `WTMARK_DB` schema in Snowflake containing reference tables for each source table
3. **ADF Pipeline Development** — Built the pipeline with dynamic source/sink configurations to handle multiple tables without code changes
4. **Copy Activity Configuration** — Configured Copy Activities with parameterized queries to extract only new records based on watermark values
5. **Error Handling & Monitoring** — Implemented ADF alerting and monitoring for pipeline health and failure notifications

## Watermark Reference Table Structure

![Detailed Watermark Reference Table](../assets/images/projects/adf-watermark-pipeline/fig-3.png)

Each watermark reference table in the `WTMARK_DB` schema contains:

| Column | Description |
|--------|-------------|
| `TABLE_SCHEMA` | Source table schema name |
| `TABLE_NAME` | Source table name |
| `WATERMARK_COLUMN` | Column used for change tracking (e.g., `ModifiedDate`) |
| `LAST_WATERMARK_VALUE` | Last processed watermark value |
| `LAST_LOAD_TIMESTAMP` | Timestamp of last successful load |

This metadata-driven approach allows the pipeline to be **table-agnostic** — new tables are added simply by inserting a new row into the reference table.

## Activities Breakdown

### Lookup Activity

![Lookup Activity Configuration](../assets/images/projects/adf-watermark-pipeline/fig-4.png)

The Lookup Activity reads the watermark reference table to get the last processed value for the current source table. This value is passed as a parameter to the subsequent Copy Activity.

### If Condition Activities

![True Activities](../assets/images/projects/adf-watermark-pipeline/fig-5.png)

![False Activities](../assets/images/projects/adf-watermark-pipeline/fig-6.png)

![When New Records Are Available](../assets/images/projects/adf-watermark-pipeline/fig-7.png)

The If Condition Activity evaluates whether new records exist based on the watermark comparison:

- **True branch** — Executed when new records are found; proceeds to Copy Activity
- **False branch** — Executed when no new records exist; skips the copy and logs no-op

### Copy Activity Configuration

![Copy Data Source Configuration](../assets/images/projects/adf-watermark-pipeline/fig-8.png)

![Copy Data Sink Configuration](../assets/images/projects/adf-watermark-pipeline/fig-9.png)

The Copy Activity is configured with:

- **Source**: SQL Server query parameterized by the watermark value from Lookup
- **Sink**: Snowflake stage or direct table write
- **Mapping**: Dynamic column mapping to handle schema differences between source and destination

## Challenges & Solutions

### 1. Automating Incremental Load for Multiple Tables

**Challenge:** Managing dozens of individual pipelines — one per table — was unsustainable as the number of source tables grew.

**Solution:** Built a For Each Loop-driven architecture that reads watermark reference tables and iterates through each table dynamically. A single pipeline now handles all tables.

### 2. Watermark Value Tracking Across Tables

**Challenge:** Each source table had its own watermark column and last processed value, requiring a scalable tracking mechanism.

**Solution:** Created a dedicated `WTMARK_DB` schema in Snowflake containing watermark reference tables. The pipeline looks up the last watermark value before each copy, making the process stateless and repeatable.

### 3. Dynamic Source Table Handling

**Challenge:** Source tables had varying schemas, making it difficult to build a one-size-fits-all Copy Activity.

**Solution:** Configured Copy Activity with dynamic source queries and sink mappings using ADF parameters, so new tables can be added without modifying the pipeline code.

### 4. Preventing Duplicate Data Loads

**Challenge:** Copy Activity failing mid-load could result in duplicate records or missed updates if not handled properly.

**Solution:** Implemented conditional copy logic: Copy Activity only executes when new records are detected, and the watermark value is updated **after** a successful copy within the same loop iteration.

## Results & Impact

| Metric | Before | After |
|--------|--------|-------|
| Pipelines to manage | Dozens of individual ADF pipelines | **1 reusable watermark pipeline** |
| New table onboarding | Build entirely new pipeline | **Add row to watermark reference table** |
| Data freshness | Manual or batch-triggered | **Automated near-real-time sync** |
| Operational overhead | High — each pipeline needs monitoring | **Single pipeline with centralized monitoring** |
| Data duplication risk | Moderate | **Eliminated via conditional copy logic** |

## Conclusion

The ADF Watermark Pipeline transformed how AMNT handles incremental data loading from SQL Server to Snowflake. By introducing a metadata-driven, reusable pattern, the project reduced pipeline management overhead, improved data freshness, and established a scalable foundation for adding new source tables without additional development effort.
