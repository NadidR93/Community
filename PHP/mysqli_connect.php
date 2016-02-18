<?php
//Database access depreciated 12/24.

DEFINE ('HOST', 'mock.host');
DEFINE ('USER', 'mock.user');
DEFINE ('PASS', 'mock.password');
DEFINE ('DB_NAME', 'mock.database');


$dbc = @mysqli_connect(HOST, USER, PASS, DB_NAME)
OR die('Could not connect to MySQL: ' .
mysqli_connect_error());
?>