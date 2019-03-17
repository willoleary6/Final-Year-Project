#INSERT INTO `detections` (`auto_id`, `objects_detected`, `file_path`, `start_timestamp`, `end_timestamp`, `minimum_number_of_detections`, `maximum_number_of_detections`) VALUES (NULL, '[\'Ten Cent\',\'Five Cent\',\'One Euro\']\r\n', 'C:\\SourceCode\\Final-Year-Project\\Workspace\\Human_detector\\test_videos\\VID_20190303_200842.mp4', '10.5', '16.34', '1', '4')
#delete from detections;
UPDATE `detections` SET `isActive` = '1'; 
select * from detections where isActive > 0
