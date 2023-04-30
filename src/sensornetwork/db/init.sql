CREATE DATABASE IF NOT EXISTS sensornetwork;
CREATE USER IF NOT EXISTS 'sensor';
GRANT EXECUTE ON sensornetwork.* TO 'sensor'@'%';

-- Define the Data Recording table
CREATE TABLE IF NOT EXISTS sensornetwork.data_record(
    record_id INT NOT NULL AUTO_INCREMENT,
    recording DECIMAL(5, 2),
    record_time TIMESTAMP NOT NULL,
    PRIMARY KEY(record_id)
);

-- Define the Temperature Recording table
CREATE TABLE IF NOT EXISTS sensornetwork.temperature_recording(
    record_id INT NOT NULL,
    PRIMARY KEY(record_id),
    FOREIGN KEY (record_id) REFERENCES sensornetwork.data_record(record_id)
);

CREATE TABLE IF NOT EXISTS sensornetwork.humidity_recording(
    record_id INT NOT NULL,
    PRIMARY KEY(record_id),
    FOREIGN KEY (record_id) REFERENCES sensornetwork.data_record(record_id)
);

CREATE TABLE IF NOT EXISTS sensornetwork.light_recording(
    record_id INT NOT NULL,
    PRIMARY KEY(record_id),
    FOREIGN KEY (record_id) REFERENCES sensornetwork.data_record(record_id)
);

-- Create user procedures for recording data
CREATE PROCEDURE sensornetwork.record_temperature(IN recording DECIMAL(5, 2))
BEGIN
    DECLARE rec_id INT;
    DECLARE val DECIMAL(5, 2) DEFAULT recording;
    START TRANSACTION;

    IF ISNULL(recording) THEN
        SET val = (SELECT AVG(data_record.recording) FROM sensornetwork.temperature_recording JOIN sensornetwork.data_record ON data_record.record_id = temperature_recording.record_id);
    END IF;
    INSERT INTO sensornetwork.data_record(recording, record_time) VALUES (val, NOW());
    SET rec_id = LAST_INSERT_ID();
    INSERT INTO sensornetwork.temperature_recording(record_id) VALUES (rec_id);
    COMMIT;
END;

CREATE PROCEDURE sensornetwork.record_humidity(IN recording DECIMAL(5, 2))
BEGIN
    DECLARE rec_id INT;
    DECLARE val DECIMAL(5, 2) DEFAULT recording;
    START TRANSACTION;

    IF ISNULL(recording) THEN
        SET val = (SELECT AVG(data_record.recording) FROM sensornetwork.humidity_recording JOIN sensornetwork.data_record ON data_record.record_id = humidity_recording.record_id);
    END IF;
    INSERT INTO sensornetwork.data_record(recording, record_time) VALUES (val, NOW());
    SET rec_id = LAST_INSERT_ID();
    INSERT INTO sensornetwork.humidity_recording(record_id) VALUES (rec_id);
    COMMIT;
END;

CREATE PROCEDURE sensornetwork.record_light(IN recording DECIMAL(5, 2))
BEGIN
    DECLARE rec_id INT;
    DECLARE val DECIMAL(5, 2) DEFAULT recording;
    START TRANSACTION;

    IF ISNULL(recording) THEN
        SET val = (SELECT AVG(data_record.recording) FROM sensornetwork.light_recording JOIN sensornetwork.data_record ON data_record.record_id = light_recording.record_id);
    END IF;
    INSERT INTO sensornetwork.data_record(recording, record_time) VALUES (val, NOW());
    SET rec_id = LAST_INSERT_ID();
    INSERT INTO sensornetwork.light_recording(record_id) VALUES (rec_id);
    COMMIT;
END;
