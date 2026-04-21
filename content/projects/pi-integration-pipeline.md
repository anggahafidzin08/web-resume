# PI Integration Pipeline

![PI Integration Pipeline Overview](../assets/images/projects/pi-integration-pipeline/fig-1.png)

## Overview

Designed and built a real-time streaming ELT pipeline to move high-volume sensor data from the on-prem AVEVA PI System into Snowflake, using PI Integrator for Business Analytics, Kafka Confluent, and Snowpipe — replacing slow batch-loading with continuous streaming ingestion.

## Project Background

AMNT (Amman Mineral Nusa Tenggara) operates a mining facility that relies heavily on real-time monitoring of critical equipment and processes. The AVEVA PI System served as the primary repository for real-time sensor data — including equipment status, production metrics, and environmental readings — ingested directly from field devices and sensors.

The challenge was that PI System data was locked in a **high-volume stream format** stored on-premises. Loading data from the PI server became increasingly slow due to the sheer number of rows being generated continuously across all sensor tags. The operations team needed a way to **pull this real-time data into Snowflake** (a cloud data warehouse) for analytics, reporting, and dashboards — without waiting for long-running batch queries against the PI server.

This led to the solution: **PI Integrator for Business Analytics** as the data producer, **Kafka Confluent** as the message broker, and **Snowpipe** as the bridge into Snowflake.

## Solution Architecture

### Data Flow

```
AVEVA PI System (On-Prem)
        ↓
PI Integrator for Business Analytics  (Producer — streams data to Kafka)
        ↓
Kafka Confluent  (Message Broker)
        ↓
Snowpipe  (Ingestion bridge — Kafka to Snowflake)
        ↓
Snowflake  (Cloud Data Warehouse)
        ↓
PowerBI  (User-owned analytics and reporting)
```

### Technology Stack

| Layer            | Technology                           | Purpose                                         |
| ---------------- | ------------------------------------ | ----------------------------------------------- |
| Data Source      | AVEVA PI System (On-Prem)            | Real-time sensor data repository                |
| Data Producer    | PI Integrator for Business Analytics | Publishes PI data streams to Kafka              |
| Message Broker   | Kafka Confluent                      | Durable, scalable message streaming             |
| Ingestion Bridge | Snowpipe                             | Streaming ingestion from Kafka to Snowflake     |
| Data Warehouse   | Snowflake                            | Cloud data warehouse for analytics              |
| Reporting Tool   | PowerBI                              | End-user analytics and reporting (not in scope) |

## Key Responsibilities

1. **Architecture Design** — Designed the end-to-end data flow from PI System to Snowflake using PI Integrator, Kafka Confluent, and Snowpipe
2. **PI Integrator Configuration** — Configured PI Integrator for Business Analytics to produce real-time data streams to designated Kafka topics
3. **Kafka Confluent Management** — Managed the Confluent Kafka cluster including topic creation, schema handling, and consumer group configuration
4. **Snowpipe Integration** — Set up Snowpipe to stream data directly from Kafka topics into Snowflake tables without batch processing
5. **Snowflake Schema Design** — Designed the catalog, database, and schema structure to organize raw streaming data for analytics
6. **Snowflake Tasks** — Created scheduled Snowflake Tasks for data transformation, aggregation, and enrichment
7. **Dashboard & Monitoring** — Set up PowerBI visualization is managed by the user separately

## Data Ingestion with PI Integrator

![PI Integrator for Business Analytics](../assets/images/projects/pi-integration-pipeline/fig-2.png)

Configured **AVEVA PI Integrator for Business Analytics** to publish real-time data streams from PI tags. The integrator continuously produces high-volume messages and publishes them to a designated Kafka topic, serving as the bridge between the PI System and the Kafka cluster.

## Kafka Messaging Layer

![Confluent Kafka Console](../assets/images/projects/pi-integration-pipeline/fig-3.png)

Managed the **Confluent Kafka cluster** for message brokering. All messages from PI Integrator flow through Kafka topics where they are buffered, partitioned, and made available for downstream consumers with built-in fault tolerance and durability.

## Snowflake Integration

![Kafka to Snowflake Connector](../assets/images/projects/pi-integration-pipeline/fig-4.png)

Implemented **Snowpipe streaming** to ingest data directly from Kafka into Snowflake. The Kafka-Snowflake connector on the cluster reads from Kafka topics and streams data into Snowflake tables in real time, eliminating the need for batch loading.

## Data Storage Schema

![Snowflake Database Schema](../assets/images/projects/pi-integration-pipeline/fig-5.png)

Designed the Snowflake **catalog and warehouse schema** to organize incoming streaming data. The raw layer ingests Kafka messages, with proper staging tables and column definitions to support analytics workloads.

## Scheduled Data Processing

![Snowflake Tasks](../assets/images/projects/pi-integration-pipeline/fig-6.png)

Created **Snowflake Tasks** to process streaming data on a periodic basis. These tasks handle data transformation, aggregation, and enrichment — turning raw streaming records into analytics-ready datasets on a scheduled cadence.

## Transformation & Loading Flow

![Transformation and Loading Flow](../assets/images/projects/pi-integration-pipeline/fig-7.png)

Built the complete **ELT pipeline** that transforms raw PI data into business-ready formats. The flow moves data from the raw Kafka payload through cleaning and deduplication steps, applies business logic, and loads final tables for consumption via PowerBI.

## Challenges & Solutions

### 1. PI Integrator to Kafka Configuration

**Challenge:** Configuring PI Integrator for Business Analytics to reliably produce messages to Kafka Confluent topics required careful setup of the message format, topic routing, and authentication between the on-prem PI System and the Kafka cluster.

**Solution:** Set up proper topic destinations in PI Integrator, configured message schemas, and ensured the Kafka producer settings matched the downstream consumer expectations.

### 2. Kafka Topic Design and Schema Handling

**Challenge:** Managing message schemas as new PI tags were added required a scalable approach to schema management without breaking existing consumers.

**Solution:** Used Confluent Schema Registry to manage and version message schemas, ensuring backward compatibility as the pipeline expanded to more sensor tags.

### 3. Snowpipe Streaming Configuration

**Challenge:** Setting up Snowpipe to continuously ingest data from Kafka topics into Snowflake without manual intervention required configuring the Kafka-Snowflake connector properly and managing table definitions.

**Solution:** Configured the Kafka-Snowflake connector on the Confluent cluster, defined Snowflake tables with proper column mappings, and enabled Snowpipe for continuous streaming ingestion.

### 4. Snowflake Schema Design for Streaming Data

**Challenge:** Designing a Snowflake schema that could handle high-volume streaming data efficiently while supporting analytics queries required careful partitioning and staging table design.

**Solution:** Designed a raw/staging/final table structure with proper Snowflake clustering keys and auto-ingest settings to optimize query performance.

### 5. Scheduled Data Processing with Snowflake Tasks

**Challenge:** Transforming and enriching raw streaming data into business-ready datasets on a reliable schedule required orchestrating Snowflake Tasks with proper dependencies and error handling.

**Solution:** Created Snowflake Tasks with DAG-based dependencies to handle data transformation, deduplication, and aggregation on a configurable schedule.

## Results & Impact

| Metric                  | Before                                         | After                                |
| ----------------------- | ---------------------------------------------- | ------------------------------------ |
| Data access             | Slow PI server queries due to large row volume | **Real-time streaming** to Snowflake |
| Report generation       | 50+ manual Excel reports/day                   | Fully automated dashboards           |
| Data latency            | Long load times from on-prem PI server         | **1 second** real-time               |
| Manual effort           | ~4 hours/day of manual work                    | Zero manual intervention             |
| PI tags integrated      | 0 (not accessible for analytics)               | **100+ tags**                        |
| Data delivery guarantee | Occasional data loss                           | **Zero data loss** (exactly-once)    |
| Management visibility   | Delayed, static reports                        | **Real-time access** via PowerBI     |

## Conclusion

This pipeline transformed how AMNT's operations team accessed and used real-time sensor data. By replacing slow batch-loaded PI server queries with a fully automated streaming pipeline, the project delivered immediate operational value — enabling real-time dashboards, advanced analytics, and machine learning use cases on Snowflake.
