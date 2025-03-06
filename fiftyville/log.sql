-- Keep a log of any SQL queries you execute as you solve the mystery.

SELECT * FROM crime_scene_reports WHERE (day = 28 AND month = 7 AND street = 'Humphery Street'); --get the crime id
SELECT * FROM crime_scene_reports WHERE (id = 295); --double check the crime
SELECT * FROM interviews WHERE ((day = 28 AND month = 7 AND year = 2023) AND transcript LIKE '%bakery%'); --get witness info of that day

SELECT * FROM bakery_security_logs WHERE(month = 7 AND day = 28 AND hour = 10); --get logs

SELECT * FROM people WHERE people.license_plate IN
(SELECT bakery_security_logs.license_plate FROM bakery_security_logs WHERE
(month = 7 AND day = 28 AND hour = 10 AND minute > 14 AND minute <35)); --get suspects whose license is within 10 mins of the theft

SELECT * FROM atm_transactions WHERE --get that morning transactions
(year = 2023 AND month = 7 AND day = 28 AND transaction_type = 'withdraw' AND atm_location = 'Leggett Street');

SELECT * FROM people WHERE people.id IN --get suspects accounts
(SELECT person_id FROM bank_accounts WHERE bank_accounts.account_number IN
(SELECT atm_transactions.account_number FROM atm_transactions WHERE(year = 2023 AND month = 7 AND day = 28 AND transaction_type = 'withdraw' AND atm_location = 'Leggett Street')));

--filter suspects
SELECT * FROM people WHERE id IN(SELECT id FROM people WHERE people.license_plate IN(SELECT bakery_security_logs.license_plate FROM bakery_security_logs WHERE(month = 7 AND day = 28 AND hour = 10 AND minute > 14 AND minute <35)) --filter the suspects
) and  id IN (SELECT id FROM people WHERE people.id IN(SELECT person_id FROM bank_accounts WHERE bank_accounts.account_number IN(SELECT atm_transactions.account_number FROM atm_transactions WHERE(year = 2023 AND month = 7 AND day = 28 AND transaction_type = 'withdraw' AND atm_location = 'Leggett Street'))));

SELECT * FROM phone_calls WHERE (year = 2023 AND month = 7 AND day = 28 AND duration < 60); --get phone call suspects

--filter all info so far
SELECT * FROM people WHERE id IN(SELECT id FROM people WHERE people.license_plate IN(SELECT bakery_security_logs.license_plate FROM bakery_security_logs WHERE(month = 7 AND day = 28 AND hour = 10 AND minute > 14 AND minute <35)) --filter the suspects
) and  id IN (SELECT id FROM people WHERE people.id IN(SELECT person_id FROM bank_accounts WHERE bank_accounts.account_number IN(SELECT atm_transactions.account_number FROM atm_transactions WHERE(year = 2023 AND month = 7 AND day = 28 AND transaction_type = 'withdraw' AND atm_location = 'Leggett Street')))
and id IN (SELECT id FROM people WHERE phone_number IN(SELECT caller FROM phone_calls where (year = 2023 AND month = 7 AND day = 28 AND duration < 60))));

--only 2 possible suspects: diana or bruce

SELECT * FROM flights WHERE (year = 2023 AND month = 7 AND day = 29) ORDER BY hour ASC, minute ASC; --find the next day first flight

SELECT * FROM passengers WHERE flight_id = 36; --search the next day flight passengers

SELECT * FROM people WHERE people.passport_number IN(SELECT passengers.passport_number FROM passengers WHERE flight_id = 36); --search the flight suspects

--last fillter
SELECT * FROM people WHERE id IN(SELECT id FROM people WHERE people.license_plate IN(SELECT bakery_security_logs.license_plate FROM bakery_security_logs WHERE(month = 7 AND day = 28 AND hour = 10 AND minute > 14 AND minute <35)) --filter the suspects
) and  id IN (SELECT id FROM people WHERE people.id IN(SELECT person_id FROM bank_accounts WHERE bank_accounts.account_number IN(SELECT atm_transactions.account_number FROM atm_transactions WHERE(year = 2023 AND month = 7 AND day = 28 AND transaction_type = 'withdraw' AND atm_location = 'Leggett Street')))
and id IN (SELECT id FROM people WHERE phone_number IN(SELECT caller FROM phone_calls where (year = 2023 AND month = 7 AND day = 28 AND duration < 60))
and id IN (SELECT id FROM people WHERE people.passport_number IN(SELECT passengers.passport_number FROM passengers WHERE flight_id = 36))));

--target found: bruce

SELECT * FROm airports WHERE id = 4; --search the destination

--city New York City

SELECT * FROM phone_calls where (year = 2023 AND month = 7 AND day = 28 AND duration < 60);

SELECT * FROM people WHERE phone_number IN
(SELECT receiver FROM phone_calls WHERE caller in (select phone_number from people where name = 'Bruce'))
and phone_number IN (SELECT receiver FROM phone_calls where (year = 2023 AND month = 7 AND day = 28 AND duration < 60));

--accomplice found: robin
