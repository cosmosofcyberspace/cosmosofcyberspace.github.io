<?php
// CORS başlıklarını ekle
header('Access-Control-Allow-Origin: localhost');
header('Access-Control-Allow-Credentials: true');
header('Access-Control-Allow-Methods: GET, POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');

if ($_SERVER["REQUEST_METHOD"] == "GET" && isset($_GET['comment'])) {
    $user_input = $_GET['comment'];
    
    $file = fopen("comments.txt", "a");
    fwrite($file, $user_input . "\n");
    fclose($file);
    
    setcookie("last_comment", $user_input, time() + 3600); // 1 saat geçerli
    
    echo "Yorumunuz kaydedildi!";
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>XSS Zafiyetli Uygulama</title>
</head>
<body>
    <h1>Yorum Yapın</h1>
    <form method="GET">
        <textarea name="comment" rows="4" cols="50"></textarea><br>
        <input type="submit" value="Gönder">
    </form>
    
    <h2>Önceki Yorumlar:</h2>
    <?php
    if (file_exists("comments.txt")) {
        $comments = file_get_contents("comments.txt");
        // XSS zafiyeti: Kullanıcı girdisi doğrudan HTML'e yazdırılıyor
        echo $comments;
    }
    ?>
</body>
</html>
