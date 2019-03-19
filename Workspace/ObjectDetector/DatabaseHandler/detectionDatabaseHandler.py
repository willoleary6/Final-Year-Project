import sys
from Workspace.ObjectDetector.config import Config
import pymysql


class DetectionDatabaseHandler:
    def __init__(self):
        # rds settings
        host = Config.DATABASE_HOST
        username = Config.DATABASE_USERNAME
        password = Config.DATABASE_PASSWORD
        db_name = Config.DATABASE_NAME
        self.connection = ""

        try:
            self.connection = pymysql.connect(
                host,
                user=username,
                passwd=password,
                db=db_name,
                connect_timeout=100
            )
        except Exception as  e:
            print("ERROR: Unexpected error: Could not connect to MySql instance.")
            print(e)
            sys.exit()

    def select_all_detections(self):
        with self.connection.cursor() as cur:
            # run query
            cur.execute(
                "select * from detections where isActive > 0"
            )
            self.connection.commit()
        return self.__format_results(cur)

    def insert_new_detection(self, objects_detected, file_path, start_timestamp, end_timestamp,
                             minimum_number_of_detections,
                             maximum_number_of_detections):
        with self.connection.cursor() as cur:
            # run query
            cur.execute("INSERT INTO `detections` (`auto_id`, `objects_detected`, `file_path`, `start_timestamp`, "
                        "`end_timestamp`, `minimum_number_of_detections`, `maximum_number_of_detections`) "
                        "VALUES (""NULL, \'" + str(objects_detected).replace("\'", "\\'") + "\r\n', \'" + str(
                file_path).replace("\\", "\\\\") + "\',\'" + str(start_timestamp)
                        + "\',\'" + str(end_timestamp) + "\',\'"
                        + str(minimum_number_of_detections) + "\',\'" + str(maximum_number_of_detections) + "\');")
            self.connection.commit()
        return cur.description

    def delete_detection(self, detection_id):
        with self.connection.cursor() as cur:
            # run query
            cur.execute(
                "UPDATE `detections` SET `isActive` = '0' WHERE `detections`.`auto_id` = " + str(detection_id) + ";")
            self.connection.commit()
        return cur.description

    def close_connection(self):
        self.connection.close()

    @staticmethod
    def __format_results(cur):
        # retrieve the column names as keys
        keys = []
        for description in cur.description:
            keys.append(description[0])

        rows = cur.fetchall()
        results = []
        i = 0
        # store results as array of dictionaries
        for row in rows:
            j = 0
            results.append({})
            for key in keys:
                results[i][str(key)] = row[j]
                j += 1
            i += 1
        return keys, results
