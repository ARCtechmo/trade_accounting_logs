/* test for alias */
/* 
SELECT time_log.activity_id as activity, time_log.broker_id as broker
FROM time_log; 
*/

/* test WHERE clause */
/* 
SELECT  time_log.activity_id as activity, time_log.broker_id as broker
FROm time_log
WHERE activity = 3; 
*/

/* test aliases and WHERE clause */
/*
SELECT 
 time_log.start_time as start,
 time_log.end_time as end,
 time_log.activity_id as activity,
 time_log.broker_id as broker 
 FROM time_log
WHERE activity = 1 OR  activity = 3;
*/

/* no errors */
/*
 SELECT
 time_log.start_time as start,
 time_log.end_time as end,
 time_log.activity_id as activity,
 time_log.broker_id as broker
FROM time_log 
  LEFT JOIN activity_log ON activity_log.activity_id = activity
  LEFT JOIN brokers ON brokers.broker_id = broker 

/* no errors but no output --- test different methods to get this to work */
SELECT
 time_log.start_time as start,
 time_log.end_time as end,
 time_log.activity_id as activity,
 time_log.broker_id as broker
FROM time_log
  LEFT JOIN activity_log ON activity_log.activity_id = activity
  LEFT JOIN brokers ON brokers.broker_id = broker
  WHERE activity LIKE 'trading%';


































