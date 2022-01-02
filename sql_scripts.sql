/* alias */
SELECT time_log.activity_id as activity, time_log.broker_id as broker
FROM time_log; 


/* WHERE clause */ 
SELECT  time_log.activity_id as activity, time_log.broker_id as broker
FROm time_log
WHERE activity = 3; 


/* aliases and WHERE clause */
SELECT 
 time_log.start_time as start,
 time_log.end_time as end,
 time_log.activity_id as activity,
 time_log.broker_id as broker 
 FROM time_log
WHERE activity = 1 OR  activity = 3;


/* foreign key relationshipts */
SELECT
 time_log.start_time as start,
 time_log.end_time as end,
 time_log.activity_id,
 activity
FROM time_log
    LEFT JOIN activity_log
    WHERE time_log.activity_id = activity_log.activity_id

/* foreign key relationshipts */
SELECT
 time_log.start_time as start,
 time_log.end_time as end,
 time_log.activity_id,
 activity
FROM time_log
    LEFT JOIN activity_log
    ON time_log.activity_id = activity_log.activity_id


/*two foreign keys and two LEFT JOIN ON */
SELECT
 time_log.start_time as start,
 time_log.end_time as end,
 time_log.activity_id,
 activity,
 time_log.broker_id,
 broker
FROM time_log
    LEFT JOIN activity_log
    ON time_log.activity_id = activity_log.activity_id

    LEFT JOIN brokers
    ON time_log.activity_id = brokers.broker_id

/*two foreign keys, two LEFT JOIN ON, and a conditional WHERE clause */
SELECT
 time_log.start_time as start,
 time_log.end_time as end,
 time_log.activity_id,
 activity,
 time_log.broker_id,
 broker
FROM time_log
    LEFT JOIN activity_log
    ON time_log.activity_id = activity_log.activity_id

    LEFT JOIN brokers
    ON time_log.activity_id = brokers.broker_id
WHERE activity LIKE 'trading%'


SELECT
 time_log.start_time as start,
 time_log.end_time as end,
 time_log.activity_id,
 activity,
 time_log.broker_id,
 broker
FROM time_log
    LEFT JOIN activity_log
    ON time_log.activity_id = activity_log.activity_id

    LEFT JOIN brokers
    ON time_log.activity_id = brokers.broker_id
WHERE activity LIKE 'trading%'
OR activity LIKE 'accounting%'


/*two foreign keys, two LEFT JOIN ON, two conditional WHERE OR clauses */
SELECT
 time_log.start_time as start,
 time_log.end_time as end,
 time_log.activity_id,
 activity,
 time_log.broker_id,
 broker
FROM time_log
    LEFT JOIN activity_log
    ON time_log.activity_id = activity_log.activity_id

    LEFT JOIN brokers
    ON time_log.activity_id = brokers.broker_id
WHERE activity LIKE 'trading%'
OR activity LIKE 'accounting%'

/* two foreign keyS, LEFT JOIN ON, conditional WHERE OR clauses, case insensitivity */
SELECT
 time_log.start_time as start,
 time_log.end_time as end,
 time_log.activity_id,
 activity,
 time_log.broker_id,
 broker
FROM time_log
    LEFT JOIN activity_log
    ON time_log.activity_id = activity_log.activity_id

    LEFT JOIN brokers
    ON time_log.activity_id = brokers.broker_id
WHERE broker LIKE 'forex%'
OR activity LIKE 'TRADING%'































