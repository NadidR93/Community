<?php

//newsDB class made to hold each news article objects in an array
//Which is then organized by city in a JSON output format.
class newsDB {
	
	public $city_name    = "";
	public $title        = "";
	public $picture_link = "";
	public $short_desc   = "";
	public $link         = "";

	function __construct($city_name, $title, $picture_link, $short_desc, $link){
		$this->city_name = $city_name;
		$this->title = $title;
		$this->picture_link = $picture_link;
		$this->short_desc = $short_desc;
		$this->link  = $link;
	}
}	

?>