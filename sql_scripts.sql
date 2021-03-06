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

/* two foreign keyS, LEFT JOIN ON, conditional WHERE IN clauses, YYYY-MM-DD HH:MM */
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
WHERE '2022-01-04 10:00' IN (start)

/* two foreign keyS, LEFT JOIN ON, conditional WHERE NOT IN clauses, YYYY-MM-DD HH:MM */
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
WHERE '2022-01-04 10:00' NOT IN (start)

/* fx_log foreign key WHERE conditional */
SELECT *
FROM fx_log
    LEFT JOIN brokers
    ON fx_log.broker_id = brokers.broker_id
WHERE broker LIKE 'forex%'

/* fx_log negative /  positive numbers WHERE conditional */
SELECT *
FROM fx_log
    LEFT JOIN brokers
    ON fx_log.broker_id = brokers.broker_id
WHERE gross_gain <0

/* fx_log queries */
SELECT *
FROM fx_log
    LEFT JOIN brokers
    ON fx_log.broker_id = brokers.broker_id
/* WHERE gross <0 */
/* WHERE gross >0 */
/* WHERE broker LIKE 'interactive%' */
/* WHERE entry_time > '10:00' */

/* select the interest_debit column  from the fx_interest_debit table */
select fx_interest_debit.interest_debit from fx_interest_debit;

/* sum  the interest_debit from  the fx_interest_debit table  */
select sum(fx_interest_debit.interest_debit) from fx_interest_debit;
select sum(interest_debit) from fx_interest_debit where entry_month = 1;
select sum(fx_interest_debit.interest_debit) from fx_interest_debit where entry_month = 1;

/* query the sum of the interest_debit and sum of the interest_ credit from the fx_interest_debit and fx_interest_income tables */
select sum(interest_debit) from fx_interest_debit where entry_month = 1
UNION ALL
select sum(interest_credit) from fx_interest_income where entry_month = 1;

/* query the commission, financing, realized P&L and broker credit */
select sum(commissions_cost) from fx_commissions where entry_month = 1
UNION ALL
select sum(interest_debit) from fx_interest_debit where entry_month = 1
UNION ALL
select sum(interest_credit) from fx_interest_income where entry_month = 1
UNION ALL
select sum(gross) from fx_log where entry_month = 1
UNION ALL 
select sum(broker_credit) from fx_broker_credit_income where entry_month = 1;















