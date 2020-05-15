<?php
session_start();
require 'db.php5';
        
    try {
        $query = $_POST['query'];

        $pdo = Database::connect();
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        $pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_OBJ);

        //$stmt = $pdo->query("SELECT * FROM login");
        $stmt = $pdo->query($query);
        //$data = $stmt->fetch();        
        while($rows = $stmt->fetch(PDO::FETCH_ASSOC)){
            var_dump($rows);
       }
        Database::disconnect();

    } catch (PDOException $e) {
        //echo "Error: " . $e->getMessage();
        //echo "An SQL Error occurred!";
    }
    

?>