
<?php 
// populated from the database
$students = [
    [
        'id' => "1",
        'name' => "Ahmad",
        'surname' => "Mammadov",
    ],
    [
        'id' => "2",
        'name' => "Firuza",
        'surname' => "Hasanova",
    ],
    [
        'id' => "3",
        'name' => "Rustam",
        'surname' => "Azadaliyev",
    ],
    [
        'id' => "4",
        'name' => "Student4",
        'surname' => "Student4",
    ],
];

header('Access-Control-Allow-Origin: *');
header('Content-Type: application/json; charset=utf-8');
echo json_encode($students);