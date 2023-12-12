# MTBL - Extract
A script that runs the all MTBL Extract system subprocesses.

## Dependencies
Lg_Manager_Getter --> Rosters_Getter
- all other scripts are independent

## Threading Considerations
- Runtime for synchronous Python is **2min15sec** on MacBP M2 Pro 32GB RAM.
- Runtime for multithreaded Ruby is **1min08sec => 1.99x** speed increase
- the longest running script is the Frangraphs Data Getter which could increase performance by grouping positions and projections v. stats systems.
    - would produce 4 threads
