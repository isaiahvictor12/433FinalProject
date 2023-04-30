CREATE DATABASE IF NOT EXISTS sensornetwork;
CREATE USER IF NOT EXISTS 'sensor';
GRANT INSERT ON sensornetwork.* TO 'sensor'@'%';

-- Define the Data Recording table
CREATE TABLE IF NOT EXISTS sensornetwork.data_record(
    record_id INT NOT NULL AUTO_INCREMENT,
    recording DECIMAL(5, 2),
    PRIMARY KEY(record_id)
);

-- Define the Temperature Recording table
CREATE TABLE IF NOT EXISTS sensornetwork.temperature_recording(

)