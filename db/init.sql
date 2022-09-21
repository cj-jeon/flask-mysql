create database testdb;
use testdb;

CREATE TABLE test_table (
  id VARCHAR(20),
  name VARCHAR(10)
);

INSERT INTO test_table 
  (id, name)
VALUES
  ('001', 'scott'),
  ('002', 'tiger'),
  ('003', 'artemis');
  
COMMIT;
