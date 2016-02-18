<?php
//Script is used to post JSON objects.

require_once('news_DB.php');
require_once('mysqli_connect.php');

if(mysqli_connect_errno()){
	printf("Database Connection failed: %s\n", mysqli_connect_error());
	exit();
}

$query = "SELECT A.city, B.author, B.title, B.picture_link, B.short_description, B.link
		 FROM CITY AS A INNER JOIN NEWS AS B ON(A.city_id=B.city_id)"; 
$news_array = array();

if($result = $dbc->query($query)){
	while($row = $result->fetch_object()){
		$tmp_news = new newsDB($row->city, $row->title, $row->picture_link, 
			$row->short_description, $row->link);
		$news_array[] = $tmp_news;
		
	}	
}

$query = "SELECT city FROM CITY";
$j = 0;
$k = 0;
/*
	Formatting in JSON objects is tricky especially when attempting to organize 
	news by cities. What I needed to do is to have the list of cities available 
	where each city contains news articles.
*/
if($result = $dbc->query($query)){
	echo '{';
	while($row = $result->fetch_object()){
		echo '"', $row->city, '":[<br />';
		for($i = 0; $i < count($news_array);++$i){
			if( strcmp(strtolower($row->city), strtolower($news_array[$i]->city_name)) == 0){
				$json_data = json_encode($news_array[$i]);
				if($j == 0){
					$j = 1;
					echo $json_data;
				}
				else{
					echo ',' , $json_data;
				}
			}
		}
		echo ']';
		$j = 0;
		if($result->num_rows <= ($k - 1)){
		
		}
		else{
			echo ',', '<br />';
		}
		$k = $k + 1;
	}
	echo '}';
}

//From there, you should see generate_json.php create a JSON repository w/o
//the use of a MySQL Database connection, except inside the php script.
?>