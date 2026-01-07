```mermaid
flowchart TB
    subgraph Flyte
        T1[Extract Tasks]
        T2[Write Bronze]
        T3[Transform Silver]
        T4[Load Dimensions]
        T5[Load Facts]
    end

    subgraph Bronze
        B1[Raw Delta Tables<br/>Partitioned]
    end

    subgraph Silver
        S1[Validated & Enriched Data]
        S2[Dim Tables]
        S3[Fact Tables]
    end

    subgraph Gold
        G1[Denormalized Tables]
    end

    T1 --> T2
    T2 --> B1
    B1 --> T3
    T3 --> S1
    S1 --> T4
    S1 --> T5
    T4 --> S1
    T5 --> S2
    S1 --> G1
    S2 --> G1
