<?php 
// populated from database
$students = [
    '1' => [
        'name' => "Ahmad",
        'surname' => "Mammadov",
    ],
    '2' => [
        'name' => "Firuza",
        'surname' => "Hasanova",
    ],
    '3' => [
        'name' => "Rustam",
        'surname' => "Azadaliyev",
    ],
];
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>List of students (Monolith)</h1>
    <table border=1>
        <tr style="background: red; color: white;">
            <th>id</th>
            <th>Name</th>
            <th>Surname</th>
        </tr>
        <?php foreach($students as $id => $student) { ?>
        <tr>
            <td><?= $id ?></td>
            <td><?= $student['name'] ?></td>
            <td><?= $student['surname'] ?></td>
        </tr>
        <?php } ?>
    </table>
</body>
</html>