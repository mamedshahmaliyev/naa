

<?php 

// get this data from database
$university = [
    'name' => "National Aviation Academy",
    "short_name" => 'NAA'
];


// header('Access-Control-Allow-Origin: *');
header('Content-Type: application/json; charset=utf-8');
echo json_encode($university);